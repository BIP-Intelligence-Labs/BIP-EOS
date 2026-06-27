
"""
REP-006
create_geb_001_008.py

Installs the Repository Manifest module.

Run from the Genesis repository root:

    python create_geb_001_008.py
"""

from pathlib import Path

TARGET = Path("src/genesis/engines/repository/manifest.py")

CONTENT = """\
\"\"\"Repository Manifest support for Genesis EEOS.\"\"\"

from dataclasses import dataclass
from pathlib import Path
import tomllib


@dataclass(slots=True)
class RepositoryManifest:
    name: str
    version: str
    package: str


class ManifestLoader:
    \"\"\"Loads repository manifest information.\"\"\"

    def load(self, root: str | Path) -> RepositoryManifest:
        root = Path(root)

        genesis = tomllib.loads((root / "genesis.toml").read_text(encoding="utf-8"))
        package = tomllib.loads((root / "package.toml").read_text(encoding="utf-8"))

        return RepositoryManifest(
            name=genesis.get("name", "Genesis"),
            version=genesis.get("version", "0.0.0"),
            package=package.get("name", "genesis"),
        )
"""

TARGET.parent.mkdir(parents=True, exist_ok=True)

backup = TARGET.with_suffix(".py.bak")
if TARGET.exists():
    backup.write_text(TARGET.read_text(encoding="utf-8"), encoding="utf-8")

TARGET.write_text(CONTENT, encoding="utf-8")

print("Repository Manifest module installed.")
print(f"Backup : {backup if backup.exists() else 'None'}")
print(f"Updated: {TARGET}")
