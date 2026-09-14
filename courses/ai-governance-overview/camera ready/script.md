# AI Governance Overview — voiceover script

The full spoken script, one block per course slide, in course-slide order.
The engine reads this file for the narration and generates each slide's
hidden notes from it. Research brief, outline and frontmatter stay in
[course.md](./course.md); source IDs below refer to its Research Brief.

Times are measured, not estimated. After editing, restamp them:

```bash
python3 scripts/course/stamp-times.py courses/ai-governance-overview
```

## Narration

This is the full revised voiceover, organised by section and course-slide number.
Source IDs refer to the Research Brief. They are production references and are
not read aloud. Hypothetical examples and recommended controls are identified
separately from findings in a legal decision. Slide notes are generated from these
passages, not independently rewritten.

### S1 · The launch decision

#### 01 · AI Governance Overview

**Sources:** [R00]
**Time:** 0:23  ·  50 words at 130 wpm

**Narration:**
Welcome to AI Governance Overview. I am Ray Han, Chief AI Trainer at HGT Consultancy.
We will define AI governance, examine its scope and components, and compare selected regulatory approaches.
We will then use cases to connect governance responsibilities to decisions at work.
The final roadmap sets out implementation actions.

#### 02 · Would you approve the launch?

**Sources:** [R00], [R04]
**Time:** 1:13  ·  114 words at 130 wpm + 20s pause
**Delivery:** Allow 20 seconds to choose; reveal the answer before advancing.

**Narration:**
Consider this hypothetical proposal. A Singapore retailer wants to launch a customer-service chatbot.
The supplier says its product follows Singapore's Model AI Governance Framework.
The chatbot will answer customers' questions about products, orders and returns.
Would you approve the launch, reject it, or request more information?
Pause here and choose an answer.

Requesting more information is the best next step. The supplier's statement does not establish whether this deployment is ready.
Approval requires evidence about the proposed use and the controls around it.
Rejecting the proposal permanently also goes beyond the information available.
For now, withhold launch approval and identify what needs to be checked.
We will revisit this retailer through out the course.

#### 03 · At least four more things you need to know

**Sources:** [R00], [R04], [R05]
**Time:** 1:03  ·  137 words at 130 wpm

**Narration:**
First, what personal data will the chatbot collect or use?
The retailer needs to understand customer inputs, retained conversations and access to order records.
Training-data provenance is another question for the supplier; it is distinct from the retailer's use of customer data.

Second, what commitments can the chatbot make to customers? An incorrect statement about refunds may affect the business financially.
Third, which jurisdictions will it serve? The retailer's location alone does not settle every applicable obligation.
Fourth, who will be accountable for its operation, including complaints and errors?

The asterisk identifies the question with direct personal-data relevance. Other questions may also involve data protection.
Singapore's Model AI Governance Framework is voluntary. Applicable obligations under the Personal Data Protection Act remain binding.
Following a framework is one input to an assessment, rather than a complete approval record.

### S2 · What AI governance covers

#### 04 · What is an AI system?

**Sources:** [R01], [R00]
**Time:** 1:01  ·  133 words at 130 wpm

**Narration:**
An AI system is a machine-based system that infers from inputs how to produce outputs.
Those outputs may be predictions, content, recommendations or decisions, and can affect physical or virtual environments.
Systems vary in their autonomy and in whether they adapt after deployment.
This is a plain-language paraphrase of the definition used by the Organisation for Economic Co-operation and Development, or OECD.

Examples include a model that estimates credit risk, a chatbot that generates replies, and an agent that acts through software tools.
For governance, examine how the system is used as well as what the model produces.
A recommendation shown to an experienced employee has a different operating context from an automatic customer decision.
A supplier's model description therefore needs to be connected to the workflow, data and people in the organisation.

#### 05 · What is AI governance?

**Sources:** [R02], [R03], [R00]
**Time:** 1:03  ·  136 words at 130 wpm

**Narration:**
In this course, AI governance means the responsibilities, policies, decision processes and controls through which an organisation oversees AI.
It covers development, procurement and use throughout the lifecycle.
Its purpose is to achieve intended benefits, meet applicable obligations and manage harm.
This is our working definition, drawing on management-system and AI risk-management approaches.

Governance determines who may approve a use, what evidence they require and when a decision must be reconsidered.
Risk management identifies and assesses possible harm, then implements and checks the response.
Compliance establishes which external requirements the organisation must meet.
These activities are connected, but meeting a legal minimum may still leave business or ethical concerns to address.

For the retailer, governance includes an accountable business owner, approved customer commitments and a process for handling failures.
It continues after the supplier completes installation.

#### 06 · Governance covers the AI lifecycle

**Sources:** [R02], [R03], [R00]
**Time:** 1:05  ·  140 words at 130 wpm

**Narration:**
Governance starts when a business identifies a proposed AI use.
The organisation should define its purpose, expected benefit, affected people and acceptable limits.
During development or procurement, it examines data, supplier dependencies and evidence about the system.
Before deployment, it tests the intended workflow and decides whether the controls justify proceeding.

Once the system is operating, people need to monitor outcomes, handle incidents and review material changes.
A new model, data source, customer group or permission can change the original risk assessment.
Retirement also needs planning: access should be removed, records handled appropriately, and dependent workflows replaced.

The same lifecycle covers predictive models, generative AI and agents.
It includes internally developed systems, purchased services and AI already being used by staff.
Policies and management oversight apply across these activities. The diagram is a repeating lifecycle, with review when circumstances change.

#### 07 · Six components of organisational AI governance

**Sources:** [R02], [R03], [R04], [R00]
**Time:** 1:08  ·  148 words at 130 wpm

**Narration:**
We will organise the course around six components. This is a teaching synthesis, not a universal six-part legal standard.

Accountability and oversight establish responsibility, approval authority and escalation.
Inventory and impact assessment identify the uses, purposes, affected people and potential consequences.
Data and supplier governance address privacy, data quality, security and third-party responsibilities.
Testing and human oversight establish whether the system performs acceptably and whether people can intervene effectively.
Transparency and recourse address what people are told and how they can raise concerns or request review.
Monitoring and improvement cover outcomes, incidents, material changes and eventual retirement.

The components overlap. Supplier evidence contributes to testing, while complaints can reveal issues that monitoring has missed.
An inventory entry should connect to an owner and a decision record, so it supports action.
For a low-impact internal use, the evidence may be brief. More consequential uses require stronger review and controls.

#### 08 · Who reviews an AI proposal before launch?

**Sources:** [R02], [R03], [R00]
**Time:** 1:06  ·  144 words at 130 wpm

**Narration:**
A business owner defines the intended use, expected benefit and acceptable outcomes.
Technical and data teams explain the system, its limitations and the results of relevant testing.
Risk, legal and compliance functions assess applicable obligations and challenge the proposed safeguards.
An accountable executive approves the deployment conditions and accepts residual risk within the organisation's authority limits.

These are illustrative responsibilities. Job titles and reporting lines will differ between organisations.
The important operational question is whether every review has an owner and a recorded conclusion.

For our retailer, customer operations can define permitted refund information and complaint handling.
The technical team can demonstrate failure handling and access controls.
The privacy function can examine collection and retention of customer conversations.
The approving executive should be able to see the unresolved issues before deciding.
The same responsibilities continue when the system changes or a significant incident occurs.

### S3 · How rules apply

#### 09 · AI governance across jurisdictions

**Sources:** [R04], [R05], [R07], [R08], [R09], [R24], [R25]
**Time:** 1:45  ·  228 words at 130 wpm
**Delivery:** Select each jurisdiction as it is named. Allow the map to settle before moving on.

**Narration:**
Your systems, your suppliers and the people affected by them can sit in different countries.
The map groups nine jurisdictions by the kind of instrument each relies on, because that difference matters more than the map's geography.
These are selected examples, not a complete list.

Three have binding AI law. The European Union's AI Act sets cross-sector requirements that depend on the system, the activity and your role.
South Korea's AI Framework Act has been in force since January 2026.
China has no single AI law, and it does enforce binding rules on generative AI and on labelling AI-generated content.

Five rely on existing law supported by guidance. Singapore combines existing legal obligations with sector supervision and voluntary frameworks.
The United Kingdom relies on its existing regulators, with policy principles supporting implementation.
Japan passed a promotion act that carries no penalties provision.
India works through sectoral regulators, and separately requires the labelling of synthetically generated content.
Malaysia has voluntary guidelines, and a governance Bill that has been drafted but not tabled.

The United States is different again. There is no federal AI statute, and state laws are now being challenged by the federal government.

Identify the use, the affected people, the locations served, and whether your organisation is a provider or a deployer.
One service can require you to consider more than one jurisdiction at the same time.

#### 10 · Different instruments have different legal effects

**Sources:** [R04], [R05], [R08], [R09], [R10]
**Time:** 0:57  ·  123 words at 130 wpm

**Narration:**
Start with the legal form of the instrument.
Acts, regulations and binding regulatory requirements create enforceable duties within their scope.
They can apply to AI-enabled activities even when written before the technology became common.

Supervisory statements and guidance require closer reading.
Some explain how a regulator interprets existing law; others set expectations for firms under its supervision.

An instrument may be non-binding in itself while influencing assessment or corrective action under the regulator's powers.
The instrument and legal authority determine consequences, including whether a penalty applies.

Voluntary frameworks provide methods and recommended practices. Contracts or policies may create additional commitments.
These categories can overlap for a single use. They are not three risk levels, and every use need not fall under all three.

#### 11 · AI Governance in Singapore

**Sources:** [R04], [R05], [R10]
**Time:** 1:01  ·  133 words at 130 wpm

**Narration:**
For a Singapore organisation, begin with the obligations attached to its activity and data.
The Personal Data Protection Act applies to relevant collection, use and disclosure of personal data, subject to its scope and exceptions.
For the retailer's chatbot, the review should examine purposes, notification, protection and retention of customer information.
Other business and customer obligations may also apply.

Singapore's Model AI Governance Framework provides voluntary guidance for responsible deployment.
Its second edition addresses internal governance, human involvement, operations management and stakeholder communication.
They do not replace applicable law.

Sector instruments add detail where the organisation conducts a regulated activity.
A financial institution therefore needs to review the relevant MAS requirements and guidance as well.
Document the source, scope and status of each instrument, including whether a cited document is a consultation proposal.

#### 12 · EU AI Act

**Sources:** [R07], [R08], [R00]
**Time:** 1:54  ·  181 words at 130 wpm + 30s pause
**Delivery:** Allow 30 seconds to read the timeline after explaining the four components.

**Narration:**
The EU AI Act contains several groups of requirements.
Prohibited practices are uses the Act disallows within its scope.
High-risk systems face requirements concerning matters such as risk management, data, documentation and human oversight.
General-purpose AI model providers have a separate set of obligations.
Transparency requirements address specified interactions and content, including informing people in relevant circumstances that they are interacting with AI.
These groups can overlap; they are not four mutually exclusive boxes for every product.

Application is phased. Prohibitions began applying in February 2025, and general-purpose AI provisions in August 2025.
The general application milestone, including Article 50 transparency, was August 2026, subject to transitional provisions.
Following the July 2026 amendment, Annex III high-risk requirements apply from 2 December 2027.
The product-related Annex I high-risk requirements apply from 2 August 2028.
Future dates are labelled explicitly on the timeline.

A non-EU organisation can also be within scope, including certain cases where system outputs are used in the Union.
Check its provider or deployer role and the relevant scope provisions before concluding that the Act does or does not apply.

#### 13 · Assess applicable obligations and potential harm

**Sources:** [R00], [R02], [R05]
**Time:** 0:56  ·  122 words at 130 wpm

**Narration:**
Legal applicability and potential harm answer different questions.
Identify the duties and expectations relevant to the use.
Assess who could be harmed, its severity and likelihood, and whether it can be corrected.
Both assessments help determine the controls and approval authority required.

Compare two hypothetical uses within the same retailer.
An employee uses AI to draft an internal meeting summary, then checks it before circulation.
Another system automatically refuses customer refunds using order histories and complaint records.
Both can involve personal data, but their effects and operating safeguards differ.
The second use can directly affect customers and requires closer examination of the decision and review arrangements.
A voluntary framework label alone does not tell the approver which use presents the greater risk.

#### 14 · Does following a framework resolve the data issue?

**Sources:** [R00], [R04], [R05]
**Time:** 1:22  ·  113 words at 130 wpm + 30s pause
**Delivery:** Allow 30 seconds to choose; reveal all option explanations before advancing.

**Narration:**
Our retailer's chatbot collects contact details and purchase histories to personalise offers.
Assume the notification obligation applies and no exception removes it.
The retailer has not told customers why it collects or uses this information.
The supplier follows the Model AI Governance Framework and displays an AI label.
Does this resolve the data issue?

Option A says yes, because the supplier follows a framework. That statement does not establish that the retailer has met its notification obligation.
Option B says the retailer must address the applicable PDPA obligation before launch. This is the best answer.
Option C says an AI label alone provides the required explanation. It does not explain the data-use purposes.

### S4 · Cases and their lessons

#### 15 · Failure pattern: regulatory action

**Sources:** [R13], [R00]
**Time:** 1:06  ·  142 words at 130 wpm

**Narration:**
Foodinho, a company in the Glovo group, used a digital platform to manage delivery riders in Italy.
In November 2024, the Italian data-protection authority imposed a five-million-euro penalty for unlawful processing of riders' data.
Its notice described an automated message sent when an account was blocked or deactivated.
That message did not inform riders about contesting the decision and requesting restoration of the account.

This provides a specific example of contestability: an affected person needs a usable route to challenge an outcome.
That is different from merely receiving a description of how an algorithm works.
The enforcement covered multiple data-protection issues; the penalty should not be attributed to one missing feature alone.

For a business implementing consequential decisions, our recommended control is a documented review route with an authorised human reviewer.
Test whether customers or employees can actually find and use it.

#### 16 · Case study: HSBC's credit-assessment disclosures

**Sources:** [R14], [R00]
**Time:** 1:09  ·  149 words at 130 wpm

**Narration:**
In 2018, an unsuccessful credit-card applicant asked HSBC Singapore for its internal evaluation report.
The bank provided a report with some information redacted.
The applicant sought access to the remaining information, and the dispute reached the Personal Data Protection Commission.

In its March 2021 decision, the Commission accepted that specified information could be withheld under the evaluative-purpose exception.
The decision also considered HSBC's explanations of how it used data and technology for credit assessments.
HSBC provided its Principle for the Ethical Use of Big Data and AI and its Credit Decisioning Policy Statement.
The Commissioner commented favourably on accountability and disclosure.

The legal exception supported withholding the specified data. The disclosure documents served a separate explanatory purpose.
Our governance lesson is to prepare accurate explanations of data use and decision processes, while applying the relevant access rights and exceptions.
This was not certification of HSBC's entire AI governance programme.

#### 17 · Failure pattern: customer claims and business losses

**Sources:** [R15], [R16], [R00]
**Time:** 1:10  ·  151 words at 130 wpm

**Narration:**
Two other examples show why the consequence of poor deployment is broader than a regulatory fine.
Air Canada's chatbot gave a customer incorrect information about bereavement fares.
The British Columbia Civil Resolution Tribunal held the airline responsible for the misleading information in that case.
For a customer-facing service, test policy answers and provide a route to resolve errors.

Zillow's 2021 filing reported a three-hundred-and-four-point-four-million-US-dollar inventory write-down associated with Zillow Offers.
The company cited home-pricing unpredictability, capacity constraints and other operational challenges when it decided to wind down the business.
It would be inaccurate to reduce that business outcome to one defective algorithm.
The deployment lesson is to examine forecasting uncertainty, operational capacity and financial exposure together.

These are different mechanisms: a customer claim in one case and an inventory loss in the other.
A governance review should consider both legal exposure and the organisation's ability to absorb or reverse an error.

### S5 · What sectors add

#### 18 · Financial Sector in Singapore

**Sources:** [R10], [R17], [R18]
**Time:** 1:04  ·  139 words at 130 wpm

**Narration:**
MAS's FEAT principles address Fairness, Ethics, Accountability and Transparency in the use of AI and data analytics.
They are advisory principles, first published in 2018.
They provide a useful way to examine fair outcomes, responsibility and communication in financial services.

A separate November 2025 consultation proposed Guidelines on AI Risk Management.
The proposal includes maintaining an AI inventory and proportionate risk management across the lifecycle.
We are discussing that consultation document as a proposal, not presenting it as an issued rule.
An organisation using a consultation proposal should check the current issued requirements before relying on it.

For a financial institution, the practical task is to connect AI controls to its existing governance, risk and compliance arrangements.
The review should distinguish binding requirements, advisory principles and proposals, rather than treat every MAS publication as having the same legal effect.

#### 19 · Financial Sector in the United Kingdom

**Sources:** [R11], [R12], [R00]
**Time:** 1:03  ·  136 words at 130 wpm

**Narration:**
The FCA explains that its existing frameworks apply to firms' use of AI.
Its approach identifies the Consumer Duty and senior-management accountability as relevant foundations.
The regulator can use its existing supervisory and enforcement powers where a firm's use of AI breaches the relevant financial regulatory requirements.

Responsibilities should follow the firm's activities and its documented management arrangements.
A business decision, a technology system and a risk control may involve different people, but their responsibilities must connect.
Avoid assigning all AI risk automatically to the chief technology officer or creating a new title without decision authority.

For a credit-decisioning tool, the firm should establish who owns the lending use, who challenges the risk assessment and who authorises deployment.
Supplier testing can contribute evidence. It does not remove the firm's responsibility for how the tool is used.

#### 20 · Apply these governance practices in your sector

**Sources:** [R00], [R02], [R03]
**Time:** 0:55  ·  120 words at 130 wpm

**Narration:**
The transferable practices are to map obligations, assign responsibility and retain evidence.
Start with the activity your organisation performs and identify the requirements already attached to it.
Then assign an accountable owner and an appropriate independent review.
Keep evidence of testing, decisions and monitoring so management can understand whether controls are working.

For a retailer, this may involve customer communications, personal data and refund decisions.
For an employer, it may involve recruitment, employee information and review of consequential decisions.
These are examples of questions to investigate, not a statement that identical duties apply to both.
Financial-services regulation does not automatically apply to another sector.
The useful lesson is how a regulated organisation connects its obligations to owners, controls and evidence.

#### 21 · Who must own this before launch?

**Sources:** [R00], [R11], [R12]
**Time:** 1:25  ·  120 words at 130 wpm + 30s pause
**Delivery:** Allow 30 seconds to choose; reveal before advancing.

**Narration:**
A UK-regulated bank is preparing a vendor-built credit-decisioning tool.
Its documented management responsibilities place this lending activity with an existing senior manager.
The vendor says it tests the model, but the bank's risk function has not reviewed the deployment.
Who needs to act before launch?

Option A leaves accountability with the vendor. Supplier responsibilities remain important, but do not replace the bank's own obligations.
Option B requires the responsible senior manager to ensure the bank completes its review before approval. This is the best answer.
Option C waits for an AI-specific job title. The FCA's approach relies on existing frameworks and accountability arrangements.
The bank should document both its own responsibilities and what evidence or support the supplier must provide.

### S6 · Apply the controls

#### 22 · Three questions and the evidence to request

**Sources:** [R00], [R13], [R14], [R11]
**Time:** 0:51  ·  110 words at 130 wpm

**Narration:**
Three questions help a business leader examine a proposal.
Who is accountable for this use? Request a named owner, a decision authority and an escalation route.
How can an affected person challenge an outcome? Request the review procedure and evidence that someone can change the decision.
What have we told people about the system? Request accurate explanations of its purpose, limitations and use of data.

Foodinho illustrates the importance of a usable challenge route. HSBC illustrates disclosure alongside legal access limits.
These cases support different lessons, rather than one universal explainability requirement.
The questions address responsibility, recourse and communication. The approval decision also needs evidence about performance and operating controls.

#### 23 · What evidence is needed before approval?

**Sources:** [R00], [R02], [R03], [R19]
**Time:** 0:54  ·  117 words at 130 wpm

**Narration:**
Ask for testing in the intended setting, including relevant users and foreseeable failure conditions.
Confirm that a person can intervene and has the authority, information and time to do so.
Identify what production monitoring will detect, who receives alerts and when escalation is required.
Finally, examine a tested way to stop, restrict or roll back the system.

Singapore's agentic guidance recommends human review for high-stakes or irreversible actions.
This is voluntary guidance; it should not be described as a general statutory prohibition.
For any proposed use, connect oversight to the consequence of an error and the permissions the system holds.
An approval record should identify the evidence reviewed, unresolved limitations, deployment conditions and the next review trigger.

#### 24 · Would you approve the chatbot now?

**Sources:** [R00], [R02], [R05]
**Time:** 1:00  ·  131 words at 130 wpm

**Narration:**
Return to the retailer introduced at the start. In this hypothetical continuation, the team now supplies four items of evidence.
The Head of Customer Operations owns the use. Customers can reach a human reviewer who can correct an outcome.
The proposed disclosures describe data use and the chatbot's limits.
A supervised trial has tested the permitted questions, escalation and shutdown process.

One limitation remains: refund-policy answers have not passed the retailer's acceptance tests.
The appropriate decision in this example is to restrict the pilot to product information and order status.
Keep refund decisions with staff until testing and controls justify expanding the scope.
Monitoring, access limits and a tested stop process must operate during the pilot.
The decision is now connected to evidence and restrictions, with the owner responsible for reassessment.

#### 25 · Approve, restrict or pause?

**Sources:** [R00], [R02], [R03]
**Time:** 1:25  ·  120 words at 130 wpm + 30s pause
**Delivery:** Allow 30 seconds to choose; reveal all feedback.

**Narration:**
An insurance tool flags claims for manual review. It has an owner, a review procedure and accurate customer information.
Testing has used only a supplier benchmark. There is no production monitoring or rollback process.
Should the organisation approve production use, run an unrestricted pilot, or pause production and establish safeguards?

Pausing production and establishing safeguards is the best answer.
A bounded pilot may then be appropriate, with suitable testing, monitoring, human review and rollback in place.
Approving production would leave the stated gaps unresolved. Calling a deployment a pilot does not resolve them either.
Manual referral can still cause harm through delay, bias or excessive reliance on automated recommendations.
Assess the actual workflow before deciding how much control is needed.

### S7 · Implementation

#### 26 · Record the next decision for each priority AI use

**Sources:** [R00], [R02], [R03]
**Time:** 0:51  ·  111 words at 130 wpm

**Narration:**
A short decision record makes the next action explicit.
Use five fields: the use case, accountable owner, review route, evidence and next decision with a date.
For a hypothetical complaints-triage tool, the owner is the Head of Customer Operations.
The record shows that some escalated complaints are closed without human review and testing uses only supplier data.
The next decision is whether a controlled pilot can proceed after those gaps are addressed.

Link the record to the relevant inventory entry and assessment.
When a field is incomplete, record the action, responsible person and deadline for resolving it.
This gives management a specific issue to review and a way to follow up.

#### 27 · Which action should come first?

**Sources:** [R00], [R02], [R03]
**Time:** 1:08  ·  104 words at 130 wpm + 20s pause
**Delivery:** Allow 20 seconds to choose; reveal before the roadmap.

**Narration:**
A firm has completed its AI inventory. Next week it plans to activate a tool that automatically declines insurance claims.
There is no appeals route or production monitoring. The board has also asked about ISO certification.
Which action should come first?

Pause the launch and establish the missing controls before deployment.
Starting certification does not resolve next week's control gap. Expanding the inventory also does not address this known exposure.
The organisation can pursue those activities alongside the urgent work, with clear ownership and priorities.
Certification may provide useful assurance, but it is separate from deciding whether this particular system is ready to operate.

#### 28 · AI Governance implementation roadmap

**Sources:** [R00], [R02], [R03], [R04], [R18]
**Time:** 1:01  ·  132 words at 130 wpm
**Delivery:** Hold the final roadmap for 20 seconds so learners can read or capture it.

**Narration:**
Begin with the foundation: create an AI inventory and assign responsibility for keeping it current.
Record each use's purpose, owner, users, data, supplier and deployment status.
Address urgent known risks while the wider inventory is being completed.

Assess the uses and establish controls. Identify applicable obligations, approval authority, testing, human review, disclosures and supplier requirements.
Then operate and improve the programme through monitoring, complaints, incident response, change review and tested rollback or retirement.

Use NIST, ISO and Singapore's governance guidance to support this work, with sector-specific sources where relevant.
The MAS inventory reference shown here comes from a consultation proposal for financial institutions.
Add assurance tools, dedicated resources or certification when risk, scale or contractual needs justify them.
Select one priority use, name its owner and record the next decision and date.

## Production review · 12 September 2026

Steps 1–3 are drafted and checked: revised 30-slide outline, complete source
narration, and an 18-slide representative Gate 2 sample. The earlier full deck
is preserved pending sample review. No acceptance hash has been set.

### Estimated recording duration

Counts include only spoken narration, excluding headings, references and delivery
instructions. At 150 words per minute, the spoken estimate below leaves time for
learner response, diagram reading, case reflection and transitions. This is a
production budget, not a measured recording. Rehearse before final recording.

| Section | Spoken words | Spoken minutes | Non-spoken allowance (seconds) | Total minutes |
|---|---:|---:|---:|---:|
| S1 | 395 | 2.63 | 22 | 3 |
| S2 | 701 | 4.67 | 20 | 5 |
| S3 | 900 | 6.00 | 60 | 7 |
| S4 | 442 | 2.95 | 63 | 4 |
| S5 | 515 | 3.43 | 34 | 4 |
| S6 | 478 | 3.19 | 49 | 4 |
| S7 | 347 | 2.31 | 41 | 3 |

Total: **3,778 spoken words**, approximately
**25.19 spoken minutes**, with planned holds
and transitions bringing the course to **30 minutes**.

Use S1's allowance for the opening response; S2's for the lifecycle and role
diagrams; S3's for the EU timeline and legal quiz; S4's for reflection on the
three cases; S5's for the ownership quiz; S6's for the callback and deployment
quiz; S7's for the priority question and final roadmap. Individual delivery
notes indicate the principal holds. Adjust pace and holds after rehearsal.

### Language and visual review

Applied no-ai-slop first, then sg-english, to the rewritten source and extracted
sample copy. Removed vague slogans, unfinished transitions and the survey-to-quiz
comparison. Expanded unfamiliar acronyms; used Singapore/British spelling;
preserved legal scope, conditions and distinctions. Ray's requested learner
question headings take precedence over generic style restrictions.

All 18 sample slides and both quiz reveal states passed the 1920×1080 text-bounds
and layout-stability checks and were visually inspected. Keyboard reveal/advance
and all three map controls passed. The PDF contains 18 landscape 16:9 pages,
with revealed answers, complete map, readable case attribution and no visible
clipping. Source limitations remain explicitly recorded in the Research Brief.

Detailed artifacts and remaining review decisions: `gate2/README.md`,
`gate2/checks.json`, `gate2/REVIEW.md`, and `FEEDBACK.md`.
