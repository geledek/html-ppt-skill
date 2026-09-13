# Slide design guidelines

Consolidated from five rounds of review on the first course
(`courses/ai-governance-overview`, September 2026). Every rule here was written
down because a slide broke it and Ray had to say so. The feedback rounds
themselves are kept verbatim in that course's `FEEDBACK*.md`; the `R#-##` codes
below point back to them.

Read this **before composing slides**, not after. It is the design half of
[course-workflow.md](./course-workflow.md), which owns the gates.

## The five things asked for most often

1. **One slide, one idea, and the whole frame used for it.** Sparse slides and
   overloaded slides came back equally often.
2. **The visual matches the content shape.** A list gets a list, a chronology
   gets a table, one claim gets the whole frame. Not everything is a box.
3. **Nothing on the slide is written for the reviewer.** Hedges, provenance
   notes and artefact labels all get cut.
4. **Motion is paced to the voice and stepped by the learner.**
5. **One emphasis colour, and it is the blue.**

---

## The slide

**One slide, one idea.** A slide carrying three unrelated components is split, or
its weakest part is cut. The symptom is an orphan line that explains nothing on
its own — if a learner would ask "what is that doing there?", it goes. (R2-06,
R2-07)

**A category list must not contain the thing it categorises.** "AI governance has
three parts, one of which is governance" is a broken taxonomy, and a learner
notices before you do. (R2-07)

**No text block exceeds three lines.** Not the headline, not a callout, not a
quiz option, not a cell. If it runs to four, cut words — do not shrink the type.

**Use the full width.** Bodies are full width by default, and a wide measure with
a three-line ceiling means *fewer* lines, not a longer read.

**Fill the lower frame.** Four items on a slide means four larger items, not four
small ones with an empty half beneath. Growing the type is the first move; a
second supporting element is the second. (R4-10, R5-02)

**Both bands are pinned.** Every slide is a grid with one `minmax(0,1fr)` column
and `justify-items:start`, so the kicker, headline and body start at the same x
and y throughout. Without the explicit column the implicit one is auto-sized and
centred, and the headline slides sideways between slides.

**The stage is fixed at 1920×1080** and scaled to fit (docs/adr/0006). Size type
for that canvas, not for a browser window.

**Every slide carries its number**, cover included, numbered by course-slide
number. A missing number reads as a missing slide, and numbering "around" the
cover makes every slide read one low. (R4-11)

## Choosing a visual

A component list without this guidance produces a deck where every slide is the
same grid of boxes. Measured on the first agent-built pass: **17 of 25 slides**
were a `concept-box` grid, several boxing two-word fragments. A box around two
words adds a border and nothing else.

| The slide is… | Use | Not |
|---|---|---|
| one claim that deserves the whole frame | `quote-slide`, type scaled up | a box |
| one number that carries the point | `stat-row` | a box with a number in it |
| a named source saying something quotable | `quote-slide` with visible attribution | a box with a quotation in it |
| a list of things | a list, bulleted, one item a line | boxes or prose |
| several concurrent things | `layer-stack` | columns, which say "pick one" |
| a chronology or a two-column comparison | a table | boxes |
| a short table of two-line entries | one column, no header, no numbering | a numbered three-column grid |
| genuinely 2–4 parallel items of equal weight | bordered card, name in the emphasis colour, rounded corners | an unbordered column |

**Rough target: no more than half the slides are card grids.** If a section is
all boxes, at least one of its slides is really a quote or a statistic.

`layer-stack` means *concurrent layers*. Do not use it for a sequence or a
timeline; it teaches the wrong shape. (R2-08, R2-13, R4-06, R5-11, R5-12, R5-14)

**A diagram must be complete for the claim it makes.** A world map showing
"jurisdictions" must not omit the largest ones, and every highlighted region must
be labelled. An unlabelled highlight is a question the learner cannot answer.
(R2-09)

## Copy

**Headlines are claims, not script fragments.** Lifting the first sentence of the
script produces "Your sector adds to it." Write what the slide argues:
"Singapore finance: advisory, and still unissued."

**A kicker must not repeat the line beneath it.** Kickers orient; they do not
restate. (R2-01)

**Cut every label that names the artefact instead of the content.**
"PLAIN-LANGUAGE PARAPHRASE", "COURSE WORKING DEFINITION", "SECOND EDITION, 2020",
"Teaching synthesis", "Illustrative responsibilities", "These figures do not
measure how firms would answer the launch question." Each was written for a
reviewer, not a learner. Provenance belongs in the research brief and the
references; the slide is about the subject. (R2-05, R2-07, R2-12, R4-05, R4-08,
R4-09)

**Status labels that repeat their own group heading are noise.** A timeline under
"when each part applies" does not need every entry labelled APPLICABLE. (R5-12)

**Do not restate a point on a slide where it is not the point.** A caveat
belonging to another slide dilutes this one. (R5-04)

**Both language passes, every time.** `no-ai-slop` then `sg-english`, over slide
text as well as narration, and over every revision. Watch in particular for words
that read as machine-written to a Singapore audience — "defensible" was the one
Ray named.

## Motion and interaction

**Builds step on the learner's input, never on a timer.** Space or the forward
key reveals the next item in a `.stagger` group; once the group is complete the
next press advances the slide. A timed build forces the narrator's pace on
someone reading faster or slower, and cannot be re-watched in step. Leaving a
slide resets its build. (R4-01, R4-03, R5-08, R5-10)

**Pace motion to the voice, not the eye.** A narrator needs roughly 2.5 seconds
an item at 150 wpm. A stagger finishing in 1.3 seconds is decoration. (R3-06)

**Animate what the voice enumerates. Leave static what the learner reads at
once.** A list the narrator walks through builds. A definition, a quotation, a
decision record, a quiz's options and a reference block do not — a learner
choosing a quiz answer needs every option visible at the same time. (R3-03,
R3-18)

**An interaction must show its result unmistakably.** If clicking changes
something the learner has to hunt for, the interaction has failed. Selection is
drawn in the emphasis colour, the detail appears where the eye already is, and a
connector line ties it to what was clicked. (R2-10, R3-14, R5-09)

**Set the stage scale before first paint.** The engine emits a blocking head
script that sets `--stage-scale` and a `booting` class suppressing transitions
for the first frame. Without it the deck paints at 1920×1080 and snaps, which
reads as a shake on every slide. (R4-02)

**Every capture path must force the finished state.** With speech-paced motion a
screenshot or a PDF page catches a slide part-built. The `stills` body class is
applied by `?stills` and by `beforeprint`. Forgetting it produces contact sheets
of half-drawn slides.

## Colour

**One emphasis colour across the deck, named as a token.** A theme carries two
accents and they are not interchangeable. In `corporate-clean`, `--accent` is the
navy `#0a2540` for headlines and rules; `--accent-2` is the blue `#1d4ed8` for
emphasis — card headings, kickers, list numbers, highlight fills, selection
states.

```css
.tpl-course { --emphasis: var(--accent-2); }
.tpl-course .named-box h4, .tpl-course .op-label, … { color: var(--emphasis) }
```

A round-5 note that said "unify emphasis on the accent" was applied to
`--accent`, which removed the blue from the deck rather than standardising it.
Route every emphasis rule through one token, so a change of emphasis colour is
one line. **Verify by measurement** — read `getComputedStyle(el).color` back from
the built deck — not by eye. (R5-03, R5-06, R5-13)

## The deck as a whole

**The cover is one line.** Course title, then presenter name and credential,
series owner, and a contact address in the footer. No kicker. (R3-02)

**Repeated per-slide citations belong at the back.** A reference block on every
slide stops being read. Keep a source marker on the slide and put the full list
on a closing References slide. No "Sources xx" in the footer. (R3-01, R4-04)

**The takeaways one-pager carries every enumerated set the course taught.** If
the course taught five steps, six components and three questions, the learner
leaves with all three sets on one page. A takeaways slide that introduces a
fourth framing teaches a fourth thing at the end. (R3-12, R5-16)

**The deck has an overview.** Esc opens a grid of slides by `data-title`, so a
learner or a reviewer can see the shape without arrowing through it. (R3-05)

**The gate 2 sample is a design proof, not a draft deck.** One slide per layout
family, to show layouts and motion. Once it grows into a draft deck it has
stopped doing its job, and the accepted layouts belong in `index.html`. (R3-07)

## Evidence

**Prefer the most recent and most local evidence.** For a Singapore audience a
Singapore source outranks a UK one, and a 2026 source outranks a 2024 one. Where
only distant or older evidence exists, say so on the slide rather than letting it
pass as current. (R2-04)

**Date-stamp jurisdiction slides consistently.** If one carries "as at <date>",
they all do. A reader treats an undated slide as timeless. (R2-14)

**Every slide needs a connecting sentence in the script.** In a recorded course
the narrator must never read the slide title aloud to bridge from the previous
slide, or the recording reads as a sequence of captions. (R2-03)

---

## What is enforced, and what is not

`./scripts/check-slides.sh courses/<name>` measures rather than eyeballs. Exit 0
means every hard rule holds.

| Rule | Check |
|---|---|
| No text block over three lines | hard fail |
| Headline and body pinned on every slide | hard fail |
| No heading rendered twice | hard fail |
| Nothing overflows the 1080px stage | hard fail |
| No kicker repeats the line beneath it | hard fail |
| Every slide carries its number | hard fail |
| Nothing moves on quiz reveal | hard fail |
| Self-contained — no local subresources (Safari) | hard fail |
| Lower frame left empty | **warning** — a quote slide is legitimately sparse, so this is a list to walk at gate 3 |

Everything else on this page is judgement, and is checked by reading the deck.

## Adding to this page

When Ray gives design feedback, **write the rule down before applying it**:

1. Add it here in one sentence, with the reason and the `R#-##` code.
2. If it can be measured, add it to `scripts/check-slides.sh`.
3. **Prove the check fails.** Break the rule deliberately in a copy of the deck
   and confirm a non-zero exit. A check that only ever passes is worthless — the
   line-count check shipped broken because an inline element's bounding rect is
   its glyph box rather than lines × line-height, and only a deliberate failure
   exposed it.
4. Then fix the deck.

Applying feedback without recording it means relearning it on the next course.
