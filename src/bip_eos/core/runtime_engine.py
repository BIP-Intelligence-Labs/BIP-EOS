#!/usr/bin/env python3
"""
runtime_engine.py

BIP EOS Runtime Engine

Coordinates the core engines and provides a single
startup/shutdown interface for the platform.
"""

from __future__ import annotations

from pathlib import Path

from bip_eos.core.repository.repository_engine import RepositoryEngine
from bip_eos.core.registry.registry_engine import RegistryEngine
from bip_eos.core.logging.logger import LoggerEngine
from bip_eos.core.version.version_engine import VersionEngine
from bip_eos.core.documentation.documentation_engine import DocumentationEngine
from bip_eos.core.plugins.plugin_engine import PluginEngine


class RuntimeEngine:
    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()

        self.logger = LoggerEngine(self.root)
        self.repository = RepositoryEngine(self.root)
        self.registry = RegistryEngine(self.root)
        self.version = VersionEngine(self.root)
        self.documentation = DocumentationEngine(self.root)
        self.plugins = PluginEngine(self.root)

    def startup(self):
        self.logger.startup()
        self.plugins.discover()
        self.plugins.load()
        self.registry.build()

        return {
            "repository": self.repository.summary(),
            "registry": self.registry.build(),
            "version": self.version.status(),
            "plugins": self.plugins.status(),
            "documentation": self.documentation.status(),
            "logger": self.logger.status(),
        }

    def shutdown(self):
        self.logger.shutdown()

    def doctor(self):
        return {
            "repository": self.repository.doctor(),
            "registry": self.registry.build(),
            "version": self.version.status(),
            "plugins": self.plugins.status(),
            "documentation": self.documentation.status(),
            "logger": self.logger.status(),
        }


def main():
    engine = RuntimeEngine()

    print("=" * 70)
    print("BIP EOS Runtime Engine")
    print("=" * 70)

    status = engine.startup()

    for name in status:
        print(f"[ OK ] {name}")

    print("=" * 70)


if __name__ == "__main__":
    main()
