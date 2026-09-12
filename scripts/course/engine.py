"""html-ppt :: course build engine.

Generates a course deck from three inputs:

  courses/<name>/course.md    narration, per-slide sources, outline
  courses/<name>/slides.py    audience-facing compositions (SLIDES, SOURCE_LABELS)
  courses/<name>/style.css    course-specific CSS (optional)

Everything reusable lives here; everything about one course lives in that course
directory. Run it through scripts/build-course.sh.

Two guards are deliberate and should not be relaxed:
  * a slide may not cite a source its narration block does not declare, and
  * every declared source must have a label, or the build fails.
Both exist so a citation on a slide always traces to the narration it came from.
"""
import html, json, re, hashlib, importlib.util, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def load_course(course_dir):
    course = Path(course_dir).resolve()
    spec = importlib.util.spec_from_file_location('course_slides', course / 'slides.py')
    mod = importlib.util.module_from_spec(spec)
    sys.modules['course_slides'] = mod
    spec.loader.exec_module(mod)
    return course, mod


def narration_blocks(source):
    narration = source.split('## Narration\n', 1)[1]
    pattern = r'^#### (\d+) · ([^\n]+)\n(.*?)\*\*Narration:\*\*\n(.*?)(?=^#### |^### S\d|^## [^#]|\Z)'
    blocks = {}
    for match in re.finditer(pattern, narration, re.M | re.S):
        n, title, metadata, text = match.groups()
        blocks[int(n)] = {'title': title, 'sources': re.findall(r'\[(R\d+)\]', metadata), 'text': text.strip()}
    if not blocks:
        raise ValueError('No narration blocks found. Each slide needs a "#### NN · Title" '
                         'heading followed by "**Narration:**" under "## Narration".')
    gaps = sorted(set(range(1, max(blocks) + 1)) - set(blocks))
    if gaps:
        raise ValueError(f'Narration missing for slide(s): {gaps}')
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
    data = json.loads((REPO / 'assets/geo/world.geojson').read_text())
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



def section_for(n, bounds):
    return next(i + 1 for i, b in enumerate(bounds) if n <= b)



def build(course_dir, out_name='index.html', only=None, section_bounds=None):
    """Assemble a course. `only` limits the build to a list of course-slide
    numbers, which is how the Gate 2 sample is produced from the same source."""
    course, mod = load_course(course_dir)
    SLIDES = [s for s in mod.SLIDES if only is None or s[0] in only]
    LABELS = mod.SOURCE_LABELS
    bounds = section_bounds or getattr(mod, 'SECTION_BOUNDS', [len(mod.SLIDES)])
    order = {}

    source = (course / 'course.md').read_text()
    notes = narration_blocks(source)
    registered = set(re.findall(r'^### (R\d+) ·', source, re.M))
    unknown = set(LABELS) - registered - {'R00'}
    if unknown:
        raise ValueError(f'Source labels with no Research Brief entry: {sorted(unknown)}')

    fragments = []
    (course / 'sections').mkdir(exist_ok=True)
    for n, kicker, title, body, refs in SLIDES:
        if n not in notes:
            raise ValueError(f'Slide {n} has no narration block in course.md')
        if set(refs) - set(notes[n]['sources']):
            raise ValueError(f'Slide {n} cites a source its narration does not declare')
        if '{{WORLD_MAP}}' in body:
            body = body.replace('{{WORLD_MAP}}', world_map())
        if '{{MAP_CONTROLS}}' in body:
            body = body.replace('{{MAP_CONTROLS}}', map_controls())
        note_html = ''.join('<p>' + html.escape(p.replace('\n', ' ')) + '</p>'
                            for p in notes[n]['text'].split('\n\n'))
        marks = ', '.join(str(order.setdefault(r, len(order) + 1)) for r in refs)
        src_line = f'<p class="source-line">{marks}</p>' if refs else ''
        total = len(mod.SLIDES)
        # A cover carries its own title block, so it gets no generated head, no
        # position marker and no source line. Without this the title renders twice.
        is_cover = 'cover-main' in body
        attrs = (f'data-section="{section_for(n, bounds)}" data-course-slide="{n}" '
                 f'data-title="{html.escape(title)}"')
        if is_cover:
            markup = (f'<section class="slide cover" {attrs}>{body}'
                      f'<div class="notes">{note_html}</div></section>')
        else:
            pos = (f'<span class="course-position" aria-label="Course slide {n} of {total}">'
                   f'{n:02d} / {total}</span>') if n else ''
            head = (f'<header class="slide-head"><p class="kicker">{html.escape(kicker)}</p>'
                    f'<h2 class="h2 mt-s">{html.escape(title)}</h2></header>')
            markup = (f'<section class="slide" {attrs}>{head}{pos}'
                      f'<div class="slide-body">{body}<div class="notes">{note_html}</div></div>'
                      f'{src_line}</section>')
        (course / 'sections' / f'{n:02d}.html').write_text(
            '<!-- GENERATED by scripts/course/engine.py; edit slides.py and course.md. -->\n' + markup + '\n')
        fragments.append(markup)

    if order:
        rows = []
        for rid, num in sorted(order.items(), key=lambda kv: kv[1]):
            label, url = LABELS[rid]
            link = f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>' if url else html.escape(label)
            rows.append(f'<li><span class="ref-no">{num}</span>{link}</li>')
        fragments.append(
            '<section class="slide" data-section="99" data-title="References">'
            '<header class="slide-head"><p class="kicker">SOURCES</p>'
            '<h2 class="h2 mt-s">References</h2></header>'
            '<div class="slide-body"><ol class="ref-list">' + ''.join(rows) + '</ol>'
            '<div class="notes">Every figure, date and quotation in this course is drawn from '
            'these sources. The numbers beside each slide correspond to this list.</div>'
            '</div></section>')

    theme = re.search(r'^theme:\s*(\S+)', source, re.M)
    theme = theme.group(1) if theme else 'corporate-clean'
    title = re.search(r'^title:\s*(.+)$', source, re.M)
    title = title.group(1).strip() if title else 'Course'

    css_paths = ['assets/fonts.css', 'assets/base.css', f'assets/themes/{theme}.css',
                 'assets/animations/animations.css', 'templates/full-decks/course/style.css']
    css = '\n'.join((REPO / p).read_text() for p in css_paths)
    course_css = course / 'style.css'
    if course_css.exists():
        css += '\n' + course_css.read_text()
    js = '\n'.join('<script>\n' + (REPO / p).read_text() + '\n</script>'
                   for p in ['assets/runtime.js', 'assets/quiz.js', 'assets/stage.js',
                             'assets/course-interactions.js'])

    out = ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(title)}</title>'
           '<!-- GENERATED by scripts/course/engine.py. Edit slides.py and course.md. -->'
           '<style>' + css + '</style></head><body class="tpl-course stage-fixed"><div class="deck">'
           + '\n'.join(fragments) + '</div>' + js + '</body></html>')
    (course / out_name).write_text(out)

    (course / 'manifest.json').write_text(json.dumps({
        'course_source_sha256': hashlib.sha256((course / 'course.md').read_bytes()).hexdigest(),
        'output': out_name,
        'output_sha256': hashlib.sha256(out.encode()).hexdigest(),
        'slides': [s[0] for s in SLIDES],
        'slide_count': len(fragments),
        'references': len(order),
    }, indent=2) + '\n')
    print(f'{out_name}: {len(fragments)} slides, {len(order)} references -> {course / out_name}')
    return course / out_name
