"""
rename_engineering_ids.py

Genesis EEOS Engineering ID Migration Tool

Run:
    python rename_engineering_ids.py
"""

from pathlib import Path
import re

ROOT = Path(".")

REPLACEMENTS = {
    r"GEB-001\.000": "REP-001",
    r"GEB-001\.001": "REP-002",
    r"GEB-001\.002": "GEN-001",
    r"GEB-001\.003": "REP-003",
    r"GEB-001\.004": "VER-001",
    r"GEB-001\.005": "EXC-001",
    r"GEB-001\.006": "REP-004",
    r"GEB-001\.007": "REP-005",
    r"GEB-001\.008": "REP-006",
    r"GEB-001\.009": "REP-007",
}

EXTENSIONS = {".py", ".md", ".toml", ".txt"}

updated = 0

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    if ".git" in path.parts or ".venv" in path.parts:
        continue

    if path.suffix.lower() not in EXTENSIONS:
        continue

    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue

    original = text

    for old, new in REPLACEMENTS.items():
        text = re.sub(old, new, text)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"UPDATED: {path}")
        updated += 1

print("=" * 60)
print(f"Files Updated: {updated}")
print("=" * 60)
