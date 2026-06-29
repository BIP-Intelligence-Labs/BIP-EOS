#!/usr/bin/env python3
"""
__main__.py

Allows BIP EOS to be started with:

    python -m bip_eos
"""

from __future__ import annotations

from bip_eos.launcher import launch


def main() -> int:
    return launch()


if __name__ == "__main__":
    raise SystemExit(main())
