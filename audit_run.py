#!/usr/bin/env python3
"""Self-audit for the md3e skill repository.

Run **from the repository root**:

    python audit_run.py

Checks frontmatter, required files, cross-document number consistency, the
m3-content mirror, and — when a release package exists — the packaged zip.
Exit code 0 = everything passed.

No third-party dependencies (PyYAML is deliberately not required).
"""

import os
import re
import sys
import zipfile

ROOT = os.getcwd()

# Knowledge baseline declared in SKILL.md / README — update when refreshing the docs.
KNOWLEDGE_BASELINE = '2026-10-08'

# Directories excluded from repo-wide scans.
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', 'dist'}

# Reference files that are large upstream snapshots and legitimately contain
# historical version numbers / dates — excluded from the stale-baseline scan.
SNAPSHOT_PREFIXES = ('references/m3-content/', 'references/compose-api-full.md')

checks = []


def check(label, ok, detail=None):
    checks.append((label, bool(ok), detail))


def parse_frontmatter(text):
    """Minimal top-level scalar parser so we do not need PyYAML."""
    data = {}
    for line in text.splitlines():
        m = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in '"\'':
            value = value[1:-1]
        data[key] = value
    return data


def iter_markdown():
    """Yield repo-relative paths of Markdown files, skipping excluded dirs."""
    for dirpath, dirnames, filenames in os.walk('.'):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), '.').replace('\\', '/')
            yield rel


def read(path):
    with open(path, encoding='utf-8', errors='replace') as fh:
        return fh.read()


# ------------------------------------------------------------- frontmatter ---
skill = read('SKILL.md')
m = re.match(r'^---\n(.*?)\n---', skill, re.S)
check('SKILL.md has frontmatter', bool(m))
if m:
    fm = parse_frontmatter(m.group(1))
    name = fm.get('name', '')
    check('frontmatter name=md3e', name == 'md3e', name)
    # Agent-skill naming convention (mirrors skill-creator/quick_validate.py).
    check('name is hyphen-case', bool(re.fullmatch(r'[a-z0-9-]+', name)), name)
    check('name has no leading/trailing/double hyphen',
          not (name.startswith('-') or name.endswith('-') or '--' in name), name)
    check('frontmatter version present', bool(fm.get('version')), fm.get('version'))
    desc = fm.get('description', '')
    check('description length <= 1024', len(desc) <= 1024, len(desc))
    check('description has no angle brackets', '<' not in desc and '>' not in desc)
    for token in ['Material 3 Expressive', 'MD3E', 'MaterialExpressiveTheme', 'Material Design 3']:
        check(f'description contains {token!r}', token in desc)
    check(f'declared baseline mentions {KNOWLEDGE_BASELINE}', KNOWLEDGE_BASELINE in desc)

lines = skill.splitlines()
check('SKILL.md line count <= 200', len(lines) <= 200, len(lines))

# ---------------------------------------------------------- required paths ---
required = [
    'SKILL.md', 'README.md', 'README.zh-CN.md', 'CHANGELOG.md', 'LICENSE',
    'PUBLISH.md', 'CONTRIBUTING.md', '.gitignore',
    'references/version-baseline.md', 'references/design-tokens.md',
    'references/components-catalog.md', 'references/m3-vs-m3e-diff.md',
    'references/compose-api-full.md', 'references/expressive-design-tactics.md',
    'references/design-research.md',
    'references/m3e/design-system.md', 'references/m3e/color-typography-shape.md',
    'references/m3e/motion-physics.md', 'references/m3e/components.md',
    'references/m3e/compose-api.md',
    'references/m3e/design-system.en.md', 'references/m3e/color-typography-shape.en.md',
    'references/m3e/motion-physics.en.md', 'references/m3e/components.en.md',
    'references/m3e/compose-api.en.md',
    'assets/templates/MD3ETheme.kt', 'assets/templates/Color.kt',
    'assets/templates/Type.kt', 'assets/templates/Shape.kt',
    'scripts/generate_theme.py', 'scripts/package_skill.py',
]
for path in required:
    check(f'exists: {path}', os.path.exists(path))

# --------------------------------------------------------- content details ---
for fn, label in [('references/design-tokens.md', 'design-tokens'),
                  ('references/m3-vs-m3e-diff.md', 'm3-vs-m3e-diff')]:
    bad = [i + 1 for i, l in enumerate(read(fn).splitlines()) if 'Typography now supports' in l]
    check(f'{label}: no false defaultFontFamily claim', not bad, bad)

dp = [i + 1 for i, l in enumerate(read('references/design-tokens.md').splitlines()[128:144])
      if 'dp' in l]
check('design-tokens: letterSpacing units are sp not dp', not dp, dp)

# ------------------------------------------------------------- m3-content ---
check('m3-content dir exists', os.path.isdir('references/m3-content'))
if os.path.isdir('references/m3-content'):
    spec_pages, hub_pages = [], []
    for dirpath, _dirnames, filenames in os.walk('references/m3-content'):
        for name in filenames:
            if name.endswith('.md'):
                path = os.path.join(dirpath, name)
                (spec_pages if re.match(r'^---\s*\n', read(path)) else hub_pages).append(path)
    total = len(spec_pages) + len(hub_pages)
    check('m3-content has >= 200 md files', total >= 200, total)
    # Documented split must match what is on disk (docs claim 249 spec + 7 hub).
    check('m3-content spec page count (249)', len(spec_pages) == 249, len(spec_pages))
    check('m3-content hub page count (7)', len(hub_pages) == 7, len(hub_pages))

# --------------------------------------------- cross-document consistency ---
stale = []
contradictory = []
for rel in iter_markdown():
    # CHANGELOG quotes historical wording verbatim, so it is exempt from these scans.
    if rel.startswith(SNAPSHOT_PREFIXES) or rel == 'CHANGELOG.md':
        continue
    text = read(rel)
    if f'baseline: 2026-09-14' in text or f'基线：2026-09-14' in text:
        stale.append(rel)
    for bad in ('10K+ lines', '10000+ 行'):
        if bad in text:
            contradictory.append(f'{rel} ({bad})')
check('no stale 2026-09-14 baseline declarations', not stale, stale)
check('no contradictory line-count claims', not contradictory, contradictory)

# -------------------------------------------------------------------- zip ---
ZIP = os.path.join(os.pardir, 'dist', 'md3e.zip')
if not os.path.exists(ZIP):
    print('note: ../dist/md3e.zip not found — skipping release-package checks')
    print('      (generate it with PUBLISH.md step 3 before releasing)\n')
else:
    if os.path.getmtime(ZIP) >= max(os.path.getmtime(p) for p in required if os.path.exists(p)):
        check('dist/md3e.zip newer than sources', True)
    else:
        check('dist/md3e.zip newer than sources', False, 'stale package — rebuild it')

    with zipfile.ZipFile(ZIP) as z:
        names = z.namelist()

        def entry(rel):
            """Resolve a skill-relative path inside the archive (top folder agnostic)."""
            return next((n for n in names if n == rel or n.endswith('/' + rel)), None)

        def has(rel):
            return entry(rel) is not None

        def read_entry(rel):
            name = entry(rel)
            return z.read(name).decode('utf-8', errors='replace') if name else ''

        # Distribution-format checks: exactly one top-level skill folder, POSIX separators.
        tops = {n.split('/')[0] for n in names}
        check('zip has exactly one top-level folder', len(tops) == 1, sorted(tops))
        check('zip top-level folder is "md3e"', tops == {'md3e'}, sorted(tops))
        backslashed = [n for n in names if '\\' in n]
        check('zip entries use forward slashes (ZIP spec)', not backslashed, backslashed[:3])

        check('zip has SKILL.md', has('SKILL.md'))
        check('zip has design-tokens.md', has('references/design-tokens.md'))
        check('zip has generate_theme.py', has('scripts/generate_theme.py'))
        for en in ['references/m3e/design-system.en.md', 'references/m3e/color-typography-shape.en.md',
                   'references/m3e/motion-physics.en.md', 'references/m3e/components.en.md',
                   'references/m3e/compose-api.en.md']:
            check(f'zip has {os.path.basename(en)}', has(en))

        # Content (not line-number) based freshness checks.
        check('zip design-tokens.md has no false claim',
              'Typography now supports' not in read_entry('references/design-tokens.md'))
        check('zip m3-vs-m3e-diff.md has no false claim',
              'Typography now supports' not in read_entry('references/m3-vs-m3e-diff.md'))

# ----------------------------------------------------------------- PUBLISH ---
pub = read('PUBLISH.md')
check('PUBLISH.md no obsolete "git tag v1.0.0"', 'git tag v1.0.0' not in pub)

# ------------------------------------------------------------------ output ---
fails = [(label, detail) for label, ok, detail in checks if not ok]
passes = sum(1 for _l, ok, _d in checks if ok)
for label, ok, detail in checks:
    mark = 'PASS' if ok else 'FAIL'
    extra = f'  detail={detail}' if (detail is not None and not ok) else ''
    print(f'{mark}  {label}{extra}')
print()
print(f'SUMMARY: {passes}/{len(checks)} passed, {len(fails)} failed')
sys.exit(1 if fails else 0)
