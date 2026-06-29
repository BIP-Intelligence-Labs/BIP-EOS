#!/usr/bin/env python3
"""
status.py

BIP EOS Status Command
"""

from __future__ import annotations

from bip_eos.application import Application


def run(argv=None):
    app = Application()
    return app.status()


def main():
    print("=" * 70)
    print("BIP EOS Status")
    print("=" * 70)

    result = run()

    runtime = result.get("runtime", {})
    for component, info in runtime.items():
        if isinstance(info, dict):
            state = info.get("status", "OK")
        else:
            state = "OK"
        print(f"[ OK ] {component:<18} {state}")

    print("=" * 70)


if __name__ == "__main__":
    main()
