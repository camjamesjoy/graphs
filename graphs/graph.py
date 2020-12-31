from .node import Node
from .edge import Edge
from queue import Queue


class Graph:

    def __init__(self):
        self.graph = {}

    def reset_visited(self):
        """
        after doing a search algorithm often times nodes will be marked as
        visited. This marks all nodes as not visited, typically done before
        or after a search is done
        """
        for node in self.graph.keys():
            node.visited = False
            for edge in self.graph[node]:
                edge.end.visited = False
                edge.start.visited = False

    def make_unweighted_from_list(self, nodes, directed=True):
        """
        accepts a list of pairs of nodes and creates a graph from it
        ex: [[a,b][a,c][b,c]]
        """
        for path in nodes:
            self.add_node(path, directed=directed)

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

    def add_node(self, path, weight=0, directed=True):
        """
        takes a list [start, end] and creates node objects and adds the values
        to the graph if they are not already a part of the graph
        """
        start = path[0]
        start_node = Node(start)
        if len(path) == 1:
            if start_node not in self.graph:
                self.graph[start_node] = []
            return

        end = path[1]
        end_node = Node(end)
        if len(path) == 3:
            weight = path[2]



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

    def modify_weight(self, edge, new_weight):
        """
        accepts a list representing an edge and searches for that edge in the
        graph. If the edge is in the graph, all edges with the values represented
        by the list have their weight value updated to new_weight

        edge: list of the format ["start","end",weight]. Note that the start and
              end do not need to be str and weight does not need to be int. The
              weight should be the old weight not the new weight that it will be
              set to
        new_weight: int representing weight
        """
        edge = Edge(edge[0], edge[1], edge[2])
        if edge.start not in self.graph:
            print(f"{edge} is not in graph cannot modify its weight")
        possible_edges = self.graph[edge.start]
        for possible_edge in possible_edges:
            if edge == possible_edge:
                possible_edge.weight = new_weight

    def depth_first_search(self, start, target):
        """
        Searches a graph for the given target node starting from the given start node

        graph: A graph to search of type Graph
        start: Node to start search from of type Node
        target: Node to search for of type Node
        """
        #TODO lots of reused error checking should probably abstract this out
        if start not in self.graph:
            raise ValueError(f"Given start node {start} is not in the graph")
        if target not in self.graph:
            raise ValueError(f"Given start node {target} is not in the graph")

        self.reset_visited()
        def dfs_recurse(curr_node, path, solution):
            curr_node.visited = True
            path.append(curr_node)
            if curr_node == target:
                return path
            for neighbor in self.graph[curr_node]:
                if neighbor.end.visited == False and neighbor.end != start:
                    solution = dfs_recurse(neighbor.end, path, solution)
                    if solution and solution[-1] == target:
                        return solution
            path.pop()
            return solution

        solution = dfs_recurse(start, [], [])
        self.reset_visited()
        return solution

    def breadth_first_search(self, start, target):
        """
        Searches a graph for the given target node starting from the given start node

        graph: A graph to search of type Graph
        start: Node to start search from of type Node
        target: Node to search for of type Node
        """
        if start not in self.graph:
            raise ValueError(f"Given start node {start} is not in the graph")
        if target not in self.graph:
            raise ValueError(f"Given start node {target} is not in the graph")

        next_nodes = Queue()
        self.reset_visited()
        next_nodes.put([start]) # make queue of lists so we can append to paths
        while not next_nodes.empty():
            path = next_nodes.get()
            curr_node = path[-1]
            if curr_node.visited == False:
                curr_node.visited = True
                if curr_node == target:
                    self.reset_visited()
                    return path
                for neighbor in self.graph[curr_node]:
                    if not neighbor.start.visited:
                        next_nodes.put(path + [neighbor.end])
        self.reset_visited()
        return []
