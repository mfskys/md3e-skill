#!/usr/bin/env python3
"""Package the md3e skill into a distributable zip.

Produces ``dist/md3e.zip`` containing a single top-level ``md3e/`` folder, which
is what the agent-skill distribution format expects — users extract the archive
and drop the resulting ``md3e/`` folder straight into their skills directory:

    md3e.zip
    └── md3e/
        ├── SKILL.md
        ├── references/
        ├── assets/
        └── scripts/

Every archive entry uses a forward slash. Windows PowerShell's
``Compress-Archive`` writes backslashes instead, which the ZIP specification
forbids: on macOS/Linux the tree then extracts as one flat pile of files whose
names contain literal ``\\`` characters.

Usage:
    python scripts/package_skill.py
    python scripts/package_skill.py --source . --out ../dist --name md3e
"""

import argparse
import fnmatch
import os
import sys
import zipfile
from pathlib import Path

DEFAULT_NAME = 'md3e'

# VCS, editor, build and OS cruft — never packaged.
EXCLUDE_DIRS = {'.git', '.github', '.idea', '.vscode', '__pycache__',
                'dist', 'output', 'theme', 'node_modules'}
EXCLUDE_FILES = {'.gitignore', '.gitattributes', '.DS_Store', 'Thumbs.db'}
EXCLUDE_PATTERNS = ('*.pyc', '*.pyo', '*.zip')


def iter_skill_files(root: Path):
    """Yield skill-relative paths of everything that should ship."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
        for name in sorted(filenames):
            if name in EXCLUDE_FILES or any(fnmatch.fnmatch(name, p) for p in EXCLUDE_PATTERNS):
                continue
            yield Path(dirpath, name).relative_to(root)


def main():
    ap = argparse.ArgumentParser(description='Package the md3e skill into a distributable zip.')
    ap.add_argument('--source', default='.', help='skill source directory (default: current directory)')
    ap.add_argument('--out', default=os.path.join('..', 'dist'), help='output directory for the zip')
    ap.add_argument('--name', default=DEFAULT_NAME, help='skill folder name used inside the archive')
    args = ap.parse_args()

    src = Path(args.source).resolve()
    if not (src / 'SKILL.md').is_file():
        sys.exit(f'error: no SKILL.md found in {src}')

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f'{args.name}.zip'

    files = sorted(iter_skill_files(src))
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for rel in files:
            # as_posix() guarantees '/' separators on every platform.
            archive.write(src / rel, (Path(args.name) / rel).as_posix())

    size_mb = sum((src / rel).stat().st_size for rel in files) / 1024 / 1024
    print(f'Packaged {len(files)} files ({size_mb:.1f} MB)')
    print(f'  archive : {zip_path}')
    print(f'  contents: {args.name}/  (SKILL.md + references/ + assets/ + scripts/)')


if __name__ == '__main__':
    main()
