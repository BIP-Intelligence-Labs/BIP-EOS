"""
bootstrap_vm003.py

VM-003
Canonical Engineering Registry (CER Registry)

Bootstraps the registry-driven engineering foundation.
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "bootstrap/engineering/registry/families",
    "bootstrap/engineering/registry/schemas",
    "bootstrap/engineering/registry/metadata",
    "bootstrap/engineering/registry/validation",
    "bootstrap/engineering/registry/relationships",
]

FAMILIES = [
    "ea","ec","adr","es","eg","ssc","sp","er",
    "qr","sr","rm","op","re","ap","ai","pr","ts"
]

TEMPLATE = """family: {family}
title: {title}
owner: Engineering
version: 1.0.0
status: Draft
description: Canonical Engineering Record family.
"""

print("="*60)
print("BIP UE")
print("VM-003 Canonical Engineering Registry")
print("="*60)

dirs = files = 0

for d in DIRECTORIES:
    p = ROOT / d
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
        print(f"[CREATE] {d}")
        dirs += 1
    else:
        print(f"[SKIP]   {d}")

for fam in FAMILIES:
    p = ROOT / "bootstrap" / "engineering" / "registry" / "families" / f"{fam}.yaml"
    if not p.exists():
        p.write_text(
            TEMPLATE.format(
                family=fam.upper(),
                title=f"{fam.upper()} Registry"
            ),
            encoding="utf-8",
        )
        print(f"[CREATE] {p.relative_to(ROOT)}")
        files += 1
    else:
        print(f"[SKIP]   {p.relative_to(ROOT)}")

print("-"*60)
print(f"Directories : {dirs}")
print(f"Registry Files : {files}")
print("Status : SUCCESS")
print()
print("VM-003 Initialized")
print("Engineering Knowledge -> Canonical Registry -> EDE")
