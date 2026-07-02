"""Graph statistics CLI."""

from ueos.engineering_graph.graph_engine import EngineeringGraph


def main():
    graph = EngineeringGraph()
    print(graph.stats())


if __name__ == "__main__":
    main()
