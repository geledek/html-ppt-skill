# Courses assemble from per-section fragments

`SKILL.md` advertises the skill as "One command, no build. Pure static
HTML/CSS/JS", so a build step inside it looks wrong at first glance. We added one
anyway for Courses: Section slides live in `courses/<name>/sections/NN.html` and
`scripts/assemble-course.sh` concatenates them into `index.html`. The reason is
context, not tidiness — Courses support Section-scoped revision (ADR: see
`CONTEXT.md` "Stale"), and with a monolithic `index.html` every section-level
edit would mean reading a ~60-slide file into a model's context to locate the
edit site, repeatedly, with the cost growing exactly as the course gets long
enough for revision to matter. With fragments, regenerating one Section writes
one small file and never reads the rest of the Course.

## Consequences

- The *deliverable* is unchanged: a single static `index.html` that opens with no
  toolchain. Assembly is authoring-time, like the existing `render.sh`.
- The Section→Slide map is true by construction — it is the directory listing —
  rather than bookkeeping that can drift.
- Hand-edits to `index.html` are clobbered on the next assembly. `index.html`
  carries a generated-file banner pointing at `course.md` and `sections/`.
  This matches the workflow: narration is edited directly, slides are revised
  through the skill.
