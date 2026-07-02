from ueos.engineering_graph.node import Node,NodeType

def test_node_label():
    n=Node("1","runtime",NodeType.MODULE)
    assert "runtime" in n.label

def test_node_dict_roundtrip():
    n=Node("1","runtime",NodeType.MODULE)
    assert Node.from_dict(n.to_dict()).name=="runtime"
