"""
bootstrap_m007_1_test_suite_normalization.py

M-007.1 - Test Suite Normalization

Creates a recommended pytest configuration and audits duplicate test
modules that commonly cause "import file mismatch" errors.

Usage:
    python bootstrap_m007_1_test_suite_normalization.py
"""

from pathlib import Path

ROOT = Path.cwd()

PYPROJECT_SNIPPET = """
# -----------------------------------------------------------------
# M-007.1 Test Suite Normalization
# Merge this into your existing pyproject.toml if not already present.
# -----------------------------------------------------------------

[tool.pytest.ini_options]
minversion = "8.0"

testpaths = [
    "tests",
    "src/ueos/core/kernel/tests"
]

norecursedirs = [
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "engineering",
    "tools/migrations",
    ".migration_backup"
]

python_files = [
    "test_*.py"
]
""".strip()

README = """
# M-007.1 Test Suite Normalization

Objectives

- Exclude roadmap tests from the default pytest run.
- Exclude migration scaffold tests.
- Use package imports in kernel tests.
- Keep only production tests in the default collection.

Kernel import example

Replace:

    from runtime_state_machine import RuntimeState

With:

    from ueos.core.kernel.runtime_state_machine import RuntimeState
""".strip()

def audit_duplicates():
    seen = {}
    duplicates = []
    for test in ROOT.rglob("test_*.py"):
        name = test.name
        if name in seen:
            duplicates.append((name, seen[name], test))
        else:
            seen[name] = test
    return duplicates

def main():
    outdir = ROOT / "engineering" / "roadmaps" / "M-007.1_Test_Suite_Normalization"
    outdir.mkdir(parents=True, exist_ok=True)

    (outdir / "README.md").write_text(README + "\n", encoding="utf-8")
    (outdir / "pytest.toml.snippet").write_text(PYPROJECT_SNIPPET + "\n", encoding="utf-8")

    report = outdir / "duplicate_tests.md"
    dups = audit_duplicates()

    with report.open("w", encoding="utf-8") as f:
        f.write("# Duplicate Test Module Audit\n\n")
        if not dups:
            f.write("No duplicate test filenames found.\n")
        else:
            for name, a, b in dups:
                f.write(f"- {name}\n")
                f.write(f"  - {a}\n")
                f.write(f"  - {b}\n\n")

    print("=" * 60)
    print("M-007.1 Test Suite Normalization")
    print("=" * 60)
    print(f"Artifacts: {outdir}")
    print(f"Duplicate test names: {len(dups)}")
    print()
    print("Next:")
    print("1. Merge pytest.toml.snippet into pyproject.toml")
    print("2. Update kernel tests to use package imports")
    print("3. Run: pytest")

if __name__ == "__main__":
    main()
