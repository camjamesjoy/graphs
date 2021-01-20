
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

class PriorityNode:
    """
    A class that allows you to assign a priority to a Node
    Especially useful for putting nodes into a PriorityQueue
    """
    def __init__(self, node, priority):
        self.priority = priority
        self.node = node

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return(f"{self.node.name} has priority {self.priority}")
