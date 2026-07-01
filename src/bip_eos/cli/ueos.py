# UEOS CLI router (updated)
# Rename this file to ueos.py after downloading.

from __future__ import annotations
import sys

from bip_eos.cli import (
    install,
    audit,
    registry,
    graph,
    compiler,
    publish,
    academy,
    runtime,
    migration,
)

VERSION="0.1.0"
CODENAME="Genesis"

def help_command():
    print("="*72)
    print("UEOS")
    print("Universal Engineering Operating System")
    print("="*72)
    print("Usage")
    print("    ueos <system> <command> [arguments]")
    print()
    print("Systems")
    for s in ("install","audit","registry","graph","compiler","publish","academy","runtime","migration"):
        print(f"    {s}")
    print()
    print("Examples")
    print("    ueos install audit")
    print("    ueos audit discover")
    print("    ueos migrate plan")
    print("    ueos migrate validate")
    print("    ueos migrate execute")
    print("    ueos version")

def version():
    print(f"UEOS {VERSION} ({CODENAME})")

ROUTES={
    "install":install.handle,"inst":install.handle,
    "audit":audit.handle,
    "registry":registry.handle,"reg":registry.handle,
    "graph":graph.handle,
    "compiler":compiler.handle,"compile":compiler.handle,
    "publish":publish.handle,
    "academy":academy.handle,
    "runtime":runtime.handle,
    "migration":migration.handle,"migrate":migration.handle,
}

def route(system, command, args):
    system=system.lower()
    if system in ("help","--help","-h"):
        help_command(); return
    if system in ("version","--version","-v"):
        version(); return
    handler=ROUTES.get(system)
    if handler is None:
        print(f"Unknown system: {system}")
        return
    handler(command,args)

def main():
    argv=sys.argv[1:]
    if not argv:
        help_command(); return
    route(argv[0], argv[1] if len(argv)>1 else None, argv[2:])

if __name__=="__main__":
    main()
