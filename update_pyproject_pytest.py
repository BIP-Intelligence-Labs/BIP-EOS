"""
update_pyproject_pytest.py

Safely updates pyproject.toml with recommended pytest configuration
for M-007.1 Test Suite Normalization.

- Creates a backup: pyproject.toml.bak
- Appends the pytest section only if it is not already present.

Usage:
    python update_pyproject_pytest.py
"""

from pathlib import Path
import shutil
import sys

PYTEST_BLOCK = """

# -----------------------------------------------------------------
# M-007.1 Test Suite Normalization
# -----------------------------------------------------------------
[tool.pytest.ini_options]
minversion = "8.0"

testpaths = [
    "tests",
    "src/ueos/core/kernel/tests",
]

norecursedirs = [
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "engineering",
    "tools/migrations",
    ".migration_backup",
]

python_files = [
    "test_*.py",
]
"""

def main():
    pyproject = Path("pyproject.toml")

    if not pyproject.exists():
        print("ERROR: pyproject.toml not found.")
        sys.exit(1)

    text = pyproject.read_text(encoding="utf-8")

    if "[tool.pytest.ini_options]" in text:
        print("pytest configuration already exists.")
        print("No changes made.")
        return

    backup = pyproject.with_suffix(".toml.bak")
    shutil.copy2(pyproject, backup)
    print(f"Backup created: {backup}")

    pyproject.write_text(text.rstrip() + "\n\n" + PYTEST_BLOCK.strip() + "\n",
                         encoding="utf-8")

    print("pyproject.toml updated successfully.")
    print("Next:")
    print("  pytest")

if __name__ == "__main__":
    main()
