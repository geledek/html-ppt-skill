/* html-ppt :: stage.js — fixed 1920x1080 stage, scaled to fit.
 *
 * HTML decks reflow with the window while their type stays at fixed px, so the
 * same deck looks different on every screen: headlines wrap at one width and not
 * another, and content drifts. PowerPoint does not have this problem because it
 * has a FIXED CANVAS and scales the whole thing.
 *
 * This does the same. The deck is laid out at exactly 1920x1080 and transformed
 * to fit whatever window it is in, letterboxed. What you position stays
 * positioned, on every screen, at every size.
 *
 * A new file rather than an edit to runtime.js, per docs/adr/0001. Opt in by
 * putting class="stage-fixed" on <body> (the course template does).
 */
(function () {
  'use strict';
  if (!document.body || !document.body.classList.contains('stage-fixed')) {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    if (!document.body.classList.contains('stage-fixed')) return;
    var W = 1920, H = 1080;
    function fit() {
      var s = Math.min(window.innerWidth / W, window.innerHeight / H);
      document.documentElement.style.setProperty('--stage-scale', String(s));
    }
    window.addEventListener('resize', fit);
    window.addEventListener('orientationchange', fit);
    fit();
  }
})();
