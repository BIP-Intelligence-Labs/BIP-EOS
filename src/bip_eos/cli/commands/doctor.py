#!/usr/bin/env python3
from __future__ import annotations

from bip_eos.application import Application


def run(argv=None):
    return Application().doctor()


def main():
    print("=" * 70)
    print("BIP EOS Doctor")
    print("=" * 70)
    result = run()
    for component, info in result.items():
        state = info.get("status", "OK") if isinstance(info, dict) else "OK"
        print(f"[ OK ] {component:<18} {state}")
    print("=" * 70)


if __name__ == "__main__":
    main()
