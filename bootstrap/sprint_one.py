#!/usr/bin/env python3
"""
BIP EOS - Sprint One Bootstrap
"""

from pathlib import Path
from datetime import datetime
import json

VERSION = "0.1.0"
CODENAME = "Genesis"
ROOT = Path(__file__).resolve().parent.parent

FOLDERS = [
    "bootstrap","bip","bip/core","bip/cli","bip/docs","bip/adr",
    "bip/plugins","bip/academy","bip/ai","bip/builders","bip/sales",
    "bip/reports","docs","docs/adr","docs/governance",
    "docs/architecture","docs/api","docs/engineering","logs",
    "plugins","plugins/academy","plugins/ai","plugins/builders",
    "plugins/sales","plugins/reports","registry","templates","tests"
]

FILES = {
    "README.md": "# BIP Engineering Operating System\n",
    "CHANGELOG.md": "# Changelog\n",
    "LICENSE": "MIT License\n",
    "docs/engineering/engineering-log.md": "# Engineering Log\n",
    "registry/registry.json": json.dumps({
        "version": VERSION,
        "codename": CODENAME,
        "plugins": [],
        "commands": []
    }, indent=4)
}

PLUGIN_TEMPLATE = """class Plugin:
    name = "{name}"

    def load(self):
        print("Loading {{}} plugin".format(self.name))
"""

MANIFEST_TEMPLATE = """name: {name}
version: 0.1.0
author: BIP EOS
"""

def main():
    print("="*60)
    print("BIP EOS Sprint One Bootstrap")
    print("="*60)

    for folder in FOLDERS:
        (ROOT / folder).mkdir(parents=True, exist_ok=True)

    for rel, content in FILES.items():
        p = ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists():
            p.write_text(content, encoding="utf-8")

    for plugin in ["academy","ai","builders","sales","reports"]:
        d = ROOT / "plugins" / plugin
        d.mkdir(parents=True, exist_ok=True)
        (d / "plugin.py").write_text(
            PLUGIN_TEMPLATE.format(name=plugin),
            encoding="utf-8"
        )
        (d / "manifest.yaml").write_text(
            MANIFEST_TEMPLATE.format(name=plugin),
            encoding="utf-8"
        )
        (d / "README.md").write_text(
            f"# {plugin.title()} Plugin\n",
            encoding="utf-8"
        )

    log = ROOT / "logs" / f"{datetime.now():%Y-%m-%d}.log"
    log.write_text(f"{datetime.now()}: Sprint One Bootstrap executed\n", encoding="utf-8")

    print("Sprint One bootstrap completed successfully.")

if __name__ == "__main__":
    main()
