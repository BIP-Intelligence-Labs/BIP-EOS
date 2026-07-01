from bip_eos.engineering_graph.graph_engine import EngineeringGraph, GraphNode, GraphEdge

def test_graph_workflow():
    graph = EngineeringGraph()
    graph.add_node(GraphNode("repo","repository"))
    graph.add_node(GraphNode("pkg","package"))
    graph.add_edge(GraphEdge("repo","pkg","contains"))

    assert graph.node_count() == 2
    assert graph.edge_count() == 1
    assert graph.neighbors("repo")[0].id == "pkg"
