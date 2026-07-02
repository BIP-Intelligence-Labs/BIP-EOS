from ueos.compiler.frontend.diagnostics import Diagnostic


def test_diagnostic():
    d = Diagnostic("error", "message")
    assert d.message == "message"
