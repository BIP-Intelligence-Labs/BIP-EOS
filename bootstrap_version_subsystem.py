"""
EOS Version Bootstrap
"""

from pathlib import Path

ROOT = Path.cwd()
BASE = ROOT / "src" / "bip_eos" / "core" / "version"
BASE.mkdir(parents=True, exist_ok=True)

FILES = {}

FILES['__init__.py'] = '"""EOS Version Subsystem"""\n\nfrom .version import EOS_VERSION\nfrom .version_engine import VersionEngine\n'
FILES['version.py'] = '"""Canonical EOS Version Information"""\n\nfrom dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass EOSVersion:\n    version: str = "0.1.0"\n    codename: str = "Genesis"\n    platform: str = "Engineering Operating System"\n    release: str = "Development"\n\nEOS_VERSION = EOSVersion()\n'
FILES['version_engine.py'] = '"""EOS Version Engine"""\n\nfrom .version import EOS_VERSION\n\nclass VersionEngine:\n    @staticmethod\n    def banner() -> str:\n        return ("="*60+"\\n"+f"{EOS_VERSION.platform}\\n"+"="*60+"\\n"+f"Version : {EOS_VERSION.version}\\n"+f"Codename: {EOS_VERSION.codename}\\n"+f"Release : {EOS_VERSION.release}\\n")\n'

print("="*70)
print("EOS Version Bootstrap")
print("="*70)
for name, content in FILES.items():
    path = BASE / name
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.write_text(content, encoding='utf-8')
        print(f"[FILE] {path}")