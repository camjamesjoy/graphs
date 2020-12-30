from graphs.graph import Graph
from queue import Queue

"""
Searches a Graph for a target node using a breadth first search approach.
"""

def breadth_first_search(graph, start, target):
    """
    Searches a graph for the given target node starting from the given start node

    graph: A graph to search of type Graph
    start: Node to start search from of type Node
    target: Node to search for of type Node
    """
    if start not in graph.graph:
        raise ValueError(f"Given start node {start} is not in the graph")
    if target not in graph.graph:
        raise ValueError(f"Given start node {target} is not in the graph")

    next_nodes = Queue()
    graph.reset_visited()
    next_nodes.put([start]) # make queue of lists so we can append to paths
    while not next_nodes.empty():
        path = next_nodes.get()
        curr_node = path[-1]
        if curr_node.visited == False:
            curr_node.visited = True
            if curr_node == target:
                graph.reset_visited()
                return path
            for neighbor in graph.graph[curr_node]:
                if not neighbor.start.visited:
                    next_nodes.put(path + [neighbor.end])
    graph.reset_visited()
    return []
