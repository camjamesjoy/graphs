
class Edge:
    """
    Represents the connection from one node to another
    can be directed or undirected, weighted or unweighted
    Attributes:
        - end -> Node
        - weight -> int
    """
    def __init__(self, start, end, weight=0):
        self.end = end
        self.start = start
        self.weight = weight

    def __repr__(self):
        if self.weight == 0:
            return f"{self.end}"
        return f"{self.end} : {self.weight}"

    def __eq__(self, other):

        try:
            return self.end == other.end and self.weight == other.weight
        except AttributeError:
            return False
