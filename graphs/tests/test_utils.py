from graphs.graph import Graph

def get_default_graph(directed=True):
    graph = Graph()
    nodes = [["a","b"],["a","c"],["a","d"],["b","e"],["b","d"],["c","f"]]
    graph.make_unweighted_from_list(nodes, directed)
    return graph


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
