# AI Governance Overview: proposed revision

> **Superseded.** This evaluated the 35-slide deck at baseline `c23627ed`, before
> the rebuild. The deck is now 28 slides and the score below does not describe
> it. Kept as the record of what the review found and why the rebuild happened.
> The rubric it used has been replaced by [course-qa.md](../../../references/course-qa.md).

12 September 2026 · Discussion draft for Ray and Claude Code

## Recommendation

Reopen the outline as well as Gate 2. The current course teaches regulatory exposure and launch approval more thoroughly than it teaches AI governance itself. Ray's intended scope is an overview of the concept, scope and components, supported by cases. That requires an explicit foundation before the regulatory comparison.

Preserve the visual system and the opening chatbot scenario. Rebuild the teaching sequence around:

**Launch question → definitions → scope and components → jurisdictions → cases → sector application → launch decision → implementation roadmap.**

This document proposes changes; it does not record approval or alter the existing course source, fragments or generated deck. The existing HTML contains **35 slides**, rather than the approximately 26 in the outline. Ray's financial-sector comment numbered 18 corresponds to actual slide 19; his regulatory-language comment corresponds to slides 20–21. References below use actual HTML slide numbers and titles.

## Revised learning outcomes

After 30 minutes, learners should be able to:

1. Explain what an AI system is and what organisational AI governance covers.
2. Identify the main governance components, responsible functions and lifecycle activities.
3. Distinguish applicable laws, supervisory expectations and voluntary frameworks, using Singapore, the EU and the UK as examples.
4. Recognise specific governance failures in cases and identify a suitable control.
5. Assess a proposed deployment and identify the next implementation actions.

These replace the current emphasis on a 90-day approval checklist. They retain its useful executive application while making the overview promised by the title explicit.

## Proposed 30-slide sequence

| Section | Minutes | New slides | Teaching content and reuse |
|---|---:|---|---|
| 1. The launch decision | 3 | 1–4 | Cover; opening chatbot decision; immediate feedback and missing information; properly scoped adoption statistics. Rework current 1–4. |
| 2. What AI governance covers | 5 | 5–9 | AI system; AI governance; lifecycle and scope; governance components; responsibilities. Replace current 5 and 7 and add the missing concepts. |
| 3. How rules apply | 7 | 10–16 | Jurisdiction map; legal force; Singapore overview; EU AI Act; UK overview; legal obligation versus potential harm; application quiz. Reuse current 6, 8–13, with the general UK material moved here. |
| 4. Cases and their lessons | 4 | 17–19 | Foodinho: contestability; HSBC: disclosure and access limits; Air Canada and Zillow: customer liability and operational loss. Consolidate current 14–17 and 30–31. |
| 5. What sectors add | 4 | 20–23 | Singapore finance; UK finance; transfer to other sectors; jurisdiction-specific ownership quiz. Rework current 19–23. |
| 6. Apply the controls | 4 | 24–27 | Three questions with evidence; operational approval evidence; return to the chatbot; approve/restrict/pause quiz. Merge current 24–25; rework 26–29. |
| 7. Implementation | 3 | 28–30 | A completed governance record; priority question; implementation roadmap as the final slide. Rework current 33–34 and finish with 32. Remove current 35. |

Total: **30 minutes**. These are allocation estimates; measure the revised narration and explicit pause/reveal time before Gate 2. The 30-slide target depends on consolidation, not on fitting more text into each box. Preserve space for learners to pause.

Move the broad fine-outcome catalogue to optional references. Retain the Dutch and Robodebt cases as optional alternatives or narration examples if there is time; do not compress three different legal histories into a shared finding that their sources do not establish.

## Content to establish before the jurisdiction section

**AI system — proposed learner-facing paraphrase:** A machine-based system that infers from inputs how to produce predictions, content, recommendations or decisions. Its outputs can affect physical or virtual environments. Systems vary in autonomy and in whether they adapt after deployment.

Introduce the **Organisation for Economic Co-operation and Development (OECD)** below the definition. Mark this as a paraphrase, and put the formal definition and version history in the reference/narration. Add examples: a credit-scoring model, a customer chatbot, and an agent that takes actions. Explain that the governed system includes its deployment context, data, interfaces and human processes, rather than treating the model as the entire system. [OECD explanatory memorandum](https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html).

**AI governance — proposed course working definition:** The responsibilities, policies, decision processes and controls through which an organisation directs and oversees its development, procurement and use of AI throughout its lifecycle.

Label this a course working definition, not an OECD quotation. Explain its purpose: achieving intended benefits, meeting applicable obligations and managing harm. It synthesises the management-system approach described by [ISO/IEC 42001](https://www.iso.org/standard/42001) and the cross-cutting GOVERN function in the [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

**Scope:** organisation-wide policy and oversight; individual AI uses and systems; suppliers and affected people; the lifecycle from selection and procurement through testing, deployment, monitoring, change and retirement. Include predictive AI, generative AI and agents. Wider automated decision-making cases may teach relevant governance lessons without necessarily meeting every legal definition of AI.

**Components — teaching synthesis, not a purported universal numbered standard:**

| Component | What learners should recognise |
|---|---|
| Accountability and oversight | A responsible owner, approval authority, escalation and independent challenge. |
| Inventory, purpose and impact assessment | What is used, why, by whom, and who may be affected; applicable obligations and acceptable risk. |
| Data and supplier governance | Data rights, privacy, quality, security, supplier evidence and contractual responsibilities. |
| Testing and human oversight | Performance in the intended setting, fairness, reliability and usable intervention controls. |
| Transparency and recourse | Appropriate disclosures, explanations, complaints and review of consequential decisions. |
| Monitoring and improvement | Production monitoring, incidents, change approval, rollback, retirement and management review. |

Use a lifecycle diagram with these responsibilities spanning it. Avoid implying that a framework's adoption is itself evidence that all controls work.

**Roles:** Business owners define purpose and acceptable outcomes; technical and data teams supply evidence; risk/legal/compliance functions assess obligations and challenge controls; accountable executives approve residual risk and deployment conditions. Show when each participates: proposal, pre-launch, operation and material change. These are illustrative organisational responsibilities, not universal legal job titles.

## Decisions on Ray's slide comments

| Current slide | Recommendation and proposed wording |
|---|---|
| 1 · Cover | Use **AI Governance Overview** on one line. The existing line break is explicit markup. Retain presenter and series details. |
| 2 · Launch decision | Use **Would you approve the launch?** Keep the three choices. Reveal **Request more information before approval** after a pause, on this slide or immediately at the top of slide 3. Explain that withholding approval is reasonable; the facts do not justify approval or establish that deployment must be permanently rejected. Current choices are static boxes, not functioning quiz controls. |
| 3 · Missing information | Use **At least four more things you need to know**. Questions: **What personal data will it collect or use?***; **What commitments can it make to customers?**; **Which jurisdictions will it serve?**; **Who will be accountable for its operation?** Keep training-data provenance as supporting narration rather than conflating it with runtime collection. |
| 3 · Framework/PDPA | Name **Singapore's Model AI Governance Framework**. Suggested explanation: **Following the voluntary framework does not establish compliance with applicable law.** An asterisk may identify the direct personal-data question, but its legend must say **Direct PDPA relevance where personal data is involved; other questions may also raise data-protection obligations.** Avoid teaching that only one category can engage the PDPA. |
| 4 · Statistics | Remove the entire “If you picked yes” link: a survey of understanding does not establish how respondents would answer this launch question. “You have company” means others are in a similar position, but is inappropriate here. Use **AI adoption and oversight in UK financial services**, with **2024 survey** clearly visible. Retain 75% adoption and 46% partial understanding; add **one-third of AI use cases were third-party implementations**. Optional fourth statistic: **84% reported an accountable person for their AI framework**. Label denominators and do not generalise to all businesses. Three figures are sufficient; do not add numbers merely to fill space. |
| 5 · Definition | Replace the entire chronology with the AI-system definition and examples above. Expand OECD. Keep dates and EU adoption as secondary reference information. |
| 6 · Jurisdictions | Use **AI governance across jurisdictions**. An animated world map is suitable for orientation: name regions, reveal short factual labels sequentially, and retain a labelled static state for PDF and reduced-motion use. The EU should be shown as a region. A map cannot replace explanations of obligations. “Guidance rather than rules” wrongly hides existing binding law in Singapore and the UK. |
| 7 · Roles | Replace **Ask a better question** with **Who reviews an AI proposal before launch?** Show role, question and evidence required. Avoid claiming that every applicability assessment can be completed in an afternoon. |
| 8 · Legal force | Use **Identify the legal obligations and guidance relevant to each AI use**. Explain binding requirements, supervisory expectations and voluntary frameworks separately. They **can overlap**; all three do not necessarily apply to every use. Use one neutral border colour or explicit labelled categories. Remove “Written for something else”, “Not optional either”, and “Genuinely voluntary”. |
| 9 · Comparison | Use **Singapore and UK: examples of laws and guidance**. Keep two columns if this comparison remains; do not expand a dense table to six jurisdictions. The global map serves that purpose. Clearly distinguish regulator guidance explaining law from a standalone supervisory instrument. Date commencement-sensitive examples; being enacted does not establish that an obligation currently applies. |
| 10 · Supervisory response | Use **Supervisory expectations can lead to corrective action**. Shorten the source excerpt, emphasise exact phrases with bold/underline, and label **Draft MAS third-party risk management guidelines, March 2026**. The middle category can be non-binding in legal form while having supervisory consequences. Do not equate those consequences with automatic civil fines for breaching a guideline. Delete the unsupported assurance that a firm “keeps its licence”. Verify the issued instrument or draft before using the extract. |
| 11 · Two dimensions | Use **Assess applicable obligations and potential harm**. Explain: **Which legal duties and supervisory expectations apply?** and **Who could be harmed, how severely, and how likely is that harm?** Replace the fragmentary closing instruction with **Use both assessments to determine the controls and approval level required.** A small worked example is more useful than another slogan. |
| 12 · EU | Use **EU AI Act**. Teach prohibited practices, high-risk systems, general-purpose AI and transparency requirements before showing their application dates. Distinguish categories that overlap from mutually exclusive tiers. Use labelled timeline boxes; future items may be grey, but also say **Not yet applicable**. Add the non-EU scope condition in plain language. Attach the maximum fine to its breach category rather than implying every breach attracts 7%. |
| 13 · PDPA quiz | Retain near the legal-force explanation. Provide immediate per-option feedback. Explicitly connect the missing data-use information to the legal issue; following a framework is not a substitute. |
| 14 · Public-sector/rider cases | Add **CASE STUDIES**. These do **not** establish one common explainability requirement. Explanation, contestability, fair/lawful data use and substantive legality are different matters. Prefer a fully explained Foodinho case; use Dutch and Robodebt as separate optional examples. If retained together, give each a distinct failure, decision and lesson. |
| 15 · Fine outcomes | Remove from the core 30-minute overview. “Did not survive” conflates annulment, collection, appeal status and inspection findings. If retained in an appendix, use **AI enforcement: different procedural outcomes**, date each status and cite the current decision. Ray's paired failure headings would work better on the substantive regulatory case and the commercial cases, not on this catalogue. |
| 16 · Air Canada quote | Integrate the quote into a case slide after the background. Prefer **Case study: Air Canada's customer chatbot**. Explain wrong fare advice, the company's responsibility and the tribunal outcome. A genuine source/headline crop may support the story, with date and credit; never manufacture a news headline image. |
| 17 · Other consequences | Ray's pairing is useful with a qualification: use **Failure pattern: regulatory action** for Foodinho and **Failure pattern: customer claims and business losses** for Air Canada/Zillow. “Without a regulator” must not suggest absence of legal accountability: Air Canada involved a tribunal. Replace the final sentence with **Control customer-facing advice and limit exposure when automated forecasts fail.** Describe the different mechanisms in the two cases. |
| 18 · Rider quiz | Retain or fold into the Foodinho case. Distinguish an explanation from a review by someone authorised to change the outcome. Avoid implying that accuracy never mattered in the underlying enforcement. |
| 19 · Singapore finance | Use **Financial Sector in Singapore** as requested. Expand FEAT: **Fairness, Ethics, Accountability and Transparency**. Label it **Advisory principles**. Label the AI Risk Management Guidelines **Consultation proposal** unless an issued version is verified. Explain ownership, proportionate assessment, testing and lifecycle oversight; status alone is not enough content. |
| 20 · FCA quote | “Regulatory bite” means enforcement powers under existing rules. Replace the standalone quotation with a plain-language explanation on the UK finance slide. If quoting, preserve the original words and identify them as a quotation. The cited document is a report published on 20 January 2026; that is not necessarily the hearing date. |
| 21 · UK | Agree on adjacency for the **general UK overview**: place it beside the EU and Singapore overviews. Keep FCA/PRA detail in the sector section. Teach existing law, the regulators' respective roles and organisational implications. The operations/risk roles are examples; responsibility must follow the firm's actual activities and allocation. |
| 22 · Transfer | Use **Apply these governance practices in your sector**. Three actions: **Map existing obligations to the AI use; assign an accountable owner and independent review; retain evidence of testing, decisions and monitoring.** Mark these as transferable practices, not claims that MAS or FCA rules bind every sector. |
| 23 · Ownership quiz | Name the jurisdiction. Current feedback mixes Singapore FEAT and UK SM&CR/Consumer Duty as though all bind an unspecified bank. Use a UK-regulated bank for the UK legal lesson, or rewrite the Singapore version using Singapore sources. Supplier duties and internal accountability can coexist. |
| 24 + 25 · Three questions | Merge. Each column contains **component → complete question → concrete evidence/example**. Accountability: named owner and approval record. Contestability: accessible human-review route, tied to Foodinho. Disclosure: accurate statements about capability and use, tied to the relevant case. Avoid claiming every component is supported by every case. |
| 26 · Evidence | Use **What evidence is needed before approval?** and a vertical list: testing in the intended setting; workable human intervention; production monitoring; tested stop/rollback. These checks operationalise the earlier components. Add the running-example label if the chatbot is used on this slide. |
| 27 · Agentic quote | Merge into slide 26 as a short attributed source note. Identify voluntary guidance. The narration must not turn “high stakes **or** irreversible” into only irreversible actions, or convert a “should” recommendation into a statutory prohibition. |
| 28 · Return | Kicker **OPENING CASE REVISITED**; heading **Would you approve the chatbot now?** Reuse the exact scenario identifier and a small visual from slide 2. Use a numbered list of owner, customer review, accurate disclosures and operating evidence. Show a decision or explicitly state what evidence is still missing; another list of questions alone does not resolve the opening. |
| 29 · Decision quiz | Repair the answer conditions. A tool referring claims to human review can still cause harm through delay, bias or automation bias. Say **Pause production deployment; permit a bounded pilot only after monitoring, human safeguards and rollback are established.** Do not approve a pilot while the stated safeguards are absent. |
| 30 + 31 · HSBC | Merge and move into the case section. Use **Case study: HSBC's credit-assessment disclosures**. Show background, access request, legal outcome and governance lesson before a short extract. The application was made in **2018**; the decision was in **2021**. The exception justified withholding specified evaluative data. Disclosure documents were favourably considered, but do not prove an audit of the bank's entire governance system or faster case resolution. |
| 32 · Roadmap | Use **AI Governance implementation roadmap**, kicker **TAKEAWAYS**. “Executive Summary” suits a briefing better than this closing teaching slide. First action **Create an AI inventory**; stage label **Foundation**. Move references below the diagram and label draft sources as drafts. Add testing, monitoring, incident response and periodic review, which are underrepresented in the current roadmap. See the proposed wording below. |
| 33 · Worked record | Retain before the final roadmap. Use **Record the next decision for each priority AI use**. Keep the useful worked example, but remove legal-status colours from ordinary record fields. Five fields are shown; narration currently calls them four lines. |
| 34 · Priority quiz | Retain before the final roadmap. Correct the feedback's repeated unsupported Dutch/contestability generalisation. State that the launch is paused until the relevant controls are operating. |
| 35 · Closing slogan | Remove. Finish on the implementation roadmap so the final frame is the promised usable takeaway. Inventory is foundational, but an urgent known deployment risk need not wait for an organisation-wide inventory to be complete. |

## Roadmap wording proposal

| Stage | Actions |
|---|---|
| **Foundation** | **Create an AI inventory.** Record purpose, owner, users, data, supplier and deployment status. Assign responsibility for maintaining it. |
| **Assess and establish controls** | Assess impact and applicable obligations. Assign approval authority. Test the system and establish human review, disclosures and supplier requirements. |
| **Operate and improve** | Monitor outcomes, handle complaints and incidents, reassess material changes, and test rollback or retirement arrangements. Report significant issues to management. |

Below the main diagram: **Add assurance tools, dedicated resources or certification when risk, scale or contractual requirements justify them.** This is not a reason to defer useful ISO management practices until certification is required.

Reference strip: **NIST AI RMF 1.0; ISO/IEC 42001:2023; Singapore Model AI Governance Framework; MAS AI Risk Management consultation proposal, P017-2025, §3.4 (draft; finance-specific).** Cite individual actions to the relevant source in the narration. Do not present the synthesis as a mandated sequence.

## Gate 2 revision package

1. Update the intended scope and outline in `course.md`; record the new version as proposed, not approved. Once adopted, mark affected narration and slides stale.
2. Correct the Research Brief's interpretations before reusing them. Several accepted corrections are present in the review log but absent from the later narration.
3. Rewrite the course-wide narration to the revised sequence. Apply **no-ai-slop**, then **sg-english**. Preserve the learner questions Ray requested; the skill's generic restriction on rhetorical questions does not override that instruction. Expand OECD and FEAT for this introductory audience.
4. Extract on-slide teaching content from that narration. Definitions, case backgrounds, decisions and practical implications must remain visible; avoid turning either the full narration or its conversational transitions into slide text.
5. Build a representative sample covering the hardest comparison, EU timeline, case layout, a revealed quiz and the roadmap. These are the revised section's design stress points. Include the quiz's before/after states and a static map state.
6. Check every slide and every quiz state, all quote bounds, the one-line cover, 16:9 playback and an actual PDF export. Keep a safe area around text and source attribution. A three-line checker alone cannot establish visual or instructional readiness.

The existing deck's design can be reused. The revision should be judged first on whether learners can define governance, name its components and connect a case to a control.
