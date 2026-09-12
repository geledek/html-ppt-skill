#!/usr/bin/env bash
# html-ppt :: new-course.sh — scaffold a Course for the three-gate workflow
#
# Usage:
#   new-course.sh <name> [series]
#
# Creates courses/<name>/{course.md,sections/} in the CURRENT WORKING DIRECTORY's
# repo root — not inside the installed skill. Courses are deliverables; the skill
# is source. See docs/adr/0001.
#
# Run scripts/assemble-course.sh <course-dir> once sections exist.

set -euo pipefail

NAME="${1:-}"
SERIES="${2:-}"
if [[ -z "$NAME" ]]; then
  echo "usage: new-course.sh <name> [series]" >&2
  exit 1
fi

HERE="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$HERE/courses/$NAME"

if [[ -e "$DIR" ]]; then
  echo "error: $DIR already exists" >&2
  exit 1
fi
mkdir -p "$DIR/sections"

SERIES_LINE=""
[[ -n "$SERIES" ]] && SERIES_LINE="series: $SERIES"

cat > "$DIR/course.md" <<MD
---
title: $NAME
${SERIES_LINE}
template: course
theme: course-warm
themes: course-warm,academic-paper,minimal-white,tokyo-night,swiss-grid
lang: en
delivery:          # presenter-led | self-paced | recorded  (gate 1)
rate:              # words/min — 150 spoken EN, 220 字 spoken CN, 250 silent read
duration:          # minutes
accepted_hash:     # set at gate 3; a mismatch means index.html has diverged
---

# $NAME

## Audience & outcomes

<!-- gate 1 input. Who is this for, and what can they do afterwards that they
     could not before? -->

## Research Brief

<!-- Findings, each with the quote and URL it came from. A Finding without a
     traceable source is not a Finding. Claims in Narration must trace here or
     to supplied material, or be marked illustrative. Quiz answer keys cite. -->

## Outline

<!-- Approved at gate 1, together with the Research Brief above.
     Strategy: concept-first | example-first | problem-first -->

| # | Section | Min | Teaching intent | Findings | Outline | Narration | Slides |
|---|---------|-----|-----------------|----------|---------|-----------|--------|
| 1 |         |     |                 |          | pending | pending   | pending |

<!-- Per-Section status is the gate. A gate passes when every Section has passed
     it. Changing a Section's outline marks that Section's narration and slides
     stale — and nothing else. -->

## Narration

<!-- One script for the whole course, organised by Section, written against the
     minute budgets above. Edit directly; hand-edits are detected by hash. -->

### 1.

MD

echo "✔ created $DIR"
echo ""
echo "next:"
echo "  1. gate 1 — fill audience/outcomes/delivery/duration, research, outline"
echo "  2. gate 2 — narration + render the representative section"
echo "  3. $HERE/scripts/assemble-course.sh $DIR"
