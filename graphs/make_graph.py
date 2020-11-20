from node import Node
from edge import Edge


class Graph:


    def __init__(self):
        self.graph = {}

    def make_unweighted_from_list(self, nodes, directed=True):
        """
        accepts a list of pairs of nodes and creates a graph from it
        ex: [[a,b][a,c][b,c]]
        """
        for path in nodes:
            self.add_node(path, directed=directed)


    def add_node(self, path, weight=0, directed=True):
        """
        takes a list [start, end] and creates node objects and adds the values
        to the graph if they are not already a part of the graph
        """
        start = path[0]
        end = path[1]

        start_node = Node(start)
        end_node = Node(end)
        edge = Edge(end=end_node, weight=weight)
        print(edge.weight)

        if start_node in self.graph:
            self.graph[start_node].append(edge)
        else:
            self.graph[start_node] = [edge]

        if end_node not in self.graph and directed:
            self.graph[end_node] = []
        elif not directed:
            edge = Edge(end=start_node, weight=weight)
            if end_node not in self.graph:
                self.graph[end_node] = [edge]
            elif end_node in self.graph:
                self.graph[end_node].append(edge)


    def remove_node(self, node):
        """
        takes a node object or a list a string representing the node to remove
        """
        if node in self.graph or node.name in self.graph:
            del self.graph[node]
        for edges in self.graph.values():
            for edge in edges:
                if edge.end == node:
                    edges.remove(edge)


    def make_weighted_from_list(self, nodes, directed=True):
        """
        accepts a list of pairs of nodes and weights and creates a graph from it
        ex: [[a,b,1][a,c,2][b,c,9]]
        """
        for path in nodes:
            if len(path) == 3:
                weight = path[2]
                self.add_node(path, weight=weight, directed=directed)
            else:
                print(f"{path} does not have a weight this function is for weighted graphs only")
                continue



def test_unweighted_graph():
    print("testing make unweighted graph")
    def test_directed():
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"]]
        graph.make_unweighted_from_list(nodes)
        test_graph = {"a":["b","c"], "b":["c"], "c":[]}
        assert graph.graph == test_graph

    def test_undirected():
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"]]
        graph.make_unweighted_from_list(nodes, False)
        test_graph = {"a":["b","c"], "b":["a","c"], "c":["b","a"]}
        assert graph.graph == test_graph

    def test_list_of_int():
        graph = Graph()
        nodes = [[1, 2], [2, 3], [3, 5], [5, 1], [2,5]]
        graph.make_unweighted_from_list(nodes)
        test_graph = {1:[2], 2:[3, 5], 3:[5], 5:[1]}
        assert graph.graph == test_graph

    def test_edges_set():
        test_graph = {"a":["b","c"], "b":["c"], "c":[]}
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
        test_graph = {"a":["b","c"], "b":["c","b"], "c":[]}
        assert test_graph == graph.graph

    def test_remove_node_str():
        # make a graph. remove node and assert its equal what it should be
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"],["c","a"]]
        graph.make_unweighted_from_list(nodes)
        graph.remove_node("a")
        test_graph = {"b":["c"], "c":[]}
        assert graph.graph == test_graph

    def test_remove_node_node():
        graph = Graph()
        nodes = [["a","b"],["b","c"],["a","c"],["c","a"]]
        graph.make_unweighted_from_list(nodes)
        graph.remove_node(Node("a"))
        test_graph = {"b":["c"], "c":[]}
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
    def test_directed():
        graph = Graph()
        nodes = [["a","b",1],["b","c",2],["a","c",3]]
        graph.make_weighted_from_list(nodes)
        test_graph = {
                     Node("a"):[Edge("b",1),Edge("c",2)],
                     Node("b"):[Edge("c",2)],
                     Node("c"):[]
                     }
        print(graph.graph)
        print(test_graph)
        assert graph.graph == test_graph

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

def test_node():
    print("testing node class")
    def test_name_set():
        node = Node()
        node.name = "node"
        assert node.name == "node"
    def test_edges_set():
        node = Node()
        node.edges = [["a","b"], ["b","c"]]
        assert node.edges == [["a","b"], ["b","c"]]
    test_name_set()
    test_edges_set()
    print("node tests passed")

def test_edge():
    print("testing edge class")
    def test_start_set():
        edge = Edge()
        edge.start = "a"
        assert "a" == edge.start
    def test_end_set():
        edge = Edge()
        edge.end = "b"
        assert "b" == edge.end
    def test_weight_set():
        edge = Edge()
        edge.weight = 99
        assert edge.weight == 99
    def test_default_weight():
        edge = Edge()
        assert edge.weight == 0
    test_start_set()
    test_end_set()
    test_weight_set()
    test_default_weight()
    print("edge tests passed")


if __name__ == "__main__":
    test_weighted_graph()
    #test_unweighted_graph()
    #test_node()
    #test_edge()
