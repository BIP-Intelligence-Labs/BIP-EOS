"""
rename_builders_to_home_builders.py

Atlas Repository Migration
--------------------------
Renames the 'builders' domain to 'home_builders' across the UEOS repository.

Run from the repository root:

    python rename_builders_to_home_builders.py

Actions:
- Renames directories named 'builders' -> 'home_builders'
- Updates *.py, *.md, *.toml, *.yaml, *.yml, *.json, *.txt imports/references
- Never overwrites existing directories
"""

from pathlib import Path

ROOT = Path.cwd()

TEXT_EXTENSIONS = {
    ".py", ".md", ".toml", ".yaml", ".yml",
    ".json", ".txt", ".rst"
}

REPLACEMENTS = [
    ("bip.home_builders", "bip.home_builders"),
    ("bip_eos.home_builders", "bip_eos.home_builders"),
    ("/home_builders/", "/home_builders/"),
    ("\\home_builders\\", "\\home_builders\\"),
    (" home_builders ", " home_builders "),
]

# ---------------------------------------------------------------------

for directory in sorted(ROOT.rglob("builders"), reverse=True):
    if directory.is_dir():
        target = directory.with_name("home_builders")
        if target.exists():
            print(f"SKIP directory (exists): {target}")
            continue
        print(f"Rename: {directory} -> {target}")
        directory.rename(target)

# ---------------------------------------------------------------------

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    if path.suffix.lower() not in TEXT_EXTENSIONS:
        continue

    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue

    updated = text

    for old, new in REPLACEMENTS:
        updated = updated.replace(old, new)

    if updated != text:
        path.write_text(updated, encoding="utf-8")
        print(f"Updated: {path.relative_to(ROOT)}")

print("\nMigration complete.")
