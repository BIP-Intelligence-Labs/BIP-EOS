"""
bootstrap_repository_audit.py

Audits the repository for cleanliness without modifying anything.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = {
    "Root Empty Directories": [
        "cli",
        "config",
        "core",
    ],
}

print("=" * 70)
print("BIP EOS Repository Audit")
print("=" * 70)

issues = 0

print("\nEmpty Root Directories")
print("-" * 70)

for name in CHECKS["Root Empty Directories"]:
    path = ROOT / name

    if not path.exists():
        print(f"[ OK ] {name} (missing)")
        continue

    children = [p for p in path.iterdir() if p.name != "__pycache__"]

    if children:
        print(f"[KEEP] {name} ({len(children)} item(s))")
    else:
        print(f"[EMPTY] {name}")
        issues += 1

print("\nPython Cache")
print("-" * 70)

cache_count = 0
for p in ROOT.rglob("__pycache__"):
    cache_count += 1
    print(f"[CACHE] {p.relative_to(ROOT)}")

print(f"\nTotal cache directories : {cache_count}")

print("\nCompiled Python")
print("-" * 70)

compiled = 0
for pattern in ("*.pyc", "*.pyo"):
    for p in ROOT.rglob(pattern):
        compiled += 1
        print(f"[FILE] {p.relative_to(ROOT)}")

print(f"\nCompiled files : {compiled}")

print("\nLegacy Runtime")
print("-" * 70)

legacy = ROOT / "src" / "genesis"

if legacy.exists():
    py_files = list(legacy.rglob("*.py"))
    print(f"[FOUND] src/genesis ({len(py_files)} Python files)")
else:
    print("[ OK ] No legacy runtime")

print("\n" + "=" * 70)
if issues:
    print(f"Potential cleanup items : {issues}")
else:
    print("Repository structure is clean.")
print("=" * 70)
