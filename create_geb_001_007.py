
"""
REP-005
create_geb_001_007.py

Installs the Repository Validation module.

Run from the Genesis repository root:

    python create_geb_001_007.py
"""

from pathlib import Path

TARGET = Path("src/genesis/engines/repository/validators.py")

CONTENT = """\
\"\"\"Repository validation for Genesis EEOS.\"\"\"

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
    \"\"\"Validates a Genesis repository layout.\"\"\"

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
"""

TARGET.parent.mkdir(parents=True, exist_ok=True)

backup = TARGET.with_suffix(".py.bak")
if TARGET.exists():
    backup.write_text(TARGET.read_text(encoding="utf-8"), encoding="utf-8")

TARGET.write_text(CONTENT, encoding="utf-8")

print("Repository Validation module installed.")
print(f"Backup : {backup if backup.exists() else 'None'}")
print(f"Updated: {TARGET}")
