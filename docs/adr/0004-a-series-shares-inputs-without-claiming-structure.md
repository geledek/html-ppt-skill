# A Series shares inputs without claiming structure

Two related sessions may turn out to be one Course taught across two sittings, or
two Courses that each stand alone — and that is usually not knowable until both
Outlines exist and can be compared side by side. Committing early is expensive in
both directions: build two independent Courses and the Research Brief gets made
twice, terminology drifts and themes diverge; build one Course with two Sessions
and you have invented cross-deck navigation and progress for a relationship that
may not hold.

So a **Series** (`courses/<series>.md`) shares only the inputs that are expensive
to unify later — one audience, one Research Brief, one Theme, one Template — and
deliberately makes no claim about the structural relationship between its
members. Each Course still assembles and ships independently. The test for
settling it, once the Outlines exist: *does session 2 make sense to someone who
missed session 1?* If no, they are one Course.

## Consequences

- Session 2's gate 1 mostly skips research: the brief exists, so the Research
  Plan becomes "what does this session need that the brief does not cover?"
  That saving is what the Series is for.
- Series members stay **flat** — `courses/<series>-01-name/`, not
  `courses/<series>/01-name/`. Nesting would put `index.html` three deep and
  forfeit the `../../assets/` prefix that ADR 0001 exists to preserve.
- Promoting several Courses into one Course with several Decks is later a
  grouping change over Section fragments that already exist (ADR 0002), so
  nothing here is a one-way door.
