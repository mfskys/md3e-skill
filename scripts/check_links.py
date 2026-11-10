"""Verify that `*.md` references in the docs actually resolve.

Skips references that are intentionally not files in this repo: the rules-mode
install targets (AGENTS.md, GEMINI.md, QWEN.md, .cursor/.clinerules/... ) and the
post-install path `md3e/SKILL.md`.

Usage:
    python scripts/check_links.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_NAMES = {
    "AGENTS.md",
    "GEMINI.md",
    "QWEN.md",
    "SKILL.md",  # post-install path md3e/SKILL.md
}
SKIP_PARTS = (".clinerules/", ".continue/", ".github/", ".trae/", ".windsurf/", ".cursor/")

bad = []
checked = 0

for f in list(ROOT.glob("*.md")) + list((ROOT / "references").rglob("*.md")):
    text = f.read_text(encoding="utf-8")
    for m in re.finditer(r"`([A-Za-z0-9_\-./]+\.md)`", text):
        ref = m.group(1)
        if ref.startswith(("http", "androidx")) or ref == ".en.md":
            continue
        if ref.split("/")[-1] in SKIP_NAMES or any(p in ref for p in SKIP_PARTS):
            continue
        checked += 1
        cands = (ROOT, ROOT / "references", ROOT / "references" / "m3e", f.parent)
        if not any((c / ref).exists() for c in cands):
            bad.append(f"{f.relative_to(ROOT)} -> {ref}")

print(f"checked {checked} in-repo md refs")
if bad:
    print("BROKEN:")
    for b in sorted(set(bad)):
        print("  ", b)
    sys.exit(1)
print("no broken refs")
