"""
============================================================
 BIP EOS Academy
 Student 0001 Generator
============================================================
"""

import json
from pathlib import Path

ROOT = Path("bootstrap") / "academy" / "students"

STUDENT = {
    "id": "STUDENT-0001",
    "name": "Planner Agent",
    "status": "Active",
    "engineering_level": "Apprentice",
    "curriculum": "Engineering Core",
    "knowledge": 0,
    "lessons_completed": 0,
    "exercises_completed": 0,
    "certifications": [],
    "enrolled": "2026-06-28",
    "mentor": "BIP EOS Academy",
    "notes": [
        "First Academy student.",
        "Founding engineering agent."
    ]
}


def banner():
    print("=" * 60)
    print(" BIP EOS Student Generator")
    print("=" * 60)


def create_student():
    ROOT.mkdir(parents=True, exist_ok=True)

    file = ROOT / "planner-agent.json"

    if file.exists():
        print(f"• Exists   {file}")
        return

    with open(file, "w", encoding="utf-8") as f:
        json.dump(STUDENT, f, indent=4)

    print(f"✓ Created {file}")


def summary():
    print("-" * 60)
    print("Student #0001 enrolled.")
    print("Planner Agent is ready for training.")
    print("=" * 60)


def main():
    banner()
    create_student()
    summary()


if __name__ == "__main__":
    main()
