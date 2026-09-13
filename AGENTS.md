# Working in this repository

## The repository is a fork

`origin` is `geledek/html-ppt-skill` (ours). `upstream` is `lewislulu/html-ppt-skill`.
**Push to `origin` only.** Prefer adding new files over editing upstream-tracked
ones, so the fork keeps merging cleanly.

## Branches and worktrees

| Work | Where |
|---|---|
| The skill — workflow, design guide, templates, scripts | `main` |
| A course | its own worktree, branch `course/<name>` |

```bash
git worktree add .Codex/worktrees/<name> -b course/<name> main
```

**One worktree per course**, under `.Codex/worktrees/` (git-excluded), so two
courses can be in flight without one's half-built deck showing up in the other's
diff. Start it from `main` and fast-forward it when the skill moves:

```bash
git -C .Codex/worktrees/<name> merge --ff-only main
```

Skill improvements found while building a course belong on `main`, not on the
course branch — that is how the next course inherits them.

**Commit when asked, and offer a commit at a gate. Never push unprompted.**

## Building a course

Read [references/course-workflow.md](references/course-workflow.md) for the three
gates and [references/slide-design.md](references/slide-design.md) for the design
rules **before composing any slide**. The design guide is the consolidated
feedback from every review round; each rule carries the code of the round that
produced it.

The rules that get broken most often when they are not read:

- **`index.html`, `sample.html` and `sections/` are generated.** Never hand-edit
  them. Edit `course.md`, `slides.py` or `style.css` and rebuild.
- **Both language passes, in order, over every piece of prose** — `no-ai-slop`
  then `sg-english` — including revisions, and including on-slide text as well as
  narration.
- **The build is self-contained** (docs/adr/0005). Safari refuses `file://`
  subresources from parent directories, so a linked build renders completely
  unstyled in the default macOS browser while looking perfect in headless Chrome.
  Never review a course only in Chrome.
- **Run `./scripts/check-slides.sh courses/<name>` before every review.** Eight
  hard checks and one warning; exit 0 means the measurable rules hold.

## When Ray gives design feedback

Write the rule down **before** applying it:

1. Record it in `references/slide-design.md`, one sentence with the reason.
2. If it can be measured, add a check to `scripts/check-slides.sh`.
3. **Prove the check fails** on a deliberate violation. A check that only ever
   passes is worthless — the line-count check shipped broken and only a
   deliberate failure exposed it.
4. Then fix the deck.

Applying feedback without recording it means relearning it on the next course.
