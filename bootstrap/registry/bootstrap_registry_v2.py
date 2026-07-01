#!/usr/bin/env python3
"""
EA-012 — Registry Bootstrap v2

BIP UE Engineering Operating System

Architecture

Registry
    ├── Families
    ├── Schemas
    ├── Metadata
    ├── Relationships
    ├── Templates
    └── Validation
            │
            ▼
    Engineering Model
            │
            ▼
    Generator Engine
            │
            ├── CER
            ├── ERMS
            ├── BGF
            └── EDE

This bootstrap intentionally DOES NOT generate engineering artifacts.
It validates and builds the engineering model that later generators consume.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]

REGISTRY = ROOT / "bootstrap" / "engineering" / "registry"

SECTIONS = (
    "families",
    "schemas",
    "metadata",
    "relationships",
    "templates",
    "validation",
)


@dataclass
class RegistryModel:
    sections: Dict[str, List[Path]] = field(default_factory=dict)


class RegistryBootstrap:

    def discover(self) -> RegistryModel:
        model = RegistryModel()

        if not REGISTRY.exists():
            raise FileNotFoundError(f"Registry not found: {REGISTRY}")

        for section in SECTIONS:
            folder = REGISTRY / section
            files = []
            if folder.exists():
                files = sorted(
                    p for p in folder.rglob("*")
                    if p.is_file() and not p.name.startswith(".")
                )
            model.sections[section] = files

        return model

    def validate(self, model: RegistryModel):
        missing = [s for s in SECTIONS if not (REGISTRY / s).exists()]
        if missing:
            raise RuntimeError(f"Missing registry sections: {', '.join(missing)}")

    def summary(self, model: RegistryModel):
        print("=" * 72)
        print("BIP EOS - Registry Bootstrap v2")
        print("=" * 72)
        print(f"Repository : {ROOT}")
        print(f"Registry   : {REGISTRY}\n")

        total = 0
        for section, files in model.sections.items():
            print(f"{section:15} {len(files):4} files")
            total += len(files)

        print("-" * 72)
        print(f"Registry objects : {total}")
        print("\nEngineering model successfully initialized.")
        print("Next stage: Engineering Compiler -> Generator Engine")


def main():
    boot = RegistryBootstrap()
    model = boot.discover()
    boot.validate(model)
    boot.summary(model)


if __name__ == "__main__":
    main()
