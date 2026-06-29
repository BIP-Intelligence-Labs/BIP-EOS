#!/usr/bin/env python3
"""
config.py

BIP EOS Configuration Manager
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json


@dataclass
class Config:
    environment: str = "development"
    debug: bool = True
    log_level: str = "INFO"
    plugin_directory: str = "src/bip_eos/plugins"


class ConfigManager:
    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()
        self.file = self.root / "config.json"

    def load(self) -> Config:
        if self.file.exists():
            return Config(**json.loads(self.file.read_text(encoding="utf-8")))
        cfg = Config()
        self.save(cfg)
        return cfg

    def save(self, config: Config) -> None:
        self.file.write_text(
            json.dumps(asdict(config), indent=2),
            encoding="utf-8"
        )

    def status(self):
        return asdict(self.load())


if __name__ == "__main__":
    mgr = ConfigManager()
    print(json.dumps(mgr.status(), indent=2))
