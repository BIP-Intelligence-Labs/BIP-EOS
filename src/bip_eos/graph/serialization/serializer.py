"""Graph serializer."""
import json

def to_json(graph):
    return json.dumps(graph.stats(), indent=2)
