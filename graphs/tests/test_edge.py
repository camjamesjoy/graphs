from graphs.edge import Edge

def test_start_set():
    edge = Edge("a",None)
    assert "a" == edge.start
def test_end_set():
    edge = Edge(None,"b")
    assert "b" == edge.end
def test_weight_set():
    edge = Edge(None,None,99)
    assert edge.weight == 99
def test_default_weight():
    edge = Edge(None,None)
    assert edge.weight == 0
