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

SOURCE_ORDER = {}

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
 'R20': ('IMDA · Singapore Digital Economy Report 2025 · data year 2024', 'https://www.imda.gov.sg/assets/e77d879a-6b39-4de4-b024-5e0c6da0eff3.pdf'),
 'R21': ('MAS · Information paper on AI model risk management · 5 December 2024', 'https://www.mas.gov.sg/publications/monographs-or-information-paper/2024/artificial-intelligence-model-risk-management'),
 'R22': ('MAS · AI Risk Management Toolkit · 20 March 2026', 'https://www.mas.gov.sg/news/media-releases/2026/mas-partners-industry-to-develop-ai-risk-management-toolkit-for-the-financial-sector'),
 'R23': ('AI Risk Management Toolkit · gov.uk · 8 September 2026', 'https://www.gov.uk/government/publications/ai-risk-management-toolkit'),
 'R24': ('Malaysia · National Guidelines on AI Governance and Ethics, 2024 · AI Governance Bill consultation, July 2026', 'https://upc.mpc.gov.my/view-consultation/264'),
 'R25': ('Japan · Act on Promotion of R&D and Utilization of AI-Related Technologies, 2025', 'https://laws.e-gov.go.jp/law/507AC0000000053'),
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

# Jurisdictions shown on the map, and how their approach is classified.
# Classification drives colour; omitting a major economy or colouring binding law
# the same as guidance would both mislead. See R01-R25 in course.md.
REGIONS = {
    'eu': ('binding',   'European Union',  'Cross-sector AI Act. Duties by system, activity and role.',            15,   49,  14,   4),
    'kor':('binding',   'South Korea',     'AI Framework Act in force since 22 January 2026.',                    127.8, 36,  14,   4),
    'chn':('binding',   'China',           'Binding rules on generative AI and content labelling, already enforced.', 104, 35, -60, -14),
    'sgp':('guidance',  'Singapore',       'Existing law, sector supervision and voluntary frameworks.',         103.8,  1.35, -78, 34),
    'gbr':('guidance',  'United Kingdom',  'Existing regulators and legal frameworks, plus policy principles.',    -2,   54, -48, -16),
    'jpn':('guidance',  'Japan',           'A promotion act with no penalties provision.',                        138,   37,  16,  -6),
    'ind':('guidance',  'India',           'Sectoral regulators, plus binding labelling of synthetic content.',     79,   22, -52,  20),
    'mys':('guidance',  'Malaysia',        'Voluntary guidelines. A governance Bill is drafted, not tabled.',      102,   4,  -70, -18),
    'usa':('fragmented','United States',   'No federal AI statute. State laws, and federal action against them.',  -99,  40, -58, -22),
}
ISO_TO_REGION = {'GBR':'gbr','KOR':'kor','CHN':'chn','SGP':'sgp','JPN':'jpn','IND':'ind','MYS':'mys','USA':'usa'}
# EU members' overseas territories (French Guiana, Réunion, the Canaries…) sit far
# from Europe. Highlighting them paints unlabelled patches on other continents,
# so EU rings are clipped to a Europe bounding box.
EU_BOX = (-32, 34, 45, 72)   # lon_min, lat_min, lon_max, lat_max


def world_map():
    data = json.loads((HERE/'assets/world.geojson').read_text())
    title = 'AI governance approaches in nine selected jurisdictions'
    parts=[f'<svg class="world-map" viewBox="0 0 900 415" role="img" aria-labelledby="map-title map-desc"><title id="map-title">{title}</title><desc id="map-desc">Nine jurisdictions are shaded by the kind of instrument they rely on: binding law, guidance and voluntary frameworks, or fragmented state-level law. Selecting one explains its approach.</desc>']
    for f in data['features']:
        p,g=f['properties'],f['geometry']
        if p['ADMIN']=='Antarctica': continue
        iso=p['ADM0_A3']
        region = 'eu' if iso in EU else ISO_TO_REGION.get(iso)
        polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
        paths=[]
        for poly in polys:
            for ring in poly:
                if region=='eu':
                    lons=[c[0] for c in ring]; lats=[c[1] for c in ring]
                    cx,cy=sum(lons)/len(lons), sum(lats)/len(lats)
                    if not (EU_BOX[0]<=cx<=EU_BOX[2] and EU_BOX[1]<=cy<=EU_BOX[3]):
                        continue   # overseas territory: draw it unhighlighted below
                coords=[((lon+180)*2.5,(85-lat)*2.5) for lon,lat,*_ in ring]
                paths.append('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in coords)+'Z')
        if not paths:
            region=None
            for poly in polys:
                for ring in poly:
                    coords=[((lon+180)*2.5,(85-lat)*2.5) for lon,lat,*_ in ring]
                    paths.append('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in coords)+'Z')
        cls='country'
        attr=''
        if region:
            cls+=' selected '+REGIONS[region][0]
            attr=f' data-region="{region}"'
        parts.append(f'<path class="{cls}"{attr} d="'+''.join(paths)+f'"><title>{html.escape(p["ADMIN"])}</title></path>')
    for key,(kind,label,_desc,lon,lat,dx,dy) in REGIONS.items():
        x,y=(lon+180)*2.5,(85-lat)*2.5
        parts.append(f'<g class="map-marker {kind}" data-region="{key}"><circle class="map-pin" cx="{x:.1f}" cy="{y:.1f}" r="5"/><text class="map-label" x="{x+dx:.1f}" y="{y+dy:.1f}">{html.escape(label)}</text></g>')
    return ''.join(parts)+'</svg>'


def map_controls():
    order=['eu','kor','chn','sgp','gbr','jpn','ind','mys','usa']
    kinds={'binding':'Binding AI law','guidance':'Guidance and existing law','fragmented':'Fragmented state law'}
    groups={}
    for k in order:
        kind,label,desc,*_ = REGIONS[k]
        groups.setdefault(kind,[]).append((k,label,desc))
    out=[]
    for kind in ['binding','guidance','fragmented']:
        out.append(f'<div class="map-group-block {kind}"><p class="map-group">{kinds[kind]}</p>')
        for k,label,desc in groups[kind]:
            out.append(f'<button class="map-control {kind}" data-map="{k}" aria-pressed="false" data-desc="{html.escape(desc,quote=True)}">{html.escape(label)}</button>')
        out.append('</div>')
    return ''.join(out)


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
        if '{{MAP_CONTROLS}}' in body: body=body.replace('{{MAP_CONTROLS}}',map_controls())
        note_html=''.join('<p>'+html.escape(p.replace('\n',' '))+'</p>' for p in notes[n]['text'].split('\n\n'))
        footer=[]
        for r in refs:
            label,url=SOURCE_LABELS[r]
            footer.append(f'<a href="{html.escape(url,quote=True)}">{html.escape(label)}</a>' if url else html.escape(label))
        src=('<p class="source-line">'+', '.join(str(SOURCE_ORDER.setdefault(r,len(SOURCE_ORDER)+1)) for r in refs)+'</p>') if refs else ''
        pos=f'<span class="course-position" aria-label="Course slide {n} of 30">{n:02d} / 30</span>'
        if n==1:
            markup=f'<section class="slide cover" data-section="1" data-course-slide="1" data-title="{html.escape(title)}">{body}<div class="notes">{note_html}</div></section>'
        else:
            markup=f'<section class="slide" data-section="{section_for(n)}" data-course-slide="{n}" data-title="{html.escape(title)}"><header class="slide-head"><p class="kicker">{html.escape(kicker)}</p><h2 class="h2 mt-s">{html.escape(title)}</h2></header>{pos}<div class="slide-body">{body}<div class="notes">{note_html}</div></div>{src}</section>'
        path=HERE/'sections'/f'{n:02d}.html'
        path.write_text('<!-- GENERATED by gate2/build.py; edit gate2/slides.py and course.md. -->\n'+markup+'\n')
        fragments.append(markup)
    if SOURCE_ORDER:
        rows=[]
        for rid,num in sorted(SOURCE_ORDER.items(), key=lambda kv: kv[1]):
            label,url=SOURCE_LABELS[rid]
            link=f'<a href="{html.escape(url,quote=True)}">{html.escape(label)}</a>' if url else html.escape(label)
            rows.append(f'<li><span class="ref-no">{num}</span>{link}</li>')
        ref=('<section class="slide" data-section="8" data-course-slide="R" data-title="References">'
             '<header class="slide-head"><p class="kicker">SOURCES</p>'
             '<h2 class="h2 mt-s">References</h2></header>'
             '<div class="slide-body"><ol class="ref-list">'+''.join(rows)+'</ol>'
             '<div class="notes">Every figure, date and quotation in this course is drawn from these sources. '
             'The numbers beside each slide correspond to this list.</div></div></section>')
        fragments.append(ref)
    css_paths=['assets/fonts.css','assets/base.css','assets/themes/corporate-clean.css','assets/animations/animations.css','templates/full-decks/course/style.css']
    css='\n'.join((REPO/p).read_text() for p in css_paths)+'\n'+(HERE/'style.css').read_text()
    scripts='\n'.join('<script>\n'+(REPO/p).read_text()+'\n</script>' for p in ['assets/runtime.js','assets/quiz.js','assets/stage.js'])
    extra='''<script>
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
    </script>'''
    result='<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI Governance Overview · Gate 2 sample</title><!-- GENERATED by gate2/build.py. Selected course slides; original course numbering retained. --><style>'+css+'</style></head><body class="tpl-course stage-fixed"><div class="deck">'+'\n'.join(fragments)+'</div>'+scripts+extra+'</body></html>'
    (COURSE/'sample.html').write_text(result)
    manifest={'course_source_sha256':hashlib.sha256((COURSE/'course.md').read_bytes()).hexdigest(),'sample_sha256':hashlib.sha256(result.encode()).hexdigest(),'course_slides':[s[0] for s in SLIDES],'sample_count':len(SLIDES),'full_deck_rebuilt':False,'acceptance':'pending'}
    (HERE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'Built {len(SLIDES)} selected slides to {COURSE/"sample.html"}')

if __name__=='__main__':main()
