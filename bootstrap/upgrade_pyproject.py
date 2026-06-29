#!/usr/bin/env python3
"""
upgrade_pyproject.py

Safely upgrades an existing pyproject.toml for BIP EOS.

Features:
- Creates pyproject.toml.bak
- Adds/updates console script:
      bip = "bip_eos.__main__:main"
- Ensures setuptools package discovery uses src/
- Does NOT overwrite unrelated settings.
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()
PYPROJECT = ROOT / "pyproject.toml"
BACKUP = ROOT / "pyproject.toml.bak"


def ensure(text: str, marker: str, block: str) -> str:
    if marker in text:
        return text
    if not text.endswith("\n"):
        text += "\n"
    return text + "\n" + block.strip() + "\n"


def main():
    if not PYPROJECT.exists():
        print("[FAIL] pyproject.toml not found")
        return

    shutil.copy2(PYPROJECT, BACKUP)
    print(f"[OK] Backup created: {BACKUP.name}")

    text = PYPROJECT.read_text(encoding="utf-8")

    text = ensure(
        text,
        "[project.scripts]",
        """
[project.scripts]
bip = "bip_eos.__main__:main"
"""
    )

    text = ensure(
        text,
        "[tool.setuptools]",
        """
[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
"""
    )

    PYPROJECT.write_text(text, encoding="utf-8")

    print("[OK] pyproject.toml upgraded")
    print()
    print("Next:")
    print("  pip install -e .")
    print("  bip")


if __name__ == "__main__":
    main()
