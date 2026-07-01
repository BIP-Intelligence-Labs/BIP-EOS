from bip_eos.engineering_graph.query_engine import GraphQueryEngine
from bip_eos.engineering_graph.graph_engine import EngineeringGraph

def test_query_engine_construct():
    q=GraphQueryEngine(EngineeringGraph())
    assert q.graph is not None
