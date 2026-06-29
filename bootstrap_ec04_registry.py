"""
======================================================================
BIP Engineering Labs
Engineering Compiler
EC-04 — Engineering Registry Bootstrap
======================================================================
"""

from pathlib import Path

ROOT = Path.cwd()
COMPILER = ROOT / "bootstrap" / "compiler"
REGISTRY = COMPILER / "registry"

FILES = {
    "__init__.py": "\"\"Engineering Registry Package.\"\"\n",
    "registry.py": "class EngineeringRegistry:\n    def __init__(self):\n        self.documents = {}\n",
    "index.py": "class Index:\n    pass\n",
    "lookup.py": "class Lookup:\n    pass\n",
    "metadata.py": "class Metadata:\n    pass\n",
    "statistics.py": "class Statistics:\n    pass\n",
    "cache.py": "class Cache:\n    pass\n",
}

ENGINE = "\"\"Engineering Registry Engine.\"\"\n\nfrom registry.registry import EngineeringRegistry\n\nclass RegistryEngine:\n\n    def build(self, repository):\n        registry = EngineeringRegistry()\n        for document in repository.documents:\n            registry.documents[str(document.relative_path)] = document\n        return registry\n"

print("=" * 70)
print("Engineering Compiler Phase EC-04")
print("=" * 70)

REGISTRY.mkdir(parents=True, exist_ok=True)

created = 0
skipped = 0

for name, text in FILES.items():
    path = REGISTRY / name
    if path.exists():
        print(f"[SKIP] {path}")
        skipped += 1
    else:
        path.write_text(text, encoding="utf-8")
        print(f"[FILE] {path}")
        created += 1

engine = COMPILER / "registry_engine.py"
if engine.exists():
    print(f"[SKIP] {engine}")
    skipped += 1
else:
    engine.write_text(ENGINE, encoding="utf-8")
    print(f"[FILE] {engine}")
    created += 1

print("-" * 70)
print(f"Created : {created}")
print(f"Skipped : {skipped}")
print("Engineering Registry Ready")
print("Next Sprint: EC-05 Engineering Parser")
