from ueos.engineering_graph.graph_engine import EngineeringGraph, GraphNode, GraphEdge

def test_empty_graph():
    g=EngineeringGraph()
    assert g.node_count()==0
    assert g.edge_count()==0

def test_add_node():
    g=EngineeringGraph()
    g.add_node(GraphNode("n1","module"))
    assert g.get_node("n1") is not None

def test_add_edge():
    g=EngineeringGraph()
    g.add_node(GraphNode("a","module"))
    g.add_node(GraphNode("b","module"))
    g.add_edge(GraphEdge("a","b","depends_on"))
    assert len(g.neighbors("a"))==1
