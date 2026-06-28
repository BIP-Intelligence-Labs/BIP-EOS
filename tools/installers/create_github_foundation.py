
"""
create_github_foundation.py

Creates a professional .github structure for the Genesis repository.
Run from the Genesis repository root.
"""

from pathlib import Path

ROOT = Path(".github")

FILES = {
    "CODEOWNERS": """# Global code owners
* @mariusferezan
""",
    "PULL_REQUEST_TEMPLATE.md": """# Pull Request

## Summary

## Related ADR

## Testing

## Checklist
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] EES compliant
- [ ] EQG compliant
""",
    "FUNDING.yml": """github: []
""",
    "dependabot.yml": """version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
""",
    "workflows/ci.yml": """name: CI

on:
  push:
  pull_request:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m compileall src
""",
    "workflows/release.yml": """name: Release

on:
  workflow_dispatch:
""",
    "workflows/docs.yml": """name: Documentation

on:
  push:
    paths:
      - "docs/**"
""",
    "ISSUE_TEMPLATE/bug_report.md": """---
name: Bug Report
about: Report a defect
---

## Description

## Expected Behavior

## Steps to Reproduce
""",
    "ISSUE_TEMPLATE/feature_request.md": """---
name: Feature Request
about: Propose a new feature
---

## Problem

## Proposal

## Benefits
""",
    "ISSUE_TEMPLATE/architecture_proposal.md": """---
name: Architecture Proposal
about: Propose an architectural change
---

## Summary

## Motivation

## ADR Reference

## Impact
""",
}

print("="*60)
print("Creating .github Foundation")
print("="*60)

for rel, content in FILES.items():
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")
        print("CREATE", path)
    else:
        print("EXISTS", path)

print("="*60)
print(".github foundation complete")
