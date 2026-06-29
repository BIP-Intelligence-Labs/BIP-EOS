#!/usr/bin/env python3
"""
verify_reports_plugin.py

Verifies whether the 'reports' plugin is actually used.

Usage:
    python bootstrap\verify_reports_plugin.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()

SEARCH_TERMS = [
    "reports",
    "plugins.reports",
    "bip_eos.plugins.reports",
]

KEY_FILES = [
    "plugin_engine.py",
    "registry_engine.py",
    "plugin_registry.py",
    "registry.json",
    "plugins.json",
]

print("=" * 70)
print("BIP EOS Reports Plugin Verification")
print("=" * 70)

py_files = list(ROOT.rglob("*.py"))
json_files = list(ROOT.rglob("*.json"))

matches = []

for file in py_files + json_files:
    if "__pycache__" in file.parts or ".git" in file.parts:
        continue

    try:
        lines = file.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception:
        continue

    for i, line in enumerate(lines, start=1):
        lower = line.lower()
        if any(term.lower() in lower for term in SEARCH_TERMS):
            matches.append((file.relative_to(ROOT), i, line.strip()))

print("\nReferences Found")
print("-" * 70)

if not matches:
    print("No references to 'reports' found.")
else:
    for path, line, text in matches:
        print(f"{path}:{line}")
        print(f"    {text}")

print("\nPlugin Directory")
print("-" * 70)

plugin_dir = ROOT / "plugins" / "reports"

if not plugin_dir.exists():
    print("plugins/reports does not exist.")
else:
    files = [p.relative_to(plugin_dir) for p in plugin_dir.rglob("*") if p.is_file()]
    if not files:
        print("plugins/reports is empty.")
    else:
        print(f"{len(files)} file(s):")
        for f in files:
            print(f"  - {f}")

print("\nRegistry-related Files")
print("-" * 70)

found = False
for f in py_files + json_files:
    if f.name in KEY_FILES:
        print(f.relative_to(ROOT))
        found = True

if not found:
    print("No standard registry files found.")

print("\n" + "=" * 70)
print("Review the references above.")
print("If 'reports' only appears in discovery/registry scaffolding and")
print("the plugin directory contains no implementation, it is a candidate")
print("for removal after runtime validation.")
