
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime

@dataclass
class BuildStats:
    directories_created:int=0
    files_created:int=0
    started:datetime=field(default_factory=datetime.now)

@dataclass
class BuildContext:
    root: Path
    stats: BuildStats = field(default_factory=BuildStats)

class FilesystemError(Exception):
    pass

class DirectoryBuilder:
    def __init__(self, context: BuildContext):
        self.context=context
    def create(self, relative_path:str)->Path:
        p=self.context.root/relative_path
        p.mkdir(parents=True, exist_ok=True)
        self.context.stats.directories_created+=1
        return p

class FileWriter:
    def __init__(self, context: BuildContext):
        self.context=context
    def write(self, relative_path:str, content:str="")->Path:
        p=self.context.root/relative_path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        self.context.stats.files_created+=1
        return p

class RepositoryBuilder:
    def __init__(self, root:Path):
        self.context=BuildContext(root)
