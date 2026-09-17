#!/usr/bin/env python3
"""qa-lint :: text checks for a built course — the greps the QA rubric names.

Runs over the course SOURCE (slides.py + script.md), not the built HTML, because
these are language rules on what was authored. Three checks, each written to fire
on a real violation and stay silent on clean content — naive word-lists cry wolf
on source titles, verbatim quotes, qualified "US$", and ordinary prose, so each
check carries the exemptions that calibration against a real deck required.

  1. Closed-set language guard  — US spelling, bare "$", M/D/Y dates
  2. No anthropomorphic overclaim — "the model understands/reasons/…"
  3. Currency is dated            — a currency word with no year near it

Exit 0 if clean, 1 if any check finds a violation. Usage:
    qa_text_checks.py courses/<name>
The rules are in references/slide-design.md and references/course-qa.md.
"""
import re, sys, os

course = sys.argv[1] if len(sys.argv) > 1 else ""
course = course.rstrip("/")
slides = os.path.join(course, "slides.py")
script = os.path.join(course, "script.md")
for p in (slides, script):
    if not os.path.isfile(p):
        print("error: %s not found" % p, file=sys.stderr); sys.exit(2)

fails = 0


def lines_of(path):
    with open(path, encoding="utf-8") as f:
        return f.readlines()


# A line's quoted/source-label spans are exempt: a verbatim quote must keep the
# source's own spelling, and a source label ('McKinsey · …') is a proper title.
# We blank out double-quoted runs and the SOURCE_LABELS dict lines before scanning.
def scannable(line):
    # drop the contents of "..." and '...'  curly and straight
    line = re.sub(r'"[^"]*"', '""', line)
    line = re.sub(r'“[^”]*”', '""', line)
    return line


def is_source_label(line):
    # slides.py source dict rows look like:  'R04': ('McKinsey · …', 'https…'),
    return bool(re.match(r"\s*'R\d+':", line))


# ---- 1. closed-set language guard -------------------------------------------
# An EXPLICIT closed list of US spellings whose UK form is house style — a suffix
# pattern over-fires ("size", "prize", "seize" are not -ise words). Proper nouns
# (Bureau of Labor Statistics, an -ize source title) keep their spelling, so we
# match lower-case only and let scannable()/is_source_label() drop quotes+labels.
US_WORDS = re.compile(
    r"\b(color|colors|behavior|behaviors|favor|favors|labor|honor|honors|"
    r"organize|organizes|organized|organizing|organization|organizations|"
    r"optimize|optimizes|optimized|optimizing|optimization|"
    r"realize|realizes|realized|realizing|analyze|analyzes|analyzed|analyzing|"
    r"prioritize|prioritized|customize|customized|recognize|recognized|"
    r"maximize|minimize|summarize|emphasize|utilize|utilized|"
    r"catalog|catalogs|defense|offense|license|licensing|traveling|modeling|"
    r"canceled|labeled|fulfill|enrollment)\b")
BARE_DOLLAR = re.compile(r"(?<![A-Za-z])(?<!US)(?<!S)\$\s?\d")   # $5 but not US$5, S$5
MDY = re.compile(r"\b[01]?\d/[0-3]?\d/\d{2,4}\b")


def check_language():
    hits = []
    for path in (slides, script):
        for n, raw in enumerate(lines_of(path), 1):
            if is_source_label(raw):
                continue
            line = scannable(raw)
            for rx, label in ((US_WORDS, "US spelling"),
                              (BARE_DOLLAR, 'bare "$" (use US$/S$/… )'),
                              (MDY, "M/D/Y date")):
                m = rx.search(line)
                if m:
                    hits.append((path, n, label, m.group(0).strip()))
    if hits:
        fails_local(hits, "closed-set language guard")


# ---- 2. no anthropomorphic overclaim ----------------------------------------
# fire only when an AI subject governs the verb — a bare "reason"/"think" is fine
AI_SUBJ = r"(?:the\s+)?(?:model|models|AI|assistant|assistants|tool|tools|system|systems|chatbot|chatbots|LLM|it|they)"
ANTHRO = re.compile(
    AI_SUBJ + r"\s+(?:\w+\s+){0,2}?(understands?|knows?|reasons?|thinks?|"
    r"decides?|believes?|wants?|understand|know|reason|think|decide)\b", re.I)
ANTHRO_ADJ = re.compile(AI_SUBJ + r"\s+(?:is|are)\s+(?:\w+\s+){0,2}?"
                        r"(autonomous|unbiased|objective|sentient|conscious)\b", re.I)


def check_anthropomorphic():
    hits = []
    for path in (slides, script):
        for n, raw in enumerate(lines_of(path), 1):
            line = scannable(raw)   # quoted/attributed use is exempt
            for rx in (ANTHRO, ANTHRO_ADJ):
                m = rx.search(line)
                if m:
                    hits.append((path, n, "anthropomorphic AI claim", m.group(0).strip()))
    if hits:
        fails_local(hits, "no anthropomorphic overclaim")


# ---- 3. currency is dated ----------------------------------------------------
# A currency word makes a claim time-sensitive; it needs a year on the same line.
# Only fire when the word is used as a claim-qualifier ("currently 80%",
# "the latest model"), not ordinary time adverbs ("run it now", "get this far now").
CURRENCY = re.compile(r"\b(as of|currently|latest|most recent|at present|"
                      r"to date|the current)\b", re.I)
YEAR = re.compile(r"\b(19|20)\d{2}\b|\bas at\b")


def check_currency():
    hits = []
    for n, raw in enumerate(lines_of(script), 1):
        line = scannable(raw)
        m = CURRENCY.search(line)
        if m and not YEAR.search(line):
            hits.append((script, n, "currency word, no date", m.group(0).strip()))
    if hits:
        fails_local(hits, "currency is dated")


def fails_local(hits, name):
    global fails
    fails = 1
    print("FAIL  %s (%d):" % (name, len(hits)))
    for path, n, label, tok in hits[:12]:
        print("        %s:%d  %s — '%s'" % (os.path.basename(path), n, label, tok))


check_language()
if not fails or True:   # run all three so a review sees every failing check
    pass
check_anthropomorphic()
check_currency()

if not fails:
    print("ok    language guard, no anthropomorphic overclaim, currency dated")
sys.exit(1 if fails else 0)
