---
series: ai-for-business-leaders
template: course
theme: corporate-clean
themes: corporate-clean,minimal-white,swiss-grid,academic-paper,course-warm
lang: en
---

# AI for Business Leaders

A Series. It shares one audience, one Research Brief, one Theme and one Template,
and makes no claim yet about whether its members are sittings of one Course or
Courses in their own right. That is settled once both Outlines exist and can be
compared. The test is whether session 2 makes sense to
someone who missed session 1.

## Members

| Course | Duration | Delivery | Status |
|---|---|---|---|
| `ai-governance-overview` | 30 min | self-paced | camera-ready set delivered; `accepted_hash` not yet recorded |
| `ai-value-management` | 30 min | recorded | gate 2; 28 slides, narration in `script.md`, awaiting acceptance |

Directories are flat and unprefixed. ADR 0004 suggests `<series>-NN-name`;
`ai-governance-overview` was named and committed before the Series existed, and
renaming a course that already has an approved gate is not worth the churn.

The two Courses differ in Delivery Mode on purpose, and that is the one input a
Series does **not** share. Governance renders its Narration on-slide; Value
keeps Narration outside the deck as a voiceover script. Do not copy slide shapes
between them without re-checking where the teaching content lives.

## Shared audience

**Business leaders — executives and senior decision-makers, not practitioners.**
They approve AI spend, answer to a board, and carry the risk. They are not
lawyers, not data scientists, and will not read a regulation or a model card.

What follows from that, across every Course in the Series:

- A leader's unit of action is a **decision**: fund, stop, reassign, escalate,
  ask a harder question. Teaching material that ends in awareness has failed.
- They have delegated the detail and cannot audit it. So the useful skill is
  knowing **which question exposes the gap**, not knowing the answer.
- They are time-poor and will not return. One sitting, self-contained.

## Shared Research Brief

Findings established once for the Series. Each carries the quote and the URL it
came from. Course-specific Findings live in that Course's own brief.

<!-- Populated as Series-wide Findings are established. The governance course's
     jurisdiction and enforcement findings are specific to it and stay in
     courses/ai-governance-overview/course.md. -->

_None yet. `ai-governance-overview` was researched before the Series existed; its
Findings were not promoted here because they are jurisdiction-specific and no
second Course needs them._

## Shared terminology

Words that must not drift between Courses. The renderer vocabulary is in
[../CONTEXT.md](../CONTEXT.md); this is the teaching vocabulary the audience
hears.

| Term | Means | Avoid |
|---|---|---|
| **use** | one concrete application of AI in one process, the unit both Courses assess | use case, initiative |
| **owner** | the named person accountable for a use, by name and role | stakeholder, champion |
| **the board** | whoever the leader answers to | leadership, the business |
| **baseline** | the measure of a process recorded before the tool is used, against which any benefit is judged | before-and-after guess |
| **benefit owner** | the named person accountable for the benefit, not for the deployment | project sponsor, product owner |
| **cashable saving** | a saving that releases budget and would survive an impartial third party's review | efficiency, productivity gain |

<!-- The value terms (baseline, benefit owner, cashable saving) are now in the
     table, defined by the Value course. A third Course in the Series inherits
     them; add new shared terms here as they are defined, not per Course. -->
