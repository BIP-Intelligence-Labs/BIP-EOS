#!/usr/bin/env python3
"""
repository_semantic_analyzer.py

Analyzes the repository using semantic roles rather than duplicate names.
Read-only. Produces semantic reports for the migration planner.
"""

from pathlib import Path
import json
from collections import Counter
from datetime import datetime

ROOT = Path.cwd()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

ROLE_RULES = {
    "Production Source": ["src/genesis"],
    "Bootstrap Framework": ["bootstrap"],
    "Documentation": ["docs"],
    "Governance": ["engineering"],
    "Plugin Runtime": ["plugins"],
    "Research/Lab": ["Lab", "archive", "research"],
    "Assets": ["assets", "media"],
    "Tests": ["tests"],
    "Utilities": ["tools", "scripts"],
}

def classify(path: str):
    p = path.replace("\\", "/")
    for role, prefixes in ROLE_RULES.items():
        for prefix in prefixes:
            if p.startswith(prefix.replace("\\", "/")):
                return role
    return "Unclassified"

results = []
counts = Counter()

for item in sorted(ROOT.rglob("*")):
    rel = item.relative_to(ROOT).as_posix()
    if any(part.startswith(".git") or part == "__pycache__" for part in item.parts):
        continue

    role = classify(rel)
    counts[role] += 1

    results.append({
        "path": rel,
        "type": "directory" if item.is_dir() else "file",
        "role": role
    })

(REPORTS / "semantic_inventory.json").write_text(
    json.dumps(results, indent=2), encoding="utf-8"
)

summary = {
    "generated": datetime.now().isoformat(),
    "roles": dict(counts),
    "total_items": len(results)
}

(REPORTS / "semantic_summary.json").write_text(
    json.dumps(summary, indent=2), encoding="utf-8"
)

md = REPORTS / "semantic_architecture.md"
with md.open("w", encoding="utf-8") as f:
    f.write("# Genesis Semantic Architecture\n\n")
    f.write(f"Generated: {summary['generated']}\n\n")
    f.write("## Role Summary\n\n")
    for role, total in counts.items():
        f.write(f"- **{role}**: {total}\n")
    f.write("\n## Migration Rules\n\n")
    f.write("- Production Source is authoritative.\n")
    f.write("- Bootstrap Framework is tooling.\n")
    f.write("- Documentation is never merged by filename alone.\n")
    f.write("- Governance content remains separate from runtime code.\n")
    f.write("- Plugin Runtime is independent of Production Source.\n")
    f.write("- Human review required before any cross-role migration.\n")

print("="*60)
print("Genesis Semantic Repository Analyzer")
print("="*60)
print(f"Items classified : {len(results)}")
for role,total in counts.items():
    print(f"{role:24} {total}")
print("Reports written to:", REPORTS)
