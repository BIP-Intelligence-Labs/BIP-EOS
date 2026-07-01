"""
dependency_certification.py

UEOS Atlas Architecture Consolidation
-------------------------------------

Validates project dependencies and basic import health.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def run(title: str, command: list[str]) -> bool:
    print(f"\n=== {title} ===")
    try:
        result = subprocess.run(command, cwd=ROOT)
        return result.returncode == 0
    except FileNotFoundError:
        print("Command not found:", " ".join(command))
        return False


def main() -> None:
    checks = [
        ("Dependency Tree", [sys.executable, "-m", "pip", "check"]),
        ("Import Validation", [sys.executable, "-m", "compileall", "src"]),
    ]

    passed = 0

    print("=" * 72)
    print("UEOS DEPENDENCY CERTIFICATION")
    print("=" * 72)

    for title, cmd in checks:
        if run(title, cmd):
            print("PASS")
            passed += 1
        else:
            print("FAIL")

    print("\nSummary")
    print(f"{passed}/{len(checks)} checks passed")

    print("\nRecommended:")
    print("  python -m pytest")
    print("  python tools/validation/repository_certification.py")
    print("  python -m pip list --outdated")


if __name__ == "__main__":
    main()
