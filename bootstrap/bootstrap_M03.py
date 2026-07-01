"""
bootstrap/bootstrap_M03.py

BIP EOS
Milestone 03 Bootstrap

Creates the Builder Intelligence Platform foundation.
"""

from pathlib import Path
import sys
import platform
import importlib

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "bip_eos"
ENGINEERING = ROOT / "engineering"
TESTS = ROOT / "tests" / "unit"

CREATED = 0
SKIPPED = 0
FAILED = 0


def directory(path: Path):
    global CREATED
    if path.exists():
        return
    path.mkdir(parents=True, exist_ok=True)
    CREATED += 1
    print(f"[DIR ] {path}")


def file(path: Path, content=""):
    global CREATED, SKIPPED
    if path.exists():
        SKIPPED += 1
        print(f"[SKIP] {path}")
        return
    path.write_text(content, encoding="utf-8")
    CREATED += 1
    print(f"[FILE] {path}")


def verify():
    print("=" * 70)
    print("BIP EOS M03 Bootstrap")
    print("=" * 70)

    checks = [
        ("Python", lambda: platform.python_version()),
        ("bip_eos", lambda: importlib.import_module("bip_eos")),
        ("config", lambda: importlib.import_module("bip_eos.config")),
        ("database", lambda: importlib.import_module("bip_eos.database")),
        ("builders", lambda: importlib.import_module("bip_eos.home_builders")),
    ]

    ok = True
    for name, fn in checks:
        try:
            fn()
            print(f"[ OK ] {name}")
        except Exception as ex:
            ok = False
            print(f"[FAIL] {name}")
            print(f"       {ex}")

    if not ok:
        print("Bootstrap aborted.")
        sys.exit(1)


def generate_database():
    print("\nGenerating Database")
    db = SRC / "database"
    directory(db)
    for f in [
        "__init__.py",
        "client.py",
        "manager.py",
        "session.py",
        "repository.py",
        "health.py",
    ]:
        file(db / f)


def generate_lead():
    print("\nGenerating Lead Domain")
    lead = SRC / "builders" / "lead"
    directory(lead)
    for f in [
        "__init__.py",
        "model.py",
        "validator.py",
        "repository.py",
        "service.py",
        "api.py",
        "tests.py",
    ]:
        file(lead / f)


def generate_cli():
    print("\nGenerating CLI")
    cmd = SRC / "cli" / "commands"
    directory(cmd)
    file(cmd / "lead.py")


def generate_tests():
    print("\nGenerating Tests")
    directory(TESTS)
    file(TESTS / "test_lead.py")
    file(TESTS / "test_repository.py")


def generate_docs():
    print("\nGenerating Documentation")
    sprints = ENGINEERING / "sprints"
    milestones = ENGINEERING / "milestones"
    directory(sprints)
    directory(milestones)
    file(sprints / "SPRINT_03.md", "# Sprint 03\n")
    file(milestones / "M03.md", "# Milestone 03\n")


def summary():
    print("\n" + "=" * 70)
    print("BIP EOS M03 COMPLETE")
    print("=" * 70)
    print(f"Created : {CREATED}")
    print(f"Skipped : {SKIPPED}")
    print(f"Failed  : {FAILED}")
    print("\nDAAAAAMAGE!!")


def main():
    verify()
    generate_database()
    generate_lead()
    generate_cli()
    generate_tests()
    generate_docs()
    summary()


if __name__ == "__main__":
    main()
