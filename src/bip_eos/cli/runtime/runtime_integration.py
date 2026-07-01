"""
runtime_integration.py

M-006.2 - Runtime Integration

Purpose:
    Integrate the CLI with the UEOS runtime.

Suggested usage from your runtime after boot:

    from bip_eos.cli.main import run as run_cli

    # Runtime boot...
    print("\nStatus : READY\n")

    raise SystemExit(run_cli())
"""

from __future__ import annotations

from bip_eos.cli.command_loader import CommandLoader
from bip_eos.cli.dispatcher import CommandDispatcher
from bip_eos.cli.shell import Shell


class RuntimeIntegration:
    """Coordinates CLI startup after the runtime finishes booting."""

    def __init__(self) -> None:
        self.dispatcher = CommandDispatcher()
        self.loader = CommandLoader(self.dispatcher)

    def start(self) -> int:
        print("\nLoading Commands...\n")

        loaded = self.loader.load()

        for command in self.dispatcher.commands():
            print(f"✓ {command.name}")

        print("\n-------------------------------------")
        print(f"Loaded {loaded} command(s).")
        print()

        shell = Shell(self.dispatcher)
        shell.run()

        return 0


def run() -> int:
    """Entry point used by the UEOS runtime."""
    return RuntimeIntegration().start()


if __name__ == "__main__":
    raise SystemExit(run())
