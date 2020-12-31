from graphs.graph import Graph
from graphs.node import Node
from graphs.edge import Edge
from graphs.tests.test_utils import compare_graphs, get_default_graph
from pytest import raises

def test_find_node_in_graph():
    graph = get_default_graph()
    expected_path = ["a","c","f"]
    actual_path = graph.depth_first_search(start=Node("a"), target=Node("f"))
    assert actual_path == expected_path

def test_no_path():
    graph = get_default_graph()
    actual_path = graph.depth_first_search(start=Node("b"), target=Node("a"))
    expected_path = []
    assert actual_path == expected_path

def test_cyclic_graph():
    graph = Graph()
    nodes = [["a","b"],["b","c"],["c","d"],["d","e"],["d","a"],["a","d"],["e","z"],["z","a"]]
    graph.make_unweighted_from_list(nodes)
    expected_path = ["a","b","c","d","e","z"]
    actual_path = graph.depth_first_search(start=Node("a"), target=Node("z"))
    assert actual_path == expected_path

def test_cyclic_graph_no_path():
    graph = Graph()
    nodes = [["a","b"],["b","a"],["c"]]
    graph.make_unweighted_from_list(nodes)
    expected_path = []
    actual_path = graph.depth_first_search(start=Node("a"), target=Node("c"))
    assert actual_path == expected_path

def test_target_not_in_graph():
    graph = get_default_graph()
    with raises(ValueError):
        graph.depth_first_search(start=Node("a"), target=Node("g"))

def test_start_not_in_graph():
    graph = get_default_graph()
    with raises(ValueError):
        graph.depth_first_search(start=Node("w"), target=Node("f"))

def test_visited_reset():
    graph = get_default_graph()
    for node in graph.graph:
        assert node.visited == False
    actual_path = graph.depth_first_search(start=Node("b"), target=Node("a"))
    for node in graph.graph:
        assert node.visited == False

def test_undirected_graph():
    graph = get_default_graph(directed=False)
    expected_path = ["a","c","f"]
    actual_path = graph.depth_first_search(start=Node("a"), target=Node("f"))
    assert actual_path == expected_path

def test_start_is_target():
    graph = get_default_graph(directed=False) #shouldn't matter
    expected_path = ["f"]
    actual_path = graph.depth_first_search(start=Node("f"), target=Node("f"))
    assert actual_path == expected_path
