\
"""
consolidate_graph_framework.py

UEOS Atlas Architecture Consolidation
-------------------------------------

Consolidates generic graph infrastructure into src/bip_eos/graph
while preserving engineering-specific graph models.

Run:
    python tools/migrations/consolidate_graph_framework.py
"""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]

SRC = ROOT / "src" / "bip_eos"
GRAPH = SRC / "graph"
ENG = SRC / "engineering_graph"

MOVES = {
    ENG / "graph_engine.py": GRAPH / "kernel" / "graph.py",
    ENG / "node.py": GRAPH / "node" / "node.py",
    ENG / "edge.py": GRAPH / "edge" / "edge.py",
    ENG / "query_engine.py": GRAPH / "query" / "query_engine.py",
    ENG / "traversal.py": GRAPH / "traversal" / "traversal.py",
    ENG / "serializer.py": GRAPH / "serialization" / "serializer.py",
}

KEEP = [
    "engineering_graph.py",
    "repository_graph.py",
    "dependency_graph.py",
    "package_graph.py",
    "module_graph.py",
    "service_graph.py",
    "plugin_graph.py",
    "document_graph.py",
    "adr_graph.py",
    "test_graph.py",
]

def ensure_dirs():
    for dest in MOVES.values():
        dest.parent.mkdir(parents=True, exist_ok=True)
        (dest.parent / "__init__.py").touch(exist_ok=True)

def migrate():
    moved = skipped = 0
    print("=" * 72)
    print("UEOS GRAPH FRAMEWORK CONSOLIDATION")
    print("=" * 72)

    for src, dst in MOVES.items():
        if not src.exists():
            print(f"SKIP : {src.relative_to(ROOT)}")
            skipped += 1
            continue

        if dst.exists():
            print(f"EXISTS : {dst.relative_to(ROOT)}")
            skipped += 1
            continue

        shutil.move(str(src), str(dst))
        moved += 1
        print(f"MOVE : {src.relative_to(ROOT)}")
        print(f"     -> {dst.relative_to(ROOT)}")

    print("\nEngineering-specific modules retained:")
    for item in KEEP:
        print(f"  KEEP : engineering_graph/{item}")

    print("\nSummary")
    print(f"Moved   : {moved}")
    print(f"Skipped : {skipped}")

if __name__ == "__main__":
    ensure_dirs()
    migrate()
