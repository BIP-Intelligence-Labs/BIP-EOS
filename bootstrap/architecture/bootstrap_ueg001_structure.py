#!/usr/bin/env python3
"""
UEOS Bootstrap
UEG-001 - Unified Engineering Graph Structure

Creates the initial runtime package structure for the
Unified Engineering Graph (UEG).

Safe:
- Creates only missing directories
- Creates __init__.py only if missing
- Does not overwrite existing files
"""

from pathlib import Path

PACKAGE = [
    "src/bip_eos/graph",
    "src/bip_eos/graph/kernel",
    "src/bip_eos/graph/node",
    "src/bip_eos/graph/edge",
    "src/bip_eos/graph/property",
    "src/bip_eos/graph/traversal",
    "src/bip_eos/graph/query",
    "src/bip_eos/graph/projection",
    "src/bip_eos/graph/validation",
    "src/bip_eos/graph/serialization",
    "src/bip_eos/graph/persistence",
]

README = """# Unified Engineering Graph (UEG)

The Unified Engineering Graph is the canonical runtime representation
of the Engineering Model.

Constitutional Principle:

Reality
→ Evidence
→ Engineering Truth
→ Unified Engineering Graph
→ Engineering Views

Subpackages:

- kernel          Graph runtime kernel
- node            Node model
- edge            Relationship model
- property        Property system
- traversal       Graph traversal
- query           Query engine
- projection      View/projection engine
- validation      Graph validation
- serialization   Import/export
- persistence     Storage abstraction
"""

def find_root(start: Path) -> Path:
    cur = start.resolve()
    while cur != cur.parent:
        if (cur/"src").exists() and (cur/"bootstrap").exists():
            return cur
        cur = cur.parent
    raise RuntimeError("UEOS repository not found.")

def touch_init(path: Path):
    init = path/"__init__.py"
    if not init.exists():
        init.write_text('"""UEG Package"""\n', encoding="utf-8")

def main():
    root = find_root(Path(__file__).parent)
    print("="*72)
    print("UEG-001 Bootstrap")
    print("="*72)

    for rel in PACKAGE:
        d = root/rel
        if d.exists():
            print(f"[EXISTS ] {rel}")
        else:
            d.mkdir(parents=True, exist_ok=True)
            print(f"[CREATE ] {rel}")
        touch_init(d)

    readme = root/"src/bip_eos/graph/README.md"
    if not readme.exists():
        readme.write_text(README, encoding="utf-8")
        print("[CREATE ] src/bip_eos/graph/README.md")
    else:
        print("[EXISTS ] src/bip_eos/graph/README.md")

    print("="*72)
    print("Unified Engineering Graph structure initialized.")
    print("No existing files were overwritten.")
    print("="*72)

if __name__ == "__main__":
    main()
