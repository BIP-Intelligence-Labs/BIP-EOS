"""
search.py

UEOS CLI
Package Search Command
"""

from __future__ import annotations

import argparse

from ueos.package_manager.registry import PackageRegistry
from ueos.package_manager.manifest import PackageManifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ueos search",
        description="Search the UEOS package registry.",
    )
    parser.add_argument("query", help="Search text.")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    # TODO: Replace with persistent registry loading.
    registry = PackageRegistry()

    # Sample placeholder until registry persistence is implemented.
    registry.load([
        PackageManifest(
            name="runtime",
            version="1.0.0",
            description="UEOS Runtime",
        ),
        PackageManifest(
            name="compiler",
            version="1.0.0",
            description="UEOS Compiler",
        ),
    ])

    matches = registry.search(args.query)

    if not matches:
        print("No packages found.")
        return 1

    for manifest in matches:
        print(f"{manifest.identifier} - {manifest.description}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
