"""
migrate_compiler_bootstrap.py

Migrates legacy compiler bootstrap scripts from the old C03/C04 phase
layout to the new descriptive frontend layout.

Run:
    python migrate_compiler_bootstrap.py
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

LEGACY = ROOT / "bootstrap" / "compiler"
FRONTEND = LEGACY / "frontend"

FRONTEND.mkdir(parents=True, exist_ok=True)

MAPPINGS = {
    "c03/bootstrap_c03.py": "frontend/bootstrap_tokens.py",
    "c03/verify_c03.py": "frontend/verify_tokens.py",
    "c03/bootstrap_c03_report.py": "frontend/report_tokens.py",
    "c04/verify_c04.py": "frontend/verify_lexer.py",
}

REPLACEMENTS = {
    "bootstrap/compiler/c03/verify_c03.py":
        "bootstrap/compiler/frontend/verify_tokens.py",
    "C03 — Token System":
        "Frontend — Token System",
    "C03 Verification":
        "Frontend Token Verification",
    "compiler_c03_report.md":
        "compiler_frontend_tokens_report.md",
    "C04 — Lexer":
        "Frontend — Lexer",
}

print("=" * 70)
print("UEOS COMPILER BOOTSTRAP MIGRATION")
print("=" * 70)

for old_rel, new_rel in MAPPINGS.items():
    src = LEGACY / old_rel
    dst = LEGACY / new_rel

    if not src.exists():
        print(f"SKIP    : {old_rel}")
        continue

    dst.parent.mkdir(parents=True, exist_ok=True)

    text = src.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)

    dst.write_text(text, encoding="utf-8")
    print(f"MIGRATE : {old_rel} -> {new_rel}")

print("-" * 70)
print("Migration complete.")
print()
print("After verifying the new scripts, you may safely remove:")
for folder in [f"c{i:02d}" for i in range(1,11)]:
    print(f"  bootstrap/compiler/{folder}")
