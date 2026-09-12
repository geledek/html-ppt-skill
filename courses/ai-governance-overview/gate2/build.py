#!/usr/bin/env python3
"""Build the selected HTML sample from the course template and source narration."""
from pathlib import Path
import hashlib
import html
import json
import re
from slides import SLIDES

HERE = Path(__file__).resolve().parent
COURSE = HERE.parent
REPO = COURSE.parents[1]

SOURCE_LABELS = {
 'R00': ('Hypothetical example · course teaching synthesis', None),
 'R01': ('OECD · Organisation for Economic Co-operation and Development · 2024 explanatory memorandum', 'https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html'),
 'R02': ('NIST AI RMF 1.0', 'https://airc.nist.gov/airmf-resources/airmf/5-sec-core/'),
 'R03': ('ISO/IEC 42001:2023', 'https://www.iso.org/standard/42001'),
 'R04': ('Singapore Model AI Governance Framework · second edition, 2020', 'https://www.imda.gov.sg/-/media/imda/files/infocomm-media-landscape/sg-digital/tech-pillars/artificial-intelligence/second-edition-of-the-model-ai-governance-framework.pdf'),
 'R05': ('PDPC · Data Protection Obligations', 'https://www.pdpc.gov.sg/overview-of-pdpa/the-legislation/personal-data-protection-act/data-protection-obligations'),
 'R06': ('Bank of England / FCA · Artificial intelligence in UK financial services · 21 November 2024', 'https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024'),
 'R07': ('European Commission · AI Act overview', 'https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai'),
 'R08': ('Official implementation timeline · July 2026 amendment', 'https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline'),
 'R09': ('UK AI regulation white paper · 2023', 'https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper'),
 'R10': ('MAS · Supervisory approach and regulatory instruments', 'https://www.mas.gov.sg/regulation/mas-supervisory-approach-and-regulatory-instruments'),
 'R11': ('FCA · AI approach · February 2026', 'https://www.fca.org.uk/firms/innovation/ai-approach'),
 'R12': ('UK Treasury Committee · January 2026 report', 'https://publications.parliament.uk/pa/cm5901/cmselect/cmtreasy/684/report.html'),
 'R14': ('PDPC · Re HSBC Bank (Singapore) [2021] SGPDPC 3 · paragraphs 17–19', 'https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/commissions-decisions/decision--hsbc-bank-singapore-limited--10032021.pdf'),
 'R18': ('MAS P017-2025 §3.4 · consultation proposal, finance-specific', 'https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management'),
}

def narration_blocks(source):
    narration = source.split('## Narration\n', 1)[1]
    pattern = r'^#### (\d+) · ([^\n]+)\n(.*?)\*\*Narration:\*\*\n(.*?)(?=^#### |^### S\d|^## [^#]|\Z)'
    blocks = {}
    for match in re.finditer(pattern, narration, re.M | re.S):
        n, title, metadata, text = match.groups()
        blocks[int(n)] = {'title': title, 'sources': re.findall(r'\[(R\d+)\]', metadata), 'text': text.strip()}
    if set(blocks) != set(range(1,31)):
        raise ValueError(f'Expected exactly 30 source passages, got {list(blocks)}')
    return blocks

EU = {'AUT','BEL','BGR','HRV','CYP','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','IRL','ITA','LVA','LTU','LUX','MLT','NLD','POL','PRT','ROU','SVK','SVN','ESP','SWE'}

def world_map():
    data = json.loads((HERE/'assets/world.geojson').read_text())
    parts=['<svg class="world-map" viewBox="0 0 900 415" role="img" aria-labelledby="map-title map-desc"><title id="map-title">Singapore, the European Union and the United Kingdom</title><desc id="map-desc">Three selected jurisdictions are highlighted. The accompanying text explains their different regulatory approaches.</desc>']
    for f in data['features']:
        p,g=f['properties'],f['geometry']
        if p['ADMIN']=='Antarctica': continue
        iso=p['ADM0_A3']
        region='eu' if iso in EU else 'uk' if iso=='GBR' else None
        polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
        paths=[]
        for poly in polys:
            for ring in poly:
                coords=[((lon+180)*2.5,(85-lat)*2.5) for lon,lat,*_ in ring]
                paths.append('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in coords)+'Z')
        region_attr=f' data-region="{region}"' if region else ''
        parts.append(f'<path class="country'+(' selected' if region else '')+f'"{region_attr} d="'+''.join(paths)+'"><title>'+html.escape(p['ADMIN'])+'</title></path>')
    for key,label,lon,lat,dx,dy in [('uk','UK',-2,54,-45,-15),('eu','EU',15,49,12,6),('sg','Singapore',103.82,1.35,-75,32)]:
        x,y=(lon+180)*2.5,(85-lat)*2.5
        parts.append(f'<circle class="map-pin" data-region="{key}" cx="{x:.1f}" cy="{y:.1f}" r="6"/><text class="map-label" x="{x+dx:.1f}" y="{y+dy:.1f}">{label}</text>')
    return ''.join(parts)+'</svg>'


def section_for(n):
    return next(i+1 for i,bound in enumerate([4,9,16,19,23,27,30]) if n<=bound)


def main():
    source=(COURSE/'course.md').read_text()
    notes=narration_blocks(source)
    registered=set(re.findall(r'^### (R\d+) ·',source,re.M))
    for n, block in notes.items():
        if not block['sources'] or set(block['sources'])-registered:
            raise ValueError(f'Slide {n} has missing or unknown source IDs')
    fragments=[]
    for n,kicker,title,body,refs in SLIDES:
        if set(refs)-set(notes[n]['sources']): raise ValueError(f'Slide {n} source not in narration metadata')
        if '{{WORLD_MAP}}' in body: body=body.replace('{{WORLD_MAP}}',world_map())
        note_html=''.join('<p>'+html.escape(p.replace('\n',' '))+'</p>' for p in notes[n]['text'].split('\n\n'))
        footer=[]
        for r in refs:
            label,url=SOURCE_LABELS[r]
            footer.append(f'<a href="{html.escape(url,quote=True)}">{html.escape(label)}</a>' if url else html.escape(label))
        src='<p class="source-line">'+' · '.join(footer)+'</p>' if footer else ''
        pos=f'<span class="course-position" aria-label="Course slide {n} of 30">{n:02d} / 30</span>'
        if n==1:
            markup=f'<section class="slide cover" data-section="1" data-course-slide="1" data-title="{html.escape(title)}">{body}<div class="notes">{note_html}</div></section>'
        else:
            markup=f'<section class="slide" data-section="{section_for(n)}" data-course-slide="{n}" data-title="{html.escape(title)}"><header class="slide-head"><p class="kicker">{html.escape(kicker)}</p><h2 class="h2 mt-s">{html.escape(title)}</h2></header>{pos}<div class="slide-body">{body}<div class="notes">{note_html}</div></div>{src}</section>'
        path=HERE/'sections'/f'{n:02d}.html'
        path.write_text('<!-- GENERATED by gate2/build.py; edit gate2/slides.py and course.md. -->\n'+markup+'\n')
        fragments.append(markup)
    css_paths=['assets/fonts.css','assets/base.css','assets/themes/corporate-clean.css','assets/animations/animations.css','templates/full-decks/course/style.css']
    css='\n'.join((REPO/p).read_text() for p in css_paths)+'\n'+(HERE/'style.css').read_text()
    scripts='\n'.join('<script>\n'+(REPO/p).read_text()+'\n</script>' for p in ['assets/runtime.js','assets/quiz.js','assets/stage.js'])
    extra='''<script>
    document.querySelectorAll('.deck [data-map]').forEach(function(button){
      button.addEventListener('click',function(){
        var map=document.querySelector('.deck .world-map');
        var was=button.getAttribute('aria-pressed')==='true';
        document.querySelectorAll('.deck [data-map]').forEach(function(b){b.setAttribute('aria-pressed','false');});
        if(was){map.removeAttribute('data-focus');}else{map.setAttribute('data-focus',button.dataset.map);button.setAttribute('aria-pressed','true');}
      });
    });
    function revealForPrint(){document.querySelectorAll('.quiz').forEach(function(q){
      q.classList.add('revealed');q.querySelector('[data-correct]').classList.add('correct');
      var v=q.querySelector('.verdict');if(v)v.textContent='Answer: '+q.querySelector('[data-correct] b').textContent;
    });}
    window.addEventListener('beforeprint',revealForPrint);
    if(new URLSearchParams(location.search).has('answers'))revealForPrint();
    </script>'''
    result='<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI Governance Overview · Gate 2 sample</title><!-- GENERATED by gate2/build.py. Selected course slides; original course numbering retained. --><style>'+css+'</style></head><body class="tpl-course stage-fixed"><div class="deck">'+'\n'.join(fragments)+'</div>'+scripts+extra+'</body></html>'
    (COURSE/'sample.html').write_text(result)
    manifest={'course_source_sha256':hashlib.sha256((COURSE/'course.md').read_bytes()).hexdigest(),'sample_sha256':hashlib.sha256(result.encode()).hexdigest(),'course_slides':[s[0] for s in SLIDES],'sample_count':len(SLIDES),'full_deck_rebuilt':False,'acceptance':'pending'}
    (HERE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'Built {len(SLIDES)} selected slides to {COURSE/"sample.html"}')

if __name__=='__main__':main()
