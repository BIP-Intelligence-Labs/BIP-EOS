"""
verify.py

UEOS CLI
Package Verify Command
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ueos.package_manager.verifier import PackageVerifier


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ueos verify",
        description="Verify a UEOS package manifest or artifact.",
    )
    parser.add_argument(
        "manifest",
        help="Path to the package manifest.",
    )
    parser.add_argument(
        "--artifact",
        help="Optional package artifact to verify.",
    )
    parser.add_argument(
        "--checksum",
        help="Expected SHA-256 checksum.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    verifier = PackageVerifier()

    if args.artifact and args.checksum:
        result = verifier.verify_package(
            manifest_path=Path(args.manifest),
            artifact_path=Path(args.artifact),
            expected_checksum=args.checksum,
        )
    else:
        result = verifier.verify_manifest(
            Path(args.manifest),
        )

    print(result.message)

    if result.checksum:
        print(f"SHA256 : {result.checksum}")

    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
