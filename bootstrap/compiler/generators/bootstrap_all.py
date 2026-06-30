from pathlib import Path
import runpy

HERE = Path(__file__).parent

for script in sorted(HERE.glob("c*.py")):
    print("\n" + "="*72)
    print(f"Running {script.name}")
    print("="*72)
    runpy.run_path(str(script))
