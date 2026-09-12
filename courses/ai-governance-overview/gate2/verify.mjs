// Render and inspect the sample using an isolated Chrome profile and built-in Node CDP support.
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {spawn, spawnSync} from 'node:child_process';
const here=path.dirname(fileURLToPath(import.meta.url));
const course=path.dirname(here);
const out=path.join(here,'render');
await fs.mkdir(out,{recursive:true});
const profile=await fs.mkdtemp(path.join(os.tmpdir(),'ai-governance-chrome-'));
const chrome=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',[
 '--headless=new','--disable-gpu','--no-sandbox','--hide-scrollbars',
 '--remote-debugging-port=0','--remote-allow-origins=*',`--user-data-dir=${profile}`,'about:blank'
],{stdio:'ignore'});
let ws;
const delay=ms=>new Promise(r=>setTimeout(r,ms));
try{
 let port;
 for(let i=0;i<100;i++){
  try{port=(await fs.readFile(path.join(profile,'DevToolsActivePort'),'utf8')).split('\n')[0];break;}catch{await delay(100);}
 }
 if(!port)throw new Error('Chrome did not start');
 const tabs=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
 ws=new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);
 await new Promise((resolve,reject)=>{ws.onopen=resolve;ws.onerror=reject;});
 let serial=0;const pending=new Map();
 ws.onmessage=e=>{const msg=JSON.parse(e.data);if(msg.id){const p=pending.get(msg.id);if(p){pending.delete(msg.id);msg.error?p.reject(Error(JSON.stringify(msg.error))):p.resolve(msg.result);}}};
 const call=(method,params={})=>new Promise((resolve,reject)=>{const id=++serial;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}));});
 const evaluate=async(expression)=>{const r=await call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
 await call('Page.enable');await call('Runtime.enable');
 await call('Emulation.setDeviceMetricsOverride',{width:1920,height:1080,deviceScaleFactor:1,mobile:false});
 await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
 const base=pathToFileURL(path.join(course,'sample.html')).href;
 async function navigate(url){
  await call('Page.navigate',{url});
  for(let i=0;i<100;i++){if(await evaluate('document.readyState === "complete" && !!document.querySelector(".slide.is-active")'))break;await delay(100);}
  await evaluate('Promise.race([document.fonts.ready,new Promise(r=>setTimeout(r,8000))]).then(()=>true)');
  await evaluate('(()=>{let s=document.createElement("style");s.textContent=".slide{transition:none!important}";document.head.append(s);})()');
 }
 await navigate(base+'?preview=1');
 const manifest=JSON.parse(await fs.readFile(path.join(here,'manifest.json'),'utf8'));
 const findings=[];
 const inspect=`(()=>{
  const sl=document.querySelector('.slide.is-active'),stage=document.querySelector('.deck').getBoundingClientRect();
  const selectors='h1,h2,h3,h4,p,td,th,.mcq b,.why,.map-control b,.map-control span,.timeline time,.timeline-status';
  const issues=[];
  sl.querySelectorAll(selectors).forEach(el=>{
   if(el.closest('.notes'))return;
   const st=getComputedStyle(el),r=el.getBoundingClientRect();
   if(st.display==='none'||!r.width||!r.height)return;
   const range=document.createRange();range.selectNodeContents(el);
   const ys=[...new Set([...range.getClientRects()].filter(x=>x.width>0).map(x=>Math.round(x.top/3)*3))];
   const lineHeight=parseFloat(st.lineHeight)||parseFloat(st.fontSize)*1.4;
   const lines=st.display.startsWith('inline')?ys.length:Math.round(r.height/lineHeight);
   if(lines>3)issues.push({type:'lines',lines,text:el.textContent.trim().slice(0,90)});
   if(r.left<stage.left+39||r.top<stage.top+39||r.right>stage.right-39||r.bottom>stage.bottom-39)issues.push({type:'bounds',box:{x:r.x,y:r.y,w:r.width,h:r.height},text:el.textContent.trim().slice(0,90)});
  });
  const body=sl.querySelector('.slide-body'),source=sl.querySelector('.source-line');
  if(body&&source&&body.getBoundingClientRect().bottom>source.getBoundingClientRect().top-12)issues.push({type:'body-source-overlap',bodyBottom:body.getBoundingClientRect().bottom,sourceTop:source.getBoundingClientRect().top});
  return {courseSlide:Number(sl.dataset.courseSlide),issues};
 })()`;
 for(let i=0;i<manifest.sample_count;i++){
  await evaluate(`new Promise(resolve=>{window.postMessage({type:'preview-goto',idx:${i}},'*');setTimeout(resolve,100);})`);
  const initial=await evaluate(inspect);findings.push({...initial,state:'initial'});
  const image=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
  await fs.writeFile(path.join(out,`slide-${String(initial.courseSlide).padStart(2,'0')}.png`),Buffer.from(image.data,'base64'));
  if(await evaluate('!!document.querySelector(".slide.is-active .quiz")')){
   const geometry=await evaluate('(()=>{const q=document.querySelector(".slide.is-active .quiz");return [...q.querySelectorAll(".mcq")].map(e=>{const r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height]})})()');
   await evaluate('document.querySelector(".slide.is-active .quiz [data-correct]").click()');
   const after=await evaluate('(()=>{const q=document.querySelector(".slide.is-active .quiz");return [...q.querySelectorAll(".mcq")].map(e=>{const r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height]})})()');
   const reveal=await evaluate(inspect);
   if(JSON.stringify(geometry)!==JSON.stringify(after))reveal.issues.push({type:'quiz-layout-shift'});
   findings.push({...reveal,state:'revealed'});
   const png=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
   await fs.writeFile(path.join(out,`slide-${String(initial.courseSlide).padStart(2,'0')}-answer.png`),Buffer.from(png.data,'base64'));
  }
 }
 // Test audience navigation: first advance reveals, second advance moves on.
 await navigate(base+'#/2');
 const navBefore=await evaluate('document.querySelector(".slide.is-active").dataset.courseSlide');
 await evaluate('document.dispatchEvent(new KeyboardEvent("keydown",{key:"ArrowRight",bubbles:true}))');
 const navReveal=await evaluate('({slide:document.querySelector(".slide.is-active").dataset.courseSlide,revealed:!!document.querySelector(".slide.is-active .quiz.revealed")})');
 await evaluate('document.dispatchEvent(new KeyboardEvent("keydown",{key:"ArrowRight",bubbles:true}))');
 const navAfter=await evaluate('document.querySelector(".slide.is-active").dataset.courseSlide');
 if(navBefore!=='2'||navReveal.slide!=='2'||!navReveal.revealed||navAfter!=='3')throw Error('Quiz keyboard navigation failed');
 // All map controls must select and toggle off, with labelled pressed states.
 const mapChecks=await evaluate(`(()=>{const map=document.querySelector('.deck .world-map');return [...document.querySelectorAll('.deck [data-map]')].map(b=>{b.click();let ok=b.getAttribute('aria-pressed')==='true'&&map.dataset.focus===b.dataset.map;b.click();return {region:b.dataset.map,ok:ok&&!map.hasAttribute('data-focus')};});})()`);
 if(mapChecks.some(c=>!c.ok))console.log('Map controls:',JSON.stringify(mapChecks));
 const failures=findings.filter(f=>f.issues.length);
 const report={sampleCount:manifest.sample_count,findings,keyboard:{before:navBefore,reveal:navReveal,after:navAfter},mapChecks,failures:failures.length};
 await fs.writeFile(path.join(here,'checks.json'),JSON.stringify(report,null,2)+'\n');
 if(mapChecks.some(c=>!c.ok))throw Error('Map controls failed; see checks.json');
 if(failures.length){console.log(JSON.stringify(failures,null,2));throw Error(`${failures.length} slide states failed`);}
 // Full print has all answers and the complete map state, without presenter furniture.
 await navigate(base+'?answers=1');
 const marker='/Users/ray/.codex/plugins/cache/openai-primary-runtime/pdf/26.909.12148/skills/pdf/container_tools/mark_artifact_operation_started.mjs';
 const marked=spawnSync(process.execPath,[marker,'--operation-kind','create','--expected-output-count','1','--output-format','pdf'],{stdio:'inherit'});
 if(marked.status!==0)throw Error('PDF operation marker failed');
 const pdf=await call('Page.printToPDF',{printBackground:true,preferCSSPageSize:true,displayHeaderFooter:false});
 await fs.writeFile(path.join(course,'sample.pdf'),Buffer.from(pdf.data,'base64'));
 console.log(`PASS: ${manifest.sample_count} slides, ${findings.length} states, quiz navigation, map controls; PDF exported.`);
}finally{
 if(ws)ws.close();chrome.kill();
 // Chrome can keep child processes alive briefly; leave its isolated profile in the OS temp directory.
}
