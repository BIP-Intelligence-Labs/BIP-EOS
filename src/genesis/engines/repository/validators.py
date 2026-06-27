"""Repository validation for Genesis EEOS."""

from pathlib import Path

REQUIRED_FILES = (
    "pyproject.toml",
    "README.md",
    "genesis.toml",
)

REQUIRED_DIRS = (
    "src",
    "docs",
)


class RepositoryValidator:
    """Validates a Genesis repository layout."""

    def validate(self, root: str | Path) -> dict:
        root = Path(root)

        missing_files = [
            f for f in REQUIRED_FILES
            if not (root / f).exists()
        ]

        missing_dirs = [
            d for d in REQUIRED_DIRS
            if not (root / d).is_dir()
        ]

        return {
            "valid": not missing_files and not missing_dirs,
            "missing_files": missing_files,
            "missing_directories": missing_dirs,
        }
