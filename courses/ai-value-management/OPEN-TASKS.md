# AI Value Management — open tasks

Updated 14 September 2026, branch `course/ai-value-management`.
Remove each item when it is done. Delete this file at acceptance.

## State

- **Gate 1** approved. Research Brief R00–R39, Outline A.
- **Gate 2** narration for all slides, both language passes applied.
- **Cut 33 → 28 slides**; narration extracted into `script.md`; `course.md` holds
  the brief, outline and frontmatter only. Runtime 25:44 at `rate: 117`.
- Bar charts on slides 3, 13, 25; per-figure trend/gap lines on the stat slides.
- All eight hard checks pass. **Not yet accepted (Gate 3 pending).**
- Review with `courses/ai-value-management/script.md` beside `index.html`.

## Still open — needs Ray

1. **Verify the podcast quotes against audio.** Taken from auto-generated captions;
   cannot be verified without the recordings. Slide 20's callout, "He calls the
   original article balanced" (`slides.py`, and `script.md`), rests on:
   - Big Technology Podcast, 16 May 2025, at ~01:29
   - 20VC, 16 February 2026, at ~00:18:15
   Corroborated across both appearances and the on-record Klarna denial, so the
   risk is low, but it should be confirmed before acceptance.
2. **Gate 3 acceptance.** Record a content hash beside each accepted section, then
   set `accepted_hash` for the accepted `index.html`.

## Standing guardrail — no action, do not undo

- **Klarna headcount discrepancy stays off the slides.** His spoken peak
  (6,000 / 7,000 / 7,400) does not reconcile with the filed 5,527. Verified absent
  from slides and narration; the filing table uses the filed figures. Keep it that
  way — do not add the spoken peak for effect.

## For `main`, not this branch

- **`.quote-slide` cannot be set from `slides.py`.** The engine always writes a
  plain `<section class="slide">`; the quote is sized via course CSS instead.
- **Sample builds may number slides against the sample's size** rather than the
  course's — re-check `render`/engine numbering when a sample is next built.
- **Promotion candidates from this session** (course-local, worth promoting so the
  next course inherits them): the `bars()` helper + `.bars` CSS; `stats()` trend/gap
  support + `.stat-trend` / `.stat-trend.down`; the two-colour `.quote-text mark`.

## Done (removed from the list)

Merged `origin/main`; promoted `--emphasis`, the quiz-reveal fix and table styling
into the template (with a proven check); added the content-past-bottom overflow
check; extracted the script; cut 33 → 28; ran the full-deck language pass.
Softened the "companion session" cross-reference; kept the one-pager and the
five-quiz cadence as-is (both match the design guide); left slide 17's four-break
synthesis unlabelled (R00 marker already in its refs); corrected the brief's
"audited" wording on the Klarna $59m saving; refreshed the series Members table
and terminology (baseline, benefit owner, cashable saving); deleted the
conversational planning note under Outcomes.
