#!/usr/bin/env python3
"""
bootstrap_ea001_constitution_v1.py

Creates the official EA-001 Constitution structure for UEOS.
Standard Library only.
"""

from pathlib import Path

FILES = {
    "README.md": "# EA-001 — UEOS Constitution\n",
    "STATUS.md": """# Architecture Status

Architecture: EA-001
Version: 1.0
Status: LOCKED
Codename: Genesis

Changes require an Engineering Decision Record (EDR).
""",
    "VERSION.md": """# Architecture Versions

## v1.0 — Genesis

Status: Current
Description:
- Initial constitutional architecture.
- Runtime Architecture v1.0 established.
- UEM established.
- BES established.
- BFS established.
""",
    "CHANGELOG.md": """# Architecture Changelog

## v1.0
- Engineering Constitution
- Runtime Architecture
- Universal Engineering Meta-Model
- Bootstrap Engineering Standard
- Bootstrap Framework System
""",
    "Chapter-01-Mission.md": "# Chapter 01 — Mission\n",
    "Chapter-02-Engineering-Laws.md": "# Chapter 02 — Engineering Laws\n",
    "Chapter-03-UEOS-Architecture.md": "# Chapter 03 — UEOS Architecture\n",
    "Chapter-04-Constitutional-Objects.md": "# Chapter 04 — Constitutional Objects\n",
    "Chapter-05-Runtime-Architecture.md": "# Chapter 05 — Runtime Architecture\n",
    "Chapter-06-Constitutional-Systems.md": "# Chapter 06 — Constitutional Systems\n",
    "Chapter-07-Engineering-Lifecycle.md": "# Chapter 07 — Engineering Lifecycle\n",
    "Chapter-08-Repository-Standards.md": "# Chapter 08 — Repository Standards\n",
    "Chapter-09-Registry-Constitution.md": "# Chapter 09 — Registry Constitution\n",
    "Chapter-10-Unified-Engineering-Graph.md": "# Chapter 10 — Unified Engineering Graph\n",
    "Chapter-11-Bootstrap-Engineering-Standard.md": "# Chapter 11 — Bootstrap Engineering Standard\n",
    "Chapter-12-Constitutional-Engineering-Methodology.md": "# Chapter 12 — Constitutional Engineering Methodology\n",
}

MANIFEST = """architecture: EA-001
version: 1.0
status: LOCKED
codename: Genesis
chapters: 12
"""

def find_root(start: Path)->Path:
    cur=start.resolve()
    while cur!=cur.parent:
        if (cur/"engineering").exists() and (cur/"src").exists():
            return cur
        cur=cur.parent
    raise RuntimeError("UEOS repository root not found.")

def write_if_missing(path:Path,text:str):
    if path.exists():
        print(f"[EXISTS ] {path.relative_to(ROOT)}")
        return
    path.write_text(text,encoding="utf-8")
    print(f"[CREATE ] {path.relative_to(ROOT)}")

ROOT=None

def main():
    global ROOT
    ROOT=find_root(Path(__file__).parent)
    base=ROOT/"engineering"/"architecture"/"EA-001"
    base.mkdir(parents=True,exist_ok=True)
    for name,content in FILES.items():
        write_if_missing(base/name,content)
    m=base/"manifest.yaml"
    if not m.exists():
        m.write_text(MANIFEST,encoding="utf-8")
        print(f"[CREATE ] {m.relative_to(ROOT)}")
    else:
        print(f"[EXISTS ] {m.relative_to(ROOT)}")
    print("="*72)
    print("EA-001 Constitution v1.0 scaffold complete.")
    print("Architecture Status: LOCKED")
    print("="*72)

if __name__=="__main__":
    main()
