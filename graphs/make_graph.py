from .node import Node
from .edge import Edge


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
        edge = Edge(start=start_node, end=end_node, weight=weight)

        if start_node in self.graph:
            self.graph[start_node].append(edge)
        else:
            self.graph[start_node] = [edge]

        if end_node not in self.graph and directed:
            self.graph[end_node] = []
        elif not directed:
            edge = Edge(start=end_node, end=start_node, weight=weight)
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
