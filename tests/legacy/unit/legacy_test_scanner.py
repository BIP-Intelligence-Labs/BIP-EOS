from pathlib import Path
from ueos.compiler.frontend.scanner import Scanner

def test_scanner_discovers_files():
    scanner = Scanner()
    files = list(scanner.scan(Path('engineering')))
    assert isinstance(files, list)
