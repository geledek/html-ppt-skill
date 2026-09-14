import json, os, sys
d = json.loads(os.environ['JSON'])
fail = 0

if d['long']:
    fail = 1
    print("FAIL  text over 3 lines (%d):" % len(d['long']))
    for v in d['long']:
        print("        slide %s: %s lines - %s..." % (v['slide'], v['lines'], v['text']))
else:
    print("ok    no text block over 3 lines (max %s)" % d['maxLines'])

pos = d['pos']
if pos:
    keys = set((p['hx'], p['hy'], p['bx'], p['by']) for p in pos)
    if len(keys) == 1:
        hx, hy, bx, by = keys.pop()
        print("ok    headline and body pinned on all %d slides (h %d,%d - body %d,%d)" % (len(pos), hx, hy, bx, by))
    else:
        fail = 1
        print("FAIL  headline/body positions differ between slides:")
        for p in pos:
            print("        slide %s: h %s,%s  body %s,%s" % (p['slide'], p['hx'], p['hy'], p['bx'], p['by']))

dup = d.get('dupes') or []
if dup:
    fail = 1
    print("FAIL  heading rendered twice on %d slide(s):" % len(dup))
    for v in dup:
        print("        slide %s: %s..." % (v['slide'], v['text']))
else:
    print("ok    no duplicated headings")

ov = d.get('over') or []
if ov:
    fail = 1
    print("FAIL  content overflows the 1080px stage (%d slide(s)):" % len(ov))
    for v in ov:
        print("        slide %s: %spx past the bottom - %s..." % (v['slide'], v['px'], v['text']))
else:
    print("ok    nothing overflows the stage")

echo = d.get('echo') or []
if echo:
    fail = 1
    print("FAIL  kicker repeats the line beneath it (%d):" % len(echo))
    for v in echo:
        print("        slide %s: %r over %r..." % (v['slide'], v['kicker'], v['below']))
else:
    print("ok    no kicker repeats the line beneath it")

un = d.get('unnumbered') or []
if un:
    fail = 1
    print("FAIL  %d slide(s) carry no number: %s" % (len(un), ', '.join(str(n) for n in un)))
else:
    print("ok    every slide carries its number")


r = d['reveal']
if r is None:
    print("skip  no quiz on this deck")
elif r['moved']:
    fail = 1
    print("FAIL  layout moved on quiz reveal: %s -> %s" % (r['before'], r['after']))
elif r.get('hasWhy') and not r.get('whyShown'):
    fail = 1
    print("FAIL  quiz feedback stays hidden on reveal (.why not visible)")
else:
    print("ok    nothing moves when a quiz answer is revealed")

linked = int(os.environ['LINKED'])
if linked:
    fail = 1
    print("FAIL  %d local subresource reference(s) - unstyled in Safari" % linked)
else:
    print("ok    self-contained, no local subresources")

sparse = d.get('sparse') or []
if sparse:
    # Advisory. A quote slide is legitimately sparse, so an empty lower frame is
    # a list to walk at gate 3 rather than a build break.
    print("warn  %d slide(s) leave the lower frame empty:" % len(sparse))
    for v in sparse:
        print("        slide %s: %spx unused below the last element" % (v['slide'], v['px']))

sys.exit(fail)
