"""Audience-facing slide compositions for AI Value Management.

Narration, sources and the outline live in course.md. Shared components live in
templates/full-decks/course/style.css. Build with scripts/build-course.sh.

S5 (slides 18-23) and S6 (24-29) were the gate 2 representative sections and set
the layout conventions the other sections follow.
"""

SECTION_BOUNDS = [4, 7, 12, 17, 23, 29, 31, 33]

SOURCE_LABELS = {
 'R00': ('Course teaching synthesis', None),
 'R01': ('MIT NANDA · The GenAI Divide: State of AI in Business 2025 · July 2025', 'http://web.archive.org/web/20250818145714if_/https://nanda.media.mit.edu/ai_report_2025.pdf'),
 'R02': ('MIT NANDA · The GenAI Divide · methodology and limitations · July 2025', 'http://web.archive.org/web/20250818145714if_/https://nanda.media.mit.edu/ai_report_2025.pdf'),
 'R03': ('McKinsey · The state of AI in 2026 · 25 August 2026', 'https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai'),
 'R04': ('McKinsey · The state of AI: How organizations are rewiring to capture value · March 2025', 'https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value'),
 'R05': ('Deloitte AI Institute · State of AI in the Enterprise · January 2026', 'https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html'),
 'R06': ('S&P Global Market Intelligence · Voice of the Enterprise: AI & Machine Learning · 30 May 2025', 'https://www.spglobal.com/market-intelligence/en/news-insights/research/ai-experiences-rapid-adoption-but-with-mixed-outcomes-highlights-from-vote-ai-machine-learning'),
 'R07': ('US Census Bureau · Large Firms With at Least 20 Employees Biggest AI Users · 26 May 2026', 'https://www.census.gov/library/stories/2026/05/ai-use-businesses.html'),
 'R08': ('US Census Bureau · The Microstructure of AI Diffusion · CES-WP-26-25 · April 2026', 'https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-25.pdf'),
 'R09': ('Stanford Digital Economy Lab · The Enterprise AI Playbook · April 2026', 'https://digitaleconomy.stanford.edu/publication/enterprise-ai-playbook/'),
 'R10': ('RAND · The Root Causes of Failure for Artificial Intelligence Projects · 13 August 2024', 'https://www.rand.org/pubs/research_reports/RRA2680-1.html'),
 'R11': ('Dillon, Jaffe, Immorlica & Stanton · Shifting Work Patterns with Generative AI · 13 November 2025', 'https://arxiv.org/abs/2504.11436'),
 'R12': ('Humlum & Vestergaard · Still Waters, Rapid Currents · 13 March 2026', 'https://www.rfberlin.com/wp-content/uploads/2026/03/26078.pdf'),
 'R13': ('Cui et al. · The Effects of Generative AI on High-Skilled Work · Management Science', 'https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf'),
 'R14': ('METR · Early-2025 AI and experienced open-source developer productivity · 10 July 2025', 'https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/'),
 'R15': ('METR · We are Changing our Developer Productivity Experiment Design · 24 February 2026', 'https://metr.org/blog/2026-02-24-uplift-update/'),
 'R16': ('Brynjolfsson, Li & Raymond · Generative AI at Work · Quarterly Journal of Economics, 2025', 'https://danielle-li.github.io/assets/docs/GenerativeAIatWork.pdf'),
 'R17': ('Dell’Acqua et al. · Navigating the Jagged Technological Frontier · Organization Science', 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321'),
 'R18': ('Acemoglu · The Simple Macroeconomics of AI · Economic Policy, 2025', 'https://www.nber.org/papers/w32487'),
 'R19': ('Bick, Blandin & Deming · Federal Reserve Bank of St. Louis · 13 November 2025', 'https://www.stlouisfed.org/on-the-economy/2025/nov/state-generative-ai-adoption-2025'),
 'R20': ('US Bureau of Labor Statistics · Productivity and Artificial Intelligence · 8 June 2026', 'https://www.bls.gov/productivity/articles-and-research/ai-and-productivity/home.htm'),
 'R21': ('Brynjolfsson, Rock & Syverson · Artificial Intelligence and the Modern Productivity Paradox · 2017', 'https://www.nber.org/papers/w24001'),
 'R22': ('Klarna Group plc · Form 20-F, financial year 2025 · 26 February 2026', 'https://www.sec.gov/Archives/edgar/data/2003292/000200329226000007/klar-20251231.htm'),
 'R23': ('Klarna · Q3 2025 earnings call · 18 November 2025', 'https://www.investing.com/news/transcripts/earnings-call-transcript-klarna-q3-2025-reveals-growth-stock-dips-93CH-4365461'),
 'R24': ('Presto Automation · Form 10-K, 11 October 2023, and Form 10-Q, 21 February 2024', 'https://www.sec.gov/Archives/edgar/data/1822145/000155837023016336/prst-20230630x10k.htm'),
 'R25': ('Commonwealth Bank of Australia · 2026 Full Year Results Presentation', 'https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf'),
 'R26': ('IBM · Q4 2025 earnings call and 2025 Annual Report', 'https://www.sec.gov/Archives/edgar/data/51143/000005114326000027/ibmars2025.pdf'),
 'R27': ('Gertler et al. · Impact Evaluation in Practice · World Bank, 2016', 'https://openknowledge.worldbank.org/handle/10986/25030'),
 'R28': ('Gordon, Zettelmeyer, Bhargava & Chapsky · Advertising measurement at Facebook · Marketing Science, 2019', 'https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_18-113.pdf'),
 'R29': ('Lewis & Rao · The Unfavorable Economics of Measuring the Returns to Advertising · QJE, 2015', 'https://academic.oup.com/qje/article-abstract/130/4/1941/1914592'),
 'R30': ('Cabinet Office and HM Treasury · Government efficiency savings technical note', 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1064110/government-efficiency-savings-technical-note.pdf'),
 'R31': ('HM Treasury · The Green Book, 2026', 'https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf'),
 'R32': ('HM Treasury · The Magenta Book · March 2020', 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/879438/HMT_Magenta_Book.pdf'),
 'R33': ('BCG · AI Radar: From Potential to Profit · January 2025', 'https://web-assets.bcg.com/0b/f6/c2880f9f4472955538567a5bcb6a/ai-radar-2025-slideshow-jan-2025-r.pdf'),
 'R34': ('IBM Institute for Business Value · Solving the AI ROI puzzle · 13 July 2025', 'https://www.ibm.com/downloads/documents/us-en/1379d32d7fdaec18'),
 'R35': ('Kohavi et al. · Online Controlled Experiments at Large Scale · KDD 2013', 'https://exp-platform.com/Documents/2013%20controlledExperimentsAtScale.pdf'),
 'R36': ('Sculley et al. · Hidden Technical Debt in Machine Learning Systems · NeurIPS 2015', 'https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf'),
 'R37': ('MIT Department of Economics · Assuring an accurate research record · 16 May 2025', 'https://economics.mit.edu/news/assuring-accurate-research-record'),
 'R38': ('Brynjolfsson & Hitt · Beyond Computation · Journal of Economic Perspectives, 2000', 'https://www.aeaweb.org/articles?id=10.1257/jep.14.4.23'),
 'R39': ('Klarna press release, 27 February 2024 · Bloomberg, 8 May 2025 · The Diary of a CEO, 26 March 2026', 'https://www.youtube.com/watch?v=Cn8HBj8QAbk'),
}


def question(options, cls=''):
    """options: (answer, feedback, correct). Every option carries its own
    feedback, including the right one; that feedback is the teaching."""
    rows = []
    for i, (answer, feedback, correct) in enumerate(options):
        rows.append(f'<button type="button" class="mcq"' + (' data-correct' if correct else '') +
                    f'><span class="letter">{chr(65+i)}</span><span><b>{answer}</b>'
                    f'<span class="why">{feedback}</span></span></button>')
    return (f'<div class="quiz {cls}" aria-label="Choose one answer">' + ''.join(rows) +
            '<p class="verdict" aria-live="polite"></p></div>')


def stats(*items, cls=''):
    """One or more headline figures: (figure, unit) or (figure, unit, trend).
    The optional trend is a small line under the unit — a prior-year comparison
    the figure can be checked against. A trend may be a string (neutral, blue) or
    a (text, 'down') tuple to mark an unfavourable direction in the negative
    colour."""
    cells = []
    for it in items:
        fig, unit = it[0], it[1]
        trend = it[2] if len(it) > 2 else None
        cell = f'<p class="stat-fig">{fig}</p><p class="stat-unit">{unit}</p>'
        if trend:
            text, tcls = trend if isinstance(trend, tuple) else (trend, '')
            cls_attr = f'stat-trend {tcls}'.strip()
            cell += f'<p class="{cls_attr}">{text}</p>'
        cells.append(f'<div>{cell}</div>')
    return f'<div class="stat-row {cls}">' + ''.join(cells) + '</div>'


def steps(*items, build=True, cls=''):
    """A list the narrator walks through: (name, detail). Builds on input."""
    cls = f'q-list roomy {cls}' + (' stagger' if build else '')
    return f'<ol class="{cls}">' + ''.join(
        f'<li><b>{name}</b><span>{detail}</span></li>' for name, detail in items) + '</ol>'


def quote(text, attribution):
    return (f'<div class="quote-body"><p class="quote-mark">“</p><p class="quote-text">{text}</p>'
            f'<p class="quote-attr">{attribution}</p></div>')


def callout(text):
    return f'<p class="callout mt-l">{text}</p>'


def stem(text):
    return f'<p class="lede quiz-stem">{text}</p>'


# Each tuple: course slide, kicker, heading, composition, source IDs.
SLIDES = [

# ---- S1 · The number everyone quotes -----------------------------------------

(1, '', 'AI Value Management',
 '<div class="cover-main"><p class="cover-series">AI for Business Leaders · Online Series for ISCA</p>'
 '<h1 class="cover-title">AI Value Management</h1><div class="cover-rule"></div>'
 '<p class="cover-by">Ray Han, PhD (Computer Science, NTU)</p>'
 '<p class="cover-role">Chief AI Trainer, HGT Consultancy Pte Ltd</p></div>'
 '<div class="cover-foot"><span>ray.han@hgtconsultancy.com</span><span>30 minutes · recorded</span></div>',
 []),

(2, 'MIT NANDA · JULY 2025', 'Everyone quotes ‘95 per cent of AI pilots fail’.',
 stem('This is the most quoted statistic in enterprise AI. What does the 95 per cent in the report count?') +
 question([
   ('AI pilots that failed to reach production',
    'The report’s own funnel gives a different figure for pilots.', False),
   ('Organisations getting zero return on their investment',
    'The report’s words: “95% of organizations are getting zero return.”', True),
   ('AI projects abandoned before they were deployed',
    'Abandonment is a different measure, reported by other surveys.', False),
 ]),
 ['R01']),

(3, 'THE REPORT’S OWN FUNNEL', 'It counts organisations, not pilots.',
 stats(('60%', 'of organisations evaluated task-specific tools'),
       ('20%', 'reached a pilot'),
       ('5%', 'reached production')),
 ['R01']),

(4, 'READ THE DOCUMENT', 'The report relabelled its own finding.',
 steps(('Success', 'What users or executives remarked upon, not what was measured'),
       ('Definitions', 'An appendix gives a stricter one, and the two do not agree'),
       ('Sample', '52 organisations interviewed and 153 leaders surveyed at four conferences'),
       ('Status', 'Preliminary findings. The original MIT link no longer serves the file'),
       cls='short'),
 ['R01', 'R02']),

# ---- S2 · What the evidence agrees on instead ---------------------------------

(5, 'READING THE EVIDENCE', 'Different studies count different things.',
 '<div class="lead-box">All four ask whether AI produces measurable value. '
 'Each counts a different unit, so their headline figures are not directly comparable.</div>'
 '<table class="data-table"><thead><tr><th>Source</th><th>What it counts</th></tr></thead><tbody>'
 '<tr><td>McKinsey, 2026</td><td>EBIT impact</td></tr>'
 '<tr><td>Deloitte, 2026</td><td>Benefits achieved today</td></tr>'
 '<tr><td>S&amp;P Global, 2025</td><td>Projects abandoned</td></tr>'
 '<tr><td>US Census Bureau</td><td>Whether AI is used at all</td></tr>'
 '</tbody></table>',
 ['R03', 'R05', 'R06', 'R07']),

(6, 'THE COMMON ANSWER', 'Few organisations can show material impact.',
 stats(('37%', 'of McKinsey respondents report any EBIT impact', ('Down from 39% in 2025', 'down')),
       ('6%', 'attribute 5 per cent or more of EBIT to AI', 'Flat, about 6% in 2025'),
       ('20%', 'of Deloitte’s leaders already grow revenue from AI', ('Against 74% who hope to', 'down'))),
 ['R03', 'R05']),

(7, 'THE EVIDENCE BASE', 'Every figure here is a self-report.',
 stats(('60%', 'of firms in one survey monitor no financial measure for AI', ('Only 40% track any', 'down')),
       ('68%', 'of chief AI officers start projects they cannot assess', ('Though 72% fear falling behind', 'down')), cls='big') +
 callout('No study located for this session audits financial statements or deployment records.'),
 ['R33', 'R34']),

# ---- S3 · The value was never stuck in the model ------------------------------

(8, 'STANFORD DIGITAL ECONOMY LAB', 'Same technology, very different outcomes.',
 quote('The difference was never the <mark class="not">AI model</mark>. It was always the <mark>organisation</mark>.',
       '<b>The Enterprise AI Playbook</b> · 51 enterprise deployments · April 2026'),
 ['R09']),

(9, 'WHAT GOT IN THE WAY', 'Technology was the easiest part.',
 stats(('77%', 'of the hardest challenges were change, data and process, not technology'), cls='big') +
 callout('“All the hard work is in process documentation and data architecture.” <b>Executive, telecom company</b>'),
 ['R09']),

(10, 'US CENSUS BUREAU · 117,000 FIRMS', 'Most firms changed nothing else.',
 stats(('64%', 'of AI-using firms made no institutional adjustments', ('Bought the tool, nothing more', 'down')),
       ('15%', 'trained staff, and a similar share developed new workflows'), cls='big') +
 callout('Changes to data practices reached only 7 to 8 per cent of these firms.'),
 ['R08']),

(11, 'ROOT CAUSES', 'The symptoms are not the causes.',
 '<table class="data-table figures ranked"><thead><tr><th>Root cause of failure</th><th>Share of cases</th></tr></thead><tbody>'
 '<tr><td>The organisation was not ready to adopt</td><td>35%</td></tr>'
 '<tr><td>Critical knowledge was never captured</td><td>27%</td></tr>'
 '<tr><td>Legal or compliance blocked the project</td><td>18%</td></tr>'
 '<tr><td>The technology was not mature enough</td><td>16%</td></tr>'
 '</tbody></table>' +
 callout('RAND: 84 per cent of practitioners named leadership’s framing of the problem as a root cause.'),
 ['R09', 'R10']),

(12, 'CHECK YOUR UNDERSTANDING', 'Why did this pilot stall?',
 stem('A promising AI pilot has not reached production after a year. On the evidence, which cause is most likely?') +
 question([
   ('The model was not accurate enough',
    'Immature technology accounted for 16 per cent of failures in the Stanford cases.', False),
   ('The organisation was not ready to adopt it',
    'The leading cause at 35 per cent, and consistent with the Census finding.', True),
   ('The team could not prove its return',
    'The study treats that as a consequence of other failures, not a cause.', False),
 ]),
 ['R08', 'R09']),

# ---- S4 · Which stage are you stuck at ----------------------------------------

(13, 'A DIAGNOSIS FOR YOUR PORTFOLIO', 'Four stages, four different failures.',
 steps(('Never started', 'The use was never thought relevant'),
       ('Piloted, never shipped', 'The pilot stopped before production'),
       ('Shipped, not adopted', 'Delivered, but people do not use it'),
       ('Adopted, no benefit shown', 'In use, with no financial effect demonstrated')),
 ['R00']),

(14, 'STAGE ONE', 'Most firms that never started think AI does not apply.',
 stats(('65%', 'of non-adopting firms say AI is not applicable to their business'), cls='big') +
 callout('Laws and regulations ranked among the least common barriers to adoption.'),
 ['R08']),

(15, 'STAGE TWO', 'Nearly half of projects stop before adoption.',
 stats(('46%', 'of projects abandoned between proof of concept and adoption, on average'),
       ('42%', 'of companies abandoned most initiatives, up from 17 per cent a year earlier'), cls='big') +
 callout('The direction is consistent across sources. The precision is not.'),
 ['R06']),

(16, 'STAGE THREE', 'Use is highest where employers encourage it.',
 stats(('40%', 'used chatbots at work with no employer encouragement', 'Encouragement more than doubles it'),
       ('93%', 'used them where encouragement, tools and training combined'), cls='big') +
 callout('Tools and training without encouragement were linked to smaller reported gains.'),
 ['R12']),

(17, 'STAGE FOUR', 'Which stage is this organisation in?',
 stem('Staff use an AI assistant every day and report saving time. Finance cannot show any change in cost or revenue.') +
 question([
   ('Stage two: piloted, never shipped',
    'The tool has shipped and is in daily use.', False),
   ('Stage three: shipped, not adopted',
    'Stage three would mean people are not using it. Here they are.', False),
   ('Stage four: adopted, no benefit shown',
    'The tool is in use and the financial benefit is unevidenced.', True),
 ]),
 ['R03', 'R12']),

# ---- S5 · Why a working model does not move the accounts --------------------

(18, 'RANDOMISED TRIAL', 'AI saved each worker two hours of email a week.',
 stats(('2 hrs', 'less time on email each week, per worker using the tool'),
       ('7,137', 'knowledge workers in 66 firms, over six months'), cls='big') +
 '<p class="callout mt-l">A measured benefit for each worker. The open question is what happened next.</p>',
 ['R11']),

(19, 'WHAT DID NOT CHANGE', 'The saved time moved no measured output.',
 steps(('Email threads answered', 'The same in treated and control groups'),
       ('Meetings attended', 'The same in treated and control groups'),
       ('Documents completed', 'The same in treated and control groups')),
 ['R11']),

(20, 'NATIONAL RECORDS', 'Pay and hours show no effect above two per cent.',
 stats(('2%', 'the largest effect on earnings or hours the data allow'),
       ('25,000', 'workers per survey round, linked to national records'), cls='big') +
 '<p class="callout mt-l">A precise null. Any effect was too small to distinguish from zero.</p>',
 ['R12']),

(21, 'WHERE THE TIME WENT', 'Most of the new work was supervising the tool.',
 stats(('59%', 'of new AI tasks are oversight and integration'),
       ('41%', 'of new AI tasks involve using the tool productively'), cls='big') +
 '<p class="callout mt-l">About a quarter of users now spend longer on the very tasks they first saved time on.</p>',
 ['R12']),

(22, 'FROM TASK TO ACCOUNTS', 'A faster task breaks down four times before the accounts.',
 steps(('Laboratory to field', 'Field gains were substantially smaller than laboratory gains'),
       ('Task to job', 'Time saved on one task is not output gained across a job'),
       ('Worker to firm', 'No study located measures both worker gains and firm profit'),
       ('Firm to economy', 'Official statistics do not measure AI separately')),
 ['R13', 'R20', 'R00']),

(23, 'CHECK YOUR UNDERSTANDING', 'Has a rollout that saves two hours a week paid for itself?',
 '<p class="lede quiz-stem">A colleague says an AI rollout has paid for itself, because staff '
 'now save two hours a week. Which statement does the evidence support?</p>' +
 question([
   ('The tools do not save staff time.',
    'A randomised trial across 66 firms measured two hours a week saved on email.', False),
   ('The research cannot yet say anything about financial effects.',
    'A precise null on earnings and hours is a finding, not an absence of research.', False),
   ('Time savings are well evidenced. Firm-level financial effects are not.',
    'The trial found no change in output, and national records rule out effects above two per cent.', True),
 ]),
 ['R11', 'R12']),

# ---- S6 · One company, read two ways ----------------------------------------

(24, 'KLARNA · FEBRUARY 2024', 'The 700-agent figure came from Klarna itself.',
 stats(('700', 'full-time agents’ worth of work, in Klarna’s own release')) +
 '<div class="grid g2 mt-l">'
 '<article class="named-box"><h4>An equivalence estimate</h4><p>Not a count of people made redundant.</p></article>'
 '<article class="named-box"><h4>People still available</h4><p>Customers could still choose to speak to a live agent.</p></article>'
 '</div>',
 ['R39']),

(25, 'MAY 2025', 'The interview blamed cost. The headlines blamed AI.',
 '<table class="data-table compare"><thead><tr><th>What he said</th><th>What was reported</th></tr></thead><tbody>'
 '<tr><td>Cost was weighted too heavily, and quality fell</td><td>AI had failed</td></tr>'
 '<tr><td>A pilot of two new agents</td><td>A hiring spree</td></tr>'
 '<tr><td>Headcount to keep falling, to about 2,500</td><td>A reversal on AI</td></tr>'
 '</tbody></table>'
 '<p class="callout mt-l">He calls the original article balanced. His objection is to the headline and what was built on it.</p>',
 ['R39']),

(26, 'SECURITIES FILINGS', 'In its filings, headcount fell every year.',
 '<div class="grid g2 filing-grid">'
 '<table class="data-table figures"><thead><tr><th>Year end</th><th>Full-time employees</th></tr></thead><tbody>'
 '<tr><td>2022</td><td>5,527</td></tr><tr><td>2023</td><td>4,352</td></tr>'
 '<tr><td>2024</td><td>3,422</td></tr><tr><td>2025</td><td>2,831</td></tr>'
 '</tbody></table>' +
 stats(('80%', 'of chats handled by AI in 2025, up from 69% at listing')) +
 '</div>',
 ['R22', 'R39']),

(27, 'ONE ANNUAL FILING', 'A claimed saving and a smaller bill are different things.',
 stats(('US$59m', 'cost savings the filing attributes to the assistant'),
       ('+US$4m', 'rise in customer service and operations expenses')) +
 '<p class="callout mt-l">Volumes grew 32 per cent in the same year. The saving is measured '
 'against a counterfactual; the expense line records what was spent.</p>',
 ['R22']),

(28, 'TWO DISCLOSED RATES', 'A rate is only as honest as its denominator.',
 '<div class="grid g2">'
 '<article class="named-box"><h4>Presto Automation</h4><p class="box-fig">85%</p><p>‘Non-intervention’ excluded the offsite agents '
 'who entered the orders. The US regulator opened an investigation.</p></article>'
 '<article class="named-box"><h4>Commonwealth Bank of Australia</h4><p class="box-fig">86%</p><p>A resolve rate whose footnote defines the '
 'denominator as chats resolved without a human.</p></article>'
 '</div>'
 '<p class="callout mt-l">For any rate, ask what the denominator is and who it leaves out.</p>',
 ['R24', 'R25']),

(29, 'CHECK YOUR UNDERSTANDING', 'What should a board rely on in the Klarna case?',
 '<p class="lede quiz-stem">A board paper cites Klarna as proof that an AI assistant cuts customer '
 'service costs. Which evidence should the board rely on?</p>' +
 question([
   ('The US$59 million saving in the annual filing',
    'It is a saving against what costs would otherwise have been, not a fall in spending.', False),
   ('The 853 full-time jobs equivalent from the earnings call',
    'An equivalence estimate stated on a call, with no baseline and no definition of a job.', False),
   ('Neither alone. Compare the saving claim with the expense line.',
    'Read together, they show costs growing more slowly than volumes, not costs falling.', True),
 ]),
 ['R22', 'R23', 'R39']),

# ---- S7 · Can value be attributed at all --------------------------------------

(30, 'THE SAME DATA, THREE METHODS', 'Observational methods were off by a factor of three.',
 stats(('416%', 'lift from a naive comparison of exposed and unexposed users'),
       ('77%', 'lift measured by the randomised experiment'), cls='big') +
 callout('Careful matching narrowed it to 102 per cent. The World Bank calls a before-and-after comparison a counterfeit estimate.'),
 ['R28', 'R27']),

(31, 'THE LIMIT OF MEASUREMENT', 'Attribution works at the workflow, not the accounts.',
 stats(('62×', 'larger campaign needed, at the median, to detect a 10 per cent difference in return'), cls='big') +
 callout('Record a baseline on one process before anyone touches the tool. It cannot be reconstructed afterwards.'),
 ['R29', 'R32']),

# ---- S8 · The next ninety days ------------------------------------------------

(32, 'UK TREASURY GUIDANCE', 'Four conditions separate a saving from an estimate.',
 steps(('Already happened', 'The cash relates to an activity that has taken place'),
       ('Not moved or deferred', 'Costs are not merely relocated or deferred'),
       ('Net of double counting', 'No benefit is claimed twice'),
       ('Reasonable to a third party', 'An impartial reviewer would accept it'), cls='tight') +
 callout('<b>Deadweight</b> Outcomes that would have occurred without any intervention are not a benefit.'),
 ['R30', 'R31']),

(33, 'TAKEAWAYS', 'What to do, and what to stop.',
 '<div class="takeaways">'
 '<section class="tk-recall">'
 '<div class="tk-block"><p class="tk-label">Where value stalls</p><ol class="tk-mini">'
 '<li>Never started</li><li>Piloted, never shipped</li><li>Shipped, not adopted</li><li>Adopted, no benefit shown</li></ol></div>'
 '<div class="tk-block"><p class="tk-label">Where the chain breaks</p><ol class="tk-mini">'
 '<li>Laboratory to field</li><li>Task to job</li><li>Worker to firm</li><li>Firm to economy</li></ol></div>'
 '<div class="tk-block"><p class="tk-label">A cashable saving</p><ol class="tk-mini">'
 '<li>Already happened</li><li>Not moved or deferred</li><li>Net of double counting</li><li>Reasonable to a third party</li></ol></div>'
 '</section>'
 '<section class="tk-act">'
 '<div class="tk-block"><p class="tk-label">Next 90 days</p><ul class="tk-do">'
 '<li>Choose one workflow where the benefit shows in a budget line</li>'
 '<li>Record the baseline before anyone uses the tool</li>'
 '<li>Hold back a comparison group, even a small one</li>'
 '<li>Run it for at least a quarter</li>'
 '<li>Name one person accountable for the benefit</li></ul></div>'
 '<div class="tk-block"><p class="tk-label">Stop</p><ul class="tk-stop">'
 '<li>Funding tools without the process work</li>'
 '<li>Accepting self-reported productivity as financial return</li>'
 '<li>Asking for enterprise-level return on investment</li></ul></div>'
 '</section></div>',
 ['R30', 'R00']),
]
