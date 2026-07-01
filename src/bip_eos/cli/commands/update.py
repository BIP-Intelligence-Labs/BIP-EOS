"""
update.py

UEOS CLI
Package Update Command
"""

from __future__ import annotations

import argparse
from pathlib import Path

from bip_eos.package_manager.service import (
    PackageManagerConfig,
    PackageManagerService,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ueos update",
        description="Update an installed UEOS package.",
    )
    parser.add_argument(
        "manifest",
        help="Path to the updated package manifest.",
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

    # Current implementation reuses install() until dedicated
    # upgrade/version resolution is implemented.
    result = service.install(args.manifest)

    print(result.message)

    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
