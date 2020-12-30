from graphs.graph import Graph
from graphs.node import Node
from graphs.edge import Edge
from graphs.scripts.dfs import depth_first_search
from graphs.tests.test_graph import compare_graphs
from pytest import raises

def get_default_graph():
    graph = Graph()
    nodes = [["a","b"],["a","c"],["a","d"],["b","e"],["b","d"],["c","f"]]
    graph.make_unweighted_from_list(nodes)
    return graph

def test_find_node_in_graph():
    graph = get_default_graph()
    expected_path = ["a","c","f"]
    actual_path = depth_first_search(start=Node("a"), target=Node("f"), graph=graph)
    assert actual_path == expected_path
