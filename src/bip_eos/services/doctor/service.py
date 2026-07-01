"""
doctor_service.py

UEOS
M-006.3 - Runtime Services

Place in:
    src/bip_eos/services/doctor/service.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(slots=True)
class DoctorResult:
    checks: int = 0
    passed: int = 0
    warnings: int = 0
    errors: int = 0


class DoctorService:
    """
    Production service behind the `UEOS> doctor` command.
    """

    REQUIRED_PATHS = (
        "src",
        "engineering",
        "docs",
        "tests",
    )

    def __init__(self, repository_root: Path | None = None):
        self.repository_root = repository_root or Path.cwd()

    def run(self) -> DoctorResult:
        result = DoctorResult()

        for required in self.REQUIRED_PATHS:
            result.checks += 1
            path = self.repository_root / required

            if path.exists():
                result.passed += 1
                print(f"✓ {required}")
            else:
                result.errors += 1
                print(f"✗ Missing: {required}")

        print("\nDoctor Summary")
        print("-------------------------")
        print(f"Checks   : {result.checks}")
        print(f"Passed   : {result.passed}")
        print(f"Warnings : {result.warnings}")
        print(f"Errors   : {result.errors}")

        return result


def main() -> int:
    result = DoctorService().run()
    return 0 if result.errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
