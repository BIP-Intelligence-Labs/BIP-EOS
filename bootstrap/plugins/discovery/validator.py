from dataclasses import dataclass
from .extractor import ExtractedDocument

@dataclass
class ValidationResult:
    valid:bool
    errors:list[str]

class DiscoveryValidator:
    def validate(self,document:ExtractedDocument):
        return ValidationResult(True,[])
