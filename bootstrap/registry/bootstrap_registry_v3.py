#!/usr/bin/env python3
"""
EA-012 — Registry Bootstrap v3

Features
--------
- Automatically discovers the BIP EOS repository root.
- Uses centralized EOSPaths.
- Validates registry structure.
- Builds an in-memory RegistryModel.
- Safe: does not modify or generate files.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


REQUIRED_ROOT_DIRS = ("bootstrap", "engineering", "src")

REGISTRY_SECTIONS = (
    "families",
    "schemas",
    "metadata",
    "relationships",
    "templates",
    "validation",
)


def find_repo_root(start: Path) -> Path:
    current = start.resolve()

    while True:
        if all((current / d).exists() for d in REQUIRED_ROOT_DIRS):
            return current

        if current == current.parent:
            break

        current = current.parent

    raise RuntimeError(
        f"Unable to locate BIP EOS repository root from {start.resolve()}"
    )


class EOSPaths:

    def __init__(self, root: Path):
        self.root = root

        self.bootstrap = root / "bootstrap"
        self.engineering = root / "engineering"
        self.src = root / "src"

        self.registry = (
            self.bootstrap
            / "engineering"
            / "registry"
        )

        self.generators = (
            self.bootstrap
            / "engineering"
            / "generators"
        )

        self.compiler = (
            self.bootstrap
            / "compiler"
        )


@dataclass
class RegistryModel:
    sections: Dict[str, List[Path]] = field(default_factory=dict)


class RegistryBootstrap:

    def __init__(self):
        self.root = find_repo_root(Path(__file__).parent)
        self.paths = EOSPaths(self.root)

    def validate_structure(self):
        if not self.paths.registry.exists():
            raise FileNotFoundError(
                f"Registry directory not found:\n{self.paths.registry}"
            )

        missing = []

        for section in REGISTRY_SECTIONS:
            folder = self.paths.registry / section
            if not folder.exists():
                missing.append(section)

        if missing:
            raise RuntimeError(
                "Missing registry sections:\n  - "
                + "\n  - ".join(missing)
            )

    def build_model(self) -> RegistryModel:

        model = RegistryModel()

        for section in REGISTRY_SECTIONS:
            folder = self.paths.registry / section

            files = sorted(
                p.relative_to(self.root)
                for p in folder.rglob("*")
                if p.is_file() and not p.name.startswith(".")
            )

            model.sections[section] = files

        return model

    def report(self, model: RegistryModel):

        print("=" * 72)
        print("BIP UE ENGINEERING OPERATING SYSTEM")
        print("Registry Bootstrap v3")
        print("=" * 72)

        print(f"Repository : {self.root}")
        print(f"Registry   : {self.paths.registry}")
        print()

        total = 0

        for section in REGISTRY_SECTIONS:
            files = model.sections[section]
            total += len(files)

            print(f"{section:<15} {len(files):>5} files")

        print("-" * 72)
        print(f"Registry Objects : {total}")
        print("-" * 72)

        print()
        print("Status")
        print("------")
        print("✓ Repository discovered")
        print("✓ Registry validated")
        print("✓ Engineering model built")
        print()
        print("Ready for Engineering Compiler.")


def main():

    bootstrap = RegistryBootstrap()

    bootstrap.validate_structure()

    model = bootstrap.build_model()

    bootstrap.report(model)


if __name__ == "__main__":
    main()
