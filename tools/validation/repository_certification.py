\
"""
repository_certification.py

UEOS Atlas Architecture Consolidation
-------------------------------------

Runs repository certification checks after consolidation.

Usage:
    python tools/validation/repository_certification.py
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

CHECKS = [
    ("Git Status", ["git", "status", "--short"]),
    ("Pytest", [sys.executable, "-m", "pytest"]),
]


def banner(title: str):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def run_check(name: str, command: list[str]) -> bool:
    banner(name)
    try:
        result = subprocess.run(command, cwd=ROOT)
        return result.returncode == 0
    except FileNotFoundError:
        print(f"Unable to execute: {' '.join(command)}")
        return False


def main():
    print("=" * 72)
    print("UEOS REPOSITORY CERTIFICATION")
    print("=" * 72)

    passed = 0

    for name, command in CHECKS:
        if run_check(name, command):
            print(f"PASS : {name}")
            passed += 1
        else:
            print(f"FAIL : {name}")

    banner("Summary")
    print(f"Passed {passed}/{len(CHECKS)} checks")

    print("\nRecommended additional validation:")
    print("  • ruff check src tests")
    print("  • mypy src")
    print("  • UEOS Doctor")
    print("  • Dependency validation")
    print("  • Package validation")


if __name__ == "__main__":
    main()
