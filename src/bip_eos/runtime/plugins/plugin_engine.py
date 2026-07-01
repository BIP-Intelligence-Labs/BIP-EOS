#!/usr/bin/env python3
"""
plugin_engine.py

BIP EOS Plugin Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import importlib.util


@dataclass
class PluginInfo:
    name: str
    path: str
    loaded: bool = False


class PluginEngine:
    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()
        self.plugin_dir = self.root / "src" / "bip_eos" / "plugins"
        self.plugins: dict[str, PluginInfo] = {}

    def discover(self):
        self.plugins.clear()
        if not self.plugin_dir.exists():
            return self.plugins

        for d in sorted(self.plugin_dir.iterdir()):
            if d.is_dir():
                self.plugins[d.name] = PluginInfo(
                    name=d.name,
                    path=str(d)
                )
        return self.plugins

    def load(self):
        for info in self.plugins.values():
            plugin_file = Path(info.path) / "plugin.py"
            if not plugin_file.exists():
                continue

            spec = importlib.util.spec_from_file_location(info.name, plugin_file)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                info.loaded = True

        return self.plugins

    def status(self):
        return {
            "plugin_directory": str(self.plugin_dir),
            "discovered": len(self.plugins),
            "loaded": sum(1 for p in self.plugins.values() if p.loaded),
        }


def main():
    engine = PluginEngine()
    engine.discover()
    engine.load()

    print("=" * 70)
    print("BIP EOS Plugin Engine")
    print("=" * 70)

    status = engine.status()
    print(f"Plugin Directory : {status['plugin_directory']}")
    print(f"Discovered       : {status['discovered']}")
    print(f"Loaded           : {status['loaded']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
