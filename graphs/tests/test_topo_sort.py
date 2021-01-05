from graphs.graph import Graph, CyclicGraphException
from graphs.node import Node
from graphs.edge import Edge
from graphs.tests.test_utils import compare_graphs, get_default_graph
from pytest import raises

def test_sort_default_graph():
    graph = get_default_graph()
    actual_path = graph.topological_sort()
    expected_path = ["a", "d", "c", "f", "b", "d", "e"]
    assert actual_path == expected_path

def test_cyclic_graph():
    graph = Graph()
    nodes = [["a","b"],["b","c"],["c","d"],["d","e"],["d","a"],["a","d"],["e","z"],["z","a"]]
    graph.make_unweighted_from_list(nodes)
    with raises(CyclicGraphException):
        actual_path = graph.topological_sort()
