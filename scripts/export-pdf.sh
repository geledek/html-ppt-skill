#!/usr/bin/env bash
# html-ppt :: export-pdf.sh — a course deck as a 1920x1080 PDF, one slide a page.
#
# Usage:
#   export-pdf.sh <course-dir|html> [out.pdf]
#
# ?stills forces every build to its finished state, so a slide that reveals on
# input is printed complete rather than half-drawn. The print stylesheet lays the
# slides out one per page at the full stage size; without it Chrome prints the
# single visible slide on Letter.
set -euo pipefail

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || { echo "error: Chrome not found at $CHROME" >&2; exit 1; }

TARGET="${1:-}"
[[ -n "$TARGET" ]] || { echo "usage: export-pdf.sh <course-dir|html> [out.pdf]" >&2; exit 1; }
[[ -d "$TARGET" ]] && TARGET="${TARGET%/}/index.html"
[[ -f "$TARGET" ]] || { echo "error: $TARGET not found" >&2; exit 1; }

ABS="$(cd "$(dirname "$TARGET")" && pwd)/$(basename "$TARGET")"
OUT="${2:-${ABS%.html}.pdf}"

"$CHROME" --headless=new --disable-gpu --no-sandbox \
  --virtual-time-budget=15000 --no-pdf-header-footer \
  --print-to-pdf="$OUT" "file://$ABS?stills" >/dev/null 2>&1

[[ -s "$OUT" ]] || { echo "error: no PDF written" >&2; exit 1; }
printf '%s (%s KB)\n' "$OUT" "$(( $(wc -c < "$OUT") / 1024 ))"
