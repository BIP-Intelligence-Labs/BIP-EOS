from bip_eos.compiler.frontend.semantic_analyzer import SemanticAnalyzer


def test_semantic_analyzer():
    analyzer = SemanticAnalyzer()
    assert analyzer.analyze(None) == []
