#!/usr/bin/env python3
"""
repository_auditor.py

Read-only repository auditor for Genesis/BIP EOS.
Scans the repository and generates audit reports.
"""

from pathlib import Path
import json
from collections import defaultdict
from datetime import datetime

ROOT = Path.cwd()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

IGNORE = {
    ".git", ".venv", "venv", "__pycache__", ".mypy_cache",
    ".pytest_cache", ".idea", ".vscode"
}

folder_names = defaultdict(list)
file_names = defaultdict(list)
missing_init = []
empty_dirs = []
inventory = []

for path in ROOT.rglob("*"):
    rel = path.relative_to(ROOT)

    if any(part in IGNORE for part in rel.parts):
        continue

    inventory.append(str(rel))

    if path.is_dir():
        folder_names[path.name].append(str(rel))
        try:
            if not any(path.iterdir()):
                empty_dirs.append(str(rel))
        except PermissionError:
            pass

        if (path.parent.name == "genesis" or "src" in rel.parts):
            init = path / "__init__.py"
            if not init.exists():
                missing_init.append(str(rel))

    else:
        file_names[path.name].append(str(rel))

duplicates = {
    "folders": {k: v for k, v in folder_names.items() if len(v) > 1},
    "files": {k: v for k, v in file_names.items() if len(v) > 1},
}

summary = {
    "generated": datetime.now().isoformat(),
    "root": str(ROOT),
    "folders_scanned": sum(1 for p in ROOT.rglob("*") if p.is_dir()),
    "files_scanned": sum(1 for p in ROOT.rglob("*") if p.is_file()),
    "duplicate_folder_names": len(duplicates["folders"]),
    "duplicate_file_names": len(duplicates["files"]),
    "empty_directories": len(empty_dirs),
    "missing_init_packages": len(missing_init),
}

(REPORTS / "repository_inventory.json").write_text(
    json.dumps(inventory, indent=2), encoding="utf-8"
)

(REPORTS / "duplicates.json").write_text(
    json.dumps(duplicates, indent=2), encoding="utf-8"
)

(REPORTS / "summary.json").write_text(
    json.dumps(summary, indent=2), encoding="utf-8"
)

md = REPORTS / "repository_audit.md"
with md.open("w", encoding="utf-8") as f:
    f.write("# Repository Audit\n\n")
    f.write(f"Generated: {summary['generated']}\n\n")
    f.write("## Summary\n")
    for k, v in summary.items():
        if k != "generated":
            f.write(f"- **{k}**: {v}\n")
    f.write("\n## Duplicate Folders\n")
    for k, v in duplicates["folders"].items():
        f.write(f"\n### {k}\n")
        for item in v:
            f.write(f"- {item}\n")
    f.write("\n## Duplicate Files\n")
    for k, v in duplicates["files"].items():
        f.write(f"\n### {k}\n")
        for item in v:
            f.write(f"- {item}\n")
    f.write("\n## Empty Directories\n")
    for d in empty_dirs:
        f.write(f"- {d}\n")
    f.write("\n## Missing __init__.py\n")
    for d in missing_init:
        f.write(f"- {d}\n")

print("="*60)
print("BIP EOS Repository Auditor")
print("="*60)
for k,v in summary.items():
    print(f"{k:25} {v}")
print("\nReports written to:", REPORTS)
