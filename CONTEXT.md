# html-ppt

Authoring system for static HTML presentations. A renderer (themes, layouts,
animations, keyboard runtime) plus authored workflows that drive it.

## Language

### Output

**Deck**:
One HTML file containing a flat, ordered list of Slides, navigated by
`runtime.js`. The unit the renderer understands.
_Avoid_: presentation, PPT, slideshow

**Slide**:
One `<section class="slide">`. Exactly one is `.is-active` at a time.
_Avoid_: page, card

**Course**:
A teaching artifact produced by the course workflow, defined by an audience,
learning outcomes, and a duration budget. Today it renders to one Deck; it may
span several Decks in future.
_Avoid_: curriculum, class, training

**Section**:
A teaching unit within a Course — one coherent chunk of instruction. Spans one
or more Slides. Not a renderer concept; the renderer sees only Slides.
_Avoid_: chapter, module, unit, part

**Delivery Mode**:
How a Course reaches its learner — presenter-led, self-paced, or recorded.
Declared at gate 1. Selects the speaking or reading rate behind Time Allocation,
whether Narration renders as Speaker Notes or as on-slide content, and whether
quizzes must actually work.

**Section Divider**:
A Slide that visually announces a Section. A layout, not a container — it does
not group the Slides that follow it.

### Workflow

**Outline**:
The ordered list of Sections for a Course, with each Section's teaching intent.
Approved at gate 1 before any narration exists.

**Narration**:
The complete spoken script for a Course, organised by Section. Authored once
course-wide, not per Slide.
_Avoid_: script, speaker notes, 逐字稿

**Speaker Notes**:
The per-Slide `<div class="notes">` the renderer shows in presenter mode. One of
the two projections of Narration onto Slides — the other is on-slide prose. Which
projection applies is fixed by Delivery Mode. Projecting a self-paced Course into
Speaker Notes hides its entire teaching content.

**Representative Section**:
The one Section rendered to real HTML at gate 2 so a human can judge the design
before the whole Course is generated. Chosen as the *most demanding* Section —
largest Time Allocation, densest content — and always covering the quiz, since a
sample that survives the hardest page generalises and one that survives the
easiest page does not. Proposed with its reasoning; a human may override.

**Acceptance**:
The terminal approval of a Course, recording the content hash of `index.html` in
`course.md`. A later hash mismatch means the Course has diverged from what was
accepted — it does not mean the new version is wrong, only that it is unblessed.

### Process

**Teaching Strategy**:
The pedagogical sequencing an Outline commits to — concept-first, example-first,
problem-first. What the three alternatives at gate 1 actually differ on, with
outcomes and duration held constant. Each names its own failure mode.

**Time Allocation**:
Minutes assigned to a Section in the Outline, summing to the Course duration.
An estimate at gate 1; measurable only at gate 2, when Narration exists and can
be counted against a stated speaking rate.

**Gate**:
A point where generation stops and a human must approve a named artifact before
the next stage begins. Approval is of an exact version, not of a direction.
Quantified over Sections: a gate passes when every Section has passed it.

**Stale**:
The state of a Section artifact whose upstream input changed after it was
approved — narration whose outline moved, slides whose narration moved. Staleness
is Section-scoped; only Course-wide artifacts (Research Brief, Teaching Strategy,
duration) invalidate everything.

### Appearance

**Theme**:
A file defining design tokens on `:root`, swapped via `<link id="theme-link">`.
Changing a Course's Theme costs a re-assembly and makes no Section Stale.

**Template**:
The structural CSS and slide shapes a Deck is built from. Changing a Course's
Template regenerates every Section's slide markup — all Slides go Stale, though
Narration survives. Not interchangeable with Theme: most full-deck templates
define their own tokens scoped to `.tpl-*`, which shadows any Theme entirely.

### Evidence

**Research Plan**:
The set of questions research will answer and the kinds of sources it will
answer them against. Put to a human and redirected *before* any agent is
dispatched — the only cheap moment to change direction.

**Finding**:
One claim established by research, carried with the quote and URL it came from.
A Finding without a traceable source is not a Finding.

**Research Brief**:
The accumulated Findings for a Course, recorded in `course.md` as they are
established. Approved at gate 1 together with the Outline built on it.

**Provenance**:
The trace from a claim in Narration back to supplied material or a Finding.
Claims with neither must be marked illustrative. Quiz answer keys must cite.
