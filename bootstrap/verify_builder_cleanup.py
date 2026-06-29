#!/usr/bin/env python3
"""
verify_builder_cleanup.py

Audits the legacy layer-based builder folders before removal.

Usage:
    python bootstrap\verify_builder_cleanup.py
"""

from pathlib import Path

ROOT = Path.cwd()

TARGETS = [
    "src/bip_eos/builders/api",
    "src/bip_eos/builders/models",
    "src/bip_eos/builders/repositories",
    "src/bip_eos/builders/reports",
]

print("=" * 70)
print("BIP EOS Legacy Builder Verification")
print("=" * 70)

safe = True

for rel in TARGETS:
    path = ROOT / rel

    print(f"\n{rel}")

    if not path.exists():
        print("  [OK] Directory does not exist.")
        continue

    files = [p for p in path.rglob("*") if p.is_file()]

    if not files:
        print("  [OK] Empty directory.")
        continue

    print(f"  [FOUND] {len(files)} file(s):")

    for f in files:
        rel_file = f.relative_to(ROOT)
        size = f.stat().st_size
        print(f"     - {rel_file} ({size} bytes)")

        if size > 0:
            text = ""
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                pass

            lines = len(text.splitlines()) if text else 0

            if lines <= 5 and (
                "__init__" in f.name
                or "pass" in text
                or '"""' in text
            ):
                print("         -> scaffold/stub")
            else:
                print("         -> POSSIBLE IMPLEMENTATION")
                safe = False

print("\n" + "-" * 70)

if safe:
    print("RESULT: SAFE TO REMOVE")
    print("Suggested command:")
    print("python bootstrap\\remove_layered_builders.py --apply")
else:
    print("RESULT: REVIEW REQUIRED")
    print("One or more directories contain implementation code.")
    print("Migrate those files before deleting the legacy folders.")
