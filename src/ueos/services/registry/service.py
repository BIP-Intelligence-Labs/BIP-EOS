"""
registry_service.py

UEOS
M-006.3 - Runtime Services

Place in:
    src/bip_eos/services/registry/service.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class RegistryStatus:
    services: int
    healthy: bool
    entries: Dict[str, str] = field(default_factory=dict)


class RegistryService:
    """
    Central service registry for UEOS runtime services.
    """

    def __init__(self) -> None:
        self._entries: dict[str, str] = {}

    def register(self, name: str, implementation: str) -> None:
        self._entries[name] = implementation

    def unregister(self, name: str) -> None:
        self._entries.pop(name, None)

    def status(self) -> RegistryStatus:
        return RegistryStatus(
            services=len(self._entries),
            healthy=True,
            entries=dict(sorted(self._entries.items())),
        )

    def display(self) -> RegistryStatus:
        status = self.status()

        print("=" * 60)
        print("UEOS Service Registry")
        print("=" * 60)

        if not status.entries:
            print("No services registered.")
        else:
            for name, impl in status.entries.items():
                print(f"✓ {name:<20} {impl}")

        print("-" * 60)
        print(f"Registered Services : {status.services}")
        print(f"Healthy             : {'YES' if status.healthy else 'NO'}")

        return status


def main() -> int:
    service = RegistryService()

    service.register("doctor", "DoctorService")
    service.register("runtime", "RuntimeService")
    service.register("graph", "GraphService")

    service.display()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
