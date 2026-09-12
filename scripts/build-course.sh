#!/usr/bin/env bash
# html-ppt :: build-course.sh — assemble a course deck.
#
# Usage:
#   build-course.sh <course-dir>                 # full deck -> index.html
#   build-course.sh <course-dir> --sample 1,5,10 # selected slides -> sample.html
#
# Reads course.md (narration, sources), slides.py (compositions) and an optional
# style.css from the course directory. Everything reusable is in
# scripts/course/engine.py and templates/full-decks/course/.
set -euo pipefail
DIR="${1:-}"
[[ -n "$DIR" ]] || { echo "usage: build-course.sh <course-dir> [--sample N,N,N]" >&2; exit 1; }
HERE="$(cd "$(dirname "$0")" && pwd)"
if [[ "${2:-}" == "--sample" ]]; then
  python3 -c "
import sys; sys.path.insert(0,'$HERE/course')
import engine
engine.build('$DIR', out_name='sample.html', only=[int(x) for x in '${3:-}'.split(',') if x])
"
else
  python3 -c "
import sys; sys.path.insert(0,'$HERE/course')
import engine
engine.build('$DIR')
"
fi
