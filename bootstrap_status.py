"""
bootstrap_status.py

Displays the overall health of Bootstrap Engineering Lab.

Run:
    python bootstrap_status.py
"""

from pathlib import Path

ROOT = Path(".")
BOOTSTRAP = ROOT / "bootstrap"

def count(pattern: str) -> int:
    return len(list(ROOT.rglob(pattern)))

print("=" * 55)
print(" Bootstrap Engineering Lab Status")
print("=" * 55)

print("\nRepository")
print(f"  Root............... {ROOT.resolve()}")

print("\nComponents")
components = [
    ("Kernel", BOOTSTRAP / "kernel"),
    ("CLI", BOOTSTRAP / "cli"),
    ("Plugins", BOOTSTRAP / "plugins"),
    ("Engineering", ROOT / "engineering"),
    ("Docs", ROOT / "docs"),
    ("Tests", ROOT / "tests"),
]

for name, path in components:
    status = "✓ Installed" if path.exists() else "✗ Missing"
    print(f"  {name:<15} {status}")

print("\nStatistics")
print(f"  Python Files....... {count('*.py')}")
print(f"  Markdown Files..... {count('*.md')}")
print(f"  Test Files......... {len(list(ROOT.rglob('test_*.py')))}")
print(f"  Plugins............ {len([p for p in (BOOTSTRAP/'plugins').iterdir() if p.is_dir()]) if (BOOTSTRAP/'plugins').exists() else 0}")

print("\nRepository Health")
duplicates = list(ROOT.rglob("* (1).py"))
backups = list(ROOT.rglob("*.py.bak"))

if duplicates:
    print(f"  ⚠ Duplicate files.. {len(duplicates)}")
else:
    print("  ✓ Duplicate files.. None")

if backups:
    print(f"  ⚠ Backup files..... {len(backups)}")
else:
    print("  ✓ Backup files..... None")

print("\nDoctor")
if not duplicates and not backups:
    print("  🚀 ALL SYSTEMS GO")
else:
    print("  ⚠ Cleanup recommended")

print("=" * 55)
