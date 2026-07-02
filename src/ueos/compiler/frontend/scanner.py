from pathlib import Path
from .source_file import SourceFile

class Scanner:
    DEFAULT_EXTENSIONS = {'.md','.yaml','.yml','.json','.bip','.adr'}

    def scan(self, root: Path):
        root = Path(root)
        for path in root.rglob('*'):
            if path.is_file() and path.suffix.lower() in self.DEFAULT_EXTENSIONS:
                yield SourceFile(
                    path=path,
                    text=path.read_text(encoding='utf-8', errors='replace')
                )
