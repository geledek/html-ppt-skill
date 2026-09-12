# Gate 2 revision review

12 September 2026 · Ready for Ray's review · Not yet accepted

## Completed in the requested order

1. Reworked the outline around an introductory overview: concept, lifecycle, components, roles, jurisdictions, cases, sector application and implementation.
2. Rewrote all 30 narration passages in `course.md`, corrected the active source ledger and applied no-ai-slop followed by sg-english. The slide-by-slide disposition is in `../FEEDBACK.md`.
3. Built an 18-slide representative sample covering course slides 1–14, 16, 18, 26 and 30. The full deck remains at the committed baseline.

The scope change adds explicit definitions and components before legal comparisons. It brings the UK overview beside Singapore and the EU, gives cases backgrounds and specific lessons, connects the final decision visually to the opening, and ends with a practical roadmap.

## Verification

- Course template checker: passed self-containment, selected text line limits, fixed canvas geometry and sampled quiz stability.
- Browser render at 1920×1080: 18 slides plus two revealed quiz states, no reported bounds, line-count or body/source-overlap issues. See `checks.json`.
- Opening keyboard interaction: first advance reveals while staying on slide 2; second advances to slide 3.
- Map: all three labelled jurisdiction controls select and toggle off correctly. Checks exclude navigation thumbnails. Animation respects reduced motion.
- Visual review: inspected all sample slides and both quiz states in `contact-1.jpg` through `contact-4.jpg`.
- PDF: 18 pages, each 1440×810 points (16:9). All pages rasterised and inspected in `pdf-contact-1.jpg` through `pdf-contact-3.jpg`. Answers are revealed; source attributions remain within the frame; map is complete; presenter notes are excluded. Poppler emitted Type 3 glyph bounding-box warnings, but rendered text and glyphs showed no visible clipping or missing content.
- Opening the sample in a connected user browser was unavailable in this session; interactive checks ran in isolated Chrome instead.
- Sample notes are generated from the corresponding source narration. `manifest.json` records the course source and sample hashes.

## Timing and editorial pass

3,778 spoken words at 150 words/minute gives approximately 25.19 minutes of narration. The remaining 4.81 minutes are allocated to question pauses, diagram/case reading and transitions. Section estimates and counting method are in `timing.json`; this is not a timed rehearsal.

The language pass removed “you have company”, “many rulebooks”, “regulatory bite” and other ambiguous fragments. Sentences identify actors, actions and conditions. It retains necessary distinctions: policy versus law, supervisory consequences versus automatic fines, access exceptions versus disclosure, and operational losses versus enforcement. Questions requested by Ray are preserved. Definition paraphrases and course teaching syntheses are labelled rather than passed off as formal quotations.

## Matters for review and later release

- Review the 30-slide order and the alternatives proposed in `../FEEDBACK.md`, especially case consolidation and the replacement of the enforcement-outcome catalogue.
- The remaining 12 slides have revised narration but await the full build after sample review. News headline imagery is optional and not included in this sample.
- Source refresh limits are documented in the Research Brief: current MAS instrument/consultation status and the blocked Air Canada primary decision. No claim is made that the MAS proposal remains unissued. Air Canada is outside this sample.
- Rehearse and adjust pauses before recording; verify commencement-sensitive legal material again at publication.

These checks support review of the concrete sample. They do not substitute for Ray's acceptance of its teaching content or design.
