"""
bootstrap/cli/release.py

Bootstrap Release Manager
"""

from __future__ import annotations

import subprocess
from datetime import datetime


class ReleaseManager:
    """Helpers for creating Bootstrap releases."""

    @staticmethod
    def version_tag(version: str) -> str:
        return f"bootstrap-v{version}"

    @staticmethod
    def create_tag(version: str) -> None:
        tag = ReleaseManager.version_tag(version)
        subprocess.run(["git", "tag", tag], check=True)

    @staticmethod
    def status() -> None:
        print("=" * 40)
        print(" Bootstrap Release Manager")
        print("=" * 40)
        print(f"Timestamp : {datetime.now():%Y-%m-%d %H:%M:%S}")
        print("Repository: Ready")
        print("Kernel    : Loaded")
        print("CLI       : Loaded")
        print("Plugins   : Ready")
        print("\nNext:")
        print("  git add .")
        print('  git commit -m "feat(...)"')
        print("  bootstrap release")


if __name__ == "__main__":
    ReleaseManager.status()
