#!/usr/bin/env python3
from pathlib import Path

ROOT = Path.cwd()

FILES = {
"src/bip_eos/shared/__init__.py": '\"\"\"Shared utilities for BIP EOS.\"\"\"\n',
"src/bip_eos/shared/exceptions.py": 'class BIPEOSError(Exception):\n    pass\n',
"src/bip_eos/shared/types.py": 'from typing import Any, Dict\nJSON = Dict[str, Any]\n',
"src/bip_eos/shared/enums.py": 'from enum import Enum\nclass Environment(str, Enum):\n    DEVELOPMENT=\"development\"\n    TEST=\"test\"\n    PRODUCTION=\"production\"\n',
"src/bip_eos/shared/responses.py": 'from dataclasses import dataclass\nfrom typing import Any\n@dataclass\nclass Result:\n    success: bool\n    message: str = \"\"\n    data: Any = None\n',
"src/bip_eos/shared/validators.py": 'from pathlib import Path\ndef ensure_directory(path: Path):\n    path.mkdir(parents=True, exist_ok=True)\n    return path\n',
}

print("="*70)
print("BIP EOS Shared Package Bootstrap")
print("="*70)

created=0
skipped=0
for rel, data in FILES.items():
    p=ROOT/rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"[SKIP] {p}")
        skipped+=1
    else:
        p.write_text(data, encoding="utf-8")
        print(f"[FILE] {p}")
        created+=1

print("-"*70)
print(f"Created : {created}")
print(f"Skipped : {skipped}")
print("Shared package ready.")
