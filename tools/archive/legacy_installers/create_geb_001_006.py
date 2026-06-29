
"""
REP-004
create_geb_001_006.py

Installs the BIP EOS Repository Models.

Run from the Genesis repository root:

    python create_geb_001_006.py
"""

from pathlib import Path

TARGET = Path("src/genesis/engines/repository/models.py")

CONTENT = """\
\"\"\"Repository domain models for Genesis EEOS.\"\"\"

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Repository:
    name: str
    path: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    initialized: bool = False
    version: str = "0.1.0"

    def initialize(self) -> None:
        self.initialized = True


@dataclass(slots=True)
class RepositoryManifest:
    repository: str
    engine_version: str
    created_at: datetime = field(default_factory=datetime.utcnow)
"""

TARGET.parent.mkdir(parents=True, exist_ok=True)

backup = TARGET.with_suffix(".py.bak")
if TARGET.exists():
    backup.write_text(TARGET.read_text(encoding="utf-8"), encoding="utf-8")

TARGET.write_text(CONTENT, encoding="utf-8")

print("Repository Models installed.")
print(f"Backup : {backup if backup.exists() else 'None'}")
print(f"Updated: {TARGET}")
