"""Import every wiki checkbox as source evidence, never as gameplay certification."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


def git(folder, *args, input=None):
    return subprocess.run(['git', '-C', str(folder), *args], input=input,
                          check=True, capture_output=True).stdout


def tasks(text, page):
    headings, result, seen = [], [], set()
    fence = None
    comment = False
    for line_number, line in enumerate(text.splitlines(), 1):
        if fence:
            closing = re.match(r'^ {0,3}(`{3,}|~{3,})\s*$', line)
            if closing and closing[1][0] == fence[0] and len(closing[1]) >= len(fence):
                fence = None
            continue
        # Comments and fenced examples are documentation, not actual tasks.
        visible = ''
        while line:
            if comment:
                _, marker, line = line.partition('-->')
                if not marker:
                    break
                comment = False
            else:
                before, marker, after = line.partition('<!--')
                visible += before
                line = after
                if marker:
                    comment = True
                else:
                    break
        match = re.match(r'^ {0,3}(`{3,}|~{3,})', visible)
        if match:
            fence = match[1]
            continue
        heading = re.match(r'^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$', visible)
        if heading:
            level = len(heading[1])
            headings = [row for row in headings if row[0] < level]
            headings.append((level, heading[2]))
        match = re.match(r'^\s*(?:[-+*]|\d+[.)])\s+\[([ xX])\]\s+(.+?)\s*$', visible)
        if not match:
            continue
        title = match[2]
        section = [name for _, name in headings]
        identity = '\0'.join([page, *section, ' '.join(title.split())])
        key = 'wiki:' + hashlib.sha256(identity.encode('utf-8')).hexdigest()[:24]
        if key in seen:
            raise ValueError('Ambiguous duplicate task in the same section: ' + page)
        seen.add(key)
        result.append(dict(id=key, page=page, section=section, line=line_number,
                           text=title, sourceReportedChecked=match[1].lower() == 'x',
                           acceptance='source-checklist-only',
                           url='https://github.com/Herbertofury/Advent-of-Ascension/wiki/' + page[:-3]))
    return result


def snapshot(folder):
    folder = Path(folder)
    revision = git(folder, 'rev-parse', 'HEAD').decode().strip()
    if not re.fullmatch('[0-9a-f]{40,64}', revision):
        raise ValueError('An exact wiki Git revision is required')
    names = git(folder, 'ls-tree', '-rz', '--name-only', revision).split(b'\0')
    names = sorted(name.decode('utf-8') for name in names if name.endswith(b'.md'))
    if not names:
        raise ValueError('The complete wiki has no Markdown pages')
    pages, checklist = [], []
    for name in names:
        raw = git(folder, 'show', revision + ':' + name)
        pages.append(dict(path=name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()))
        checklist.extend(tasks(raw.decode('utf-8-sig'), name))
    return dict(schema=1, adapter='aoa-complete-wiki-checklist-1',
                repository='Herbertofury/Advent-of-Ascension.wiki', revision=revision,
                pages=pages, tasks=checklist,
                pageCount=len(pages), taskCount=len(checklist),
                reportedChecked=sum(row['sourceReportedChecked'] for row in checklist),
                runtimeCompletionInferred=False)


def compare(previous, current):
    before = {row['id']: row for row in previous['tasks']}
    after = {row['id']: row for row in current['tasks']}
    return dict(revisionChanged=previous['revision'] != current['revision'],
                added=sorted(after.keys() - before.keys()),
                removed=sorted(before.keys() - after.keys()),
                changed=sorted(key for key in before.keys() & after.keys() if before[key] != after[key]),
                pageChanges=previous['pages'] != current['pages'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wiki', required=True)
    parser.add_argument('--output')
    parser.add_argument('--check')
    args = parser.parse_args()
    current = snapshot(args.wiki)
    if args.output:
        Path(args.output).write_text(json.dumps(current, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.check:
        previous = json.loads(Path(args.check).read_text(encoding='utf-8'))
        changes = compare(previous, current)
        print(json.dumps(changes))
        if any(changes.values()):
            raise SystemExit('Wiki changed: reconcile its complete checklist before claiming it is current')
    else:
        print(json.dumps({k: current[k] for k in ['revision', 'pageCount', 'taskCount', 'reportedChecked']}))


if __name__ == '__main__':
    main()
