"""
============================================================
 BIP EOS CLI
 Foundation
============================================================
"""

import argparse
from pathlib import Path

ROOT = Path(__file__).parent


def academy_status():
    academy = ROOT / "bootstrap" / "academy"
    print("=" * 60)
    print(" BIP EOS Academy Status")
    print("=" * 60)

    if not academy.exists():
        print("Academy: NOT FOUND")
        return

    print(f"Academy: {academy}")

    checks = [
        ("Curriculum", academy / "curriculum"),
        ("Students", academy / "students"),
        ("Knowledge", academy / "knowledge"),
        ("Research", academy / "research"),
    ]

    for name, path in checks:
        print(f"{name:<12}: {'OK' if path.exists() else 'MISSING'}")

    lessons = list((academy / "curriculum").rglob("*.md")) if (academy / "curriculum").exists() else []
    students = list((academy / "students").glob("*.json")) if (academy / "students").exists() else []

    print("-" * 60)
    print(f"Lessons : {len(lessons)}")
    print(f"Students: {len(students)}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(prog="bip")
    sub = parser.add_subparsers(dest="command")

    academy = sub.add_parser("academy")
    academy_sub = academy.add_subparsers(dest="action")
    academy_sub.add_parser("status")

    args = parser.parse_args()

    if args.command == "academy" and args.action == "status":
        academy_status()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
