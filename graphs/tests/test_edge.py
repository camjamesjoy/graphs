from graphs.edge import Edge
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
test_edge()
