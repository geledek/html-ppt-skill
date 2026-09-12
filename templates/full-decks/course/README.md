# course · 教学课程

7-slide teaching deck: cover, objectives, core concept, worked example, exercise,
check-your-understanding (working MCQ), summary. A persistent left sidebar lists
the learning objectives and ticks them off as you advance.

Unlike the other full-deck templates, this one is **fully themeable**: it defines
no colors of its own, so every `assets/themes/*.css` reskins it and `T` cycles
themes live. Its original warm-academic palette now lives in
`assets/themes/course-warm.css`, which is what it loads by default.

The quiz is **interactive** — options are inert until clicked, then the correct
answer, the learner's mistake, and the explanations are revealed together.
Behaviour is in `assets/quiz.js`; mark the right option with `data-correct`.

**Use when:** course modules, lecture handouts, onboarding curricula, workshops.
**Feel:** a good textbook opened to a chapter — structured, quiet, encouraging.
**See also:** `full-decks/course-module` — the original, fixed-look version.
