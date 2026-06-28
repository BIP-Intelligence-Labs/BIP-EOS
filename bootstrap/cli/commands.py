"""
bootstrap/cli/commands.py

Bootstrap command registry.
"""

from __future__ import annotations

from .doctor import BootstrapDoctor
from .repair import RepairManager
from .release import ReleaseManager
from .new import NewCommand
from .discover import DiscoverCommand


class Commands:
    """Registers built-in Bootstrap CLI commands."""

    @staticmethod
    def doctor() -> int:
        return BootstrapDoctor().check()

    @staticmethod
    def repair() -> None:
        RepairManager().run()

    @staticmethod
    def release() -> None:
        ReleaseManager.status()

    @staticmethod
    def new_plugin(name: str) -> None:
        NewCommand().plugin(name)

    @staticmethod
    def discover(url: str) -> None:
        DiscoverCommand().run(url)


if __name__ == "__main__":
    print("Bootstrap Commands")
    print("==================")
    print("doctor")
    print("repair")
    print("release")
    print("discover")
    print("new_plugin(name)")
