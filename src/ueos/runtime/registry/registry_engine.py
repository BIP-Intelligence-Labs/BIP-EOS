#!/usr/bin/env python3
"""
registry_engine.py

BIP EOS Registry Engine
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import json


@dataclass
class Registry:
    plugins: list[str] = field(default_factory=list)
    commands: list[str] = field(default_factory=list)
    engines: list[str] = field(default_factory=list)


class RegistryEngine:
    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()
        self.registry_dir = self.root / "registry"
        self.registry_file = self.registry_dir / "registry.json"
        self.registry_dir.mkdir(parents=True, exist_ok=True)

    def discover_plugins(self):
        plugins = self.root / "plugins"
        if plugins.exists():
            return sorted([p.name for p in plugins.iterdir() if p.is_dir()])
        return []

    def discover_commands(self):
        cmds = self.root / "src" / "ueos" / "cli" / "commands"
        if cmds.exists():
            return sorted(
                p.stem for p in cmds.glob("*.py") if p.name != "__init__.py"
            )
        return []

    def discover_engines(self):
        core = self.root / "src" / "ueos" / "core"
        engines = []
        if core.exists():
            for f in core.rglob("*_engine.py"):
                engines.append(str(f.relative_to(core)))
        return sorted(engines)

    def build(self):
        data = {
            "generated": datetime.utcnow().isoformat(),
            "plugins": self.discover_plugins(),
            "commands": self.discover_commands(),
            "engines": self.discover_engines(),
        }
        self.registry_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return data


def main():
    engine = RegistryEngine()
    data = engine.build()
    print("=" * 70)
    print("BIP EOS Registry Engine")
    print("=" * 70)
    print(f"Plugins : {len(data['plugins'])}")
    print(f"Commands: {len(data['commands'])}")
    print(f"Engines : {len(data['engines'])}")
    print(f"Registry: {engine.registry_file}")


if __name__ == "__main__":
    main()
