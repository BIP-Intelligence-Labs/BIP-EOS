
"""
========================================================================
BIP Engineering Labs
Engineering Operating System (EOS)

Academy Curriculum Migration

Removes the legacy curriculum/core directory and creates the
canonical Academy curriculum structure.

========================================================================
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

CURRICULUM = ROOT / "bootstrap" / "academy" / "curriculum"
LEGACY = CURRICULUM / "core"

DIRECTORIES = [
    CURRICULUM / "engineering_foundation",
    CURRICULUM / "eos_compiler",
    CURRICULUM / "bip_platform",
    CURRICULUM / "academy_instructor",
    CURRICULUM / "certifications",
    CURRICULUM / "labs",
    CURRICULUM / "capstone",
]


def ensure_directory(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")


print("=" * 70)
print("EOS Academy Curriculum Migration")
print("=" * 70)

for directory in DIRECTORIES:
    ensure_directory(directory)

if LEGACY.exists():
    shutil.rmtree(LEGACY)
    print(f"[REMOVE] {LEGACY}")
else:
    print(f"[SKIP] {LEGACY}")

print("-" * 70)
print("Canonical Academy Curriculum")
print()
print("bootstrap/")
print("└── academy/")
print("    └── curriculum/")
print("        ├── engineering_foundation/")
print("        ├── eos_compiler/")
print("        ├── bip_platform/")
print("        ├── academy_instructor/")
print("        ├── certifications/")
print("        ├── labs/")
print("        └── capstone/")
print("=" * 70)
