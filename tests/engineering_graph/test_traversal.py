from bip_eos.engineering_graph.traversal import breadth_first
from bip_eos.engineering_graph.graph_engine import EngineeringGraph

def test_breadth_first_returns_list():
    assert isinstance(breadth_first(EngineeringGraph(),"root"),list)
