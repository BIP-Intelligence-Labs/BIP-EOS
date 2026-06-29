
"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Academy Curriculum Cleanup Bootstrap

Creates the canonical Academy curriculum layout.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()
BASE = ROOT / "bootstrap" / "academy" / "curriculum"

DIRECTORIES = [
    BASE / "engineering_foundation",
    BASE / "eos_compiler",
    BASE / "bip_platform",
    BASE / "academy_instructor",
    BASE / "certifications",
    BASE / "labs",
    BASE / "capstone",
]

README_FILES = {
    "engineering_foundation/README.md": "# Engineering Foundation\n",
    "eos_compiler/README.md": "# EOS Compiler\n",
    "bip_platform/README.md": "# BIP Platform\n",
    "academy_instructor/README.md": "# Academy Instructor\n",
    "certifications/README.md": "# Certifications\n",
    "labs/README.md": "# Engineering Labs\n",
    "capstone/README.md": "# Capstone Projects\n",
}


def ensure_dir(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")


def ensure_file(path: Path, content: str):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"[FILE] {path}")


print("=" * 70)
print("EOS Academy Curriculum Cleanup")
print("=" * 70)

for d in DIRECTORIES:
    ensure_dir(d)

for rel, content in README_FILES.items():
    ensure_file(BASE / rel, content)

print("-" * 70)
print("Canonical Academy curriculum structure ready.")
print()
print("Recommended manual cleanup:")
print("  Remove: bootstrap/academy/curriculum/core/")
print("  Keep only the canonical directories above.")
print("=" * 70)
