"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Version System Bootstrap

Creates the canonical version subsystem for EOS.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "src/bip_eos/core/version",
]

FILES = {
    "src/bip_eos/core/version/__init__.py": """EOS Version Subsystem"""

from .version import EOS_VERSION
from .version_engine import VersionEngine
,

    "src/bip_eos/core/version/version.py": """Canonical EOS Version Information"""

from dataclasses import dataclass

@dataclass(frozen=True)
class EOSVersion:
    version: str = "0.1.0"
    codename: str = "Genesis"
    platform: str = "Engineering Operating System"
    release: str = "Development"

EOS_VERSION = EOSVersion()
,

    "src/bip_eos/core/version/version_engine.py": """EOS Version Engine"""

from .version import EOS_VERSION

class VersionEngine:
    @staticmethod
    def banner():
        return f"""\n============================================================\n{EOS_VERSION.platform}\n\nVersion : {EOS_VERSION.version}\nCodename: {EOS_VERSION.codename}\nRelease : {EOS_VERSION.release}\n============================================================\n"""
,

    ".gitignore": """__pycache__/
*.py[cod]
*.egg-info/
.eggs/
build/
dist/
pip-wheel-metadata/
.pytest_cache/
.coverage
htmlcov/
.mypy_cache/
.ruff_cache/
.venv/
venv/
env/
.vscode/
.idea/
.DS_Store
Thumbs.db
*.log
.env
.env.*
"""
}


def create_directory(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")


def create_file(path: Path, text: str):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"[FILE] {path}")


def main():
    print("=" * 70)
    print("EOS Version System Bootstrap")
    print("=" * 70)

    for d in DIRECTORIES:
        create_directory(ROOT / d)

    for f, t in FILES.items():
        create_file(ROOT / f, t)

    print("-" * 70)
    print("Canonical Version System Installed")
    print("Git Ignore Installed")
    print("=" * 70)


if __name__ == "__main__":
    main()
