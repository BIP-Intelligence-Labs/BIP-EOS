"""
bootstrap_engineering_model.py

Bootstraps the Engineering Model package.

Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "bootstrap" / "compiler" / "engineering_model"

FILES = {
    "__init__.py": '"""Engineering Model Package."""\n',
    "platform.py": '"""Platform model."""\n\nclass Platform:\n    pass\n',
    "solution.py": '"""Solution model."""\n\nclass Solution:\n    pass\n',
    "domain.py": '"""Domain model."""\n\nclass Domain:\n    pass\n',
    "component.py": '"""Component model."""\n\nclass Component:\n    pass\n',
    "api.py": '"""API model."""\n\nclass API:\n    pass\n',
    "event.py": '"""Event model."""\n\nclass Event:\n    pass\n',
    "permission.py": '"""Permission model."""\n\nclass Permission:\n    pass\n',
    "report.py": '"""Report model."""\n\nclass Report:\n    pass\n',
    "relationship.py": '"""Relationship model."""\n\nclass Relationship:\n    pass\n',
    "dependency.py": '"""Dependency model."""\n\nclass Dependency:\n    pass\n',
    "engineering_model.py": Engineering Model (Compiler Intermediate Representation).