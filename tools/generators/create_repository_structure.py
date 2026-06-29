"""
create_repository_structure.py

Genesis EEOS
Repository Structure Organizer

Creates the recommended top-level engineering structure.

Run:

    python create_repository_structure.py
"""

from pathlib import Path

DIRECTORIES = [
    "engineering",
    "engineering/sprints",
    "engineering/standards",
    "engineering/decisions",
    "engineering/architecture",

    "tools",
    "tools/generators",
    "tools/migrations",
    "tools/cleanup",
    "tools/archive",
    "tools/installers",

    "docs",
    "tests",
]

README_CONTENT = {
    "engineering/README.md": "# Engineering\n\nEngineering artifacts, standards, decisions, and architecture.\n",
    "engineering/sprints/README.md": "# Sprints\n\nSprint planning and execution artifacts.\n",
    "engineering/standards/README.md": "# Standards\n\nEngineering standards and conventions.\n",
    "engineering/decisions/README.md": "# Architecture Decisions\n\nArchitectural Decision Records (ADRs).\n",
    "engineering/architecture/README.md": "# Architecture\n\nArchitecture diagrams and design documentation.\n",
    "tools/README.md": "# Tools\n\nRepository maintenance and engineering tools.\n",
    "tools/generators/README.md": "# Generators\n\nCode and artifact generators.\n",
    "tools/migrations/README.md": "# Migrations\n\nRepository and data migration utilities.\n",
    "tools/cleanup/README.md": "# Cleanup\n\nRepository cleanup utilities.\n",
    "tools/archive/README.md": "# Archive\n\nHistorical engineering artifacts.\n",
    "tools/installers/README.md": "# Installers\n\nProject bootstrap and installer scripts.\n",
    "docs/README.md": "# Documentation\n\nProject documentation.\n",
    "tests/README.md": "# Tests\n\nAutomated tests.\n",
}

print("=" * 60)
print("BIP EOS Repository Structure")
print("=" * 60)

for directory in DIRECTORIES:
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    print(f"DIR    {path}")

for filename, content in README_CONTENT.items():
    file = Path(filename)
    if not file.exists():
        file.write_text(content, encoding="utf-8")
        print(f"CREATE {file}")
    else:
        print(f"EXISTS {file}")

print("\nRepository structure ready.")

print("""
Suggested next moves:

1. Move cleanup scripts to tools/cleanup/
2. Move migration scripts to tools/migrations/
3. Move installer scripts to tools/installers/
4. Keep archived historical artifacts under tools/archive/
5. Reserve docs/ for end-user and developer documentation.
""")
