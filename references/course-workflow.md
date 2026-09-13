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

## Two language passes are mandatory

**Every piece of prose this workflow produces goes through both skills, in this
order, before a human sees it.** Narration, slide text, quiz stems and their
per-option feedback, the roadmap, and any revision at any gate.

1. **`no-ai-slop`** — structural. Removes AI patterns.
2. **`sg-english`** — locale. Removes the American startup register, which
   survives a slop pass because it is neither slop nor error.

Order matters: fixing structure first means the locale pass edits sentences that
are going to survive.

This applies to **revisions too**. A section rewritten at gate 3 gets both passes
again — an edited paragraph is new prose, and it is exactly where the register
creeps back.

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
./scripts/new-course.sh <name> [series]                        # scaffold
./scripts/build-course.sh courses/<name>                       # full deck -> index.html
./scripts/build-course.sh courses/<name> --sample 1,5,10       # layout proof -> sample.html
./scripts/check-slides.sh courses/<name>                       # five rules, exit 1 on any failure
```

A course is three files plus generated output:

| File | Holds | Edited by |
|---|---|---|
| `course.md` | narration, per-slide sources, research brief, outline | the human and you |
| `slides.py` | audience-facing compositions, source labels | you |
| `style.css` | course-specific CSS only | you |
| `index.html`, `sample.html`, `sections/` | **generated — never edit** | the build |

Everything reusable lives in the skill: `scripts/course/engine.py` builds,
`templates/full-decks/course/style.css` holds the components, and
`assets/course-interactions.js` holds the behaviour. **Before inventing a
component, read the template stylesheet.** When you do build something reusable,
promote it there so the next course inherits it.

**The sample and the full deck come from the same source.** `--sample` selects
course-slide numbers; nothing is authored twice. The sample exists to prove
layouts and motion, so keep it to one slide per layout family — once it grows
into a draft deck it has stopped doing its job.

Two build guards are deliberate. A slide may not cite a source its narration
block does not declare, and every cited source must have a label. Both exist so a
citation on a slide always traces back to the narration it came from.

**The default build inlines everything and that is deliberate** (docs/adr/0005).
Safari refuses to load `file://` subresources from parent directories, so a
linked build renders **completely unstyled** in the default macOS browser while
looking perfect under `render.sh`, which is headless Chrome. A Course also gets
emailed and opened on machines that have never seen this repo.

**Never review a course only in Chrome.** Open the built file in Safari too, or
check that `grep -cE '(src|href)="\.\.' index.html` returns 0.

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

**Run both language passes** (see "Two language passes are mandatory" above)
before showing the Narration. For a recorded Course, run them over the script
*and* over the on-slide text, which are different prose with different jobs.

Why `no-ai-slop` matters here specifically: it is not a
polish pass — for a self-paced Course the Narration *is* the learner-facing
content, and the patterns that skill bans are exactly the ones executive material
attracts: importance puffery, weasel attribution ("experts agree"), colon
reveals, summary-recap endings. Edit mode, minimum effective edit, then self-check
against its `eval.md`. Its rule against inventing claims and its demand for named
sources reinforce the provenance rule above rather than competing with it.

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

Generate the remaining Sections, one fragment each, then assemble. Run
`./scripts/check-slides.sh courses/<name>` before review — it fails on anything
that breaks the layout rules.

**Any Section you rewrite here goes back through both language passes.**

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

## Slide layout rules

**No text block exceeds three lines.** Not the headline, not a callout, not a
quiz option, not a cell. If it runs to four, cut words — do not shrink the type.
Audit it rather than eyeballing it: measure each block's height against its
computed `line-height` and fail the build in review if anything exceeds three.

**Use the full width.** Bodies are full width by default, and a wide measure with
a three-line ceiling means *fewer* lines, not a longer read. The line count is
the constraint; the width is what buys it.

**Both bands are pinned.** Every slide is a grid with one `minmax(0,1fr)` column
and `justify-items:start`, so the kicker, headline and body start at the same x
and y on every slide. Without the explicit column the implicit one is auto-sized
to its content and centred, and the headline slides sideways between slides.

**Nothing may move on reveal.** Quiz explanations and the verdict use
`visibility`, not `display`, so they occupy their space from the start. With
`display:none` every option grows when the answer is revealed and pushes the
slide down.

**The stage is fixed at 1920×1080** and scaled to fit (docs/adr/0006), so
positions are deterministic. Size type for that canvas, not for a browser window.

### Choosing a visual: when NOT to use a box

A component list without this guidance produces a deck where every slide is the
same grid of boxes. Measured on the first agent-built pass: **17 of 25 slides**
were a `concept-box` grid, several of them boxing two-word fragments. A box
around two words adds a border and nothing else.

Before reaching for `grid g2` of `concept-box`, check whether the slide is
actually one of these:

| The slide is… | Use | Not |
|---|---|---|
| one claim that deserves the whole frame | `quote-slide` | a box |
| one number that carries the point | `stat-row` | a box with a number in it |
| a named source saying something quotable | `quote-slide` | a box with a quotation in it |
| several concurrent things | `layer-stack` | columns, which say "pick one" |
| a chronology or a comparison across two columns | a table | boxes |
| genuinely 2–4 parallel items of equal weight | `concept-box` grid | — |

**Rough target: no more than half the slides should be box grids.** If a section
is all boxes, at least one of its slides is really a quote or a statistic.

`layer-stack` means *concurrent layers*. Do not use it for a sequence or a
timeline; it teaches the wrong shape.

**Headlines are claims, not script fragments.** An agent lifting the first
sentence of a slide's script produces "Your sector adds to it." and "Each comes
from a case you just saw." Write what the slide argues: "Singapore finance:
advisory, and still unissued."

### Motion rules

**Builds step on the learner's input, never on a timer.** Space or the forward
key reveals the next item in a `.stagger` group; once the group is complete the
next press advances the slide. A timed build forces the narrator's pace on
someone reading faster or slower, and cannot be re-watched in step. Leaving a
slide resets its build so it replays correctly on return.

**Set the stage scale before first paint.** `scripts/course/engine.py` emits a
blocking head script that sets `--stage-scale` and a `booting` class that
suppresses transitions for the first frame. Without it the deck paints once at
1920×1080 and then snaps, which reads as a shake on every slide.

**Pace motion to the voice, not the eye.** In a recorded course a narrator needs
roughly 2.5 seconds an item at 150 wpm. A stagger that finishes in 1.3 seconds is
decoration; the learner has read the whole list before the voice reaches item two.

**Animate what the voice enumerates. Leave static what the learner reads at
once.** A list the narrator walks through should build. A definition, a quotation,
a decision record, a quiz's options and a reference block should not — a learner
choosing a quiz answer needs to see every option at the same time.

**Every capture path must force the finished state.** With speech-paced motion a
screenshot or a PDF page catches a slide part-built. The deck carries a `stills`
body class, applied by `?stills`, by `beforeprint`, and available to any renderer.
Forgetting it produces contact sheets of half-drawn slides.

**Repeated per-slide citations belong at the back.** A reference block on every
slide stops being read. Keep a source marker on the slide and put the full list on
a closing References slide.

### Content and copy rules

**A kicker must not repeat the line beneath it.** If the headline already says
it, the kicker is noise. Kickers orient; they do not restate. Audit every slide
for a kicker whose words appear in the next element.

**A list of things gets a list layout.** Not boxes, not prose.

**One slide, one idea.** A slide carrying three unrelated components should be
split or have its weakest part cut. The symptom is an orphan line that explains
nothing on its own — if a learner would ask "what is that doing there?", it goes.

**A category list must not contain the thing it categorises.** "AI governance has
three parts, one of which is governance" is a broken taxonomy, and a learner will
notice before you do.

**Prefer the most recent and most local evidence.** For a Singapore audience a
Singapore source outranks a UK one, and a 2026 source outranks a 2024 one. When
only distant or older evidence exists, say so on the slide rather than letting it
pass as current.

**Date-stamp jurisdiction slides consistently.** If one carries "as at
<date>", they all do. A reader treats an undated slide as timeless.

**A diagram must be complete for the claim it makes.** A world map showing
"jurisdictions" must not omit the largest ones, and every highlighted region must
be labelled. An unlabelled highlight is a question the learner cannot answer.

### Every slide needs a connecting sentence

In a recorded course the narrator must never have to read the slide title aloud
to bridge from the previous slide. Each slide's script opens with a sentence that
carries the learner across from what came before. Without it the recording reads
as a sequence of captions.

### Check them, do not remember them

```bash
./scripts/check-slides.sh courses/<name>     # exit 0 = all rules hold
```

It measures rather than eyeballs: every text block's line count, the headline and
body coordinates on every slide, **whether anything runs off the bottom of the
1080px stage**, whether anything moves when a quiz is revealed, and whether any
local subresource would leave the build unstyled in Safari.

The overflow check exists because a nine-item legend beside a map ran 691px tall
and pushed a slide 64px off the stage, while the line-count and position checks
both passed it. A slide can satisfy every rule about its parts and still not
fit.

**Run it before every gate 3 review.** A twenty-six slide deck reviewed by eye at
2am is exactly where these rules quietly degrade.

## Capturing feedback into the skill

When the human gives design or layout feedback at gate 2, **write the rule down
before applying it**, in this order:

1. Add it to "Slide layout rules" above, in one sentence, with the reason.
2. If it can be measured, add it to `scripts/check-slides.sh`.
3. **Prove the check fails.** Break the rule deliberately in a copy of the deck
   and confirm a non-zero exit. A check that only ever passes is worthless — the
   line-count check shipped broken because an inline element's bounding rect is
   its glyph box rather than lines × line-height, and only a deliberate failure
   exposed it.
4. Then fix the deck.

Applying feedback without recording it means relearning it on the next course.
