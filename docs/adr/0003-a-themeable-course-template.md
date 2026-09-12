# A themeable course template, built new rather than in place

The repo has two authoring tracks the README describes as one. The scaffold
track (`templates/deck.html` + `templates/single-page/*` + `assets/themes/*`) is
genuinely token-driven: a theme defines tokens on `:root`, and swapping the
`<link id="theme-link">` reflows the deck. The full-deck track is not — 14 of 15
full-deck templates ship no `theme-link` at all, and each redefines the same
token names scoped to its own `.tpl-*` wrapper, which shadows `:root` for the
whole subtree. So `T` is inert on them and the template *is* the look.

Courses need `course-module`'s teaching furniture (objectives sidebar, worked
example, MCQ) *and* theme freedom, since we let a Course pick a theme at gate 1
and swap it freely at gate 2. So we build a themeable course template: lift
`course-module`'s scoped token block out into a theme file, keep the structural
CSS, and replace its remaining hardcoded colors with the tokens that already
hold those same values (`#2d7d6e` is `--accent`; `rgba(45,125,110,.06)` is that
same accent at 6%). The refactor is mechanical, not a redesign.

It is built as a **new** template directory rather than an edit to
`course-module/`, for the reason in ADR 0001: that file is upstream-tracked and
editing it creates permanent merge conflict surface. Same rationale as putting
the quiz reveal behaviour in a new `assets/quiz.js` instead of `runtime.js`.

## Consequences

- Theme becomes free to change for a Course (a re-assembly, no Section goes
  Stale); template does not (slide markup regenerates, Narration survives).
- `course-module` stays untouched and keeps working for anyone using it directly.
