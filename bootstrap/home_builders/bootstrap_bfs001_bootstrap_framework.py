#!/usr/bin/env python3
"""
bootstrap_bfs001_bootstrap_framework.py

UEOS Bootstrap Framework System (BFS-001)

Purpose
-------
Scaffold the Bootstrap Framework used to construct future UEOS
subsystems in a consistent, standards-driven manner.

Characteristics
---------------
- Python Standard Library only
- Safe by default
- Never overwrites existing files
"""

from pathlib import Path

FRAMEWORK_MODULES = {
    "__init__.py": '"""UEOS Bootstrap Framework."""\n',
    "builder.py": '"""Bootstrap builder orchestration."""\n',
    "bootstrap.py": '"""Bootstrap entry point."""\n',
    "filesystem.py": '"""Filesystem helpers."""\n',
    "writer.py": '"""Safe file writer."""\n',
    "template_engine.py": '"""Template rendering engine."""\n',
    "manifest.py": '"""Manifest generation."""\n',
    "validator.py": '"""Bootstrap validation."""\n',
    "reporting.py": '"""Bootstrap reporting."""\n',
    "discovery.py": '"""Repository discovery."""\n',
    "version.py": '__version__ = "0.1.0"\n',
}

TEMPLATE_DIRS = [
    "subsystem",
    "runtime",
    "engineering",
    "tests",
    "documentation",
]

README = """# Bootstrap Framework System (BFS)

## Constitutional Purpose

The Bootstrap Framework constructs UEOS subsystems in accordance with
the Bootstrap Engineering Standard (BES).

This package is construction infrastructure and is not part of the
UEOS runtime.
"""

def find_root(start: Path) -> Path:
    cur = start.resolve()
    while cur != cur.parent:
        if (cur / "bootstrap").exists() and (cur / "src").exists():
            return cur
        cur = cur.parent
    raise RuntimeError("UEOS repository root not found.")

def write_if_missing(path: Path, content: str):
    if path.exists():
        print(f"[EXISTS ] {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"[CREATE ] {path.relative_to(ROOT)}")

ROOT = None

def main():
    global ROOT
    ROOT = find_root(Path(__file__).parent)

    fw = ROOT / "bootstrap" / "framework"
    fw.mkdir(parents=True, exist_ok=True)

    write_if_missing(fw / "README.md", README)

    for name, content in FRAMEWORK_MODULES.items():
        write_if_missing(fw / name, content)

    tmpl = ROOT / "bootstrap" / "templates"
    tmpl.mkdir(parents=True, exist_ok=True)

    for d in TEMPLATE_DIRS:
        p = tmpl / d
        p.mkdir(parents=True, exist_ok=True)
        write_if_missing(p / ".gitkeep", "")

    manifest = fw / "manifest.yaml"
    if not manifest.exists():
        manifest.write_text(
            "system: BFS-001\n"
            "name: Bootstrap Framework System\n"
            "version: 0.1.0\n"
            "status: scaffolded\n",
            encoding="utf-8"
        )
        print(f"[CREATE ] {manifest.relative_to(ROOT)}")
    else:
        print(f"[EXISTS ] {manifest.relative_to(ROOT)}")

    print("=" * 72)
    print("BFS-001 Bootstrap Framework scaffold complete.")
    print("Existing files were preserved.")
    print("=" * 72)

if __name__ == "__main__":
    main()
