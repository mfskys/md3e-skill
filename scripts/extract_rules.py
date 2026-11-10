"""Extract usable rules out of a mirrored m3.material.io component folder.

The mirror is mostly images + captions. This pulls out what survives losing the
images: Do/Don't/Caution/Note callouts, requirement sentences, tables.
"""
import json
import re
import sys
from pathlib import Path

# Windows terminals default to GBK; the mirror contains NBSP and typographic quotes.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:  # pragma: no cover
    pass

NOISE = re.compile(r"\[More on|\[Learn more|^\s*$|^!\[")
LABELS = {"do", "don't", "don’t", "dont", "caution", "note", "warning", "error"}


def clean(line: str) -> str:
    t = line.strip()
    t = re.sub(r"^[-*]\s+", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def is_rule(s: str) -> bool:
    if len(s) < 8 or len(s) > 400:
        return False
    if s.startswith(("|", "![", "#", ">", "```")):
        return False
    if NOISE.search(s):
        return False
    return True


def extract(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = {"callouts": [], "tables": [], "requirements": []}
    i = 0
    table_buf = []
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith("|"):
            table_buf.append(line)
            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith("|"):
                if len(table_buf) >= 2:
                    out["tables"].append("\n".join(table_buf))
                table_buf = []
            i += 1
            continue

        m = re.match(r"^(check|close|exclamation|star|error|warning)\b\s*(.*)$", line)
        if m:
            kind, inline = m.groups()
            rule = clean(inline)
            j = i + 1
            # a bare "Do" / "Don't" / "Caution" label: the rule follows
            if rule.lower().strip(":") in LABELS or not rule:
                while j < len(lines) and not lines[j].strip():
                    j += 1
                rule = ""
                # skip another bare label line
                while j < len(lines) and lines[j].strip().lower().strip(":") in LABELS:
                    j += 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                if j < len(lines):
                    rule = clean(lines[j])
            if rule and rule.lower().strip(":") not in LABELS:
                out["callouts"].append((kind, rule))
            i = j + 1
            continue

        s = clean(line)
        if is_rule(s) and re.search(
            r"\b(should|must|need|avoid|don't|do not|no longer|use .* instead|ensure|keep)\b",
            s,
            re.I,
        ):
            out["requirements"].append(s)

        i += 1
    return out


if __name__ == "__main__":
    if sys.argv[1] == "--all":
        root = Path(sys.argv[2])
        data = {}
        for d in sorted(root.iterdir()):
            if not d.is_dir():
                continue
            entry = {}
            for name in ("overview", "guidelines", "specs", "accessibility"):
                f = d / f"{name}.md"
                if f.exists():
                    entry[name] = extract(f)
            data[d.name] = entry
        Path(sys.argv[3]).write_text(
            json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        tot = sum(
            len(v.get("callouts", [])) + len(v.get("requirements", []))
            for e in data.values()
            for v in e.values()
        )
        print(f"components={len(data)} extracted_items={tot}")
    else:
        for name in sys.argv[1:]:
            p = Path(name)
            r = extract(p)
            print(f"\n===== {p} =====")
            for k, v in r["callouts"]:
                print(f"  [{k}] {v}")
            for t in r["tables"]:
                print(t)
            for v in r["requirements"]:
                print(f"  - {v}")
