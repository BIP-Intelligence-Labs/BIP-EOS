"""
test_end_to_end.py

UEOS Atlas
End-to-End Package Manager Tests

Exercises the complete package management workflow.
"""

from __future__ import annotations

import hashlib
import json

from bip_eos.package_manager.cache import PackageCache
from bip_eos.package_manager.service import (
    PackageManagerConfig,
    PackageManagerService,
)
from bip_eos.package_manager.verifier import PackageVerifier


def test_end_to_end_package_workflow(tmp_path):
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

    service = PackageManagerService(
        PackageManagerConfig(
            registry_path=tmp_path / "registry",
            cache_path=tmp_path / "cache",
            install_path=tmp_path / "packages",
        )
    )

    install_result = service.install(manifest)

    assert install_result.success
    assert install_result.package is not None

    verifier = PackageVerifier()

    manifest_result = verifier.verify_manifest(manifest)

    assert manifest_result.success

    cache = PackageCache(tmp_path / "cache")

    artifact = b"compiler-package"

    entry = cache.store(
        package="compiler",
        version="1.0.0",
        artifact=artifact,
    )

    checksum_result = verifier.verify_artifact(
        entry.location,
        hashlib.sha256(artifact).hexdigest(),
    )

    assert checksum_result.success
    assert cache.exists("compiler", "1.0.0")

    installed = service.list_installed()

    assert "compiler" in installed

    uninstall_result = service.uninstall("compiler")

    # Current service implementation marks removal but does not
    # delete package files yet.
    assert uninstall_result.success
