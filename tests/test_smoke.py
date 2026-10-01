from click.testing import CliRunner

from indiarealtime import IndiaRealTime, MandiPrice
from indiarealtime.cli import cli


def test_package_exports():
    assert IndiaRealTime is not None
    assert MandiPrice.__name__ == "MandiPrice"


def test_cli_help_smoke():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])

    assert result.exit_code == 0
    assert "IndiaRealTime CLI" in result.output
