#!/usr/bin/env python3
"""
bootstrap_constitutional_library_v1.py

Creates the UEOS Constitutional Library skeleton.

Engineering/
└── architecture/
    ├── CL-001/
    ├── EA-001/
    ├── BFS-001/
    ├── EAuS-001/
    ├── ERS-001/
    ├── UEG-001/
    ├── ECS-001/
    ├── EPF-001/
    ├── EKS-001/
    └── EAS-001/
"""

from pathlib import Path

BOOKS = {
    "CL-001": "UEOS Constitutional Library",
    "EA-001": "Universal Engineering Architecture",
    "BFS-001": "Bootstrap Framework System",
    "EAuS-001": "Engineering Audit System",
    "ERS-001": "Engineering Registry System",
    "UEG-001": "Unified Engineering Graph",
    "ECS-001": "Engineering Compiler System",
    "EPF-001": "Engineering Publishing Framework",
    "EKS-001": "Engineering Knowledge System",
    "EAS-001": "Engineering Academy System",
}

CHAPTERS = [
    "README.md",
    "Chapter-01-Mission.md",
    "Chapter-02-Architecture.md",
    "Chapter-03-Constitutional-Objects.md",
    "Chapter-04-Lifecycle.md",
    "Chapter-05-Subsystems.md",
    "Chapter-06-Governance.md",
    "Chapter-07-Standards.md",
    "Chapter-08-Interfaces.md",
    "Chapter-09-Extensibility.md",
    "Chapter-10-Roadmap.md",
    "manifest.yaml",
]

def write(path: Path, text: str):
    if path.exists():
        print(f"[EXISTS ] {path}")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"[CREATE ] {path}")

def main():
    root = Path.cwd() / "engineering" / "architecture"
    root.mkdir(parents=True, exist_ok=True)

    print("="*72)
    print("UEOS Constitutional Library v1.0")
    print("="*72)

    # Library
    lib = root / "CL-001"
    lib.mkdir(exist_ok=True)

    write(lib / "README.md", "# CL-001\n\nUEOS Constitutional Library\n")
    write(lib / "Constitutional-Library.md",
"""# UEOS Constitutional Library

## Constitutional Hierarchy

EC-001  Engineering Constitution

CL-001  UEOS Constitutional Library

EA-001  Universal Engineering Architecture

BFS-001 Bootstrap Framework System

EAuS-001 Engineering Audit System
ERS-001 Engineering Registry System
UEG-001 Unified Engineering Graph
ECS-001 Engineering Compiler System
EPF-001 Engineering Publishing Framework
EKS-001 Engineering Knowledge System
EAS-001 Engineering Academy System
""")
    write(lib / "Architecture-Map.md", "# Architecture Map\n")
    write(lib / "Library-Manifest.yaml", "version: 1.0\nstatus: approved\n")

    for code, title in BOOKS.items():
        d = root / code
        d.mkdir(exist_ok=True)
        for ch in CHAPTERS:
            p = d / ch
            if ch == "README.md":
                txt = f"# {code}\n\n{title}\n"
            elif ch == "manifest.yaml":
                txt = f"id: {code}\ntitle: {title}\nversion: 1.0\nstatus: draft\n"
            else:
                txt = f"# {ch[:-3].replace('-', ' ')}\n\n{title}\n"
            write(p, txt)

    print("="*72)
    print("Constitutional Library initialized.")
    print("="*72)

if __name__ == "__main__":
    main()
