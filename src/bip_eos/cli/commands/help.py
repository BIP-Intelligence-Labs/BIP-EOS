#!/usr/bin/env python3
"""
help.py

BIP EOS Help Command
"""

from __future__ import annotations

from bip_eos.cli.dispatcher import Dispatcher


def run(argv=None):
    dispatcher = Dispatcher()
    return {
        "commands": dispatcher.commands()
    }


def main():
    print("=" * 70)
    print("BIP EOS Help")
    print("=" * 70)

    result = run()

    print("Available Commands\n")

    for command in result["commands"]:
        print(f"  bip {command}")

    print("=" * 70)


if __name__ == "__main__":
    main()
