from graphs.graph import Graph
from graphs.node import Node
from graphs.edge import Edge
from graphs.tests.test_utils import compare_graphs, get_default_graph

def test_straight_line_graph():
    # a straight line graph is one that has only one path at each node
    graph = Graph()
    nodes = [["a","b",1],["b","c",1]]
    graph.make_weighted_from_list(nodes)
    expected_path = ["a","b","c"]
    print(graph.graph)
    actual_path = graph.dijkstra(Node("a"),Node("c"))
    assert actual_path == expected_path