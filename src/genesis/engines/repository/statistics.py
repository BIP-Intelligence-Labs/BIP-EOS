"""
Repository Statistics
Genesis EEOS
"""

from pathlib import Path


class RepositoryStatistics:
    """
    Collects basic repository statistics.
    """

    def collect(self, root: str | Path) -> dict:
        root = Path(root)

        engines = list((root / "src" / "genesis" / "engines").rglob("*.py"))
        core = list((root / "src" / "genesis" / "core").glob("*.py"))

        return {
            "engine_modules": len(engines),
            "core_modules": len(core),
            "repository_name": root.name,
            "repository_exists": root.exists(),
        }
