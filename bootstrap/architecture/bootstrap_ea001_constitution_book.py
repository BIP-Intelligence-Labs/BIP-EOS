#!/usr/bin/env python3
"""
UEOS Bootstrap
EA-001 Constitutional Book Bootstrap

Creates the constitutional book structure for EA-001.

Safe:
- Creates missing directories
- Creates placeholder files only if they do not already exist
- Never overwrites existing content
"""

from pathlib import Path
import yaml

CHAPTERS = {
    "README.md": "# EA-001 — Constitution of the BIP Universal Engineering Operating System (UEOS)\n\nThis directory contains the constitutional chapters of UEOS.\n",
    "Chapter-01-Mission.md": "# Chapter 01 — Mission\n",
    "Chapter-02-Engineering-Laws.md": "# Chapter 02 — Engineering Laws\n",
    "Chapter-03-UEOS-Architecture.md": "# Chapter 03 — UEOS Architecture\n",
    "Chapter-04-Constitutional-Objects.md": "# Chapter 04 — Constitutional Objects (CO-UEOS)\n",
    "Chapter-05-Subsystems.md": "# Chapter 05 — UEOS Subsystems\n",
    "Chapter-06-Governance.md": "# Chapter 06 — Governance\n",
    "Chapter-07-Engineering-Lifecycle.md": "# Chapter 07 — Engineering Lifecycle\n",
    "Chapter-08-Repository-Standards.md": "# Chapter 08 — Repository Standards\n",
    "Chapter-09-Registry-Constitution.md": "# Chapter 09 — Registry Constitution\n",
    "Chapter-10-Unified-Engineering-Graph.md": "# Chapter 10 — Unified Engineering Graph\n",
}

MANIFEST = {
    "constitution": "EA-001",
    "title": "Constitution of the BIP Universal Engineering Operating System",
    "codename": "UEOS Constitution",
    "version": "0.1.0",
    "chapters": list(CHAPTERS.keys()),
}


def find_root(start: Path) -> Path:
    cur = start.resolve()
    while cur != cur.parent:
        if (cur / "engineering").exists() and (cur / "src").exists():
            return cur
        cur = cur.parent
    raise RuntimeError("UEOS repository root not found.")


def main():
    root = find_root(Path(__file__).parent)
    target = root / "engineering" / "architecture" / "EA-001"
    target.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("EA-001 Constitutional Book Bootstrap")
    print("=" * 72)

    for filename, content in CHAPTERS.items():
        path = target / filename
        if path.exists():
            print(f"[EXISTS ] {path.relative_to(root)}")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"[CREATE ] {path.relative_to(root)}")

    manifest = target / "manifest.yaml"
    if manifest.exists():
        print(f"[EXISTS ] {manifest.relative_to(root)}")
    else:
        manifest.write_text(yaml.safe_dump(MANIFEST, sort_keys=False), encoding="utf-8")
        print(f"[CREATE ] {manifest.relative_to(root)}")

    print("=" * 72)
    print("EA-001 constitutional structure initialized.")
    print("Existing files were preserved.")
    print("=" * 72)


if __name__ == "__main__":
    main()
