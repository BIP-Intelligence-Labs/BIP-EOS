"""
finalize_toolchain_layout.py

Genesis EEOS Toolchain Finalizer
"""

from pathlib import Path
import shutil

ROOT = Path(".")

for d in [
    "tools/archive/legacy_installers",
    "tools/cleanup",
    "tools/generators",
    "tools/installers",
    "tools/managers",
    "tools/migrations",
]:
    Path(d).mkdir(parents=True, exist_ok=True)

moves = {
    "tools/generators/create_github_foundation.py":
        "tools/installers/create_github_foundation.py",
    "tools/generators/create_repository_cleanup.py":
        "tools/cleanup/create_repository_cleanup.py",
    "create_repository_engine_package.py":
        "tools/installers/create_repository_engine_package.py",
}

for src, dst in moves.items():
    s = Path(src)
    t = Path(dst)
    if s.exists():
        t.parent.mkdir(parents=True, exist_ok=True)
        if not t.exists():
            shutil.move(str(s), str(t))
            print(f"MOVED  {s} -> {t}")

stubs = {
    "tools/managers/manager.py": '"""Genesis Tool Manager"""\n\nprint("Genesis Tool Manager")\n',
    "tools/managers/engineering_manager.py": '"""Engineering Manager"""\n',
    "tools/managers/builder_manager.py": '"""Builder Manager"""\n',
    "tools/managers/release_manager.py": '"""Release Manager"""\n',
}

for filename, content in stubs.items():
    p = Path(filename)
    if not p.exists():
        p.write_text(content, encoding="utf-8")
        print(f"CREATE {p}")

print("\nDone.")
print("git status")
print("git add .")
print('git commit -m "refactor(repository): finalize engineering toolchain"')
