from dataclasses import dataclass
@dataclass
class MigrationResult:
    files_scanned:int=0
    files_modified:int=0
