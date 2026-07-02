from ueos.compiler.frontend.ast import ASTNode


def test_ast_node():
    node = ASTNode("Program")
    assert node.kind == "Program"
