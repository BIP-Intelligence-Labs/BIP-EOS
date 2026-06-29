#!/usr/bin/env python3
"""
logger.py

BIP EOS Logging Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import logging


@dataclass
class LogConfig:
    level: int = logging.INFO
    filename: str = "bip_eos.log"


class LoggerEngine:
    def __init__(self, root: Path | None = None, config: LogConfig | None = None):
        self.root = root or Path.cwd()
        self.config = config or LogConfig()

        log_dir = self.root / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        self.log_file = log_dir / self.config.filename

        logging.basicConfig(
            filename=self.log_file,
            level=self.config.level,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

        self.logger = logging.getLogger("bip_eos")

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def startup(self):
        self.info("BIP EOS started")

    def shutdown(self):
        self.info("BIP EOS stopped")

    def status(self):
        return {
            "log_file": str(self.log_file),
            "exists": self.log_file.exists(),
            "timestamp": datetime.utcnow().isoformat(),
        }


def main():
    engine = LoggerEngine()
    engine.startup()

    print("=" * 70)
    print("BIP EOS Logger Engine")
    print("=" * 70)
    print(engine.status())


if __name__ == "__main__":
    main()
