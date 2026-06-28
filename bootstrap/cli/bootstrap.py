"""
bootstrap/cli/bootstrap.py

Bootstrap CLI application.
"""

from __future__ import annotations

import argparse

from .commands import Commands
from .project_locator import ProjectLocator


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="bootstrap")
    sub = p.add_subparsers(dest="command")

    sub.add_parser("doctor")
    sub.add_parser("repair")
    sub.add_parser("release")
    sub.add_parser("root")

    new = sub.add_parser("new")
    new_sub = new.add_subparsers(dest="resource")
    plugin = new_sub.add_parser("plugin")
    plugin.add_argument("name")

    return p


def main() -> int:
    args = parser().parse_args()

    match args.command:
        case "doctor":
            return Commands.doctor()
        case "repair":
            Commands.repair()
        case "release":
            Commands.release()
        case "root":
            print(ProjectLocator.find_root())
        case "new":
            if args.resource == "plugin":
                Commands.new_plugin(args.name)
            else:
                print("Unknown resource.")
                return 1
        case _:
            parser().print_help()
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
