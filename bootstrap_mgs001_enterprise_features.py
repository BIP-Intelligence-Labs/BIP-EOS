#!/usr/bin/env python3
"""
MGS-001 Enterprise Migration Executor Features

Additions:
- Conflict detection
- SHA-256 file hashing
- Import validation
- Dry-run statistics
- Persistent rollback manifest
- Transaction execution
"""

from __future__ import annotations
from pathlib import Path
import hashlib, json, ast, shutil
from dataclasses import dataclass

@dataclass(slots=True)
class MigrationTask:
    source: Path
    destination: Path

class ConflictDetector:
    @staticmethod
    def has_conflict(src: Path, dst: Path) -> bool:
        if not dst.exists():
            return False
        if src.is_dir() != dst.is_dir():
            return True
        if src.is_file():
            return FileHasher.sha256(src) != FileHasher.sha256(dst)
        return False

class FileHasher:
    @staticmethod
    def sha256(path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            while chunk := f.read(65536):
                h.update(chunk)
        return h.hexdigest()

class ImportValidator:
    @staticmethod
    def validate(root: Path):
        errors=[]
        for py in root.rglob("*.py"):
            try:
                ast.parse(py.read_text(encoding="utf-8"), filename=str(py))
            except SyntaxError as e:
                errors.append(f"{py}: {e}")
        return len(errors)==0, errors

class DryRunReporter:
    @staticmethod
    def report(tasks):
        files=dirs=0
        for t in tasks:
            if t.source.is_dir():
                dirs+=1
            else:
                files+=1
        return {
            "tasks":len(tasks),
            "directories":dirs,
            "files":files,
            "mode":"DRY RUN"
        }

class RollbackManifest:
    def __init__(self, path:Path):
        self.path=path
    def save(self, entries):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(entries,indent=4),encoding="utf-8")
    def load(self):
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text())

class TransactionExecutor:
    def __init__(self):
        self.completed=[]
    def execute(self,tasks,root:Path):
        for task in tasks:
            src=root/task.source
            dst=root/task.destination
            if ConflictDetector.has_conflict(src,dst):
                raise RuntimeError(f"Conflict detected: {dst}")
            dst.parent.mkdir(parents=True,exist_ok=True)
            if src.is_dir():
                shutil.copytree(src,dst,dirs_exist_ok=True)
            else:
                shutil.copy2(src,dst)
            self.completed.append({"source":str(src),"destination":str(dst)})
        return self.completed

if __name__=="__main__":
    print("MGS-001 Enterprise Features Ready")
