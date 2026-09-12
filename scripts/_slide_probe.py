import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src).read()
probe = """<script>
document.addEventListener('DOMContentLoaded', function () {
  var SEL = '.h2,.lede,.callout,.concept-box p,.layer-note,.mcq b,.mcq .why,' +
            '.rm-gate p,.rm-track span,.rm-beyond li,td,.layer .layer-name';
  var long = [], pos = [], max = 0;
  document.querySelectorAll('.slide').forEach(function (sl, i) {
    sl.querySelectorAll(SEL).forEach(function (el) {
      var cs = getComputedStyle(el), lh = parseFloat(cs.lineHeight);
      if (isNaN(lh)) lh = parseFloat(cs.fontSize) * 1.4;
      // An inline element's bounding rect is its GLYPH box, not lines x
      // line-height, so height/lh undercounts: 4 lines of 40px measured 137px
      // and rounded to 3. getClientRects() returns one rect per line box, which
      // is the count itself. Block elements get one rect, so they use height.
      var n = cs.display.indexOf('inline') === 0
        ? el.getClientRects().length
        : Math.round(el.getBoundingClientRect().height / lh);
      if (n > max) max = n;
      if (n > 3) long.push({slide: i + 1, lines: n, text: el.textContent.trim().slice(0, 50)});
    });
    var h2 = sl.querySelector('.h2'), bd = sl.querySelector('.slide-body');
    if (h2 && bd) {
      var a = h2.getBoundingClientRect(), b = bd.getBoundingClientRect();
      pos.push({slide: i + 1, hx: Math.round(a.left), hy: Math.round(a.top),
                bx: Math.round(b.left), by: Math.round(b.top)});
    }
  });
  var shift = null, q = document.querySelector('.quiz');
  if (q) {
    var opt = q.querySelector('.mcq');
    var snap = function () {
      var r = q.getBoundingClientRect(), o = opt.getBoundingClientRect();
      return [Math.round(r.top), Math.round(r.left), Math.round(o.height)];
    };
    var before = snap(); opt.click(); var after = snap();
    shift = {before: before, after: after,
             moved: before[0] !== after[0] || before[1] !== after[1] || before[2] !== after[2]};
  }
  document.title = JSON.stringify({maxLines: max, long: long, pos: pos, reveal: shift});
});
</script>"""
open(out, 'w').write(s.replace('</body></html>', probe + '\n</body></html>'))
