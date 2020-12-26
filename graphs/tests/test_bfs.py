from graphs.graph import Graph
from graphs.node import Node
from graphs.edge import Edge
from graphs.scripts.bfs import breadth_first_search
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
    actual_path = breadth_first_search(start=Node("a"), target=Node("f"), graph=graph)
    assert actual_path == expected_path

def test_target_not_in_graph():
    graph = get_default_graph()
    expected_path = ["a","c","f"]
    with raises(ValueError):
        breadth_first_search(start=Node("a"), target=Node("g"), graph=graph)

def test_start_not_in_graph():
    graph = get_default_graph()
    with raises(ValueError):
        breadth_first_search(start=Node("w"), target=Node("f"), graph=graph)

def test_cyclic_graph_small():
    graph = Graph()
    nodes = [["a","b"],["b","a"]]
    graph.make_unweighted_from_list(nodes)
    expected_path = ["a","b"]
    actual_path = breadth_first_search(start=Node("a"), target=Node("b"), graph=graph)
    assert actual_path == expected_path

def test_cyclic_graph_large():
    graph = Graph()
    nodes = [["a","b"],["b","c"],["c","d"],["d","e"],["d","a"],["a","d"],["e","z"],["z","a"]]
    graph.make_unweighted_from_list(nodes)
    expected_path = ["a","d","e","z"]
    actual_path = breadth_first_search(start=Node("a"), target=Node("z"), graph=graph)
    assert actual_path == expected_path

def test_no_path_from_start_to_target():
    graph = get_default_graph()
    expected_path = []
    actual_path = breadth_first_search(start=Node("b"), target=Node("a"), graph=graph)
    assert actual_path == expected_path
