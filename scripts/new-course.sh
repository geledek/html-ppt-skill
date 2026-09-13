#!/usr/bin/env bash
# html-ppt :: new-course.sh — scaffold a course for the three-gate workflow.
#
# Usage:  new-course.sh <name> [series]
#
# Creates courses/<name>/ with course.md (narration and sources), slides.py
# (compositions) and style.css (course-specific CSS only — shared components live
# in templates/full-decks/course/style.css).
#
# Build with:  ./scripts/build-course.sh courses/<name>
# Check with:  ./scripts/check-slides.sh courses/<name>
set -euo pipefail

NAME="${1:-}"; SERIES="${2:-}"
[[ -n "$NAME" ]] || { echo "usage: new-course.sh <name> [series]" >&2; exit 1; }
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$HERE/courses/$NAME"
[[ -e "$DIR" ]] && { echo "error: $DIR already exists" >&2; exit 1; }
mkdir -p "$DIR"

SERIES_LINE=""; [[ -n "$SERIES" ]] && SERIES_LINE="series: $SERIES"

cat > "$DIR/course.md" <<MD
---
title: $NAME
${SERIES_LINE}
template: course
theme: corporate-clean
lang: en
delivery:          # presenter-led | self-paced | recorded  (gate 1)
rate:              # 150 spoken wpm · 250 silent reading
duration:          # minutes
accepted_hash:     # set at gate 3
---

# $NAME

## Audience & outcomes

<!-- Who is this for, and what can they do afterwards that they could not before?
     State the delivery mode and its consequences back to the human. -->

## Research Brief

<!-- One \`### Rnn · Title\` entry per source. Each carries the claim, a direct
     quote, the URL and the date. A Finding without a traceable source is not a
     Finding. Every Rnn cited by a slide must appear here, or the build fails. -->

### R00 · Illustrations and teaching synthesis

Hypothetical examples and recommended controls, identified as such and not
attributed to any decision or regulator.

## Outline

| # | Slide | Min | Teaching intent | Sources | Outline | Narration | Slides |
|---|-------|-----|-----------------|---------|---------|-----------|--------|
| 1 |       |     |                 |         | pending | pending   | pending |

## Narration

<!-- One block per slide. The build reads these, so the numbering must match
     slides.py. Every slide's script opens with a connecting sentence from the
     previous slide — a narrator must never read the title aloud to bridge. -->

#### 01 · Cover

**Sources:** [R00]

**Narration:**
MD

cat > "$DIR/slides.py" <<'PY'
"""Audience-facing slide compositions.

Narration, sources and the outline live in course.md. Shared components live in
templates/full-decks/course/style.css — read that before inventing a new one.
Build with scripts/build-course.sh.

Shared components (templates/full-decks/course/style.css): q-list (numbered
list), stagger (builds one item at a time), concept-box in grid g2/g3,
case-quote, quiz, roadmap, stat-row, ul.check, world map.

courses/ai-governance-overview/style.css adds legal-row, lifecycle,
case-timeline and implementation. Those are that course's own. Copy one in and
promote it to the template if a second course needs it.

Rules the build and the checker enforce:
  * no text block over three lines at 1920x1080
  * a slide may only cite sources its narration block declares
  * animate what the voice enumerates; leave quizzes and records static
"""

SECTION_BOUNDS = [99]          # last course-slide number in each section

SOURCE_LABELS = {
 'R00': ('Hypothetical example · course teaching synthesis', None),
}


def question(options, cls='legal-quiz'):
    rows = []
    for i, (answer, feedback, correct) in enumerate(options):
        rows.append(f'<button type="button" class="mcq"' + (' data-correct' if correct else '') +
                    f'><span class="letter">{chr(65+i)}</span><span><b>{answer}</b>'
                    f'<span class="why">{feedback}</span></span></button>')
    return f'<div class="quiz {cls}" aria-label="Choose one answer">' + ''.join(rows) + \
           '<p class="verdict" aria-live="polite"></p></div>'


# (course slide, kicker, heading, composition, source IDs)
SLIDES = [
(1, '', 'Course title', '''<div class="cover-main">
  <p class="cover-series">Series · Client</p>
  <h1 class="cover-title">Course title</h1>
  <div class="cover-rule"></div>
  <p class="cover-by">Presenter name</p>
  <p class="cover-role">Role, organisation</p>
</div><div class="cover-foot"><span>contact@example.com</span><span>30 minutes · recorded</span></div>''', []),
]
PY

cat > "$DIR/style.css" <<'CSS'
/* Course-specific styles only.
   Shared components live in templates/full-decks/course/style.css — check there
   before adding anything here, and promote anything reusable back into it. */
CSS

echo "✔ created $DIR"
echo ""
echo "next:"
echo "  1. gate 1 — audience, outcomes, delivery mode, research, outline"
echo "  2. gate 2 — narration, then compositions in slides.py"
echo "  3. $HERE/scripts/build-course.sh courses/$NAME"
echo "     $HERE/scripts/check-slides.sh courses/$NAME"
