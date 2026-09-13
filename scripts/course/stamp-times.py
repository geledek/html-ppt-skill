"""Insert a per-slide time allowance into course.md, measured from the narration.

Recorded delivery is ~150 wpm (references/course-workflow.md, gate 1 table), so a
slide's time is its narration word count / 150, plus any pause the Delivery line
asks for. Rewrites in place and prints a per-section summary.
"""
import io, re, sys

WPM = 150
path = sys.argv[1]
s = io.open(path, encoding='utf-8').read()
head, narr = s.split('## Narration\n', 1)

block = re.compile(r'(^#### (\d+) · [^\n]+\n)(.*?)(\*\*Narration:\*\*\n)(.*?)(?=^#### |^### S\d|^## [^#]|\Z)',
                   re.M | re.S)


def words(text):
    t = re.sub(r'\[[^\]]*\]|\*\*|[_*`]', ' ', text)
    return len([w for w in t.split() if any(c.isalnum() for c in w)])


rows = []


def stamp(m):
    heading, n, meta, marker, text = m.groups()
    n = int(n)
    w = words(text)
    secs = w * 60.0 / WPM
    pause = re.search(r'Allow (\d+) seconds', meta)
    if pause:
        secs += int(pause.group(1))
    secs = int(round(secs))
    rows.append((n, w, secs))
    meta = re.sub(r'^\*\*Time:\*\* [^\n]*\n', '', meta, flags=re.M)
    line = '**Time:** %d:%02d  ·  %d words at %d wpm%s\n' % (
        secs // 60, secs % 60, w, WPM,
        ' + %ss pause' % pause.group(1) if pause else '')
    if '**Sources:**' in meta:
        meta = re.sub(r'(^\*\*Sources:\*\*[^\n]*\n)', r'\1' + line, meta, count=1, flags=re.M)
    else:
        meta = line + meta
    return heading + meta + marker + text


narr = block.sub(stamp, narr)
io.open(path, 'w', encoding='utf-8').write(head + '## Narration\n' + narr)

total = sum(r[2] for r in rows)
print('%d slides · %d words · %d:%02d total' % (len(rows), sum(r[1] for r in rows), total // 60, total % 60))
for n, w, secs in rows:
    print('  %2d  %d:%02d  %4d words' % (n, secs // 60, secs % 60, w))
