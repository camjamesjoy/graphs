from graphs.graph import Graph
from graphs.node import Node
from graphs.edge import Edge
import pytest


def compare_graphs(expected_graph, actual_graph):
    if expected_graph.keys() != actual_graph.keys():
        print("The graphs do not contain the same keys")
        print("The following keys were expected but did not appear")
        print(expected_graph.keys() - actual_graph.keys())
        print("The following keys appeared but were not expected")
        print(actual_graph.keys() - expected_graph.keys())
        return False
    for node, actual_node in zip(expected_graph, actual_graph):
        if node.visited != actual_node.visited:
            print(node.visited)
            print(actual_node.visited)
            return False
        try:
            for actual_edge, expected_edge in zip(actual_graph[node], expected_graph[node]):

                if actual_edge != expected_edge:
                    print(f"actual edge is {actual_edge}")
                    print(f"expected edge is {expected_edge}")
                    return False
        except KeyError:
            print(f"node {node} is not in the actual graph")
            return False
    return True



def test_unweighted_directed():
    graph = Graph()
    nodes = [["a","b"],["b","c"],["a","c"]]
    graph.make_unweighted_from_list(nodes)
    test_graph = {
                 Node("a"):[Edge("a","b"),Edge("a","c")],
                 Node("b"):[Edge("b","c")],
                 Node("c"):[]
                 }
    assert compare_graphs(test_graph, graph.graph) == True

def test_unweighted_undirected():
    graph = Graph()
    nodes = [["a","b"],["b","c"],["a","c"]]
    graph.make_unweighted_from_list(nodes, False)
    test_graph = {
                 Node("a"):[Edge("a","b"),Edge("a","c")],
                 Node("b"):[Edge("b","a"),Edge("b","c")],
                 Node("c"):[Edge("c","b"),Edge("c","a")]
                 }
    assert compare_graphs(test_graph, graph.graph) == True

def test_unweighted_list_of_int():
    graph = Graph()
    nodes = [[1, 2], [2, 3], [3, 5], [5, 1], [2,5]]
    graph.make_unweighted_from_list(nodes)
    test_graph = {
                 Node(1):[Edge(1,2)],
                 Node(2):[Edge(2,3), Edge(2,5)],
                 Node(3):[Edge(3,5)],
                 Node(5):[Edge(5,1)]}
    assert compare_graphs(test_graph, graph.graph) == True

def test_unweighted_edges_set():
    test_graph = {
                 Node("a"):[Edge("a","b"),Edge("a","c")],
                 Node("b"):[Edge("b","c")],
                 Node("c"):[]
                 }
    graph = Graph()
    nodes = [["a","b"],["b","c"],["a","c"]]
    graph.make_unweighted_from_list(nodes)
    for node in graph.graph:
        assert graph.graph[node] == test_graph[node.name]

def test_unweighted_add_node():
    # make the same graph as one of the ones above
    # add a node and assert its equal
    graph = Graph()
    nodes = [["a","b"],["b","c"],["a","c"]]
    graph.make_unweighted_from_list(nodes)
    graph.add_node(["b","b"])
    test_graph = {
                  Node("a"):[Edge("a","b"),Edge("a","c")],
                  Node("b"):[Edge("b","c"),Edge("b","b")],
                  Node("c"):[]
                 }
    assert compare_graphs(test_graph, graph.graph) == True

def test_unweighted_remove_node_node():
    graph = Graph()
    nodes = [["a","b"],["b","c"],["a","c"],["c","a"]]
    graph.make_unweighted_from_list(nodes)
    graph.remove_node(Node("a"))
    test_graph = {Node("b"):[Edge("b","c")], Node("c"):[]}
    assert compare_graphs(test_graph, graph.graph) == True


def test_weighted_directed():
    graph = Graph()
    nodes = [["a","b",1],["b","c",2],["a","c",3]]
    graph.make_weighted_from_list(nodes)
    test_graph = {
                 Node("a"):[Edge("a", "b",1), Edge("a","c",3)],
                 Node("b"):[Edge("b","c",2)],
                 Node("c"):[]
                 }
    assert compare_graphs(test_graph, graph.graph) == True

def test_weighted_undirected():
    graph = Graph()
    nodes = [["a","b",1],["b","c",2],["a","c",3]]
    graph.make_weighted_from_list(nodes, directed=False)
    test_graph = {
                 Node("a"):[Edge("a", "b",1), Edge("a","c",3)],
                 Node("b"):[Edge("b","a",1), Edge("b","c",2)],
                 Node("c"):[Edge("c","b",2), Edge("c","a",3)]
                 }
    assert compare_graphs(test_graph, graph.graph) == True

def test_weighted_list_of_int():
    graph = Graph()
    nodes = [[1, 2, 99], [2, 3, 26], [3, 5, 130], [5, 1, 2], [2, 5, 0]]
    graph.make_unweighted_from_list(nodes)
    test_graph = {
                 Node(1):[Edge(1,2,99)],
                 Node(2):[Edge(2,3,26), Edge(2,5,0)],
                 Node(3):[Edge(3,5,130)],
                 Node(5):[Edge(5,1,2)]}
    assert compare_graphs(test_graph, graph.graph) == True

def test_weighted_add_node():
    graph = Graph()
    nodes = [["a","b",5],["b","c",4],["a","c",3]]
    graph.make_weighted_from_list(nodes)
    graph.add_node(["b","b",2])
    graph.add_node(["b","d",1])
    test_graph = {
                  Node("a"):[Edge("a","b",5),Edge("a","c",3)],
                  Node("b"):[Edge("b","c",4),Edge("b","b",2),Edge("b","d",1)],
                  Node("c"):[],
                  Node("d"):[]
                 }
    assert compare_graphs(test_graph, graph.graph) == True

def test_weighted_remove_node():
    graph = Graph()
    nodes = [["a","b",1],["b","b",99],["c","b",2],["d","b",3],["e","b",4],["f","z","a"]]
    graph.make_weighted_from_list(nodes)
    graph.remove_node(Node("b"))
    test_graph = {
                 Node("a"):[],
                 Node("c"):[],
                 Node("d"):[],
                 Node("e"):[],
                 Node("f"):[Edge("f","z","a")],
                 Node("z"): []
                 }
    assert compare_graphs(test_graph, graph.graph) == True

def test_weighted_modify_weight():
    graph = Graph()
    nodes = [["a","b",1],["b","c",2],["a","c",3]]
    graph.make_weighted_from_list(nodes)
    graph.modify_weight(["a","b",1], 78)
    test_graph = {
                 Node("a"):[Edge("a", "b",78), Edge("a","c",3)],
                 Node("b"):[Edge("b","c",2)],
                 Node("c"):[]
                 }

    assert compare_graphs(test_graph, graph.graph) == True

def test_reset_visited():
    nodes = [["a","b"]]
    graph = Graph()
    graph.make_unweighted_from_list(nodes)
    graph.reset_visited()
    new_graph = Graph()
    new_graph.make_unweighted_from_list(nodes)
    assert compare_graphs(new_graph.graph, graph.graph) == True
    for node in graph.graph:
        node.visited = True
    assert compare_graphs(new_graph.graph, graph.graph) == False

def test_add_single_node():
    nodes = [["a"]]
    graph = Graph()
    graph.make_unweighted_from_list(nodes)
    test_graph = {Node("a"):[]}
    assert compare_graphs(test_graph, graph.graph)
