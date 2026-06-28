"""
bootstrap/kernel/cli.py

Production Bootstrap CLI.
"""

from __future__ import annotations

import argparse

from .kernel import BootstrapKernel


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bootstrap",
        description="Bootstrap Engineering Factory CLI",
    )

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Show kernel status")
    sub.add_parser("boot", help="Boot the kernel")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    kernel = BootstrapKernel()

    if args.command == "boot":
        kernel.boot()
        print("Bootstrap Kernel booted.")

    elif args.command == "status":
        print(kernel.status())

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
