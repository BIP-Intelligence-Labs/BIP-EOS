import subprocess, sys

def test_parse_cli_runs():
    result = subprocess.run(
        [sys.executable, "-m", "bip_eos.cli.commands.parse"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
