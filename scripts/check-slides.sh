#!/usr/bin/env bash
# html-ppt :: check-slides.sh — enforce the course layout rules automatically.
#
# Usage:  check-slides.sh <course-dir|html>
#
# These rules came from review feedback and are easy to re-break by hand, so they
# are measured rather than remembered:
#   1. No text block runs more than 3 lines.
#   2. Headline and body start at the same x and y on every slide.
#   3. Nothing moves when a quiz answer is revealed.
#   4. No local subresources — a linked build renders unstyled in Safari.
# Exit 0 if all pass, 1 otherwise. Run before every gate 3 review.

set -uo pipefail

TARGET="${1:-}"
[[ -n "$TARGET" ]] || { echo "usage: check-slides.sh <course-dir|html>" >&2; exit 1; }
[[ -d "$TARGET" ]] && TARGET="${TARGET%/}/index.html"
[[ -f "$TARGET" ]] || { echo "error: $TARGET not found" >&2; exit 1; }

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || { echo "error: Chrome not found at $CHROME" >&2; exit 1; }

ABS="$(cd "$(dirname "$TARGET")" && pwd)/$(basename "$TARGET")"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

LINKED="$(grep -cE '(src|href)="\.\.' "$ABS" || true)"

python3 "$(dirname "$0")/_slide_probe.py" "$ABS" "$TMP/probe.html"

JSON="$("$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=1920,1080 --virtual-time-budget=4000 --dump-dom "file://$TMP/probe.html" 2>/dev/null \
  | grep -o "<title>.*</title>" | head -1 | sed "s|<title>||; s|</title>||")"

[[ -n "$JSON" ]] || { echo "error: probe returned nothing (page failed to load?)" >&2; exit 1; }

JSON="$JSON" LINKED="$LINKED" python3 "$(dirname "$0")/_slide_report.py"
