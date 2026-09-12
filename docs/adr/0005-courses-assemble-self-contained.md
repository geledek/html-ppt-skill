# Courses assemble to one self-contained file

`assemble-course.sh` inlines every stylesheet and script into `index.html`
instead of linking `../../assets/*` the way every other deck in this repo does.
That looks wrong against the repo's idiom, so: two separate things break a
linked build, and both bite the audience rather than the author.

**Safari refuses to load `file://` subresources from parent directories.** A
course at `courses/<name>/index.html` references `../../assets/…`, two levels up.
Safari silently drops all of it and renders an unstyled page. Chrome permits it,
which is why `render.sh` — headless Chrome — produced perfect screenshots of a
file that was broken in the default macOS browser.

**A Course is a deliverable.** It gets emailed, copied to a share drive, and
opened on a machine that has never seen this repository. Relative paths out of
the course directory guarantee it arrives broken. Decks in `examples/` and
`templates/` do not have this problem in practice because they are opened in
place, by their author.

The payload is ~72KB of CSS and JS, so there is no size argument against
inlining. Webfonts stay remote; every token stack declares a local fallback.

## Consequences

- `T` theme cycling does not work in a self-contained build — there are no theme
  files to swap to. The output omits `data-themes` so the key stays inert rather
  than breaking the page. The Theme is chosen at gate 1 and proven at gate 2,
  so cycling is an authoring affordance, not a learner one.
- `assemble-course.sh <dir> --linked` keeps the old behaviour for design
  iteration, where auditioning themes with `T` is the point. Never ship it.
- The same Safari limitation affects `templates/full-decks/*/index.html`
  (`../../../assets/`) and `examples/*`. Left alone: upstream-tracked, and
  authors open those in place. Worth knowing when someone reports an unstyled
  template.
