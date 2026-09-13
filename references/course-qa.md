# Course QA rubric

Scores a built course against this workflow. Written for HTML courses produced by
[course-workflow.md](./course-workflow.md) and [slide-design.md](./slide-design.md),
for recorded delivery to executives.

It replaces a PPTX-era rubric that could not run here: half of that one's checks
were placeholder and master-slide rules that have no meaning in an HTML deck, and
its mechanical gate had to be skipped and replaced by hand. Everything below is
either measured by a script in this repo or judged against a rule written down in
this repo. **No criterion scores on taste alone.**

**This rubric evaluates. It does not rewrite.** Findings carry evidence; the fix
is a separate pass.

---

## Gate 0 — mechanical, before anything is scored

```bash
./scripts/build-course.sh courses/<name>     # must rebuild cleanly
./scripts/check-slides.sh courses/<name>     # must exit 0
python3 scripts/course/stamp-times.py courses/<name>/course.md
```

| # | Gate | How it is checked |
|---|---|---|
| G1 | Eight hard checks pass | `check-slides.sh` exits 0 |
| G2 | The deck rebuilds from source | `build-course.sh` runs without error — proves `index.html` was not hand-edited |
| G3 | Every slide cites only sources its narration declares | build guard in `engine.py` |
| G4 | Every cited source has a label | build guard in `engine.py` |
| G5 | Narration exists for every slide in the range | build guard in `engine.py` |
| G6 | Total runtime within budget | `stamp-times.py` total vs. the duration in `course.md` |
| G7 | No review labels left on slides | `REVIEW` in `slides.py` is empty |
| G8 | Self-contained | `grep -cE '(src\|href)="\.\.' index.html` returns 0 |

**A Gate 0 failure stops the review.** Do not score a deck that does not build,
and do not report a rubric percentage beside a broken gate — it reads as though
the deck is 78% acceptable when it is not acceptable at all.

## Scoring

Each dimension has five criteria. Each scores **0, 0.5 or 1**, so a dimension is
a percentage out of 5. The overall score is Σ (dimension % × weight).

| Weight | Dimension |
|---|---|
| 18% | 1 · Evidence and provenance |
| 16% | 2 · Outcomes and coverage |
| 14% | 3 · Teaching sequence and narration |
| 12% | 4 · Copy discipline |
| 12% | 5 · Visual fit and density |
| 10% | 6 · Deck furniture |
| 10% | 7 · Motion and interaction |
| 8% | 8 · Timing |

Evidence-heavy weighting is deliberate. On this workflow's first course the
failures that mattered were a statistic overstated as "most firms", a chronology
in the wrong order, and an inference presented as a finding — none of which any
layout check can see.

---

## 1 · Evidence and provenance — 18%

1. Every factual claim on a slide traces to a Finding (`R##`) or supplied
   material, or is marked illustrative.
2. No claim is stronger than its source. A 46% survey response is not "most
   firms"; a court declining to accept a defence is not the system "saving" the
   defendant.
3. Chronology and attribution are right: dates in order, the instrument named
   correctly, the regulator credited correctly.
4. Quiz answer keys cite, and the feedback on each wrong option is accurate
   rather than merely plausible.
5. Unverified items are visible as unverified — in the brief, on a review label,
   or on the slide — never silently promoted to fact.

> **Release blocker:** an unverified load-bearing claim on a slide, or a claim
> known to be wrong. Blocks regardless of the total score.

## 2 · Outcomes and coverage — 16%

1. Every learning outcome has teaching slides, and they are identifiable.
2. Every outcome has practice or assessment.
3. No orphan slides — every slide serves an outcome and carries `data-section`.
4. The course teaches its own subject before applying it. Concepts, scope and
   components come before jurisdictions and cases.
5. Scope holds: no section quietly becomes a different course (a governance
   overview is not a legal briefing).

## 3 · Teaching sequence and narration — 14%

1. **Every slide's script opens with a connecting sentence.** The narrator never
   reads the slide title aloud to bridge.
2. One slide, one idea. No slide carries three unrelated components.
3. A taxonomy does not contain the thing it categorises.
4. The script is speakable: 15–20 word sentences, one subordinate clause,
   no parenthetical asides.
5. Both language passes have been run over the script *and* the on-slide text —
   `no-ai-slop`, then `sg-english` — including every revision.

## 4 · Copy discipline — 12%

1. Headlines are claims, not lifted script fragments.
2. No kicker repeats the line beneath it. *(mechanical — check 5)*
3. No label names the artefact instead of the content: "PLAIN-LANGUAGE
   PARAPHRASE", "Teaching synthesis", "Illustrative responsibilities".
4. No hedge written for the reviewer rather than the learner.
5. British spelling, SG register, no Americanism or sports metaphor, no
   rhetorical question to the reader, and none of the named tics.

## 5 · Visual fit and density — 12%

1. The visual matches the content shape — list to list, chronology to table, one
   claim to the whole frame. *(the table in slide-design.md)*
2. No more than half the slides are card grids.
3. No text block over three lines. *(mechanical — check 1)*
4. The lower frame is used. *(mechanical — the sparse warning; a quote or cover
   slide is a legitimate exception, a card row is not)*
5. One emphasis colour, routed through one token, verified by reading computed
   styles rather than by eye.

## 6 · Deck furniture — 10%

1. Cover: one line, presenter and credential, series owner, contact address.
2. References at the back, with a marker on the slide and no per-slide block.
3. The takeaways one-pager carries every enumerated set the course taught.
4. Every slide numbered by course-slide number, cover included. *(mechanical)*
5. Esc opens the overview, and `data-title` is set on every slide.

## 7 · Motion and interaction — 10%

1. Builds step on the learner's input, never on a timer.
2. Motion is paced to the voice — roughly 2.5 seconds an item at 150 wpm.
3. What the voice enumerates animates; a definition, quotation, decision record,
   quiz or reference block does not.
4. Every interaction shows its result unmistakably, in the emphasis colour,
   where the eye already is.
5. Nothing moves on reveal *(mechanical — check 7)*, and every capture path
   forces the finished state.

## 8 · Timing — 8%

1. Every narration block carries a measured `**Time:**`, not an estimate.
2. The total is within the duration budget.
3. No single slide runs long enough to lose an executive audience — over ~2:00
   is a flag, not an automatic fail.
4. Declared pauses are real: a quiz that asks for 20 seconds has 20 seconds in
   its allowance.
5. Section allocations still match the outline, or the outline has been updated.

---

## Release blockers

Independent of the total. Any one of these means **not release-ready**:

- A Gate 0 failure.
- An unverified or known-wrong load-bearing claim on a slide.
- A review label still on a slide.
- A slide that traces to no outcome.
- Dimension 1 below 50%.

## Bands

| Score | Reading |
|---|---|
| 85–100% | Release-ready. Findings are refinements. |
| 70–84% | One revision round. Named sections, not a rebuild. |
| 55–69% | Substantial revision. Reopen the gate the failures belong to. |
| < 55% | Reopen the outline. |

A percentage is a summary, not a verdict — the blockers decide release.

## How to run a review

1. Run Gate 0. Stop if it fails.
2. Render every slide with `?stills` and read them. A rubric applied to source
   is a rubric applied to a deck nobody has seen.
3. Read `course.md` end to end as a script, aloud where the sentence is long.
4. Score each criterion with **evidence**: the slide number, the quoted line, and
   the rule or `R##` it violates. A criterion scored without evidence is not
   scored.
5. Verify the load-bearing claims against primary sources. Say which you could
   not reach. Never mark a claim verified because a prior brief marked it
   researched.
6. Write `courses/<name>/qa/REPORT.md`: summary and score, Gate 0 result,
   dimension tables, blockers, then findings ordered by severity.
7. Anything that generalises beyond this course goes into
   [slide-design.md](./slide-design.md) as a rule, and into `check-slides.sh` as
   a check that is proven to fail.

An independent reviewer — a fresh agent, or a second person — beats a self-review
by the author of the deck. The author scores what they meant; a reviewer scores
what is on the slide.
