# Contract for building one course section fragment

You are writing ONE HTML fragment for a recorded, self-paced executive course on
AI governance. Audience: business leaders in Singapore. Not practitioners, not
lawyers.

## The single most important rule

**Delivery is RECORDED.** A voiceover is read aloud from the script. Therefore:

- The script goes in `<div class="notes">` at the end of each slide's body. It is
  hidden from the audience and is what the narrator reads.
- **The slide shows the headline and the visual — never the script.** Printing
  the words while somebody reads them aloud is the worst way to present either.
- On-slide text is roughly one third of the script's length.

## Hard rules, machine-checked by scripts/check-slides.sh

1. **No text block exceeds 3 lines** when rendered at 1920x1080. Not a headline,
   not a callout, not a quiz option, not a table cell. If it runs to four, CUT
   WORDS. Never shrink type, never add inline styles to compensate.
2. Every slide has exactly this skeleton, in this order:
   ```html
   <section class="slide" data-section="N" data-title="Short title">
     <header class="slide-head">
       <p class="kicker">SHORT UPPERCASE LABEL</p>
       <h2 class="h2 mt-s">Headline sentence.</h2>
     </header>
     <div class="slide-body">
       ... visual components ...
       <div class="notes">the voiceover script for this slide</div>
     </div>
   </section>
   ```
3. Two spaces of indent before `<section`. No `<aside class="sidebar">`.
4. **Never write a colour, font-size, px value or hex code.** Every visual uses
   the component classes below. The only inline styles permitted are on `<table>`
   cells, copying the pattern from the exemplar exactly.

## Available component classes

- `.lede` — one short intro paragraph. Use sparingly; the voice usually covers it.
- `.callout` — a boxed emphasis line. `<b>` for the lead-in.
- `.concept-box` with `<h4>` and `<p class="dim">` — a card. Put 2 or 3 in a
  `<div class="grid g2">` or `g3`.
- `.layer-stack` > `.layer.is-binding` / `.is-expectation` / `.is-voluntary`,
  each containing `.layer-name` and `.layer-note` — stacked bands.
- `.pill-academic` — a small monospace tag, good for a source or a date.
- `.quiz` > `.mcq` (+ `data-correct` on the right one) each containing
  `.letter` and a div with `<b>` and `<p class="why">`, then `<p class="verdict"></p>`.
- `.roadmap` / `.rm-gate` / `.rm-join` / `.rm-tracks` / `.rm-track` / `.rm-beyond` —
  only for the roadmap slide.
- Spacing helpers: `mt-s`, `mt-m`, `mt-l`. Grid: `grid g2`, `grid g3`.
- Add `class="wide"` to `slide-head` AND `slide-body` only for a wide table.

## Choosing the visual — the most common failure

Do not default to a grid of concept boxes. On the first build of this course, 17
of 25 slides were box grids and several boxed two-word fragments.

- One claim that deserves the frame -> `quote-slide`, not a box.
- One number that carries the point -> `stat-row`, not a box.
- A named source saying something quotable -> `quote-slide`.
- Several things that apply at once -> `layer-stack` (NOT for a sequence).
- A chronology or a two-column comparison -> a table.
- Only genuinely parallel items of equal weight -> `concept-box` grid.

No more than half of your slides may be box grids.

**Headlines are claims, not the first sentence of the script.** "Your sector adds
to it." is a fragment. "Singapore finance: advisory, and still unissued." is a
headline.

## Copy rules

- **A kicker must not repeat the line beneath it.** If the headline says it, drop
  the kicker.
- **A list of things gets a list layout**, not boxes.
- **One slide, one idea.** No orphan lines that explain nothing on their own.
- **A category list must not contain the thing it categorises.**
- **Every slide's script opens with a connecting sentence** from the previous
  slide. The narrator must never need to read the title aloud.
- **Date-stamp jurisdiction slides consistently** — if one says "as at <date>",
  they all do.

## Quiz rules

- The answer key is `data-correct` on ONE option. Nothing else marks it.
- Every option needs a `<p class="why">` explaining why it is right or wrong —
  including the correct one. This feedback is the teaching.
- The stem describes CONDUCT and must not name the breach, or it gives the answer
  away.
- Questions test judgement, not recall.

## Language

British spelling throughout: organisation, recognise, licence, programme.
Formal, low-idiom Singapore Standard English. No American business idiom.
Never write "lands" for succeeds, "real" as an intensifier, or loose "with you"
attachments. No exclamation marks, no rhetorical questions to the reader.

## Evidence

Every factual claim, figure, quote and date must come from the supplied script
VERBATIM. Do not add facts, examples, figures or sources of your own. If the
script does not contain something, it does not go on the slide.

## Output

Write the fragment to the exact path given in your task. Nothing else. No
explanation, no markdown fences, no surrounding document — the file contains only
`<section>` elements.
