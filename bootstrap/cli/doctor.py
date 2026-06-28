"""
bootstrap/cli/doctor.py

Bootstrap Engineering Doctor
"""

from __future__ import annotations

from pathlib import Path

from .project_locator import ProjectLocator


class BootstrapDoctor:
    """Runs repository health checks."""

    def __init__(self) -> None:
        self.root = ProjectLocator.find_root()

    def check(self) -> int:
        checks = [
            ("Kernel", self.root / "bootstrap" / "kernel"),
            ("CLI", self.root / "bootstrap" / "cli"),
            ("Plugins", self.root / "bootstrap" / "plugins"),
            ("Engineering", self.root / "engineering"),
            ("Docs", self.root / "docs"),
            ("Tests", self.root / "tests"),
        ]

        print("=" * 40)
        print(" Bootstrap Engineering Doctor")
        print("=" * 40)
        print(f"Repository: {self.root}\n")

        failures = 0

        for name, path in checks:
            if path.exists():
                print(f"✓ {name:<12} OK")
            else:
                print(f"✗ {name:<12} Missing")
                failures += 1

        print("\nRepository Status")
        print("-----------------")
        if failures == 0:
            print("🚀 ALL SYSTEMS GO")
        else:
            print(f"⚠ {failures} issue(s) detected")

        return failures


def main() -> None:
    BootstrapDoctor().check()


if __name__ == "__main__":
    main()
