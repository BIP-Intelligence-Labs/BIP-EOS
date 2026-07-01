"""
remove.py

UEOS CLI
Package Remove Command
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
        prog="ueos remove",
        description="Remove an installed UEOS package.",
    )
    parser.add_argument(
        "package",
        help="Package name to remove.",
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

    result = service.uninstall(args.package)

    print(result.message)

    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
