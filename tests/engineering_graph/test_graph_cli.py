import subprocess
import sys

def test_graph_cli_runs():
    result = subprocess.run(
        [sys.executable, "-m", "ueos.cli.commands.graph"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
