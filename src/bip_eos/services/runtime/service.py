"""
runtime_service.py

UEOS
M-006.3 - Runtime Services

Place in:
    src/bip_eos/services/runtime/service.py
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import platform
import sys


@dataclass(slots=True)
class RuntimeStatus:
    version: str
    python_version: str
    operating_system: str
    started_at: str
    healthy: bool = True


class RuntimeService:
    """
    Provides runtime status information for UEOS.
    """

    def __init__(self) -> None:
        self.started_at = datetime.utcnow()

    def status(self) -> RuntimeStatus:
        return RuntimeStatus(
            version="0.1.0 Genesis",
            python_version=sys.version.split()[0],
            operating_system=platform.platform(),
            started_at=self.started_at.isoformat() + "Z",
            healthy=True,
        )

    def display(self) -> RuntimeStatus:
        status = self.status()

        print("=" * 60)
        print("UEOS Runtime Status")
        print("=" * 60)
        print(f"Version          : {status.version}")
        print(f"Python           : {status.python_version}")
        print(f"Operating System : {status.operating_system}")
        print(f"Started          : {status.started_at}")
        print(f"Healthy          : {'YES' if status.healthy else 'NO'}")

        return status


def main() -> int:
    RuntimeService().display()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
