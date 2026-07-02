#!/usr/bin/env python3
"""
launcher.py

BIP EOS Launcher

Single executable entry point for starting the platform.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ueos.bootstrap import main as bootstrap_main


def launch() -> int:
    """Launch BIP EOS."""
    return bootstrap_main()


if __name__ == "__main__":
    raise SystemExit(launch())
