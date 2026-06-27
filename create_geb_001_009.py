"""
REP-007
create_geb_001_009.py

Installs the Repository Statistics module.

Run from the Genesis repository root:

    python create_geb_001_009.py
"""

from pathlib import Path

TARGET = Path("src/genesis/engines/repository/statistics.py")

CONTENT = '''"""
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
'''

TARGET.parent.mkdir(parents=True, exist_ok=True)

backup = TARGET.with_suffix(".py.bak")

if TARGET.exists():
    backup.write_text(
        TARGET.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

TARGET.write_text(CONTENT, encoding="utf-8")

print("Repository Statistics installed.")
print(f"Backup : {backup if backup.exists() else 'None'}")
print(f"Updated: {TARGET}")
