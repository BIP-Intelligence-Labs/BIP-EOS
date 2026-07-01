"""
bootstrap_ec001.py
Creates EC-001 Engineering Constitution
"""
from pathlib import Path

root=Path.cwd()
target=root/"engineering"/"cer"/"EC"
target.mkdir(parents=True, exist_ok=True)
doc=target/"EC-001-Engineering-Constitution.md"

content="""# EC-001
# Engineering Constitution

Version: 1.0.0
Status: Canonical

Engineering is generated from knowledge.

🚀 ONE PLATFORM.
🚀 UNLIMITED ECOSYSTEMS.
🚀 ONE SOURCE OF ENGINEERING TRUTH.
"""

if not doc.exists():
    doc.write_text(content,encoding="utf-8")
    print(f"[CREATE] {doc}")
else:
    print(f"[SKIP]   {doc}")

print("EC-001 initialized.")
