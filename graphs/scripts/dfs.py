from graphs.graph import Graph

"""
Searches a graph for a given node using depth first search
"""

def depth_first_search(graph, start, target):
    """
    Searches a graph for the given target node starting from the given start node

    graph: A graph to search of type Graph
    start: Node to start search from of type Node
    target: Node to search for of type Node
    """
    #TODO lots of reused error checking should probably abstract this out
    if start not in graph.graph:
        raise ValueError(f"Given start node {start} is not in the graph")
    if target not in graph.graph:
        raise ValueError(f"Given start node {target} is not in the graph")

    graph.reset_visited()
    path = []
    def dfs_recurse(curr_node, path):
        curr_node.visited = True
        path.append(curr_node)
        print(path)
        if curr_node == target:
            return path
        for neighbor in graph.graph[curr_node]:
            if neighbor.end.visited == False:
                return dfs_recurse(neighbor.end, path)
        path.pop()
    output = dfs_recurse(start, [])
    return output
