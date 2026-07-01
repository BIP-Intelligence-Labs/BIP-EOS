import subprocess
import sys

def test_export_cli_runs():
    result = subprocess.run(
        [sys.executable, "-m", "bip_eos.cli.commands.export"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
