
"""
bootstrap_vm004.py

BIP UE
VM-004 Engineering Metadata Schema Bootstrap
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "bootstrap/engineering/registry/schemas",
    "bootstrap/engineering/registry/metadata",
    "bootstrap/engineering/registry/validation",
]

FILES = {
    "bootstrap/engineering/registry/schemas/engineering_record_schema.yaml": """name: EngineeringRecord
version: 1.0.0
required:
  - id
  - family
  - title
  - owner
  - version
  - status
""",
    "bootstrap/engineering/registry/schemas/lifecycle_schema.yaml": """states:
  - Draft
  - Review
  - Approved
  - Published
  - Deprecated
  - Archived
""",
    "bootstrap/engineering/registry/schemas/relationship_schema.yaml": """relationships:
  - depends_on
  - references
  - related_records
  - supersedes
  - superseded_by
""",
    "bootstrap/engineering/registry/schemas/version_schema.yaml": "semantic_version: MAJOR.MINOR.PATCH\n",
    "bootstrap/engineering/registry/schemas/publication_schema.yaml": "publication: canonical\n",
    "bootstrap/engineering/registry/schemas/validation_schema.yaml": "validation: required\n",
    "bootstrap/engineering/registry/metadata/required_fields.yaml": """fields:
  - id
  - family
  - title
  - owner
  - version
  - status
""",
    "bootstrap/engineering/registry/metadata/optional_fields.yaml": """fields:
  - description
  - tags
  - keywords
  - reviewers
  - approvers
""",
    "bootstrap/engineering/registry/metadata/ai_extensions.yaml": """ai:
  embeddings: true
  summary: true
""",
    "bootstrap/engineering/registry/validation/id_rules.yaml": "pattern: '^[A-Z]+-[0-9]{3}$'\n",
    "bootstrap/engineering/registry/validation/version_rules.yaml": "format: semver\n",
    "bootstrap/engineering/registry/validation/dependency_rules.yaml": "allow_cycles: false\n",
    "bootstrap/engineering/registry/validation/reference_rules.yaml": "validate_targets: true\n",
}

print("=" * 60)
print("BIP UE")
print("VM-004 Engineering Metadata Schema")
print("=" * 60)

dirs = 0
files = 0

for d in DIRECTORIES:
    p = ROOT / d
    if p.exists():
        print(f"[SKIP]   {d}")
    else:
        p.mkdir(parents=True, exist_ok=True)
        print(f"[CREATE] {d}")
        dirs += 1

for rel, content in FILES.items():
    p = ROOT / rel
    if p.exists():
        print(f"[SKIP]   {rel}")
    else:
        p.write_text(content, encoding="utf-8")
        print(f"[CREATE] {rel}")
        files += 1

print("-" * 60)
print(f"Directories : {dirs}")
print(f"Files       : {files}")
print("Status      : SUCCESS")
print()
print("VM-004 initialized.")
print("Engineering Metadata Schema ready.")
