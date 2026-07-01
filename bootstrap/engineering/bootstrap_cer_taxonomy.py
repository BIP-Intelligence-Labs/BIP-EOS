"""
bootstrap_cer_taxonomy.py

BIP UE
Canonical Engineering Records (CER)

Bootstraps the complete CER taxonomy.

Usage:
    py bootstrap_cer_taxonomy.py
"""

from pathlib import Path

ROOT = Path.cwd()

TAXONOMY = {
    "EA": ("Engineering Architecture",
           "Canonical engineering architecture records."),
    "EC": ("Engineering Constitution",
           "Engineering principles, constitution, and philosophy."),
    "ADR": ("Architecture Decision Records",
            "Engineering and architecture decisions."),
    "SSC": ("Software Supply Chain & Compliance",
            "Software supply chain governance and compliance."),
    "ES": ("Engineering Standards",
           "Engineering standards and conventions."),
    "EG": ("Engineering Governance",
           "Governance policies and engineering controls."),
    "SP": ("Specifications",
           "Canonical technical specifications."),
    "ER": ("Engineering Reports",
           "Engineering reports and assessments."),
    "QR": ("Quality Rules",
           "Quality assurance rules and practices."),
    "SR": ("Security Rules",
           "Security engineering standards."),
    "RM": ("Risk Management",
           "Risk identification and mitigation."),
    "OP": ("Operational Procedures",
           "Operational engineering procedures."),
    "AP": ("Academy Publications",
           "Curricula, courses, certifications, and learning content."),
    "AI": ("Artificial Intelligence Architecture & Governance",
           "AI architecture, governance, reasoning, and policies."),
    "PR": ("Product Records",
           "Product architecture and lifecycle records."),
    "RE": ("Release Engineering",
           "Build, release, deployment, and versioning."),
    "TS": ("Testing Standards",
           "Testing methodologies and standards."),
}

BASE = ROOT / "engineering" / "cer"

print("=" * 60)
print("BIP UE")
print("CER Taxonomy Bootstrap")
print("=" * 60)

dirs = files = 0

BASE.mkdir(parents=True, exist_ok=True)

index = [
    "# CER Taxonomy",
    "",
    "| Prefix | Record Family |",
    "|--------|---------------|",
]

for prefix, (title, desc) in TAXONOMY.items():
    folder = BASE / prefix
    if folder.exists():
        print(f"[SKIP]   engineering/cer/{prefix}")
    else:
        folder.mkdir(parents=True)
        print(f"[CREATE] engineering/cer/{prefix}")
        dirs += 1

    readme = folder / "README.md"
    if not readme.exists():
        readme.write_text(
f"""# {prefix}

## {title}

{desc}

Status: Canonical Engineering Record Family
""",
            encoding="utf-8",
        )
        print(f"[CREATE] engineering/cer/{prefix}/README.md")
        files += 1
    else:
        print(f"[SKIP]   engineering/cer/{prefix}/README.md")

    index.append(f"| {prefix} | {title} |")

index_file = BASE / "CER-TAXONOMY.md"
index_file.write_text("\n".join(index), encoding="utf-8")

print(f"[CREATE] engineering/cer/CER-TAXONOMY.md")
print("-" * 60)
print(f"Directories : {dirs}")
print(f"Files       : {files + 1}")
print("Status      : SUCCESS")
print()
print("CER Families")
for p, (t, _) in TAXONOMY.items():
    print(f"  {p:<4} {t}")
