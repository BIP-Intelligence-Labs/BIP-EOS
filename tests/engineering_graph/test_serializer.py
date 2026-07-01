from bip_eos.engineering_graph.serializer import to_json
from bip_eos.engineering_graph.graph_engine import EngineeringGraph

def test_serializer():
    assert "nodes" in to_json(EngineeringGraph())
