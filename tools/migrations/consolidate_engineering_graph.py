\
"""
consolidate_engineering_graph.py

UEOS Repository Migration
-------------------------

Consolidates the Engineering Graph into the generic Graph framework.

Run:
    python tools/migrations/consolidate_engineering_graph.py

This script:
  • Creates the target graph directories
  • Moves generic graph components into src/bip_eos/graph/
  • Leaves engineering-specific graph classes in place
"""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]

SRC = ROOT / "src" / "bip_eos"
ENG = SRC / "engineering_graph"
GRAPH = SRC / "graph"

DIRECTORIES = [
    GRAPH / "kernel",
    GRAPH / "node",
    GRAPH / "edge",
    GRAPH / "query",
    GRAPH / "traversal",
    GRAPH / "serialization",
]

MOVES = {
    ENG / "graph_engine.py": GRAPH / "kernel" / "graph.py",
    ENG / "node.py": GRAPH / "node" / "node.py",
    ENG / "edge.py": GRAPH / "edge" / "edge.py",
    ENG / "query_engine.py": GRAPH / "query" / "query_engine.py",
    ENG / "traversal.py": GRAPH / "traversal" / "traversal.py",
    ENG / "serializer.py": GRAPH / "serialization" / "serializer.py",
}


def ensure_dirs():
    for d in DIRECTORIES:
        d.mkdir(parents=True, exist_ok=True)


def move_files():
    for src, dst in MOVES.items():
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            print(f"MOVED   : {src.relative_to(ROOT)}")
            print(f"       -> {dst.relative_to(ROOT)}")
        else:
            print(f"SKIPPED : {src.relative_to(ROOT)} (not found)")


def create_init_files():
    for directory in DIRECTORIES:
        init = directory / "__init__.py"
        init.touch(exist_ok=True)


def report():
    print("\nEngineering-specific modules retained:")
    keep = [
        "repository_graph.py",
        "dependency_graph.py",
        "graph_builder.py",
        "graph_loader.py",
        "graph_exporter.py",
        "graph_statistics.py",
    ]
    for item in keep:
        print(f"  KEEP : engineering_graph/{item}")


if __name__ == "__main__":
    print("=" * 68)
    print("UEOS GRAPH CONSOLIDATION")
    print("=" * 68)
    ensure_dirs()
    move_files()
    create_init_files()
    report()
    print("\nDone.")
