#!/usr/bin/env python3
"""
bootstrap_reorganize_bootstrap_v1.py

UEOS Bootstrap Reorganization v1

Moves root-level bootstrap scripts into constitutional categories.

Safe:
- Creates destination directories if missing.
- Skips files already moved.
- Never overwrites existing files.
"""

from pathlib import Path
import shutil

DESTINATIONS = {
    "architecture": [
        "bootstrap_architecture.py",
        "bootstrap_runtime_architecture_v2.py",
        "bootstrap_ea001_constitution_v1.py",
        "bootstrap_ea001_constitution_book.py",
        "bootstrap_ea001_add_chapter13.py",
        "bootstrap_ea001_chapter04_co_ueos.py",
        "bootstrap_ueg001_structure.py",
    ],
    "engineering": [
        "bootstrap_engineering.py",
        "bootstrap_engineering_foundation_v1.py",
        "bootstrap_registry_foundation.py",
        "bootstrap_cer_taxonomy.py",
        "bootstrap_ssc001.py",
        "bootstrap_vm002_architecture.py",
        "bootstrap_vm003.py",
        "bootstrap_vm003 (1).py",
        "bootstrap_vm004.py",
        "bootstrap_vm_series.py",
        "bootstrap_eaus003_discovery_engine.py",
        "bootstrap_eaus003_discovery_engine_v2.py",
        "eaus001_audit_kernel.py",
        "eem001_engineering_evidence_model.py",
        "ec001_bootstrap.py",
    ],
    "registry": [
        "bootstrap_registry_v2.py",
        "bootstrap_registry_v3.py",
        "bootstrap_registry_families.py",
        "migrate_registry_yaml_to_json.py",
    ],
    "runtime": [
        "bootstrap_runtime_cleanup_v1.py",
        "bootstrap_runtime_reorganization_v1.py",
    ],
    "builders": [
        "bootstrap_bfs001_bootstrap_framework.py",
        "bootstrap_bootstrap_standards.py",
    ],
    "migrations": [
        "migrate_egf_to_epf.py",
    ],
}

def find_root(start: Path) -> Path:
    p = start.resolve()
    while p != p.parent:
        if (p / "bootstrap").exists() and (p / "src").exists():
            return p
        p = p.parent
    raise RuntimeError("Repository root not found.")

def main():
    root = find_root(Path(__file__).parent)

    for folder in DESTINATIONS:
        (root / "bootstrap" / folder).mkdir(parents=True, exist_ok=True)

    moved = skipped = missing = 0

    print("=" * 72)
    print("UEOS Bootstrap Reorganization v1")
    print("=" * 72)

    for folder, files in DESTINATIONS.items():
        target_dir = root / "bootstrap" / folder
        for name in files:
            src = root / name
            dst = target_dir / name

            if not src.exists():
                print(f"[MISSING] {name}")
                missing += 1
                continue

            if dst.exists():
                print(f"[SKIP   ] {dst.relative_to(root)}")
                skipped += 1
                continue

            shutil.move(str(src), str(dst))
            print(f"[MOVE   ] {name} -> {dst.relative_to(root)}")
            moved += 1

    print("-" * 72)
    print(f"Moved   : {moved}")
    print(f"Skipped : {skipped}")
    print(f"Missing : {missing}")
    print("=" * 72)

if __name__ == "__main__":
    main()
