#!/usr/bin/env python3
"""
repository_analyzer.py

Consumes reports produced by repository_auditor.py and generates:
- architecture_analysis.md
- duplicate_resolution.json
- migration_plan.json
- risk_assessment.json

Read-only. No files are moved or modified.
"""

from pathlib import Path
import json
from datetime import datetime

ROOT = Path.cwd()
REPORTS = ROOT / "reports"

dup_file = REPORTS / "duplicates.json"

if not dup_file.exists():
    raise SystemExit(
        "duplicates.json not found.\nRun bootstrap/repository_auditor.py first."
    )

duplicates = json.loads(dup_file.read_text(encoding="utf-8"))

PREFER = {
    "src/genesis": 100,
    "plugins": 90,
    "docs": 90,
    "registry": 90,
    "templates": 90,
    "bootstrap": 50,
    "bip": 40,
}

def score(path: str) -> int:
    for prefix, value in PREFER.items():
        if path.startswith(prefix):
            return value
    return 0

resolution = {}
migration = []
risks = []

for category in ("folders", "files"):
    for name, paths in duplicates.get(category, {}).items():
        ranked = sorted(paths, key=score, reverse=True)
        winner = ranked[0]
        losers = ranked[1:]

        resolution[name] = {
            "category": category,
            "winner": winner,
            "candidates": ranked,
            "confidence": "HIGH" if score(winner) >= 90 else "MEDIUM"
        }

        for item in losers:
            migration.append({
                "item": item,
                "recommended_destination": winner,
                "action": "REVIEW"
            })

            risks.append({
                "item": item,
                "risk": "MEDIUM",
                "reason": "Duplicate requires manual review before migration."
            })

(REPORTS / "duplicate_resolution.json").write_text(
    json.dumps(resolution, indent=2), encoding="utf-8"
)

(REPORTS / "migration_plan.json").write_text(
    json.dumps(migration, indent=2), encoding="utf-8"
)

(REPORTS / "risk_assessment.json").write_text(
    json.dumps(risks, indent=2), encoding="utf-8"
)

md = REPORTS / "architecture_analysis.md"
with md.open("w", encoding="utf-8") as f:
    f.write("# Architecture Analysis\n\n")
    f.write(f"Generated: {datetime.now().isoformat()}\n\n")
    f.write(f"Duplicate groups analyzed: {len(resolution)}\n\n")
    for name, info in resolution.items():
        f.write(f"## {name}\n")
        f.write(f"- Category: {info['category']}\n")
        f.write(f"- Recommended: {info['winner']}\n")
        f.write(f"- Confidence: {info['confidence']}\n")
        f.write("- Candidates:\n")
        for p in info["candidates"]:
            f.write(f"  - {p}\n")
        f.write("\n")

print("="*60)
print("BIP EOS Repository Analyzer")
print("="*60)
print(f"Duplicate groups analyzed : {len(resolution)}")
print(f"Migration candidates      : {len(migration)}")
print(f"Risk entries              : {len(risks)}")
print("Reports written to:", REPORTS)
