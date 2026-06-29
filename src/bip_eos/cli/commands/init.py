#!/usr/bin/env python3
"""
init.py

BIP EOS Initialization Command
"""

from __future__ import annotations

from pathlib import Path

from bip_eos.application import Application


def run(argv=None):
    app = Application()
    root = Path.cwd()

    created = []

    for folder in (
        "docs",
        "logs",
        "reports",
        "registry",
        "plugins",
    ):
        path = root / folder
        path.mkdir(parents=True, exist_ok=True)
        created.append(str(path))

    return {
        "status": "initialized",
        "project_root": str(root),
        "created": created,
        "runtime": app.status().get("runtime", {}),
    }


def main():
    print("=" * 70)
    print("BIP EOS Initialize")
    print("=" * 70)

    result = run()

    print(f"Status       : {result['status']}")
    print(f"Project Root : {result['project_root']}")
    print("\nDirectories")
    for item in result["created"]:
        print(f"  - {item}")

    print("=" * 70)


if __name__ == "__main__":
    main()
