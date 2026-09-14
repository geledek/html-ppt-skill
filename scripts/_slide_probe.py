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
    // A cover legitimately has no kicker/headline band and centres instead, so it
    // is excluded rather than forced to match. Everything with a head must match.
    var h2 = sl.querySelector('.h2'), bd = sl.querySelector('.slide-body');
    if (h2 && bd && !sl.classList.contains('cover')) {
      var a = h2.getBoundingClientRect(), b = bd.getBoundingClientRect();
      pos.push({slide: i + 1, hx: Math.round(a.left), hy: Math.round(a.top),
                bx: Math.round(b.left), by: Math.round(b.top)});
    }
  });
  // Content running off the bottom of the 1920x1080 stage. The line-count and
  // position checks both pass on a slide whose panel overflows the frame, which
  // is how an overflowing map slide shipped.
  var over = [];
  document.querySelectorAll('.slide').forEach(function (sl, i) {
    var lim = sl.getBoundingClientRect().bottom;
    var worst = 0, who = '';
    sl.querySelectorAll('.slide-body *, .cover-main *, .quote-body *').forEach(function (el) {
      if (!el.getClientRects().length) return;
      var b = el.getBoundingClientRect().bottom;
      if (b - lim > worst) { worst = b - lim; who = (el.textContent || '').trim().slice(0, 40); }
    });
    if (worst > 4) over.push({slide: i + 1, px: Math.round(worst), text: who});
  });

  // Duplicated headings. A generated slide head plus a composition that carries
  // its own title renders the title twice, and every other check passes.
  var dupes = [];
  document.querySelectorAll('.slide').forEach(function (sl, i) {
    var seen = {};
    sl.querySelectorAll('h1, h2, .h1, .h2, .cover-title').forEach(function (el) {
      var t = (el.textContent || '').trim().toLowerCase();
      if (!t) return;
      if (seen[t]) dupes.push({slide: i + 1, text: t.slice(0, 45)});
      seen[t] = 1;
    });
  });

  // A kicker that repeats the line beneath it. Feedback R2-01: the kicker read
  // "RETAILER CHATBOT" directly above a headline that said the same thing, so it
  // carried no orientation the slide did not already give.
  var echo = [];
  var norm = function (t) { return (t || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); };
  document.querySelectorAll('.slide').forEach(function (sl, i) {
    var k = sl.querySelector('.kicker');
    if (!k) return;
    var kt = norm(k.textContent);
    if (!kt || kt.split(' ').length > 6) return;
    var below = [sl.querySelector('.h2')];
    var body = sl.querySelector('.slide-body');
    if (body) below.push(body.querySelector('p, li, h3, h4, b, .lede'));
    below.forEach(function (el) {
      if (!el) return;
      var bt = norm(el.textContent);
      if (!bt) return;
      if (bt.indexOf(kt) !== -1 || (kt.indexOf(bt) !== -1 && bt.split(' ').length > 1)) {
        echo.push({slide: i + 1, kicker: k.textContent.trim().slice(0, 30),
                   below: el.textContent.trim().slice(0, 40)});
      }
    });
  });

  // Every slide carries its number. Feedback R4-11: numbers went missing on the
  // generated slides, and a missing number reads as a missing slide.
  var unnumbered = [];
  document.querySelectorAll('.slide').forEach(function (sl, i) {
    var p = sl.querySelector('.course-position');
    if (!p || !(p.textContent || '').trim()) unnumbered.push(i + 1);
  });

  // Unused lower frame. Feedback R4-10 ("too much white space") and the empty
  // half under the map. Advisory, not a failure: a quote slide and a cover are
  // legitimately sparse, so this is a list to walk at gate 3, not a build break.
  var sparse = [];
  document.querySelectorAll('.slide').forEach(function (sl, i) {
    if (sl.classList.contains('cover') || sl.querySelector('.quote-slide, .quote-body')) return;
    var body = sl.querySelector('.slide-body');
    if (!body) return;
    var lim = sl.getBoundingClientRect().bottom, low = body.getBoundingClientRect().top;
    body.querySelectorAll('*').forEach(function (el) {
      if (!el.getClientRects().length) return;
      var cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.opacity === '0') return;
      var b = el.getBoundingClientRect().bottom;
      if (b > low) low = b;
    });
    var gap = Math.round(lim - low);
    if (gap > 320) sparse.push({slide: i + 1, px: gap});
  });

  var shift = null, q = document.querySelector('.quiz');
  if (q) {
    var opt = q.querySelector('.mcq');
    var snap = function () {
      var r = q.getBoundingClientRect(), o = opt.getBoundingClientRect();
      return [Math.round(r.top), Math.round(r.left), Math.round(o.height)];
    };
    var before = snap(); opt.click(); var after = snap();
    // The per-option feedback must actually appear on reveal. display:none .why
    // reserves no space, so a broken template reveals nothing while "nothing
    // moved" still passes — the check has to verify the feedback is visible, not
    // only that the layout held. A .why is shown when it is not display:none, is
    // visibility:visible, and has a non-zero rendered box.
    var why = q.querySelector('.revealed .mcq .why') || q.querySelector('.mcq .why');
    var whyShown = null;
    if (why) {
      var wcs = getComputedStyle(why), wr = why.getBoundingClientRect();
      whyShown = wcs.display !== 'none' && wcs.visibility !== 'hidden' &&
                 wr.height > 0 && wr.width > 0;
    }
    shift = {before: before, after: after,
             moved: before[0] !== after[0] || before[1] !== after[1] || before[2] !== after[2],
             hasWhy: why !== null, whyShown: whyShown};
  }
  document.title = JSON.stringify({maxLines: max, long: long, pos: pos, reveal: shift, over: over, dupes: dupes, echo: echo, unnumbered: unnumbered, sparse: sparse});
});
</script>"""
open(out, 'w').write(s.replace('</body></html>', probe + '\n</body></html>'))
