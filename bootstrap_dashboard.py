"""
bootstrap_dashboard.py

Bootstrap Engineering Lab Dashboard

Run:
    python bootstrap_dashboard.py
"""

from pathlib import Path
from datetime import datetime

ROOT = Path(".")
BOOTSTRAP = ROOT / "bootstrap"

def count(pattern):
    return len(list(ROOT.rglob(pattern)))

python_files = count("*.py")
markdown_files = count("*.md")
test_files = len(list(ROOT.rglob("test_*.py")))

plugins = []
plugins_dir = BOOTSTRAP / "plugins"
if plugins_dir.exists():
    plugins = sorted([p.name for p in plugins_dir.iterdir() if p.is_dir()])

duplicates = len(list(ROOT.rglob("* (1).py")))
backups = len(list(ROOT.rglob("*.py.bak")))

score = max(100 - duplicates * 5 - backups * 2, 0)

print("=" * 68)
print(" Bootstrap Engineering Lab Dashboard")
print("=" * 68)
print()
print("Building the tools")
print("that build")
print("the future.")
print()

print("Platform")
print("-" * 68)
print(f"Kernel.................... {'ONLINE' if (BOOTSTRAP/'kernel').exists() else 'MISSING'}")
print(f"Engineering............... {'ONLINE' if (BOOTSTRAP/'engineering').exists() else 'MISSING'}")
print(f"AI........................ {'ONLINE' if (BOOTSTRAP/'ai').exists() else 'MISSING'}")
print(f"Plugins................... {len(plugins)} Installed")
print(f"CLI....................... {'ONLINE' if (BOOTSTRAP/'cli').exists() else 'MISSING'}")

print()
print("Repository")
print("-" * 68)
print(f"Python Files.............. {python_files}")
print(f"Markdown Files............ {markdown_files}")
print(f"Test Files................ {test_files}")

print()
print("Engineering Health")
print("-" * 68)
print(f"Engineering Score......... {score}/100")
print(f"Duplicate Files........... {duplicates}")
print(f"Backup Files.............. {backups}")
print("Status.................... 🚀 ALL SYSTEMS GO" if score == 100 else "Status.................... Needs Attention")

print()
print("Installed Plugins")
print("-" * 68)
if plugins:
    for p in plugins:
        print(f"✓ {p}")
else:
    print("None")

print()
print("Today's Mission")
print("-" * 68)
print("1. Build intelligent systems")
print("2. Improve engineering quality")
print("3. Expand platform capabilities")
print()
print("💥 LET'S DO SOME DAMAGE.")
print()
print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("=" * 68)
