from graphs.graph import Graph, DijkstrasException
from graphs.node import Node
from graphs.edge import Edge
from collections import defaultdict
from pytest import raises
from graphs.tests.test_utils import compare_graphs, get_default_graph

def test_straight_line_graph():
    # a straight line graph is one that has only one path at each node
    graph = Graph()
    nodes = [["a","b",1],["b","c",1]]
    graph.make_weighted_from_list(nodes)
    expected_path = ["a","b","c"]
    actual_path = graph.dijkstras_with_target(Node("a"),Node("c"))
    assert actual_path == expected_path
   

def test_cyclic_graph():
    graph = Graph()
    nodes = [["a","b"], ["b","c"], ["b", "a"], ["b", "z"], ["c", "d"], ["c", "e"], ["e", "a"]]
    graph.make_unweighted_from_list(nodes)
    expected_path = ["a", "b", "c", "e"]
    actual_path = graph.dijkstras_with_target(start=Node("a"), target=Node("e"))
    assert actual_path == expected_path
    
def test_strongly_connected_graph():
    graph = Graph()
    nodes = []
    nodes_to_add = set(["a","b","c","d","e","f","g","h","i"])
    for node in nodes_to_add:
        for other_node in nodes_to_add:
            if other_node != node:
                nodes.append([node,other_node])
    graph = Graph()
    graph.make_unweighted_from_list(nodes, directed=False)
    actual_path = graph.dijkstras_with_target(start = Node("f"), target = Node("i"))
    expected_path = ["f","i"]
    assert actual_path == expected_path

def test_no_path():
    graph = Graph()
    nodes = [["a","b"], ["c", "d"]]
    graph.make_unweighted_from_list(nodes)
    actual_path = graph.dijkstras_with_target(start=Node("a"), target=Node("d"))
    expected_path = []
    assert actual_path == expected_path

def test_with_disconnected_nodes():
    graph = Graph()
    nodes = [["a"], ["b"]]
    graph.make_unweighted_from_list(nodes)
    actual_path = graph.dijkstras_with_target(start=Node("a"), target=Node("b"))
    expected_path = []
    assert actual_path == expected_path

def test_fails_with_negative_weights():
    graph = Graph()
    nodes = [["a","b", -1], ["c", "d", 4]]
    graph.make_weighted_from_list(nodes)
    with raises(DijkstrasException):
        graph.dijkstras_with_target(start=Node("a"), target=Node("b"))

def test_passes_with_unused_negative_weights():
    graph = Graph()
    nodes = [["a","b", 4], ["c", "d", -1]]
    graph.make_weighted_from_list(nodes)
    actual_path = graph.dijkstras_with_target(start=Node("a"), target=Node("b"))
    expected_path = ["a", "b"]
    assert actual_path == expected_path

def test_large_vs_known_implementation():
    """
    Creates a large random graph and runs dijkstra's algorithm with this implementation
    as well as a known good implementation I grabbed from github. Compares that the results
    returned are the same
    """
    import random
    size = 1000
    my_graph = Graph()
    my_nodes = []
    other_graph = OtherGraph()
    for i in range(size):
        start_node = i
        end_node = random.randint(0, size)
        length = random.randrange(0, 10000)
        my_nodes.append([start_node, end_node, length])
        other_graph.add_edge(start_node, end_node, length)
    
    my_graph.make_weighted_from_list(my_nodes)
    my_prev, my_unvisited = my_graph.dijkstra(start=Node(0))
    other_visited, other_prev = known_dijkstras_implementation(other_graph, 0)
    unvisited_diff = my_unvisited.keys() - other_visited.keys()
    visited_diff = other_visited.keys() - my_unvisited.keys()
    
    assert my_prev == other_prev and my_unvisited.keys() == unvisited_diff and other_visited.keys() == visited_diff

"""
Both this graph class and the dijkstra's implementation below were borrowed from github 
at this link
https://gist.github.com/econchick/4666413
"""
class OtherGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        if from_node not in self.nodes:
            self.nodes.add(from_node)
        if to_node not in self.nodes:
            self.nodes.add(to_node)
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def known_dijkstras_implementation(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes: 
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

