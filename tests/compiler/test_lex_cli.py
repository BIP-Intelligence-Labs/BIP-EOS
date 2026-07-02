import subprocess, sys

def test_lex_cli_runs():
    result = subprocess.run(
        [sys.executable, "-m", "ueos.cli.commands.lex"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
