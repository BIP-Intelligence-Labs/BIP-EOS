"""
bootstrap_namespace_completion.py

M-007.0.9 - Namespace Completion

Updates legacy `bip_eos` references to `ueos` across the repository,
while skipping common build and virtual environment directories.

Usage:
    python bootstrap_namespace_completion.py --dry-run
    python bootstrap_namespace_completion.py
"""

from pathlib import Path
import argparse

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    "build",
    "dist",
}

TEXT_EXTENSIONS = {
    ".py", ".md", ".rst", ".toml", ".yaml", ".yml",
    ".json", ".ini", ".cfg", ".txt"
}

REPLACEMENTS = [
    ("from bip_eos", "from ueos"),
    ("import bip_eos", "import ueos"),
    ("bip_eos.", "ueos."),
    ("\"bip_eos\"", "\"ueos\""),
    ("'bip_eos'", "'ueos'"),
]

def should_skip(path: Path):
    return any(part in SKIP_DIRS for part in path.parts)

def process_file(path: Path, dry_run=False):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return False

    new_text = text
    changed = False

    for old, new in REPLACEMENTS:
        if old in new_text:
            new_text = new_text.replace(old, new)
            changed = True

    if changed:
        print(f"[UPDATE] {path}")
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")

    return changed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path.cwd()
    changed = 0

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if should_skip(path):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if process_file(path, args.dry_run):
            changed += 1

    print(f"\nFiles updated: {changed}")
    if args.dry_run:
        print("Dry run complete. No files were modified.")
    else:
        print("Namespace migration complete.")
        print("Next steps:")
        print("  python -m pytest")
        print("  git diff")
        print("  git status")

if __name__ == "__main__":
    main()
