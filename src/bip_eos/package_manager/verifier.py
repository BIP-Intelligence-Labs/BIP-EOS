"""
verifier.py

UEOS Atlas
Package Verifier

Verifies package manifests and cached package artifacts.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

from .manifest import ManifestLoader, ManifestError


@dataclass(slots=True)
class VerificationResult:
    success: bool
    message: str
    checksum: str = ""


class PackageVerifier:
    """Performs integrity verification for UEOS packages."""

    def __init__(self) -> None:
        self.loader = ManifestLoader()

    def verify_manifest(self, manifest_path: str | Path) -> VerificationResult:
        try:
            manifest = self.loader.load(manifest_path)
        except ManifestError as exc:
            return VerificationResult(False, str(exc))

        return VerificationResult(
            True,
            f"Manifest '{manifest.identifier}' is valid.",
        )

    def verify_artifact(
        self,
        artifact_path: str | Path,
        expected_checksum: str,
    ) -> VerificationResult:
        artifact_path = Path(artifact_path)

        if not artifact_path.exists():
            return VerificationResult(False, "Artifact not found.")

        digest = hashlib.sha256(artifact_path.read_bytes()).hexdigest()

        if digest != expected_checksum:
            return VerificationResult(
                False,
                "Checksum verification failed.",
                checksum=digest,
            )

        return VerificationResult(
            True,
            "Checksum verification passed.",
            checksum=digest,
        )

    def verify_package(
        self,
        manifest_path: str | Path,
        artifact_path: str | Path,
        expected_checksum: str,
    ) -> VerificationResult:
        manifest = self.verify_manifest(manifest_path)
        if not manifest.success:
            return manifest

        return self.verify_artifact(
            artifact_path,
            expected_checksum,
        )
