"""
list.py

UEOS CLI
Package List Command
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ueos.package_manager.service import (
    PackageManagerConfig,
    PackageManagerService,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ueos list",
        description="List installed UEOS packages.",
    )
    parser.add_argument("--registry", default=".ueos/registry")
    parser.add_argument("--cache", default=".ueos/cache")
    parser.add_argument("--packages", default=".ueos/packages")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    service = PackageManagerService(
        PackageManagerConfig(
            registry_path=Path(args.registry),
            cache_path=Path(args.cache),
            install_path=Path(args.packages),
        )
    )

    packages = service.list_installed()

    if not packages:
        print("No packages installed.")
        return 0

    print("Installed packages")
    print("-" * 40)

    for package in packages:
        print(package)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
