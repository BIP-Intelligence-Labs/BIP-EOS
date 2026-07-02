"""
main.py

UEOS CLI entry point
M-006.2

Place in:
    src/bip_eos/cli/main.py
"""

from __future__ import annotations

from ueos.cli.command_loader import CommandLoader
from ueos.cli.dispatcher import CommandDispatcher
from ueos.cli.shell import Shell


def build_shell() -> Shell:
    """
    Create the dispatcher, discover commands,
    and return a configured shell instance.
    """
    dispatcher = CommandDispatcher()

    loader = CommandLoader(dispatcher)
    loaded = loader.load()

    print(f"[UEOS] Loaded {loaded} command(s).")

    return Shell(dispatcher)


def run() -> int:
    """
    Start the interactive UEOS shell.
    """
    shell = build_shell()
    shell.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
