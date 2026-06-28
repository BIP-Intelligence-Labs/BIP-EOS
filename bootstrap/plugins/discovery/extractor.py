from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class ExtractedDocument:
    title:str
    description:str
    links:list[str]

class DiscoveryExtractor:
    def extract(self, html:str):
        soup=BeautifulSoup(html,"html.parser")
        title=soup.title.string.strip() if soup.title and soup.title.string else ""
        return ExtractedDocument(title,"",[])
