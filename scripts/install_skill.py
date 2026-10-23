#!/usr/bin/env python3
"""Install the MD3E skill into an AI assistant's skills directory.

The whole folder is copied, so relative paths such as ``references/version-baseline.md``
keep working after installation.

Usage:
    python scripts/install_skill.py --target ~/.codebuddy/skills
    python scripts/install_skill.py --assistant codebuddy --global
    python scripts/install_skill.py --assistant claude
    python scripts/install_skill.py --target ./skills --dry-run

Exit codes: 0 = installed (or dry-run OK), 1 = refused / invalid source.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

SKILL_NAME = 'md3e'
SOURCE = Path(__file__).resolve().parent.parent

REQUIRED = [
    'SKILL.md',
    'references/version-baseline.md',
    'references/component-index.md',
    'references/compose-patterns.md',
    'assets/templates/MD3ETheme.kt',
]

# Well-known skill directories, relative to the project or the user home.
ASSISTANT_DIRS = {
    'codebuddy': Path('.codebuddy') / 'skills',
    'claude': Path('.claude') / 'skills',
}

# Only skill content is installed — an allow-list keeps unrelated local folders
# (source checkouts, scratch dirs) out of the destination.
SHIP_FILES = ('SKILL.md', 'README.md', 'README.zh-CN.md', 'CHANGELOG.md', 'LICENSE')
SHIP_DIRS = ('references', 'assets', 'scripts')

EXCLUDE_DIRS = {'__pycache__', '.git', '.github', 'dist', 'output', 'theme', 'node_modules'}
EXCLUDE_FILES = {'.gitignore', '.gitattributes', '.DS_Store', 'Thumbs.db'}
EXCLUDE_SUFFIX = ('.pyc', '.pyo', '.zip')


def validate(source):
    """Return a list of problems that would make the install unusable."""
    problems = [rel for rel in REQUIRED if not (source / rel).is_file()]
    skill = source / 'SKILL.md'
    if skill.is_file():
        head = skill.read_text(encoding='utf-8', errors='replace')[:2000]
        if 'name: md3e' not in head:
            problems.append('SKILL.md frontmatter name is not "md3e"')
        if 'description:' not in head:
            problems.append('SKILL.md frontmatter has no description')
    return problems


def copy_skill(source, dest):
    count = 0
    dest.mkdir(parents=True, exist_ok=True)

    for name in SHIP_FILES:
        src = source / name
        if src.is_file():
            shutil.copy2(src, dest / name)
            count += 1

    for dirname in SHIP_DIRS:
        base = source / dirname
        if not base.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
            rel_dir = Path(dirpath).relative_to(source)
            (dest / rel_dir).mkdir(parents=True, exist_ok=True)
            for name in sorted(filenames):
                if name in EXCLUDE_FILES or name.endswith(EXCLUDE_SUFFIX):
                    continue
                shutil.copy2(Path(dirpath) / name, dest / rel_dir / name)
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description='Install the MD3E skill for an AI assistant.')
    parser.add_argument('--target', help='skills directory; the skill is created as <target>/md3e')
    parser.add_argument('--assistant', choices=sorted(ASSISTANT_DIRS),
                        help='use a well-known skills directory (project-level by default)')
    parser.add_argument('--home', action='store_true',
                        help='with --assistant, install under the user home instead of the cwd')
    parser.add_argument('--force', action='store_true', help='overwrite an existing install')
    parser.add_argument('--dry-run', action='store_true', help='report what would happen')
    args = parser.parse_args()

    if not args.target and not args.assistant:
        parser.error('pass --target <skills dir> or --assistant <name>')

    problems = validate(SOURCE)
    if problems:
        sys.exit('error: source skill is incomplete: ' + '; '.join(problems))

    if args.target:
        base = Path(os.path.expanduser(args.target))
    else:
        root = Path.home() if args.home else Path.cwd()
        base = root / ASSISTANT_DIRS[args.assistant]

    dest = base / SKILL_NAME

    try:
        dest.resolve().relative_to(SOURCE.resolve())
        sys.exit('error: refusing to install inside the source folder')
    except ValueError:
        pass

    if dest.exists() and not args.force:
        sys.exit(f'error: {dest} already exists (use --force to overwrite)')

    if args.dry_run:
        print(f'would install: {SOURCE} -> {dest}')
        return

    if dest.exists():
        shutil.rmtree(dest)
    count = copy_skill(SOURCE, dest)

    print(f'installed {count} files -> {dest}')
    print('verify: ask your assistant "What is the MD3E knowledge baseline?" '
          '(expected answer: 2026-10-23).')


if __name__ == '__main__':
    main()
