"""Download androidx material3 token files and dump their constants.

Used when writing a `references/recipes/*.md` file: the exact dp values for a
component live in `tokens/<Name>Tokens.kt`, not in the m3.material.io pages
(those keep measurements inside images).

Usage:
    python scripts/grab_tokens.py ButtonSmallTokens.kt FabMediumTokens.kt

Set HTTPS_PROXY / use a proxy if raw.githubusercontent.com is unreachable.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:  # pragma: no cover
    pass

BASE = ("https://raw.githubusercontent.com/androidx/androidx/androidx-main/"
        "compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens/")
CACHE = Path(tempfile.gettempdir()) / "md3e-token-cache"
CACHE.mkdir(exist_ok=True)

PROXY = os.environ.get("MD3E_PROXY")  # e.g. http://127.0.0.1:7897


def fetch(name: str) -> Path:
    dest = CACHE / name
    if dest.exists() and dest.stat().st_size > 100:
        return dest
    cmd = ["curl", "-sL", "--max-time", "40", BASE + name, "-o", str(dest)]
    if PROXY:
        cmd[1:1] = ["-x", PROXY]
    subprocess.run(cmd, check=False)
    return dest


def main(names):
    for name in names:
        p = fetch(name)
        if not p.exists() or p.stat().st_size < 100:
            print(f"\n### {name}  [FETCH FAILED]")
            continue
        t = p.read_text(encoding="utf-8")
        print(f"\n### {name}")
        for m in re.finditer(r"inline val (\w+):[^=]*?get\(\)\s*=\s*(.+)", t):
            k, v = m.group(1), m.group(2).strip()
            if "ColorToken" in v or v.startswith("Color"):
                continue
            print(f"  {k:32s} {v}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1:])
