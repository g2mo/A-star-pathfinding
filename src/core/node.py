"""Node representation for pathfinding algorithms"""


class Node:
    """Represents a cell in the grid"""

    def __init__(self, *coords):
        """
        Initialize a node with coordinates.
        Supports both 2D (x, y) and 3D (x, y, z) coordinates.
        """
        if len(coords) == 2:
            self.x, self.y = coords
            self.z = None
            self.coords = (self.x, self.y)
        elif len(coords) == 3:
            self.x, self.y, self.z = coords
            self.coords = (self.x, self.y, self.z)
        else:
            raise ValueError("Node requires 2 or 3 coordinates")

        self.g = float('inf')  # Cost from start to this node
        self.h = 0  # Heuristic cost from this node to goal
        self.f = float('inf')  # Total cost (g + h)
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)
