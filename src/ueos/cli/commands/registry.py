#!/usr/bin/env python3
"""
registry.py

BIP EOS Registry Command
"""

from __future__ import annotations

from ueos.application import Application


def run(argv=None):
    app = Application()
    return app.runtime.registry.build()


def main():
    print("=" * 70)
    print("BIP EOS Registry")
    print("=" * 70)

    data = run()

    print(f"Generated : {data.get('generated')}")
    print()

    print("Plugins")
    for item in data.get("plugins", []):
        print(f"  - {item}")

    print("\nCommands")
    for item in data.get("commands", []):
        print(f"  - {item}")

    print("\nEngines")
    for item in data.get("engines", []):
        print(f"  - {item}")

    print("=" * 70)


if __name__ == "__main__":
    main()
