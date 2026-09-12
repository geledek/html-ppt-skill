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

r = d['reveal']
if r is None:
    print("skip  no quiz on this deck")
elif r['moved']:
    fail = 1
    print("FAIL  layout moved on quiz reveal: %s -> %s" % (r['before'], r['after']))
else:
    print("ok    nothing moves when a quiz answer is revealed")

linked = int(os.environ['LINKED'])
if linked:
    fail = 1
    print("FAIL  %d local subresource reference(s) - unstyled in Safari" % linked)
else:
    print("ok    self-contained, no local subresources")

sys.exit(fail)
