"""
BIP EOS - Milestone 03 Bootstrap
Version: 0.3.0

Creates the core directory structure for the BIP EOS Engineering
Operating System (M03).
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "bootstrap",
    "config",
    "core",
    "core/ai",
    "core/plugins",
    "core/logging",
    "core/version",
    "core/docs",
    "core/health",
    "cli",
    "docs",
    "logs",
    "tests",
]

FILES = [
    "bootstrap/__init__.py",
    "config/__init__.py",
    "core/__init__.py",
    "core/ai/__init__.py",
    "core/plugins/__init__.py",
    "core/logging/__init__.py",
    "core/version/__init__.py",
    "core/docs/__init__.py",
    "core/health/__init__.py",
    "cli/__init__.py",
]

def main():
    print("=" * 60)
    print("BIP EOS :: Milestone 03 Bootstrap")
    print("=" * 60)

    for d in DIRECTORIES:
        path = ROOT / d
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")

    for f in FILES:
        path = ROOT / f
        path.touch(exist_ok=True)
        print(f"[FILE] {path}")

    print("\nMilestone 03 foundation created successfully.")

if __name__ == "__main__":
    main()
