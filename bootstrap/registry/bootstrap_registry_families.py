"""
bootstrap_registry_families.py

BIP UE
Registry Families Bootstrap

Creates the canonical engineering registry family definitions.
"""

from pathlib import Path
import json

ROOT = Path.cwd()

REGISTRY = ROOT / "bootstrap" / "engineering" / "registry" / "families"
REGISTRY.mkdir(parents=True, exist_ok=True)

FAMILIES = {
    "ea": ("Engineering Architecture", "EA"),
    "ec": ("Engineering Constitution", "EC"),
    "adr": ("Architecture Decision Records", "ADR"),
    "es": ("Engineering Standards", "ES"),
    "eg": ("Engineering Governance", "EG"),
    "ssc": ("Software Supply Chain & Compliance", "SSC"),
    "sp": ("Specifications", "SP"),
    "er": ("Engineering Reports", "ER"),
    "qr": ("Quality Rules", "QR"),
    "sr": ("Security Rules", "SR"),
    "rm": ("Risk Management", "RM"),
    "op": ("Operational Procedures", "OP"),
    "ap": ("Academy Publications", "AP"),
    "ai": ("Artificial Intelligence", "AI"),
    "pr": ("Product Records", "PR"),
    "re": ("Release Engineering", "RE"),
    "ts": ("Testing Standards", "TS"),
    "vm": ("Vision Milestones", "VM"),
}

print("=" * 60)
print("BIP UE")
print("Registry Families Bootstrap")
print("=" * 60)

created = skipped = 0

for key, (title, code) in FAMILIES.items():
    path = REGISTRY / f"{key}.json"
    data = {
        "family": code,
        "title": title,
        "version": "1.0.0",
        "status": "Draft",
        "owner": "Engineering",
        "generator": "EDE",
        "records": []
    }
    if path.exists():
        print(f"[SKIP]   {path.relative_to(ROOT)}")
        skipped += 1
    else:
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"[CREATE] {path.relative_to(ROOT)}")
        created += 1

print("-" * 60)
print(f"Created : {created}")
print(f"Skipped : {skipped}")
print("Status  : SUCCESS")
