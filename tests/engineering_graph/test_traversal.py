from ueos.engineering_graph.traversal import breadth_first
from ueos.engineering_graph.graph_engine import EngineeringGraph

def test_breadth_first_returns_list():
    assert isinstance(breadth_first(EngineeringGraph(),"root"),list)
