"""
bootstrap_metrics_ast.py

Engineering metrics using Python's AST.

Run:
    python bootstrap_metrics_ast.py
"""

from pathlib import Path
import ast

ROOT = Path(".")

py_files = list(ROOT.rglob("*.py"))
md_files = list(ROOT.rglob("*.md"))
test_files = list(ROOT.rglob("test_*.py"))

modules = len(py_files)
classes = methods = functions = dataclasses = async_functions = imports = 0

for file in py_files:
    try:
        tree = ast.parse(file.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        continue

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes += 1
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    methods += 1
                elif isinstance(item, ast.AsyncFunctionDef):
                    methods += 1
                    async_functions += 1

            if any(
                isinstance(d, ast.Name) and d.id == "dataclass"
                or isinstance(d, ast.Call)
                and isinstance(d.func, ast.Name)
                and d.func.id == "dataclass"
                for d in node.decorator_list
            ):
                dataclasses += 1

        elif isinstance(node, ast.FunctionDef):
            if not any(isinstance(p, ast.ClassDef) for p in ast.walk(tree) if node in getattr(p, "body", [])):
                functions += 1

        elif isinstance(node, ast.AsyncFunctionDef):
            async_functions += 1

        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            imports += 1

duplicates = list(ROOT.rglob("* (1).py"))
backups = list(ROOT.rglob("*.py.bak"))

score = 100
score -= len(duplicates) * 5
score -= len(backups) * 2
score = max(score, 0)

print("=" * 64)
print(" Bootstrap Engineering Metrics (AST)")
print("=" * 64)
print(f"\nModules................. {modules}")
print(f"Python Files............ {len(py_files)}")
print(f"Markdown Files.......... {len(md_files)}")
print(f"Test Files.............. {len(test_files)}")

print("\nCode Statistics")
print(f"Classes................. {classes}")
print(f"Methods................. {methods}")
print(f"Functions............... {functions}")
print(f"Dataclasses............. {dataclasses}")
print(f"Async Functions......... {async_functions}")
print(f"Import Statements....... {imports}")

print("\nRepository Health")
print(f"Duplicate Files......... {len(duplicates)}")
print(f"Backup Files............ {len(backups)}")

print("\nEngineering Score")
print(f"Score................... {score}/100")
print("Status.................. 🚀 ALL SYSTEMS GO" if score == 100 else "Status.................. ⚠ Review Recommended")
print("=" * 64)
