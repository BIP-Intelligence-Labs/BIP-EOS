#!/usr/bin/env python3
"""
pyproject_bootstrap.py

Generates a production-ready pyproject.toml for BIP EOS.
"""

from pathlib import Path


PYPROJECT = """[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "bip-eos"
version = "0.1.0"
description = "BIP Engineering Operating System"
readme = "README.md"
requires-python = ">=3.11"
authors = [
    { name = "BIP Intelligence Labs" }
]

[project.scripts]
bip = "bip_eos.__main__:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
"""

def main():
    root = Path.cwd()
    target = root / "pyproject.toml"

    if target.exists():
        print(f"[SKIP] {target} already exists")
        return

    target.write_text(PYPROJECT, encoding="utf-8")
    print(f"[OK] Created {target}")


if __name__ == "__main__":
    main()
