---
name: review-slide
description: Review one built course slide against its script, one slide at a time, with a screenshot. Use when the user asks to "review slide N", "review the deck slide by slide", "go through the slides", or is walking a course deck slide by slide checking the slide against the narration. Drives the built HTML deck over a local HTTP server with Playwright, shows the script block, gives a concise slide-vs-script review, proposes improvements, and waits for approval before editing.
---

# Reviewing a course slide against its script

Walk a course deck one slide at a time. For each slide: show the script, screenshot
the built slide, give a tight review, propose improvements, and **wait for approval
before changing anything**. Stay on the same slide until the user says to move on.

This skill assumes the `html-ppt` course workflow. The deck builds from `slides.py`
(on-slide composition), `script.md` (narration, deck-numbered blocks) and `style.css`;
`index.html` and `sections/` are generated — never hand-edit them.

## Per-slide loop

For slide **N**:

1. **Screenshot the built slide.** Serve the course folder over HTTP and open
   `index.html` with `?stills` (forces the finished build state) and the hash route
   `#/N`. Capture at 1920×1080.
   - Start the server once (reuse it across slides): from the course dir,
     `python3 -m http.server <port>` in the background; verify `index.html` returns 200.
   - `file://` is blocked in the browser tool — always go through HTTP.
   - Use a fresh cache-buster (`&v=<n>`) after every rebuild, or the browser serves
     a stale copy.
   - Read the saved PNG to actually look at the render.

2. **Show the script.** Read the matching `#### NN · <title>` block from `script.md`
   (deck-numbered) and quote its Narration verbatim. If the deck slide count differs
   from the script, deck slide N maps to the Nth `####` block — confirm by title, not
   by assuming N==N.

3. **Concise review — slide vs script.** Keep it tight. Cover only what matters:
   - **Lesson:** one line — what the learner should take away.
   - **Consistency:** does the on-slide text agree with the narration? Flag numbers
     that disagree, claims on one but not the other, caveats that leaked from another
     slide.
   - **AI-slop / clarity:** stage directions the narrator reads aloud ("on screen",
     "as you can see"), jargon that's opaque cold on a slide, hedges, binary contrasts,
     em-dash rhythm crutches. Run the two language passes in spirit: `no-ai-slop` then
     `sg-english`.
   - **Design:** against `references/slide-design.md` — one idea per slide, right
     visual for the content shape, one emphasis colour, ≤3 lines per block, lower
     frame filled, kicker doesn't restate the headline, quiz reveal moves nothing.
   Don't pad. If a slide is clean, say so in a sentence and stop.

4. **Ideas to improve either** the slide or the script — concrete, specific, and
   tied to the lesson. Say which file each change touches (`slides.py`, `style.css`,
   `script.md`). Prefer the fix that makes the slide teach its objective on its own.

5. **Ask for approval before editing.** Use AskUserQuestion when there's a real choice
   (wording, layout, what to cut); otherwise state the proposed change and ask to
   proceed. **Do not edit until the user approves.**

6. **If changes are approved, stay on this slide.** Apply the edit, rebuild, re-run
   the checks, re-screenshot, and show the result. Iterate on the *same* slide until
   the user says "next slide" (or names another). Only then advance.

## After any edit

- Rebuild: `./scripts/build-course.sh courses/<name>` (run it inside the worktree
  that holds `slides.py`, not from `main`).
- If `script.md` changed, restamp times: `python3 scripts/course/stamp-times.py courses/<name>`.
- Run `./scripts/check-slides.sh courses/<name>` — exit 0 means the measurable rules
  hold. Fix any FAIL before showing the slide as done. The lower-frame warning is a
  judgement call, not a fail.
- Both language passes over any prose you changed (`no-ai-slop` then `sg-english`),
  on-slide text and narration alike.

## Committing

Commit per slide when the user is happy, on the course branch, never pushing unprompted.
One commit per slide with a message saying what changed and why.

## House rules that bite (from CLAUDE.md and slide-design.md)

- The deck's narration source is the course's `script.md` (deck-numbered), not any
  stale top-level `SCRIPT.md`. Review against what actually builds.
- Builds step on the learner's input, never a timer: a `.stagger` group reveals on
  Space/arrow; `?stills` and print force the finished state.
- One emphasis colour (the blue). Red (`--bad`) is the negative/caveat colour only.
- Teaching content belongs in the voice; a lesson line that escaped onto the slide is
  narration — check the script before deleting, and if it's already spoken the slide
  loses nothing.
- When the user gives a design rule, record it in `references/slide-design.md` (with a
  measurable check in `scripts/check-slides.sh` where possible) **before** applying it.
