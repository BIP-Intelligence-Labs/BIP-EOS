"""
M-007.0.1 — Namespace Inventory

Scans the repository for legacy namespace references and produces
a Markdown report.

Run from the repository root:

    python namespace_inventory.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TEXT_EXTENSIONS = {
    ".py", ".md", ".txt", ".rst",
    ".toml", ".yaml", ".yml",
    ".json", ".cfg", ".ini"
}

PATTERNS = [
    ("bip_eos", re.compile(r"\bbip_eos\b")),
    ("BIP EOS", re.compile(r"\bBIP EOS\b")),
    ("Builder Intelligence Platform",
     re.compile(r"Builder Intelligence Platform", re.IGNORECASE)),
]

SKIP = {
    ".git", ".pytest_cache", "__pycache__",
    ".venv", "venv", "node_modules"
}


def should_scan(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return False
    return not any(part in SKIP for part in path.parts)


results = []

for file in ROOT.rglob("*"):
    if not file.is_file() or not should_scan(file):
        continue

    try:
        text = file.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue

    for label, pattern in PATTERNS:
        matches = list(pattern.finditer(text))
        if matches:
            results.append(
                (label, file.relative_to(ROOT), len(matches))
            )

report = REPORTS / "namespace_inventory.md"

with report.open("w", encoding="utf-8") as f:
    f.write("# Namespace Inventory\n\n")
    f.write("| Namespace | File | Matches |\n")
    f.write("|-----------|------|--------:|\n")
    total = 0
    for label, path, count in sorted(results):
        total += count
        f.write(f"| {label} | `{path}` | {count} |\n")
    f.write(f"\n## Total Matches\n\n**{total}**\n")

print("=" * 60)
print("UEOS Namespace Inventory")
print("=" * 60)
print(f"Matches : {len(results)}")
print(f"Report  : {report}")
