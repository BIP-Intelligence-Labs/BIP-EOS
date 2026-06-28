"""
bootstrap_docs_scaffold.py

Creates the BIP EOS documentation structure.

Run:
    python bootstrap_docs_scaffold.py
"""

from pathlib import Path

ROOT = Path("docs")

folders = [
    ROOT,
    ROOT / "architecture",
    ROOT / "manifesto",
    ROOT / "roadmap",
    ROOT / "governance",
    ROOT / "decisions",
]

files = {
    ROOT / "README.md": "# BIP EOS Documentation\n",
    ROOT / "architecture" / "system-architecture.md": "# System Architecture\n",
    ROOT / "architecture" / "ai-architecture.md": "# AI Architecture\n",
    ROOT / "architecture" / "engineering-architecture.md": "# Engineering Architecture\n",
    ROOT / "architecture" / "plugin-architecture.md": "# Plugin Architecture\n",
    ROOT / "architecture" / "kernel-architecture.md": "# Kernel Architecture\n",

    ROOT / "manifesto" / "BIP_EOS_Manifesto.md": "# BIP EOS Manifesto\n",

    ROOT / "roadmap" / "roadmap.md": "# Product Roadmap\n",
    ROOT / "roadmap" / "milestones.md": "# Milestones\n",
    ROOT / "roadmap" / "sprint-004.md": "# Sprint 004\n",
    ROOT / "roadmap" / "future.md": "# Future Vision\n",

    ROOT / "governance" / "engineering-principles.md": "# Engineering Principles\n",
    ROOT / "governance" / "coding-standards.md": "# Coding Standards\n",
    ROOT / "governance" / "contribution-guide.md": "# Contribution Guide\n",

    ROOT / "decisions" / "ADR-0001-BIP-EOS.md": "# ADR-0001\n\nDecision: Adopt BIP EOS as the platform architecture.\n",
    ROOT / "decisions" / "ADR-0002-AI-Subsystem.md": "# ADR-0002\n\nDecision: Introduce AI as a first-class subsystem.\n",
    ROOT / "decisions" / "ADR-0003-Engineering-Subsystem.md": "# ADR-0003\n\nDecision: Separate Engineering from the Kernel.\n",
    ROOT / "decisions" / "ADR-0004-Plugin-Architecture.md": "# ADR-0004\n\nDecision: Use a plugin-first architecture.\n",
    ROOT / "decisions" / "ADR-0005-Discovery-Engine.md": "# ADR-0005\n\nDecision: Discovery Engine is the first platform plugin.\n",
}

print("="*64)
print(" BIP EOS Documentation Scaffolder")
print("="*64)

created = existing = 0

for d in folders:
    d.mkdir(parents=True, exist_ok=True)
    print(f"📁 {d}")

for path, content in files.items():
    if path.exists():
        print(f"• Exists   {path}")
        existing += 1
    else:
        path.write_text(content, encoding="utf-8")
        print(f"✓ Created {path}")
        created += 1

print("-"*64)
print(f"Created : {created}")
print(f"Existing: {existing}")
print("Documentation scaffold complete.")
