"""
bootstrap_metrics.py

Engineering metrics dashboard for Bootstrap Engineering Lab.

Run:
    python bootstrap_metrics.py
"""

from pathlib import Path

ROOT = Path(".")
BOOTSTRAP = ROOT / "bootstrap"

py_files = list(ROOT.rglob("*.py"))
md_files = list(ROOT.rglob("*.md"))
test_files = list(ROOT.rglob("test_*.py"))

classes = 0
functions = 0
lines = 0

for f in py_files:
    try:
        text = f.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    lines += len(text.splitlines())
    classes += text.count("\nclass ")
    if text.startswith("class "):
        classes += 1
    functions += text.count("\ndef ")
    if text.startswith("def "):
        functions += 1

plugins = []
plugins_dir = BOOTSTRAP / "plugins"
if plugins_dir.exists():
    plugins = [p.name for p in plugins_dir.iterdir() if p.is_dir()]

score = 100
duplicates = list(ROOT.rglob("* (1).py"))
backups = list(ROOT.rglob("*.py.bak"))
score -= len(duplicates) * 5
score -= len(backups) * 2
score = max(score, 0)

print("=" * 60)
print(" Bootstrap Engineering Metrics")
print("=" * 60)

print("\nRepository")
print(f"  Python Files....... {len(py_files)}")
print(f"  Markdown Files..... {len(md_files)}")
print(f"  Test Files......... {len(test_files)}")
print(f"  Total Classes...... {classes}")
print(f"  Total Functions.... {functions}")
print(f"  Lines of Code...... {lines:,}")

print("\nPlugins")
for p in plugins:
    print(f"  ✓ {p}")

print("\nEngineering Score")
print(f"  Score.............. {score}/100")
print(f"  Duplicate Files.... {len(duplicates)}")
print(f"  Backup Files....... {len(backups)}")

print("\nStatus")
print("  🚀 ALL SYSTEMS GO" if score == 100 else "  ⚠ Improvements Available")
print("=" * 60)
