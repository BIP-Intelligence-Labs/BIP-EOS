#!/usr/bin/env python3
"""
audit.py

BIP EOS Audit Command
"""

from __future__ import annotations

from bip_eos.application import Application


def run(argv=None):
    app = Application()
    return app.runtime.repository.audit()


def main():
    print("=" * 70)
    print("BIP EOS Repository Audit")
    print("=" * 70)

    result = run()

    for key, value in result.items():
        print(f"{key:<15}: {value}")

    print("=" * 70)


if __name__ == "__main__":
    main()
