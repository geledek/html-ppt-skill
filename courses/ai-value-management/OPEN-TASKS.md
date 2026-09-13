# AI Value Management — open tasks

As at 13 September 2026, branch `course/ai-value-management`, commit `7757f69`.
Remove each item when it is done. Delete this file at acceptance.

## State

- **Gate 1** approved. Research Brief R00–R39, Outline A.
- **Gate 2** narration drafted for all 33 slides, both language passes applied.
  3,348 words, about 22.3 minutes of speech at 150 wpm.
- **Slides** built for all 33, plus a generated References slide. All eight hard
  checks pass. Not yet approved.
- Review with `courses/ai-value-management/SCRIPT.md` beside `index.html`.

## Before anything else

1. **Merge `origin/main`.** Two commits are not on this branch: a QA rubric
   (`references/course-qa.md`) and speaking-rate timing
   (`scripts/course/stamp-times.py`, which reads `rate:` instead of assuming
   150 wpm). This course sets `rate: 117`, so timings will change. It is a merge,
   not a fast-forward, because this branch has its own commits.
   Then rebuild, rerun `./scripts/check-slides.sh courses/ai-value-management`,
   and run the new QA rubric.

## Ray's review

2. **Review the script and slides together.** Compare `course.md` against
   `7757f69` so only Ray's edits show. Any edited narration goes back through
   `no-ai-slop` then `sg-english`.
3. **Confirm the judgement calls** raised at gate 2:
   - S1–S2 spend six minutes on the 95 per cent figure before teaching. If too
     long, merge S2 into S1 and give the time to S4 and S8.
   - Outcome 4 carries two minutes at the end. Enough weight?
   - The level of candour about sources: MIT's method, RAND's mis-citation,
     the Workhelix disclosure.
   - Slide 14 refers to "the companion session". Remove if the governance course
     will not reach the same audience.
   - Slide 33 carries every enumerated set, per the design guide, although the
     narration speaks only the do and stop lists.

## Content gaps

4. **S7 has no quiz.** Needs a narration block and a slide. Adding it renumbers
   S7 and S8, and moves `SECTION_BOUNDS` in `slides.py`.
5. **Verify the podcast quotes against audio.** They were taken from
   auto-generated captions. Slide 25's callout, "He calls the original article
   balanced", rests on:
   - Big Technology Podcast, 16 May 2025, at 01:29
   - 20VC, 16 February 2026, at 00:18:15
6. **Slide 22's four breaks are the course's own synthesis** across four studies
   (R13, R19, R20, R18). The narration does not say so, unlike slide 13's stages.
   Decide whether it should.
7. **Brief wording.** R22 is titled "the audited record" and R39 says "audited
   filing". The US$59m saving sits in Klarna's 20-F but is not an audited figure.
   The narration was corrected; the brief was not.
8. **Klarna headcount discrepancy stays off the slides.** His spoken peak
   (6,000, 7,000, 7,400) does not reconcile with the filed 5,527. No source
   explains the gap.

## Housekeeping

9. **Series file** `courses/ai-for-business-leaders.md`: the Members table still
   shows this course at gate 1. Add the value terms both courses now use to the
   terminology table: baseline, benefit owner, cashable saving.
10. **Planning notes under Outcomes** in `course.md` are still conversational.
    Rewrite or delete.
11. **Gate 3:** record a content hash beside each approved section, then set
    `accepted_hash` for the accepted `index.html`.

## For `main`, not this branch

Found while building this course and patched only in its `style.css`. Each is
marked PROMOTION CANDIDATE there. Checked against `origin/main` on
13 September 2026; still open.

- **Quiz feedback never appears in the shared template.** `.mcq .why` is
  `display:none` and the reveal only sets `visibility`. The "nothing moves on
  reveal" check passes the broken template because nothing is ever revealed.
- **`--emphasis` is not defined in the template**, although `slide-design.md`
  makes the blue emphasis a deck-wide rule. New courses start with navy.
- **No table styling in the template**, although the guide says comparisons and
  chronologies get tables.
- **The overflow check missed content past the bottom.** Slide 33's last list
  item was cut off below the frame and the check passed. Needs a check proven to
  fail on that case.
- **`.quote-slide` cannot be set from `slides.py`.** The engine always writes a
  plain `<section class="slide">`.
- **Sample builds number slides against the sample's size** ("23 / 30") rather
  than the course's.
