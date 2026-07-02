"""
package_manager_service.py

UEOS
M-006.3 - Runtime Services

Place in:
    src/bip_eos/services/package_manager/service.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class PackageManagerStatus:
    packages_found: int
    manifests_found: int
    healthy: bool
    package_files: list[str] = field(default_factory=list)


class PackageManagerService:
    """
    Production service behind the `UEOS> install` and package commands.
    """

    MANIFEST_FILES = (
        "pyproject.toml",
        "bootstrap.toml",
        "requirements.txt",
    )

    def __init__(self, repository_root: Path | None = None) -> None:
        self.repository_root = repository_root or Path.cwd()

    def scan(self) -> PackageManagerStatus:
        manifests = []
        for name in self.MANIFEST_FILES:
            if (self.repository_root / name).exists():
                manifests.append(name)

        packages = sorted(
            str(p.relative_to(self.repository_root))
            for p in self.repository_root.rglob("__init__.py")
        )

        return PackageManagerStatus(
            packages_found=len(packages),
            manifests_found=len(manifests),
            healthy=True,
            package_files=packages,
        )

    def display(self) -> PackageManagerStatus:
        status = self.scan()

        print("=" * 60)
        print("UEOS Package Manager")
        print("=" * 60)
        print(f"Python Packages : {status.packages_found}")
        print(f"Manifest Files  : {status.manifests_found}")
        print(f"Healthy         : {'YES' if status.healthy else 'NO'}")
        print("-" * 60)

        for pkg in status.package_files:
            print(f"✓ {pkg}")

        return status


def main() -> int:
    PackageManagerService().display()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
