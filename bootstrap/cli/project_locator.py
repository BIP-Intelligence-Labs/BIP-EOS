"""
bootstrap/cli/project_locator.py

Locate the Bootstrap project root.
"""

from pathlib import Path


class ProjectLocator:
    """Find the Bootstrap Engineering Lab project root."""

    MARKERS = (
        ".git",
        "bootstrap",
        "engineering",
    )

    @classmethod
    def find_root(cls, start=None) -> Path:
        current = Path(start or Path.cwd()).resolve()

        for directory in [current, *current.parents]:
            if cls._is_project_root(directory):
                return directory

        raise FileNotFoundError(
            "Bootstrap project root not found."
        )

    @classmethod
    def _is_project_root(cls, directory: Path) -> bool:
        return all(
            (directory / marker).exists()
            for marker in cls.MARKERS
        )


if __name__ == "__main__":
    print(ProjectLocator.find_root())
