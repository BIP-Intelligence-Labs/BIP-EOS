
"""
migrate_registry_yaml_to_json.py

BIP UE
Registry Migration Utility

Converts registry YAML files under:

bootstrap/engineering/registry/families/

into canonical JSON registry files.

Requires:
    pip install pyyaml
"""

from pathlib import Path
import json

try:
    import yaml
except ImportError:
    print("PyYAML is required.")
    print("Install with: pip install pyyaml")
    raise SystemExit(1)

ROOT = Path.cwd()
FAMILIES = ROOT / "bootstrap" / "engineering" / "registry" / "families"

print("=" * 60)
print("BIP UE")
print("Registry YAML → JSON Migration")
print("=" * 60)

created = 0
skipped = 0

if not FAMILIES.exists():
    print(f"Directory not found: {FAMILIES}")
    raise SystemExit(1)

for yaml_file in sorted(list(FAMILIES.glob("*.yaml")) + list(FAMILIES.glob("*.yml"))):
    json_file = yaml_file.with_suffix(".json")

    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    data.setdefault("version", "1.0.0")
    data.setdefault("status", "Draft")
    data.setdefault("owner", "Engineering")
    data.setdefault("generator", "EDE")
    data.setdefault("records", [])

    if json_file.exists():
        print(f"[SKIP]   {json_file.relative_to(ROOT)}")
        skipped += 1
    else:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"[CREATE] {json_file.relative_to(ROOT)}")
        created += 1

print("-" * 60)
print(f"JSON Created : {created}")
print(f"Skipped      : {skipped}")
print()
print("NOTE:")
print("Review the generated JSON files.")
print("Once verified, the YAML files may be archived or removed.")
