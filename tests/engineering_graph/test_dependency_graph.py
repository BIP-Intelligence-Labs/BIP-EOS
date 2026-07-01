from bip_eos.engineering_graph.dependency_graph import DependencyGraph

def test_dependency_graph_creation():
    graph = DependencyGraph()
    assert graph.node_count() == 0
