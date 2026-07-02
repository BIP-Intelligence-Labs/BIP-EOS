from pathlib import Path

def iter_python(root:Path):
    yield from root.rglob('*.py')
