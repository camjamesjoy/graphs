from graphs.make_graph import Graph
from graphs.node import Node
from graphs.edge import Edge

def compare_graphs(expected_graph, actual_graph):
    for node in expected_graph:
        try:
            for actual_edge, expected_edge in zip(actual_graph[node], expected_graph[node]):
                print(f"actual edge is {actual_edge}")
                print(f"expected edge is {expected_edge}")
                if actual_edge != expected_edge:
                    return False
        except KeyError:
            print(f"node {node} is not in the actual graph")
            return False
    return True

def test_unweighted_graph():
    print("testing make unweighted graph")
    def test_directed():
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"]]
        graph.make_unweighted_from_list(nodes)
        test_graph = {
                     Node("a"):[Edge("a","b"),Edge("a","c")],
                     Node("b"):[Edge("b","c")],
                     Node("c"):[]
                     }
        assert graph.graph == test_graph

    def test_undirected():
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"]]
        graph.make_unweighted_from_list(nodes, False)
        test_graph = {
                     Node("a"):[Edge("a","b"),Edge("a","c")],
                     Node("b"):[Edge("b","a"),Edge("b","c")],
                     Node("c"):[Edge("c","b"),Edge("c","a")]
                     }
        assert graph.graph == test_graph

    def test_list_of_int():
        graph = Graph()
        nodes = [[1, 2], [2, 3], [3, 5], [5, 1], [2,5]]
        graph.make_unweighted_from_list(nodes)
        test_graph = {
                     Node(1):[Edge(1,2)],
                     Node(2):[Edge(2,3), Edge(2,5)],
                     Node(3):[Edge(3,5)],
                     Node(5):[Edge(5,1)]}
        assert graph.graph == test_graph

    def test_edges_set():
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

    def test_add_node():
        # make the same graph as one of the ones above
        # add a node and assert its equal
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"]]
        graph.make_unweighted_from_list(nodes)
        graph.add_node(["b","b"])
        print(graph.graph)
        test_graph = {
                      Node("a"):[Edge("a","b"),Edge("a","c")],
                      Node("b"):[Edge("b","c"),Edge("b","b")],
                      Node("c"):[]
                     }
        assert test_graph == graph.graph

    def test_remove_node_str():
        # make a graph. remove node and assert its equal what it should be
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"],["c","a"]]
        graph.make_unweighted_from_list(nodes)
        graph.remove_node("a")
        test_graph = {Node("b"):[Edge("b","c")], Node("c"):[]}
        assert graph.graph == test_graph

    def test_remove_node_node():
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"],["c","a"]]
        graph.make_unweighted_from_list(nodes)
        graph.remove_node(Node("a"))
        test_graph = {Node("b"):[Edge("b","c")], Node("c"):[]}
        assert graph.graph == test_graph
    test_directed()
    test_undirected()
    test_list_of_int()
    test_edges_set()
    test_add_node()
    test_remove_node_str()
    test_remove_node_node()
    print("unweighted graph tests pass")

def test_weighted_graph():
    print("testing weighted graphs")
    def test_directed():
        graph = Graph()
        nodes = [["a","b",1],["b","c",2],["a","c",3]]
        graph.make_weighted_from_list(nodes)
        test_graph = {
                     Node("a"):[Edge("a", "b",1),Edge("a","c",3)],
                     Node("b"):[Edge("b","c",2)],
                     Node("c"):[]
                     }
        print(graph.graph)
        print(test_graph)
        assert compare_graphs(test_graph, graph.graph) == True

    def test_undirected():
        pass

    def test_list_of_int():
        pass

    def test_list_of_nodes():
        pass

    def test_add_node():
        pass

    def test_remove_node():
        pass

    def test_modify_weight():
        pass
    test_directed()
    test_undirected()
    test_list_of_nodes()
    test_add_node()
    test_remove_node()
    test_modify_weight()
    print("weighted graph tests passed")


test_weighted_graph()
test_unweighted_graph()
