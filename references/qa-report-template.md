# QA report — `<course>`

Copy this file to `courses/<name>/qa/REPORT.md` and fill it. Keep it short and
actionable: score at the dimension level, cite evidence **only for the misses**
(anything scoring below 1), and end with fixes ordered by severity. The rubric is
[course-qa.md](./course-qa.md); the mechanical gate is `check-slides.sh`, whose
console output stays separate from this report — this report only states the Gate 0
result, it does not reproduce the console dump.

---

**Course:** <title and ID>
**Version / date:** <version> · <DD Month YYYY>
**Reviewer:** <name or agent>
**Deck:** <N> slides (build's own count)
**Score:** <NN%> → **<band>**

## Gate 0 — <PASS | FAIL>

`check-slides.sh courses/<name>` <exit 0 | exit 1>. <One line: which gate failed, if any.>
**A Gate 0 failure stops the review — do not score below.**

## Dimension scores

| # | Dimension | Weight | Score | Misses (criterion → evidence: slide + rule/`R##`) |
|---|---|---|---|---|
| 1 | Evidence and provenance | 18% | <n/N> | <e.g. 1.2 — S8 shows Stanford bars without the success-only denominator (selection bias)> |
| 2 | Outcomes and coverage | 16% | <n/N> | <— if perfect, leave blank> |
| 3 | Teaching sequence and narration | 14% | <n/N> | |
| 4 | Copy discipline | 12% | <n/7> | |
| 5 | Visual fit and density | 12% | <n/6> | |
| 6 | Deck furniture | 10% | <n/N> | |
| 7 | Motion and interaction | 10% | <n/N> | |
| 8 | Timing | 8% | <n/N> | |

**Weighted overall:** Σ (dimension % × weight) = **<NN%>**. Band: **<band>**.

Only criteria that scored **below 1** need a row entry; a dimension with no misses
scores full and needs no evidence. This keeps the report about what to fix.

## Release blockers

<None — or list each: the blocker, the slide, why it blocks. Any one means NOT
release-ready regardless of score.>

## Findings — ordered by severity

**High**
1. <slide — the problem — the concrete fix>

**Medium**
2. <…>

**Low**
3. <…>

---

*Bands: 85–100 release-ready · 70–84 one revision round · 55–69 substantial
revision · <55 reopen the outline. The blockers decide release, not the number.*
