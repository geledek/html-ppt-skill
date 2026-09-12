/* html-ppt :: quiz.js — reveal-on-click multiple choice.
 *
 * A new file rather than an addition to runtime.js: runtime.js is
 * upstream-tracked, and this fork keeps `git pull upstream main` cheap.
 * See docs/adr/0001.
 *
 * Markup:
 *   <div class="quiz">
 *     <div class="mcq" data-correct>
 *       <div class="letter">A</div>
 *       <div><b>answer text</b><p class="why">why it is right</p></div>
 *     </div>
 *     <div class="mcq"> … </div>
 *     <p class="verdict"></p>          <!-- optional; filled on reveal -->
 *   </div>
 *
 * The answer key is `data-correct` on the option. Nothing marks the answer
 * visually until a learner clicks, so the question can actually be posed.
 * Presenter-led decks get a reveal beat; self-paced learners must commit first.
 */
(function () {
  'use strict';

  var RIGHT = 'Correct.';
  var WRONG = 'Not quite — see the highlighted answer.';
  var SKIPPED = 'Here is the answer.';

  function reveal(quiz, chosen) {
    if (quiz.classList.contains('revealed')) return;

    var opts = quiz.querySelectorAll('.mcq');
    var hit = chosen && chosen.hasAttribute('data-correct');

    for (var i = 0; i < opts.length; i++) {
      var o = opts[i];
      if (o.hasAttribute('data-correct')) o.classList.add('correct');
      else if (o === chosen) o.classList.add('wrong');
      o.setAttribute('aria-disabled', 'true');
    }

    var verdict = quiz.querySelector('.verdict');
    if (verdict) {
      var msg = chosen ? (hit ? RIGHT : WRONG) : SKIPPED;
      verdict.textContent = verdict.textContent.trim() || msg;
      verdict.classList.add(chosen && !hit ? 'miss' : 'right');
    }
    quiz.classList.add('revealed');
  }

  function wire(root) {
    var quizzes = (root || document).querySelectorAll('.quiz');
    for (var i = 0; i < quizzes.length; i++) {
      var quiz = quizzes[i];
      if (quiz.dataset.quizWired) continue;
      quiz.dataset.quizWired = '1';

      var opts = quiz.querySelectorAll('.mcq');
      for (var j = 0; j < opts.length; j++) {
        var o = opts[j];
        o.setAttribute('role', 'button');
        o.setAttribute('tabindex', '0');
        o.addEventListener('click', onPick);
        o.addEventListener('keydown', onKey);
      }
    }
  }

  function onPick(e) {
    var opt = e.currentTarget;
    var quiz = opt.closest('.quiz');
    if (quiz) reveal(quiz, opt);
  }

  // Enter/Space pick an option. Everything else — arrows especially — is left
  // alone so runtime.js keeps owning slide navigation.
  function onKey(e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    e.preventDefault();
    e.stopPropagation();
    onPick(e);
  }

  // Self-paced learners advance without answering. Reveal before they leave:
  // the first Right/Space/PageDown on an unanswered quiz reveals it, the second
  // advances. Bound in CAPTURE phase so it runs before runtime.js's bubble-phase
  // handler, which owns navigation.
  function activeUnrevealedQuiz() {
    var slide = document.querySelector('.slide.is-active') ||
                document.querySelector('.slide');
    if (!slide) return null;
    var q = slide.querySelector('.quiz');
    return (q && !q.classList.contains('revealed')) ? q : null;
  }

  function onAdvance(e) {
    if (e.key !== 'ArrowRight' && e.key !== ' ' && e.key !== 'PageDown') return;
    if (e.target && e.target.closest && e.target.closest('.mcq')) return;
    var q = activeUnrevealedQuiz();
    if (!q) return;
    reveal(q, null);          // no option chosen — show the answer, mark nothing wrong
    e.preventDefault();
    e.stopPropagation();
  }
  document.addEventListener('keydown', onAdvance, true);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { wire(); });
  } else {
    wire();
  }

  // Assembled courses and preview iframes can inject slides after load.
  window.htmlPptQuiz = { wire: wire };
})();
