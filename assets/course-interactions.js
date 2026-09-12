/* html-ppt :: course-interactions.js — behaviour shared by every course deck.
 *
 * Map selection, Esc to open the overview, click-to-reveal decision checks, and
 * the stills mode that every capture path needs once motion is paced to speech.
 * A new file rather than an edit to runtime.js, per docs/adr/0001.
 */
(function () {
  'use strict';
  function init() {
    // Map selection. Selecting a jurisdiction — from the panel OR from the map
        // itself — highlights the country, its marker and its panel entry, and draws
        // a line between the two so the eye does not have to hunt for the pairing.
        (function(){
          var layout=document.querySelector('.deck .map-layout');
          if(!layout) return;
          var stage=layout.querySelector('.map-stage');
          var link=layout.querySelector('.map-link line');
          function clear(){
            layout.classList.remove('has-selection');
            if(layout.querySelector('.map-detail')) layout.querySelector('.map-detail').innerHTML='Select a jurisdiction to see its approach.';
            layout.querySelectorAll('[data-map]').forEach(function(b){b.setAttribute('aria-pressed','false');});
            layout.querySelectorAll('.is-active').forEach(function(el){el.classList.remove('is-active');});
          }
          function draw(region){
            var marker=layout.querySelector('.map-marker[data-region="'+region+'"] .map-pin');
            var panel=layout.querySelector('[data-map="'+region+'"]');
            if(!marker||!panel||!link) return;
            var box=stage.getBoundingClientRect();
            var m=marker.getBoundingClientRect(), p=panel.getBoundingClientRect();
            link.setAttribute('x1',(m.left+m.width/2-box.left).toFixed(1));
            link.setAttribute('y1',(m.top+m.height/2-box.top).toFixed(1));
            link.setAttribute('x2',(box.width).toFixed(1));
            link.setAttribute('y2',(p.top+p.height/2-box.top).toFixed(1));
          }
          var detail=layout.querySelector('.map-detail');
          function select(region){
            var already=layout.querySelector('[data-map="'+region+'"]').getAttribute('aria-pressed')==='true';
            clear();
            if(already) return;
            layout.classList.add('has-selection');
            var btn=layout.querySelector('[data-map="'+region+'"]');
            btn.setAttribute('aria-pressed','true');
            if(detail) detail.innerHTML='<b>'+btn.textContent+'</b> '+btn.dataset.desc;
            layout.querySelectorAll('.country[data-region="'+region+'"]').forEach(function(el){el.classList.add('is-active');});
            var mk=layout.querySelector('.map-marker[data-region="'+region+'"]');
            if(mk) mk.classList.add('is-active');
            draw(region);
          }
          layout.querySelectorAll('[data-map]').forEach(function(b){
            b.addEventListener('click',function(){select(b.dataset.map);});
          });
          layout.querySelectorAll('.world-map [data-region]').forEach(function(el){
            el.style.cursor='pointer';
            el.addEventListener('click',function(){select(el.dataset.region||el.getAttribute('data-region'));});
          });
          window.addEventListener('resize',function(){
            var on=layout.querySelector('[aria-pressed="true"]');
            if(on) draw(on.dataset.map);
          });
        })();
        // R3-05: Esc opens the slide overview (runtime.js binds it to O). A second
        // press, or Esc while it is open, closes it.
        document.addEventListener('keydown', function (e) {
          if (e.key !== 'Escape') return;
          var ov = document.querySelector('.overview');
          if (ov && ov.classList.contains('open')) return;   // runtime closes it
          e.preventDefault(); e.stopPropagation();
          document.dispatchEvent(new KeyboardEvent('keydown', {key: 'o', bubbles: true}));
        }, true);
        // R3-18: the decision is revealed on request, as a check rather than a caption
        document.querySelectorAll('.decision-review button').forEach(function (b) {
          b.addEventListener('click', function () { b.closest('.decision-review').classList.add('open'); });
        });
        if(new URLSearchParams(location.search).has('stills')) document.body.classList.add('stills');
        window.addEventListener('beforeprint',function(){document.body.classList.add('stills');});
        function revealForPrint(){document.querySelectorAll('.quiz').forEach(function(q){
          q.classList.add('revealed');q.querySelector('[data-correct]').classList.add('correct');
          var v=q.querySelector('.verdict');if(v)v.textContent='Answer: '+q.querySelector('[data-correct] b').textContent;
        });}
        window.addEventListener('beforeprint',revealForPrint);
        if(new URLSearchParams(location.search).has('answers'))revealForPrint();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
