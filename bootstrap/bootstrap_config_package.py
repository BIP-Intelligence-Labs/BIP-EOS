#!/usr/bin/env python3
from pathlib import Path

ROOT = Path.cwd()

FILES = {
"src/bip_eos/config/__init__.py": '"""BIP EOS Configuration Package."""\n\nfrom .constants import *\nfrom .settings import *\nfrom .environment import *\nfrom .paths import *\n',
"src/bip_eos/config/constants.py": 'PRODUCT="BIP EOS"\nCODENAME="Genesis"\nVERSION="0.1.0"\nCOMPANY="BIP Intelligence Labs"\n',
"src/bip_eos/config/environment.py": 'import os\nENVIRONMENT=os.getenv("BIP_ENV","development")\nDEBUG=os.getenv("DEBUG","False").lower()=="true"\nSUPABASE_URL=os.getenv("SUPABASE_URL","")\nSUPABASE_KEY=os.getenv("SUPABASE_KEY","")\nOPENAI_API_KEY=os.getenv("OPENAI_API_KEY","")\nANTHROPIC_API_KEY=os.getenv("ANTHROPIC_API_KEY","")\nGOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY","")\nAI_PROVIDER=os.getenv("AI_PROVIDER","openai")\n',
"src/bip_eos/config/settings.py": 'LOG_LEVEL="INFO"\nDEFAULT_LANGUAGE="en"\nDEFAULT_TIMEOUT=30\nDEFAULT_REPORT_FORMAT="pdf"\nMAX_RETRIES=3\nENABLE_CRM=True\nENABLE_REPORTS=True\nENABLE_VOICE_AI=False\nENABLE_ANALYTICS=False\nENABLE_EXPERIMENTAL=False\n',
"src/bip_eos/config/paths.py": 'from pathlib import Path\nPROJECT_ROOT=Path(__file__).resolve().parents[3]\nSRC_DIR=PROJECT_ROOT/"src"\nDOCS_DIR=PROJECT_ROOT/"docs"\nLOGS_DIR=PROJECT_ROOT/"logs"\nREPORTS_DIR=PROJECT_ROOT/"reports"\nREGISTRY_DIR=PROJECT_ROOT/"registry"\nPLUGINS_DIR=PROJECT_ROOT/"plugins"\nENGINEERING_DIR=PROJECT_ROOT/"engineering"\nBOOTSTRAP_DIR=PROJECT_ROOT/"bootstrap"\nTEMPLATES_DIR=PROJECT_ROOT/"templates"\nTESTS_DIR=PROJECT_ROOT/"tests"\n'
}

print("="*70)
print("BIP EOS Configuration Bootstrap")
print("="*70)

created=0
skipped=0
for rel,content in FILES.items():
    p=ROOT/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():
        print(f"[SKIP] {p}")
        skipped+=1
    else:
        p.write_text(content,encoding="utf-8")
        print(f"[FILE] {p}")
        created+=1

print("-"*70)
print(f"Created : {created}")
print(f"Skipped : {skipped}")
