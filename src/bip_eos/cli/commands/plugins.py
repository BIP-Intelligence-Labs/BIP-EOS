#!/usr/bin/env python3
"""
plugins.py

BIP EOS Plugins Command
"""

from __future__ import annotations

from bip_eos.application import Application


def run(argv=None):
    app = Application()
    app.runtime.plugins.discover()
    app.runtime.plugins.load()
    return app.runtime.plugins.status()


def main():
    print("=" * 70)
    print("BIP EOS Plugins")
    print("=" * 70)

    status = run()

    print(f"Plugin Directory : {status.get('plugin_directory')}")
    print(f"Discovered       : {status.get('discovered')}")
    print(f"Loaded           : {status.get('loaded')}")

    print("=" * 70)


if __name__ == "__main__":
    main()
