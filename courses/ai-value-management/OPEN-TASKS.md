# AI Value Management — open tasks

Updated 14 September 2026, branch `course/ai-value-management`.
Remove each item when it is done. Delete this file at acceptance.

## State

- **Gate 1** approved. Research Brief R00–R39, Outline A.
- **Gate 2** narration for all slides, both language passes applied.
- **Cut 33 → 28 slides** and extracted the narration into `script.md`; `course.md`
  now holds the brief, outline and frontmatter only. Runtime 25:44 at `rate: 117`.
- Bar charts on slides 3, 13, 25; per-figure trend/gap lines on the stat slides.
- All eight hard checks pass. **Not yet accepted (Gate 3 pending).**
- Review with `courses/ai-value-management/script.md` beside `index.html`.

## Ray's review — still open

1. **Judgement calls from gate 2 that remain:**
   - `script.md:182` still says "the companion session covers them" (governance
     obligations). Remove if the governance course will not reach the same audience.
   - The one-pager (slide 28) carries every enumerated set per the design guide,
     though the narration speaks only the do and stop lists. Confirm that is wanted.
   - Whether any of the closing sections (S2, S7, S8) want a quiz. After the cut the
     quizzes sit in S1, S3, S4, S5, S6; S7 and S8 are deliberately tight (2 slides).
     The old "S7 has no quiz" task is superseded by this question.

## Content / provenance — still open

2. **Verify the podcast quotes against audio.** Taken from auto-generated captions.
   Slide 20's callout, "He calls the original article balanced" (`slides.py`, and
   `script.md:326`), rests on:
   - Big Technology Podcast, 16 May 2025, at 01:29
   - 20VC, 16 February 2026, at 00:18:15
3. **Slide 17's four breaks are the course's own synthesis** across four studies
   (R13, R19, R20, R18). The narration does not label them as ours, unlike the four
   stages on slide 10. Decide whether it should.
4. **Brief wording.** R22 is titled "the audited record" and R39 says "audited
   filing". The US$59m saving sits in Klarna's 20-F but is not an audited figure.
   The narration was corrected; the brief (`course.md`) was not.
5. **Klarna headcount discrepancy stays off the slides.** His spoken peak
   (6,000, 7,000, 7,400) does not reconcile with the filed 5,527. No source
   explains the gap.

## Housekeeping — still open

6. **Series file** `courses/ai-for-business-leaders.md`: the Members table still
   shows this course at gate 1. Add the value terms both courses now use to the
   terminology table: baseline, benefit owner, cashable saving.
7. **Planning notes under Outcomes** in `course.md` are still conversational
   ("Outcome 4 is what makes this a course for executives…"). Rewrite or delete.
8. **Gate 3:** record a content hash beside each accepted section, then set
   `accepted_hash` for the accepted `index.html`.

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
