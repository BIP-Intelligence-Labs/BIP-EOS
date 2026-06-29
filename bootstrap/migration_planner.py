#!/usr/bin/env python3
"""
migration_planner.py

Consumes:
  reports/duplicates.json
  reports/semantic_inventory.json

Produces:
  reports/final_migration_plan.json
  reports/migration_rejections.json
  reports/migration_summary.md

This planner refuses unsafe cross-role migrations.
"""

from pathlib import Path
import json
from collections import defaultdict
from datetime import datetime

ROOT = Path.cwd()
REPORTS = ROOT / "reports"

dup = REPORTS / "duplicates.json"
sem = REPORTS / "semantic_inventory.json"

if not dup.exists() or not sem.exists():
    raise SystemExit("Run repository_auditor.py and repository_semantic_analyzer.py first.")

duplicates = json.loads(dup.read_text(encoding="utf-8"))
semantic = json.loads(sem.read_text(encoding="utf-8"))

roles = {item["path"].replace("\\","/"): item["role"] for item in semantic}

SAFE_ROLE = {
    "Production Source",
    "Plugin Runtime",
    "Documentation",
    "Bootstrap Framework",
    "Governance",
    "Utilities",
    "Tests",
    "Research/Lab",
    "Assets",
}

approved = []
rejected = []

def role_for(path):
    p = path.replace("\\","/")
    best = "Unclassified"
    longest = -1
    for prefix, role in roles.items():
        if p.startswith(prefix) and len(prefix) > longest:
            best = role
            longest = len(prefix)
    return best

for category in ("folders","files"):
    for name, paths in duplicates.get(category, {}).items():
        if len(paths) < 2:
            continue
        base = paths[0]
        base_role = role_for(base)
        for candidate in paths[1:]:
            cand_role = role_for(candidate)
            record = {
                "item": name,
                "source": candidate,
                "target": base,
                "source_role": cand_role,
                "target_role": base_role
            }
            if cand_role == base_role and cand_role in SAFE_ROLE:
                record["action"] = "MERGE_REVIEW"
                approved.append(record)
            else:
                record["action"] = "REJECT"
                record["reason"] = "Cross-role migration requires manual approval."
                rejected.append(record)

(REPORTS/"final_migration_plan.json").write_text(json.dumps(approved,indent=2),encoding="utf-8")
(REPORTS/"migration_rejections.json").write_text(json.dumps(rejected,indent=2),encoding="utf-8")

with (REPORTS/"migration_summary.md").open("w",encoding="utf-8") as f:
    f.write("# Migration Summary\n\n")
    f.write(f"Generated: {datetime.now().isoformat()}\n\n")
    f.write(f"- Approved: {len(approved)}\n")
    f.write(f"- Rejected: {len(rejected)}\n\n")
    f.write("Only same-role migrations are proposed automatically.\n")

print("="*60)
print("Genesis Migration Planner")
print("="*60)
print("Approved :", len(approved))
print("Rejected :", len(rejected))
print("Reports :", REPORTS)
