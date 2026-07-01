#!/usr/bin/env python3
"""
UEOS Architecture Audit v1
--------------------------

Read-only audit of the BIP Universal Engineering Operating System repository.

This script:
- Discovers the UEOS repository root.
- Audits top-level directories.
- Classifies each directory.
- Detects likely architectural duplication.
- DOES NOT modify the repository.

Usage:
    py ueos_architecture_audit.py
"""

from pathlib import Path

REQUIRED = ("bootstrap", "engineering", "src")

CLASSIFICATION = {
    ".github": ("Infrastructure", "Keep"),
    "ai": ("AI", "Review"),
    "archive": ("Archive", "Keep"),
    "assets": ("Assets", "Keep"),
    "bip": ("Domain Modules", "Review"),
    "bootstrap": ("Engineering Source", "Keep"),
    "cli": ("Runtime", "Merge into src"),
    "config": ("Configuration", "Keep"),
    "core": ("Runtime", "Merge into src"),
    "discovery": ("Runtime", "Review"),
    "docs": ("Documentation", "Keep"),
    "engineering": ("Generated Artifacts", "Keep"),
    "Lab": ("Knowledge", "Keep"),
    "logs": ("Runtime", "Keep"),
    "media": ("Assets", "Keep"),
    "plugins": ("Runtime", "Merge into src"),
    "registry": ("Registry", "Review"),
    "reports": ("Generated", "Keep"),
    "scripts": ("Tooling", "Review"),
    "shared": ("Runtime", "Merge into src"),
    "src": ("Runtime Source", "Canonical"),
    "templates": ("Templates", "Review"),
    "tests": ("Testing", "Keep"),
    "tools": ("Tooling", "Keep"),
}


def find_root(start: Path) -> Path:
    cur = start.resolve()
    while True:
        if all((cur / d).exists() for d in REQUIRED):
            return cur
        if cur == cur.parent:
            raise RuntimeError("UEOS repository root not found.")
        cur = cur.parent


def main():
    root = find_root(Path(__file__).parent)

    print("=" * 80)
    print("UEOS ARCHITECTURE AUDIT V1 (READ ONLY)")
    print("=" * 80)
    print(f"Repository: {root}\n")

    print(f'{"Directory":<18} {"Classification":<24} Recommendation')
    print("-" * 80)

    for item in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        if not item.is_dir():
            continue
        cls, rec = CLASSIFICATION.get(item.name, ("Unclassified", "Review"))
        print(f"{item.name:<18} {cls:<24} {rec}")

    print("\nPotential duplicate architectural concepts")
    print("-" * 80)

    duplicates = {
        "Registry": [
            "registry/",
            "bootstrap/engineering/registry/",
            "src/bip_eos/core/registry/",
        ],
        "Compiler": [
            "bootstrap/compiler/",
            "engineering/compiler/",
            "src/bip_eos/compiler/",
        ],
        "Plugins": [
            "plugins/",
            "src/bip_eos/plugins/",
        ],
        "CLI": [
            "cli/",
            "src/bip_eos/cli/",
        ],
    }

    for name, paths in duplicates.items():
        existing = [p for p in paths if (root / p).exists()]
        if len(existing) > 1:
            print(f"* {name}")
            for e in existing:
                print(f"    - {e}")

    print("\nAudit complete.")
    print("Repository was NOT modified.")


if __name__ == "__main__":
    main()
