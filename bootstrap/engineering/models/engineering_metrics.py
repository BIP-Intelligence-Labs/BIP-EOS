from dataclasses import dataclass

@dataclass
class EngineeringMetrics:
    python_files: int = 0
    markdown_files: int = 0
    test_files: int = 0
    classes: int = 0
    methods: int = 0
    functions: int = 0
    imports: int = 0
    dataclasses: int = 0
    duplicate_files: int = 0
    backup_files: int = 0
    engineering_score: int = 100
