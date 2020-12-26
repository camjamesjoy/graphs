from graphs.node import Node

def test_name_set():
    node = Node()
    node.name = "node"
    assert node.name == "node"
def test_edges_set():
    node = Node()
    node.edges = [["a","b"], ["b","c"]]
    assert node.edges == [["a","b"], ["b","c"]]
