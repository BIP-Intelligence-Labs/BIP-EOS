"""
main.py

UEOS CLI entry point
M-006.2

Place in:
    src/bip_eos/cli/main.py
"""

from __future__ import annotations

from bip_eos.cli.command_loader import CommandLoader
from bip_eos.cli.dispatcher import CommandDispatcher
from bip_eos.cli.shell import Shell


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
