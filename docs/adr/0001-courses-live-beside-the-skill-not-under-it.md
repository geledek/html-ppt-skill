# Courses live beside the skill, not under it

This repo is a fork (`upstream` = lewislulu/html-ppt-skill) whose root *is* the
skill — `SKILL.md` sits at the root and `.claude/skills/html-ppt` symlinks to
`../..`. When we added a course-authoring workflow we wanted a tidy
`skills/` + `courses/` split, but moving the skill into `skills/html-ppt/` would
have conflicted every file on every future `git pull upstream main`, broken the
hardcoded relative asset paths in 54 HTML files, and broken `npx skills add`,
which expects `SKILL.md` at the root. Instead `courses/` is a top-level sibling
of `examples/`: it sits at the same depth, so `../../assets/…` resolves
unchanged and `new-deck.sh`'s path-rewriting `sed` and `render.sh` work as-is.

## Considered Options

- **`courses/` at root, skill stays at root** — chosen. Free; upstream merges
  keep working. Cost is aesthetic: skill directories and `courses/` are siblings.
- **Full restructure to `skills/` + `courses/`** — rejected. Tidy, but forfeits
  cheap upstream merges permanently and requires 54 path rewrites.
- **`skills/html-ppt` as a submodule** — rejected. Tidy and merge-preserving,
  but the workspace and skill then version independently for no present gain.

## Consequences

If sibling slide skills are ever vendored here, revisit this — but skills
install globally to `~/.claude/skills/`, so that is unlikely.
