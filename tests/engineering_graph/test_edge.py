from bip_eos.engineering_graph.edge import Edge,EdgeType

def test_edge_creation():
    e=Edge("a","b",EdgeType.DEPENDS_ON)
    assert e.source=="a"
    assert e.target=="b"
