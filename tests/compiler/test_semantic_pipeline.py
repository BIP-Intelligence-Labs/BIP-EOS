from bip_eos.compiler.frontend.semantic_analyzer import SemanticAnalyzer
from bip_eos.compiler.frontend.ast import ASTNode

def test_semantic_pipeline():
    analyzer = SemanticAnalyzer()
    diagnostics = analyzer.analyze(ASTNode("Program"))
    assert diagnostics == []
