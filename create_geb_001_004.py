
"""
VER-001
create_geb_001_004.py

Installs the Genesis Version Manager.

Run from the Genesis repository root:

    python create_geb_001_004.py
"""

from pathlib import Path

TARGET = Path("src/genesis/core/version.py")

CONTENT = """\
\"\"\"Genesis EEOS Version Manager.\"\"\"

from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def tag(self) -> str:
        return f"v{self}"


CURRENT_VERSION = Version(0, 1, 0)

VERSION = str(CURRENT_VERSION)
VERSION_TAG = CURRENT_VERSION.tag
"""

backup = TARGET.with_suffix(".py.bak")
if TARGET.exists():
    backup.write_text(TARGET.read_text(encoding="utf-8"), encoding="utf-8")

TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(CONTENT, encoding="utf-8")

print("Genesis Version Manager installed.")
print(f"Backup : {backup if backup.exists() else 'None'}")
print(f"Updated: {TARGET}")
