"""
manifest.py

UEOS Atlas
Package Manifest

Responsible for loading, validating, and writing UEOS package manifests.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


class ManifestError(Exception):
    """Raised when a package manifest is invalid."""


@dataclass(slots=True)
class PackageManifest:
    """Represents a UEOS package manifest."""

    name: str
    version: str
    description: str = ""
    author: str = ""
    license: str = ""
    homepage: str = ""
    repository: str = ""
    dependencies: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def identifier(self) -> str:
        return f"{self.name}@{self.version}"


class ManifestLoader:
    REQUIRED_FIELDS = ("name", "version")

    def load(self, manifest_path: str | Path) -> PackageManifest:
        manifest_path = Path(manifest_path)

        if not manifest_path.exists():
            raise ManifestError(f"Manifest not found: {manifest_path}")

        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ManifestError(f"Invalid JSON: {exc}") from exc

        self.validate(data)

        return PackageManifest(
            name=data["name"],
            version=data["version"],
            description=data.get("description", ""),
            author=data.get("author", ""),
            license=data.get("license", ""),
            homepage=data.get("homepage", ""),
            repository=data.get("repository", ""),
            dependencies=data.get("dependencies", {}),
            metadata=data.get("metadata", {}),
        )

    def validate(self, manifest: dict[str, Any]) -> None:
        for field in self.REQUIRED_FIELDS:
            if field not in manifest:
                raise ManifestError(f"Missing required field: {field}")
            if not manifest[field]:
                raise ManifestError(f"Empty required field: {field}")

        if not isinstance(manifest.get("dependencies", {}), dict):
            raise ManifestError("dependencies must be an object")


class ManifestWriter:
    def save(self, manifest: PackageManifest, destination: str | Path) -> None:
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)

        payload = {
            "name": manifest.name,
            "version": manifest.version,
            "description": manifest.description,
            "author": manifest.author,
            "license": manifest.license,
            "homepage": manifest.homepage,
            "repository": manifest.repository,
            "dependencies": manifest.dependencies,
            "metadata": manifest.metadata,
        }

        destination.write_text(
            json.dumps(payload, indent=4),
            encoding="utf-8",
        )


def load_manifest(path: str | Path) -> PackageManifest:
    return ManifestLoader().load(path)


def save_manifest(manifest: PackageManifest, path: str | Path) -> None:
    ManifestWriter().save(manifest, path)
