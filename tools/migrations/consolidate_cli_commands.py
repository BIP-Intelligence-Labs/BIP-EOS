\
"""
consolidate_cli_commands.py

UEOS Atlas Architecture Consolidation
-------------------------------------

Purpose:
    Consolidate CLI command modules into the canonical package:

        src/bip_eos/cli/commands/

This migration copies missing commands, reports duplicates,
and prepares legacy directories for retirement.

Run:
    python tools/migrations/consolidate_cli_commands.py
"""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]

CANONICAL = ROOT / "src" / "bip_eos" / "cli" / "commands"

LEGACY = [
    ROOT / "bootstrap" / "commands",
    ROOT / "cli",
]

CANONICAL.mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("UEOS CLI CONSOLIDATION")
print("=" * 70)

copied = 0
duplicates = 0
missing = 0

for source in LEGACY:
    if not source.exists():
        print(f"SKIP     : {source.relative_to(ROOT)} (missing)")
        continue

    print(f"\nScanning : {source.relative_to(ROOT)}")

    for py in sorted(source.rglob("*.py")):
        if py.name == "__init__.py":
            continue

        target = CANONICAL / py.name

        if target.exists():
            duplicates += 1
            print(f"DUPLICATE: {py.name}")
            continue

        shutil.copy2(py, target)
        copied += 1
        print(f"COPY     : {py.name}")

print("\n" + "-" * 70)
print(f"Copied     : {copied}")
print(f"Duplicates : {duplicates}")
print(f"Missing    : {missing}")

print("\nCanonical CLI location:")
print("  src/bip_eos/cli/commands/")

print("\nRecommended follow-up:")
print("  1. Review duplicate commands")
print("  2. Update imports")
print("  3. Run pytest")
print("  4. Remove legacy CLI directories")
