#!/usr/bin/env python3
"""
version.py

BIP EOS Version Command
"""

from __future__ import annotations

from bip_eos.application import Application


def run(argv=None):
    app = Application()
    return app.runtime.version.status()


def main():
    print("=" * 70)
    print("BIP EOS Version")
    print("=" * 70)

    info = run()

    print(f"Product   : {info.get('product')}")
    print(f"Version   : {info.get('version')}")
    print(f"Codename  : {info.get('codename')}")
    print(f"Build     : {info.get('build')}")
    print(f"Released  : {info.get('released')}")

    print("=" * 70)


if __name__ == "__main__":
    main()
