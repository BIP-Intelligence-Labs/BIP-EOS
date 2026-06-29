#!/usr/bin/env python3
"""
release.py

BIP EOS Release Command
"""

from __future__ import annotations

from datetime import datetime

from bip_eos.application import Application


def run(argv=None):
    app = Application()

    return {
        "product": "BIP EOS",
        "version": app.runtime.version.status().get("version"),
        "codename": app.runtime.version.status().get("codename"),
        "released": datetime.utcnow().isoformat() + "Z",
        "status": "ready",
    }


def main():
    print("=" * 70)
    print("BIP EOS Release")
    print("=" * 70)

    release = run()

    for key, value in release.items():
        print(f"{key:<10}: {value}")

    print("=" * 70)


if __name__ == "__main__":
    main()
