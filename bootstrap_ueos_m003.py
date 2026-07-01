#!/usr/bin/env python3
from pathlib import Path
ROOT=Path("src")/"bip_eos"/"cli"
ROOT.mkdir(parents=True,exist_ok=True)
mods={
"__init__.py":"\"\\"UEOS CLI package.\"\\"\n",
"install.py":"def handle(command,args=None):\n    print(f'[INSTALL] {command} {args or []}')\n",
"audit.py":"from bip_eos.audit.engine import AuditEngine\n\ndef handle(command,args=None):\n    if command=='discover':\n        AuditEngine('.').discover()\n    else:\n        print(f'Unknown audit command: {command}')\n",
"registry.py":"def handle(command,args=None):\n    print(f'[REGISTRY] {command}')\n",
"graph.py":"def handle(command,args=None):\n    print(f'[GRAPH] {command}')\n",
"compiler.py":"def handle(command,args=None):\n    print(f'[COMPILER] {command}')\n",
"publish.py":"def handle(command,args=None):\n    print(f'[PUBLISH] {command}')\n",
"academy.py":"def handle(command,args=None):\n    print(f'[ACADEMY] {command}')\n",
"runtime.py":"def handle(command,args=None):\n    print(f'[RUNTIME] {command}')\n",
}
for n,c in mods.items():
 p=ROOT/n
 p.write_text(c,encoding="utf-8") if not p.exists() else None
 print(f"[CREATE ] {p}" if not p.exists() else f"[EXISTS ] {p}")
ueos=ROOT/"ueos.py"
if ueos.exists():
 bak=ROOT/"ueos.py.m002.bak"
 if not bak.exists(): bak.write_text(ueos.read_text(),encoding="utf-8")
router="""from __future__ import annotations
import sys
from bip_eos.cli import install,audit,registry,graph,compiler,publish,academy,runtime
ROUTES={"install":install.handle,"inst":install.handle,"audit":audit.handle,"registry":registry.handle,"graph":graph.handle,"compiler":compiler.handle,"publish":publish.handle,"academy":academy.handle,"runtime":runtime.handle}
def main():
 a=sys.argv[1:]
 if not a: print("Usage: ueos <system> <command>"); return
 h=ROUTES.get(a[0].lower())
 if not h: print("Unknown system"); return
 h(a[1].lower() if len(a)>1 else None,a[2:])
if __name__=="__main__": main()
"""
ueos.write_text(router,encoding="utf-8")
print("[UPDATE ]",ueos)
print("UEOS M-003 bootstrap complete.")