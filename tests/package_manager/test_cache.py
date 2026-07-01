"""
test_cache.py

UEOS Atlas
Package Cache Tests
"""

from __future__ import annotations

from bip_eos.package_manager.cache import PackageCache


def test_store_package(tmp_path):
    cache = PackageCache(tmp_path)

    entry = cache.store(
        package="compiler",
        version="1.0.0",
        artifact=b"compiler-binary",
    )

    assert entry.package == "compiler"
    assert entry.version == "1.0.0"
    assert entry.location.exists()
    assert len(entry.checksum) == 64
    assert cache.exists("compiler", "1.0.0")


def test_remove_package(tmp_path):
    cache = PackageCache(tmp_path)

    cache.store(
        package="runtime",
        version="1.0.0",
        artifact=b"runtime-binary",
    )

    assert cache.remove("runtime", "1.0.0")
    assert not cache.exists("runtime", "1.0.0")


def test_remove_missing_package(tmp_path):
    cache = PackageCache(tmp_path)

    assert cache.remove("missing", "1.0.0") is False


def test_clear_cache(tmp_path):
    cache = PackageCache(tmp_path)

    cache.store("compiler", "1.0.0", b"a")
    cache.store("runtime", "1.0.0", b"b")

    cache.clear()

    assert not any(tmp_path.iterdir())
