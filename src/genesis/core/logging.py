
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path

class LogLevel(Enum):
    DEBUG="DEBUG"
    INFO="INFO"
    WARNING="WARNING"
    ERROR="ERROR"

@dataclass
class LogRecord:
    level: LogLevel
    message: str
    timestamp: datetime = datetime.now()

class Logger:
    def log(self, level: LogLevel, message: str):
        print(f"[{level.value}] {datetime.now().isoformat()} - {message}")

class ConsoleLogger(Logger):
    pass

class FileLogger(Logger):
    def __init__(self, logfile: Path):
        self.logfile = logfile

    def log(self, level: LogLevel, message: str):
        line = f"[{level.value}] {datetime.now().isoformat()} - {message}\n"
        self.logfile.parent.mkdir(parents=True, exist_ok=True)
        with self.logfile.open("a", encoding="utf-8") as f:
            f.write(line)
        print(line, end="")

class BuildLogger(FileLogger):
    def __init__(self, root: Path):
        super().__init__(root / "logs" / "genesis.log")
