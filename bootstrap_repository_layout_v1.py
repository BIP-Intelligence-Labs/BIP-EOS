#!/usr/bin/env python3
"""
bootstrap_repository_layout_v1.py

UEOS Repository Layout Bootstrap

Creates the canonical top-level repository layout defined by
UEOS Architecture Version 1.0.

Safe:
- Python Standard Library only
- Never overwrites existing files
"""

from pathlib import Path

ROOT_FILES = {
    "README.md": "# Genesis\n\nUEOS Engineering Operating System.\n",
    "LICENSE": "Copyright (c) UEOS\n",
    "pyproject.toml": """[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "bip-eos"
version = "0.1.0"
description = "Universal Engineering Operating System"
requires-python = ">=3.11"
""",
    "requirements.txt": "# Runtime dependencies\n",
    ".gitignore": """__pycache__/
*.pyc
.venv/
dist/
build/
.coverage
.pytest_cache/
.mypy_cache/
""",
}

DIRECTORIES = [
    "src",
    "engineering",
    "bootstrap",
    "tests",
    "docs",
    "tools",
]

def write_if_missing(path: Path, text: str):
    if path.exists():
        print(f"[EXISTS ] {path.name}")
        return
    path.write_text(text, encoding="utf-8")
    print(f"[CREATE ] {path.name}")

def main():
    root = Path(__file__).resolve().parent

    print("=" * 72)
    print("UEOS Repository Layout v1.0")
    print("=" * 72)

    for directory in DIRECTORIES:
        d = root / directory
        if d.exists():
            print(f"[EXISTS ] {directory}/")
        else:
            d.mkdir(parents=True)
            print(f"[CREATE ] {directory}/")

    for filename, content in ROOT_FILES.items():
        write_if_missing(root / filename, content)

    launcher = root / "bootstrap.py"
    if launcher.exists():
        print("[EXISTS ] bootstrap.py")
    else:
        print("[INFO   ] bootstrap.py not found. Add the UEOS Bootstrap Launcher here.")

    print("=" * 72)
    print("Repository layout verified.")
    print("=" * 72)

if __name__ == "__main__":
    main()
