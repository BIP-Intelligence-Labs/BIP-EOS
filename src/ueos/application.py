#!/usr/bin/env python3
"""
application.py

BIP EOS Application
"""

from __future__ import annotations

from pathlib import Path

from ueos.cli.config import ConfigManager
from ueos.core.runtime_engine import RuntimeEngine


class Application:
    """
    Root application object for BIP EOS.
    """

    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()
        self.config = ConfigManager(self.root)
        self.runtime = RuntimeEngine(self.root)

    def start(self):
        return self.runtime.startup()

    def stop(self):
        self.runtime.shutdown()

    def doctor(self):
        return self.runtime.doctor()

    def status(self):
        return {
            "configuration": self.config.status(),
            "runtime": self.runtime.startup(),
        }


def main():
    app = Application()

    print("=" * 70)
    print("BIP EOS Application")
    print("=" * 70)

    app.start()
    print(app.doctor())
    app.stop()


if __name__ == "__main__":
    main()
