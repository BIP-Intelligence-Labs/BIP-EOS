"""
======================================================================
BIP EOS Release Branding Bootstrap
======================================================================

Standardizes repository branding.

Product      : BIP EOS
Repository   : BIP EOS
Runtime      : BIP EOS
Package      : bip_eos
Release      : v0.1.0
Codename     : Genesis

Genesis is retained ONLY as the release codename.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

REPLACEMENTS = [
    ("BIP EOS Repository", "BIP EOS Repository"),
    ("BIP EOS Runtime", "BIP EOS Runtime"),
    ("BIP EOS CLI", "BIP EOS CLI"),
    ("BIP EOS Platform", "BIP EOS Platform"),
    ("BIP EOS Engine", "BIP EOS Engine"),
    ("BIP EOS v0.1.0", "BIP EOS v0.1.0"),
    ("BIP EOS v0.1.0.0", "BIP EOS v0.1.0"),
    (
        "Version : 0.1.0\nCodename: Genesis",
        "Version : 0.1.0\nRelease : v0.1.0\nCodename: Genesis",
    ),
]

EXTENSIONS = {
    ".md",
    ".py",
    ".txt",
    ".toml",
    ".yaml",
    ".yml",
    ".json",
    ".rst",
}

updated = 0

print("=" * 70)
print("BIP EOS Release Branding")
print("=" * 70)

for file in ROOT.rglob("*"):
    if not file.is_file():
        continue

    if file.suffix.lower() not in EXTENSIONS:
        continue

    try:
        text = file.read_text(encoding="utf-8")
    except Exception:
        continue

    original = text

    for old, new in REPLACEMENTS:
        text = text.replace(old, new)

    if text != original:
        file.write_text(text, encoding="utf-8")
        updated += 1
        print(f"[UPDATED] {file.relative_to(ROOT)}")

print("-" * 70)
print(f"Files Updated : {updated}")
print("=" * 70)
