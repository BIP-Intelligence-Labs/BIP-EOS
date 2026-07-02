from pathlib import Path
import re
p=re.compile(r'\b(from|import)\s+bip_eos\b')
count=0
for f in Path.cwd().rglob('*.py'):
 t=f.read_text(encoding='utf-8',errors='ignore')
 if p.search(t): print(f); count+=1
print(count)
