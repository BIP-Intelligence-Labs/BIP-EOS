"""
create_milestone_index.py

Creates an index for all engineering milestones.

Run:
    python create_milestone_index.py
"""

from pathlib import Path

root = Path("engineering") / "milestones"
root.mkdir(parents=True, exist_ok=True)

index = root / "README.md"

content = """# Engineering Milestones

This directory records the major milestones in the evolution of
Bootstrap Engineering Lab.

## Timeline

| Milestone | Status | Summary |
|-----------|--------|---------|
| MILESTONE-0001 | ✅ Complete | Bootstrap Kernel, CLI, Universal Discovery Engine, first successful discovery pipeline |

---

## Purpose

Milestones capture stable engineering achievements. They provide
historical checkpoints and document the evolution of the platform.

Bootstrap Engineering Lab

Building the tools that build the future.
"""

index.write_text(content, encoding="utf-8")

print("=" * 50)
print(" Bootstrap Engineering Milestone Index")
print("=" * 50)
print(f"✓ Created: {index}")
