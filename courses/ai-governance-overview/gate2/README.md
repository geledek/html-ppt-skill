# Revised Gate 2 sample

18 selected slides from the proposed 30-slide course: **1–14, 16, 18, 26, 30**.
Original course numbers are retained. This is a review sample, not an accepted or complete replacement for `index.html`.

## Files and regeneration

- `../course.md`: outline, source ledger and all 30 narration passages.
- `slides.py`: audience-facing markup extracted from the narration.
- `style.css`: course-specific compositions using the existing template/theme.
- `build.py`: assembles `../sample.html`, `sections/*.html` and `manifest.json`.
- `verify.mjs`: renders every sample slide, checks text bounds, quiz stability and navigation, map controls, and exports `../sample.pdf`.
- `checks.json`, `contact-*.jpg`, `pdf-contact-*.jpg`: verification record and visual review sheets.
- `../FEEDBACK.md`: disposition of each user comment.

From the repository root:

```sh
python3 courses/ai-governance-overview/gate2/build.py
./scripts/check-slides.sh courses/ai-governance-overview/sample.html
node courses/ai-governance-overview/gate2/verify.mjs
```

The verifier uses Node's built-in WebSocket and an isolated local Chrome profile. Its PDF-operation marker path is environment-specific. Chrome needs permission to launch outside the restricted sandbox. Screenshots are generated under ignored `render/`; contact sheets are retained for review.

Open `../sample.html` in a browser. Arrow keys navigate. On quiz slides, the first forward advance reveals the answer and the next advances. Clicking an option also reveals feedback. On the map slide, click a jurisdiction to emphasise it; click again to restore the full state. PDF exports reveal answers and show the complete static map. Presenter notes are sourced directly from `course.md` and excluded from the PDF.

Do not edit generated sample HTML or fragments. The existing full deck and its source fragments remain at the committed baseline pending sample review.
