"""
============================================================
 BIP EOS Academy Scaffolder
 Bootstrap Intelligence Platform
============================================================
"""

from pathlib import Path

ROOT = Path("bootstrap") / "academy"

DIRECTORIES = [
    "",
    "curriculum",
    "knowledge",
    "research",
    "lessons",
    "exercises",
    "exams",
    "certifications",
    "transcripts",
    "students",
    "reports",
    "prompts",
    "datasets",
    "simulations",
    "sandbox",
]

MODULES = {
    "academy.py": "Academy",
    "trainer.py": "Trainer",
    "evaluator.py": "Evaluator",
    "registry.py": "Registry",
    "scheduler.py": "Scheduler",
    "analytics.py": "Analytics",
    "progress.py": "Progress",
    "transcript.py": "Transcript",
    "recommendations.py": "Recommendations",
    "certification.py": "Certification",
    "graduation.py": "Graduation",
}

created = 0
existing = 0


def banner():
    print("=" * 60)
    print(" BIP EOS Academy Scaffolder")
    print("=" * 60)


def create_directory(path: Path):
    global created, existing

    if path.exists():
        existing += 1
        print(f"• Exists   {path}")
        return

    path.mkdir(parents=True, exist_ok=True)
    created += 1
    print(f"✓ Created {path}")


def create_module(filename: str, classname: str):
    global created, existing

    path = ROOT / filename

    if path.exists():
        existing += 1
        print(f"• Exists   {path}")
        return

    content = f'''"""
{classname}
Part of the BIP EOS Academy
"""

class {classname}:
    """{classname} service."""

    def __init__(self):
        pass
'''

    path.write_text(content, encoding="utf-8")

    created += 1
    print(f"✓ Created {path}")


def create_readme(path: Path, title: str):
    global created, existing

    file = path / "README.md"

    if file.exists():
        existing += 1
        return

    file.write_text(
f"""# {title}

Part of the BIP EOS Academy.

Build once.
Teach forever.
""",
        encoding="utf-8",
    )

    created += 1


def summary():
    print("-" * 60)
    print(f"Created : {created}")
    print(f"Existing: {existing}")
    print("=" * 60)
    print("Academy Ready")
    print("Ready to train BIP EOS.")
    print("=" * 60)


def main():

    banner()

    for directory in DIRECTORIES:
        create_directory(ROOT / directory)

    create_readme(ROOT, "BIP EOS Academy")

    init = ROOT / "__init__.py"

    if not init.exists():
        init.write_text("", encoding="utf-8")

    models = ROOT / "models.py"

    if not models.exists():
        models.write_text(
            '"""Academy Models"""\n',
            encoding="utf-8",
        )

    for filename, classname in MODULES.items():
        create_module(filename, classname)

    for directory in ROOT.rglob("*"):
        if directory.is_dir():
            create_readme(directory, directory.name.title())

    summary()


if __name__ == "__main__":
    main()
