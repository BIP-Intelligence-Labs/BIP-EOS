
"""
EXC-001
create_geb_001_005.py

Installs the Genesis Exception Framework.

Run from the Genesis repository root:

    python create_geb_001_005.py
"""

from pathlib import Path

TARGET = Path("src/genesis/core/exceptions.py")

CONTENT = """\
\"\"\"Genesis EEOS Exception Framework.\"\"\"

class GenesisError(Exception):
    \"\"\"Base exception for all Genesis errors.\"\"\"


class EngineError(GenesisError):
    \"\"\"Raised for engine-related failures.\"\"\"


class RepositoryError(EngineError):
    \"\"\"Raised for repository engine failures.\"\"\"


class ValidationError(GenesisError):
    \"\"\"Raised when validation fails.\"\"\"


class ConfigurationError(GenesisError):
    \"\"\"Raised for configuration errors.\"\"\"
"""

backup = TARGET.with_suffix(".py.bak")
if TARGET.exists():
    backup.write_text(TARGET.read_text(encoding="utf-8"), encoding="utf-8")

TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(CONTENT, encoding="utf-8")

print("Genesis Exception Framework installed.")
print(f"Backup : {backup if backup.exists() else 'None'}")
print(f"Updated: {TARGET}")
