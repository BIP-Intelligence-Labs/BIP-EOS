"""
test_manifest.py

UEOS Atlas
Package Manager Tests
"""

from __future__ import annotations

import json

from ueos.package_manager.manifest import (
    ManifestLoader,
    ManifestError,
    PackageManifest,
    ManifestWriter,
)


def test_load_manifest(tmp_path):
    manifest_file = tmp_path / "package.json"

    manifest_file.write_text(
        json.dumps(
            {
                "name": "compiler",
                "version": "1.0.0",
                "description": "UEOS Compiler",
                "dependencies": {
                    "runtime": ">=1.0.0"
                },
            }
        ),
        encoding="utf-8",
    )

    manifest = ManifestLoader().load(manifest_file)

    assert manifest.name == "compiler"
    assert manifest.version == "1.0.0"
    assert manifest.dependencies["runtime"] == ">=1.0.0"


def test_save_manifest(tmp_path):
    manifest = PackageManifest(
        name="runtime",
        version="1.0.0",
        description="UEOS Runtime",
    )

    output = tmp_path / "runtime.json"

    ManifestWriter().save(manifest, output)

    assert output.exists()

    loaded = ManifestLoader().load(output)

    assert loaded.identifier == "runtime@1.0.0"


def test_missing_required_field(tmp_path):
    manifest_file = tmp_path / "invalid.json"

    manifest_file.write_text(
        json.dumps({"version": "1.0.0"}),
        encoding="utf-8",
    )

    try:
        ManifestLoader().load(manifest_file)
    except ManifestError:
        return

    raise AssertionError("ManifestError was not raised")
