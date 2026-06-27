"""Repository Manifest support for Genesis EEOS."""

from dataclasses import dataclass
from pathlib import Path
import tomllib


@dataclass(slots=True)
class RepositoryManifest:
    name: str
    version: str
    package: str


class ManifestLoader:
    """Loads repository manifest information."""

    def load(self, root: str | Path) -> RepositoryManifest:
        root = Path(root)

        genesis = tomllib.loads((root / "genesis.toml").read_text(encoding="utf-8"))
        package = tomllib.loads((root / "package.toml").read_text(encoding="utf-8"))

        return RepositoryManifest(
            name=genesis.get("name", "Genesis"),
            version=genesis.get("version", "0.0.0"),
            package=package.get("name", "genesis"),
        )
