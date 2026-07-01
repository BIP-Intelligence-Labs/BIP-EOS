
"""
bootstrap_engineering.py

BIP UE
Bootstrap Generation Framework (BGF-001)

Usage:
    py bootstrap_engineering.py EA
    py bootstrap_engineering.py ALL
"""

from pathlib import Path
import sys

ROOT = Path.cwd()
CER = ROOT / "engineering" / "cer"

SERIES = {
    "EA": [
        "EA-000-Architecture-Index.md",
        "EA-001-BIP-UE-Architecture.md",
        "EA-002-Ecosystem-Topology.md",
        "EA-003-Platform-Architecture.md",
        "EA-004-Engineering-Record-Management-System.md",
        "EA-005-Engineering-Knowledge-Architecture.md",
        "EA-006-Bootstrap-Architecture.md",
        "EA-007-Compiler-Architecture.md",
        "EA-008-Artificial-Intelligence-Architecture.md",
        "EA-009-Academy-Architecture.md",
        "EA-010-Product-Architecture.md",
        "EA-011-Repository-Architecture.md",
        "EA-012-Plugin-Architecture.md",
        "EA-013-Runtime-Architecture.md",
        "EA-014-Security-Architecture.md",
        "EA-015-Deployment-Architecture.md",
        "EA-016-Data-Architecture.md",
        "EA-017-Integration-Architecture.md",
        "EA-018-Observability-Architecture.md",
        "EA-019-Future-Roadmap.md",
    ],
    "EC": ["EC-000-Constitution-Index.md","EC-001-Engineering-Constitution.md"],
    "ADR": ["ADR-000-Decision-Index.md","ADR-001-Architecture-Decision-Records.md"],
    "SSC": ["SSC-000-Compliance-Index.md","SSC-001-Software-Supply-Chain-Compliance.md"],
    "ES": ["ES-000-Standards-Index.md"],
    "EG": ["EG-000-Governance-Index.md"],
    "SP": ["SP-000-Specification-Index.md"],
    "ER": ["ER-000-Reports-Index.md"],
    "QR": ["QR-000-Quality-Rules.md"],
    "SR": ["SR-000-Security-Rules.md"],
    "RM": ["RM-000-Risk-Management.md"],
    "OP": ["OP-000-Operational-Procedures.md"],
    "AP": ["AP-000-Academy-Publications.md"],
    "AI": ["AI-000-AI-Architecture-Governance.md"],
    "PR": ["PR-000-Product-Records.md"],
    "RE": ["RE-000-Release-Engineering.md"],
    "TS": ["TS-000-Testing-Standards.md"],
}

arg = sys.argv[1].upper() if len(sys.argv) > 1 else "ALL"
targets = SERIES.keys() if arg == "ALL" else [arg]

print("="*60)
print("BIP UE")
print("Bootstrap Generation Framework")
print("BGF-001")
print("="*60)

created = 0

for family in targets:
    if family not in SERIES:
        print(f"[ERROR] Unknown family: {family}")
        continue
    folder = CER / family
    folder.mkdir(parents=True, exist_ok=True)
    for doc in SERIES[family]:
        p = folder / doc
        if not p.exists():
            p.write_text(
f"# {doc[:-3]}\n\nStatus: Draft\n\nDocument Family: {family}\n",
                encoding="utf-8")
            print(f"[CREATE] engineering/cer/{family}/{doc}")
            created += 1
        else:
            print(f"[SKIP]   engineering/cer/{family}/{doc}")

print("-"*60)
print(f"Documents created: {created}")
print("Status: SUCCESS")
