#!/usr/bin/env python3
"""
bootstrap_ea001_add_chapter13.py

Adds Chapter 13 to the EA-001 Constitution.

Standard Library only.
Safe by default (never overwrites existing files).
"""

from pathlib import Path

CHAPTER = "Chapter-13-Engineering-Academy-Constitution.md"

CONTENT = """# Chapter 13 — Engineering Academy Constitution

## Constitutional Purpose

The Engineering Academy System (EAS) transforms governed Engineering
Knowledge into Engineering Competency through structured education,
assessment, and certification.

## Constitutional Principles

- The Constitution is the authoritative curriculum.
- Engineering Knowledge is the source of instruction.
- Competencies are evidence-based.
- Certifications are earned through demonstrated capability.

## Constitutional Pipeline

Engineering Truth
        ↓
Engineering Knowledge
        ↓
Engineering Curriculum
        ↓
Engineering Competency
        ↓
Engineering Certification

## Responsibilities

- Define curriculum from constitutional chapters.
- Generate learning paths from Engineering Knowledge.
- Deliver practical laboratories.
- Assess competencies objectively.
- Award certifications.

## Certification Levels

1. UEOS Certified Engineer I — Constitution
2. UEOS Certified Engineer II — Runtime
3. UEOS Certified Engineer III — Engineering Systems
4. UEOS Architect
5. UEOS Fellow

## Constitutional Rules

CR-018
The Engineering Academy SHALL derive its curriculum from the UEOS Constitution.

CR-019
Competencies SHALL be mapped to Constitutional Systems.

CR-020
Certifications SHALL be based on demonstrated engineering capability.

Status:
Approved for Architecture Version 1.0
"""

def find_root(start: Path) -> Path:
    cur = start.resolve()
    while cur != cur.parent:
        if (cur / "engineering").exists() and (cur / "src").exists():
            return cur
        cur = cur.parent
    raise RuntimeError("UEOS repository root not found.")

def main():
    root = find_root(Path(__file__).parent)
    ea = root / "engineering" / "architecture" / "EA-001"
    ea.mkdir(parents=True, exist_ok=True)

    chapter = ea / CHAPTER
    if chapter.exists():
        print(f"[EXISTS ] {chapter.relative_to(root)}")
    else:
        chapter.write_text(CONTENT, encoding="utf-8")
        print(f"[CREATE ] {chapter.relative_to(root)}")

    manifest = ea / "manifest.yaml"
    if manifest.exists():
        text = manifest.read_text(encoding="utf-8")
        if "chapters: 13" not in text:
            text = text.replace("chapters: 12", "chapters: 13")
            manifest.write_text(text, encoding="utf-8")
            print(f"[UPDATE ] {manifest.relative_to(root)}")

    print("=" * 72)
    print("EA-001 updated with Chapter 13.")
    print("=" * 72)

if __name__ == "__main__":
    main()
