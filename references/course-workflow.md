# Course workflow — three gates

For teaching material, not decks. A **Course** is defined by an audience,
learning outcomes, a duration budget and a delivery mode; it is built through
three points where generation stops and a human approves a named artifact.

Vocabulary is in [../CONTEXT.md](../CONTEXT.md). Use those words exactly — the
distinctions between Section and Slide, and between Narration and Speaker Notes,
are load-bearing.

**The human never types a shell command.** You run the scripts, you open the
browser, you render the contact sheets. Their job is to look, judge, and say yes
or say what is wrong.

---

## Layout

```
courses/
├── <series>.md              # optional — shared audience, Research Brief, Theme
├── <course-name>/
│   ├── course.md            # frontmatter + brief + outline + narration
│   ├── sections/NN-*.html   # one fragment per Section
│   └── index.html           # GENERATED — never hand-edit
```

`courses/<name>/` is two deep, like `examples/<name>/`, so `../../assets/`
resolves unchanged. Don't nest courses under a series directory; it breaks that.

```bash
./scripts/new-course.sh <name> [series]      # scaffold
./scripts/assemble-course.sh courses/<name>  # sections/*.html -> index.html
```

## Status is per Section, not per gate

`course.md`'s Outline table carries `Outline | Narration | Slides` per Section,
each `pending | approved | stale`. **A gate passes when every Section has passed
it.** Changing Section 4's outline marks Section 4's narration and slides stale
and nothing else. Only Course-wide changes — Research Brief, Teaching Strategy,
duration, Delivery Mode, Template — invalidate everything.

Record a short content hash beside each approved Section. The human edits
`course.md` directly; a hash mismatch is how you notice, rather than trusting a
stale `approved`.

**Theme changes are free** — re-assemble, nothing goes stale. **Template changes
are not** — all Slides regenerate, though Narration survives. Never present them
as equivalent choices.

---

## Gate 1 — Research Brief + Outline

**Collect first:** audience, outcomes, duration, and **Delivery Mode**. State the
consequences of the mode back to them rather than storing it silently:

| Mode | Narration renders as | Rate | Quiz |
|---|---|---|---|
| presenter-led | `<div class="notes">`, shown by `S` | ~150 wpm EN · ~220 字/分 | reveal is a presenter beat |
| self-paced | **on-slide prose** | ~250 wpm silent reading | learner must be able to answer |
| recorded | voiceover script, not in the deck | ~150 wpm | as presenter-led |

Getting this wrong is a silent, total failure: a self-paced course whose teaching
content sits in hidden `.notes` looks perfect in review and teaches nothing.

**Then research.** Put the **Research Plan** to the human *before dispatching
anything* — the questions you intend to answer and the kinds of sources. That is
the only cheap moment to redirect. Then run background agents against primary
sources, and walk the **Findings** back here interactively: each one with its
quote and URL.

> Never justify a Finding with your own reasoning. A generated explanation is
> fluent whether or not the claim is true, and "bouncing ideas" that raises
> confidence without raising correctness is the worst outcome available. Bottom
> out in a quote and a link, or say you could not establish it.

Findings land in `course.md` as they are established, not in a write-up at the
end. If the Course belongs to a Series, read the Series brief first and research
only the gap.

**Then up to three Outlines**, differing on **Teaching Strategy** — concept-first,
example-first, problem-first — with outcomes and duration held constant. Each
names its own failure mode (concept-first loses the impatient; example-first
over-fits the example; problem-first frustrates beginners). Each Section cites
the Findings behind it and carries a **Time Allocation** in minutes summing to
the duration.

Say which you recommend and why. A flat menu pushes judgment onto them without
the reasoning.

**Offer fewer than three when the difference would be manufactured** — short
courses often collapse to one honest shape, and a fake alternative is worse than
no alternative. Say so rather than padding.

Pick Template and Theme here too. Default `template: course`, which is the only
themeable teaching template; `course-module` is its fixed-look predecessor.

**Gate: the human approves the Research Brief and the Outline together.** The
minute allocations are an *estimate* — say so. Duration is not measurable until
narration exists.

---

## Gate 2 — Narration + Representative Section

Write one script for the whole Course, organised by Section, against the minute
budgets. Report **measured words vs. allocation per Section**, so an overrun is
local and actionable rather than "the course is too long."

**Provenance is a hard rule.** Every factual claim traces to supplied material or
to a Finding, or is marked illustrative. Quiz answer keys cite. A course teaches;
learners do not fact-check the thing they are learning from, and a wrong answer
key actively trains the wrong answer.

**Choose the Representative Section** — the *most demanding* one, not the
friendliest. Largest allocation, densest content, longest code, widest table. It
must cover the quiz, or assemble the sample as that section plus the quiz slide.
State the reasoning so they can argue with it, and let them override.

> Section 1 is an introduction. It will look beautiful under any theme and
> predicts nothing. A sample that survives the hardest page generalises; one that
> survives the easiest does not.

Render it and open it **live in a browser** — 4-6 slides is short enough to walk,
and this is the gate where the quiz reveal and navigation are being proven, which
a PNG cannot show.

**Gate: the human approves the exact Narration and the Representative Section
together.** A Theme swap here is free and worth offering. A Template swap is
offered with its cost stated.

---

## Gate 3 — Acceptance

Generate the remaining Sections, one fragment each, then assemble.

Lead the review with an **inline PNG contact sheet** — the whole course on one
screen catches overflow, drift and breakage far faster than arrowing through 60
slides, and rubber-stamping starts around slide 20. Open the browser only for
Sections they flag.

Two `render.sh` traps, both upstream and both left unpatched:

- **`all` undercounts.** It greps `class="slide"` with a closing quote, so every
  `class="slide full"` is skipped — on the course template that drops the cover
  and the summary. **Pass the explicit count** that `assemble-course.sh` printed.
- **A custom out-dir is never created**, and `render_one` echoes `✔`
  unconditionally with Chrome's stderr discarded — so it reports success for
  files that do not exist. **`mkdir -p` it first**, then check the files landed.

**Gate: the human accepts the exact full-course HTML.** Record its content hash
in `course.md` as `accepted_hash`. A later mismatch means the Course has diverged
from what was accepted — not that it is wrong, only that it is unblessed.

**Offer a git commit. Never make one unprompted.**

---

## Series

Related Courses sharing one audience, one Research Brief, one Theme and one
Template, in `courses/<series>.md`. Whether its members are sittings of a single
Course or Courses in their own right is deliberately left open until their
Outlines exist and can be compared.

The test: **does session 2 make sense to someone who missed session 1?** If no,
they are one Course. If yes, they are two.

Sharing the inputs is what pays — research done once, terminology and theme that
cannot drift. Promoting several Courses into one Course with several Decks later
is a grouping change over fragments that already exist.

## Slides

Compose from `templates/full-decks/course/index.html` — sidebar with ticking
objectives, concept box, worked example, exercise, quiz, summary. Every color
comes from a token, so any theme reskins it.

Quiz markup — the answer key is `data-correct`, and nothing reveals until a
click:

```html
<div class="quiz">
  <div class="mcq"><div class="letter">A</div>
    <div><b>option</b><p class="why">why this is wrong</p></div></div>
  <div class="mcq" data-correct><div class="letter">B</div>
    <div><b>option</b><p class="why">why this is right</p></div></div>
  <p class="verdict"></p>
</div>
```

Put `data-section="N"` on every `<section class="slide">` so the Section→Slide
map stays true. Set `data-title` for the overview grid.
