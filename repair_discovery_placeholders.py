"""
repair_discovery_placeholders.py
"""
from pathlib import Path
DISCOVERY = Path("bootstrap/plugins/discovery")
FILES = {
 "extractor.py": """from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class ExtractedDocument:
    title:str
    description:str
    links:list[str]

class DiscoveryExtractor:
    def extract(self, html:str):
        soup=BeautifulSoup(html,\"html.parser\")
        title=soup.title.string.strip() if soup.title and soup.title.string else \"\"
        return ExtractedDocument(title,\"\",[])
""",
 "validator.py": """from dataclasses import dataclass
from .extractor import ExtractedDocument

@dataclass
class ValidationResult:
    valid:bool
    errors:list[str]

class DiscoveryValidator:
    def validate(self,document:ExtractedDocument):
        return ValidationResult(True,[])
""",
 "repository.py": """class DiscoveryRepository:
    def __init__(self):
        self.records=[]
    def save(self,url,document):
        self.records.append((url,document))
        return type(\"Record\",(),{\"url\":url,\"document\":document})()
""",
 "scheduler.py": """from collections import deque
class DiscoveryScheduler:
    def __init__(self):
        self.q=deque()
    def enqueue(self,url):
        self.q.append(type(\"Job\",(),{\"url\":url})())
    def dequeue(self):
        return self.q.popleft() if self.q else None
"""
}
print("Bootstrap Discovery Placeholder Repair")
for name,content in FILES.items():
    path=DISCOVERY/name
    existing=path.read_text(encoding="utf-8") if path.exists() else ""
    if len(existing.strip().splitlines())<=2:
        path.write_text(content,encoding="utf-8")
        print(f"✓ Repaired {name}")
    else:
        print(f"• Skipped {name}")
print("Repair complete.")