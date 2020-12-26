
class Node:
    """
    Attributes:
        - name -> str
        - edges -> List[Edges]
    """
    def __init__(self, name="", edges=[]):
        self.name = name
        self.visited = False

    def __repr__(self):
        return(f"{self.name}")

    def __hash__(self):
        return(self.name.__hash__())

    def __eq__(self, other):
        try:
            return self.name == other.name
        except AttributeError:
            return self.name == other
