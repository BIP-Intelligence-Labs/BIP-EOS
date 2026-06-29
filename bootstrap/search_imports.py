#!/usr/bin/env python3
"""
search_imports.py

Searches the repository for imports of selected packages.

Usage:
    python bootstrap\search_imports.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()

TARGETS = [
    "bip_eos.services",
    "bip_eos.utils",
    "bip_eos.reports",
]

PATTERNS = [
    r"from\s+{target}\b",
    r"import\s+{target}\b",
    r"from\s+{short}\b",
    r"import\s+{short}\b",
]

print("=" * 70)
print("BIP EOS Import Search")
print("=" * 70)

results = {}

py_files = [
    p for p in ROOT.rglob("*.py")
    if ".git" not in p.parts
    and "__pycache__" not in p.parts
]

for target in TARGETS:
    short = target.split(".")[-1]
    regexes = [
        re.compile(p.format(target=re.escape(target), short=re.escape(short)))
        for p in PATTERNS
    ]

    matches = []

    for file in py_files:
        try:
            lines = file.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue

        for lineno, line in enumerate(lines, start=1):
            if any(r.search(line) for r in regexes):
                matches.append((file.relative_to(ROOT), lineno, line.strip()))

    results[target] = matches

for target, matches in results.items():
    print(f"\n{target}")
    print("-" * len(target))
    if not matches:
        print("  ✓ No imports found.")
    else:
        for path, line, text in matches:
            print(f"  {path}:{line}")
            print(f"    {text}")

print("\n" + "=" * 70)
unused = [t for t, m in results.items() if not m]
if len(unused) == len(TARGETS):
    print("RESULT: No imports found for any target packages.")
else:
    print("RESULT: One or more packages are still referenced.")
