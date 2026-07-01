"""
test_verifier.py

UEOS Atlas
Package Verifier Tests
"""

from __future__ import annotations

import hashlib
import json

from bip_eos.package_manager.verifier import PackageVerifier


def test_verify_manifest_success(tmp_path):
    manifest = tmp_path / "package.json"

    manifest.write_text(
        json.dumps(
            {
                "name": "compiler",
                "version": "1.0.0",
                "description": "UEOS Compiler",
            }
        ),
        encoding="utf-8",
    )

    result = PackageVerifier().verify_manifest(manifest)

    assert result.success
    assert "valid" in result.message.lower()


def test_verify_manifest_failure(tmp_path):
    manifest = tmp_path / "invalid.json"

    manifest.write_text(
        json.dumps({"version": "1.0.0"}),
        encoding="utf-8",
    )

    result = PackageVerifier().verify_manifest(manifest)

    assert not result.success


def test_verify_artifact_success(tmp_path):
    artifact = tmp_path / "package.bin"

    data = b"ueos-package"
    artifact.write_bytes(data)

    checksum = hashlib.sha256(data).hexdigest()

    result = PackageVerifier().verify_artifact(
        artifact,
        checksum,
    )

    assert result.success
    assert result.checksum == checksum


def test_verify_artifact_failure(tmp_path):
    artifact = tmp_path / "package.bin"
    artifact.write_bytes(b"invalid")

    result = PackageVerifier().verify_artifact(
        artifact,
        "0" * 64,
    )

    assert not result.success
    assert result.checksum != "0" * 64
