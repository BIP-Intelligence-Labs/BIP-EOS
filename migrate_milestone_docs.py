"""
migrate_milestone_docs.py

Normalize engineering milestone documentation.

Run from the repository root:

    python migrate_milestone_docs.py

This script:
- Creates M-002 through M-006 folders if missing
- Creates README.md for each milestone if missing
- Moves legacy milestone markdown files into the new structure
- Never overwrites existing files
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()
MILESTONES = ROOT / "engineering" / "milestones"

TARGETS = {
    "M02_DOMAIN_ARCHITECTURE.md": ("M-002", "M-002.1-Domain-Architecture.md"),
    "M03.md": ("M-003", "M-003.1-Bootstrap.md"),
    "MILESTONE-0001.md": ("M-004", "M-004.1-Engineering-Governance.md"),
    "MILESTONE-0002.md": ("M-005", "M-005.1-Doctor.md"),
}

README = """# {name}

## Overview

This directory contains the engineering documentation for {name}.

## Documents

Each markdown file records a completed milestone or implementation
decision associated with this engineering phase.
"""

MILESTONES.mkdir(parents=True, exist_ok=True)

for i in range(2, 7):
    folder = MILESTONES / f"M-00{i}"
    folder.mkdir(exist_ok=True)

    readme = folder / "README.md"
    if not readme.exists():
        readme.write_text(README.format(name=folder.name), encoding="utf-8")

for source_name, (folder_name, target_name) in TARGETS.items():
    source = MILESTONES / source_name
    target = MILESTONES / folder_name / target_name

    if source.exists():
        if not target.exists():
            shutil.move(str(source), str(target))
            print(f"Moved: {source_name} -> {folder_name}/{target_name}")
        else:
            print(f"Skipped (target exists): {target}")
    else:
        print(f"Not found: {source_name}")

print("\nMilestone normalization complete.")
