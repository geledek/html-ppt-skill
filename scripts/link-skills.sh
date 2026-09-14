#!/usr/bin/env bash
# html-ppt :: link-skills.sh — make this repo's skills global on this machine.
#
# Usage:  ./scripts/link-skills.sh
#
# The language skills (no-ai-slop, sg-english) are versioned in .claude/skills/
# so they sync between machines through git. Inside this repo they are found
# automatically; this links them into ~/.claude/skills so they also work in any
# other project. Links point at this checkout, so every `git pull` updates them.
# Safe to re-run: existing links are replaced, real directories are left alone
# and reported, since overwriting one could destroy an unversioned edit.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"

for skill in no-ai-slop sg-english; do
  src="$ROOT/.claude/skills/$skill"
  dst="$DEST/$skill"
  [[ -d "$src" ]] || { echo "missing in repo: $src" >&2; exit 1; }
  if [[ -L "$dst" ]]; then
    ln -sfn "$src" "$dst"; echo "relinked  $dst -> $src"
  elif [[ -e "$dst" ]]; then
    echo "SKIPPED   $dst is a real directory. Diff it against $src, then remove it and re-run." >&2
  else
    ln -s "$src" "$dst"; echo "linked    $dst -> $src"
  fi
done
