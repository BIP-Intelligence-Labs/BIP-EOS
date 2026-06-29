"""
bootstrap/bootstrap_lead_model.py

Generates the Lead domain model for BIP EOS.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGET = (
    ROOT
    / "src"
    / "bip_eos"
    / "builders"
    / "lead"
    / "model.py"
)

MODEL = '''"""Lead Domain Model."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class Lead:
    """Represents a buyer lead."""

    id: Optional[str] = None

    first_name: str = ""
    last_name: str = ""

    email: str = ""
    phone: str = ""

    current_city: str = ""
    current_state: str = ""

    destination_city: str = ""
    destination_area: str = ""

    budget_min: Optional[int] = None
    budget_max: Optional[int] = None

    desired_beds: Optional[int] = None
    desired_baths: Optional[float] = None

    financing_type: str = ""
    preapproved: bool = False

    buyer_type: str = ""
    move_timeline: str = ""

    lead_score: int = 0
    status: str = "new"

    created_at: datetime | None = None
    updated_at: datetime | None = None
'''

print("=" * 70)
print("BIP EOS Lead Model Bootstrap")
print("=" * 70)

if TARGET.exists():
    print(f"[SKIP] {TARGET}")
else:
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(MODEL, encoding="utf-8")
    print(f"[FILE] {TARGET}")

print("-" * 70)
print("Lead model ready.")
