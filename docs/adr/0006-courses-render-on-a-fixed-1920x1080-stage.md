# Courses render on a fixed 1920x1080 stage

`base.css` sizes a deck to the viewport — `.deck{width:100vw;height:100vh}` and
`.slide{position:absolute;inset:0}` — while every type size is a fixed pixel
value (`.h2` is 54px, `.lede` 22px). That combination is the worst of both
models: the box reflows with the window but the type does not scale with it. The
same deck therefore looks materially different on a laptop and a monitor. A
headline wraps to two lines at one width and one line at another, which moves
everything below it, and content drifts horizontally as the measure changes.

PowerPoint does not have this problem because it has a **fixed canvas** and
scales the whole thing to the display. Courses now do the same. The deck is laid
out at exactly 1920x1080 and `assets/stage.js` sets a `--stage-scale` custom
property from `min(innerWidth/1920, innerHeight/1080)`; the CSS applies it as a
transform and letterboxes the remainder. What you position stays positioned, on
every screen, at every size.

Verified by rendering the same slide at 1920x1080, 1440x900 and 1280x1024: the
headline's left edge sits at 0.227 of frame width in the first two, and the 5:4
case scales the entire slide down and letterboxes it with proportions intact.

## Consequences

- Opt-in via `class="stage-fixed"` on `<body>`, which `assemble-course.sh` adds.
  Decks that want the old reflowing behaviour simply omit it, so nothing else in
  the repo changes.
- A new file rather than an edit to `runtime.js` or `base.css`, per ADR 0001.
- Letterbox bars use `--bg-soft` so they read as a margin rather than a border.
- Type can now be sized for a known canvas. Several components were sized for a
  reflowing viewport and read small at 1920; they were scaled up once the stage
  became fixed, which is only safe to do because the canvas no longer moves.
