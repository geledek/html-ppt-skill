"""Audience-facing slide compositions for AI Value Management.

Narration, sources and the outline live in course.md. Shared components live in
templates/full-decks/course/style.css. Build with scripts/build-course.sh.

Gate 2: only the representative sections are composed, S5 (slides 18-23) and
S6 (slides 24-29). The remaining slides are composed at gate 3.
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
    """One or more headline figures: (figure, unit)."""
    return f'<div class="stat-row {cls}">' + ''.join(
        f'<div><p class="stat-fig">{fig}</p><p class="stat-unit">{unit}</p></div>'
        for fig, unit in items) + '</div>'


def steps(*items, build=True):
    """A list the narrator walks through: (name, detail). Builds on input."""
    cls = 'q-list roomy' + (' stagger' if build else '')
    return f'<ol class="{cls}">' + ''.join(
        f'<li><b>{name}</b><span>{detail}</span></li>' for name, detail in items) + '</ol>'


# Each tuple: course slide, kicker, heading, composition, source IDs.
SLIDES = [

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
 '<article class="named-box"><h4>Commonwealth Bank of Australia</h4><p class="box-fig">86%</p><p>A resolve rate with its denominator defined '
 'in a footnote: chats resolved without a human.</p></article>'
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
]
