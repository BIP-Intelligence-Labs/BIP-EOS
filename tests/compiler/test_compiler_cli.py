import subprocess, sys

def test_compile_cli_runs():
    result = subprocess.run(
        [sys.executable, "-m", "bip_eos.cli.commands.compile"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
