from ueos.compiler.frontend.semantic_analyzer import SemanticAnalyzer
from ueos.compiler.frontend.ast import ASTNode

def test_semantic_pipeline():
    analyzer = SemanticAnalyzer()
    diagnostics = analyzer.analyze(ASTNode("Program"))
    assert diagnostics == []
