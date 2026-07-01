from bip_eos.engineering_graph.repository_graph import RepositoryGraph

def test_repository_graph_creation():
    graph = RepositoryGraph()
    assert graph.node_count() == 0
    assert graph.edge_count() == 0
