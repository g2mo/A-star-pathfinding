"""A* pathfinding algorithm implementation"""

import heapq
from .node import Node


class AStar:
    """A* pathfinding algorithm for 2D and 3D grids"""

    def __init__(self, grid):
        """
        Initialize A* pathfinder
        grid: 2D or 3D list where 0 = walkable, 1 = obstacle
        """
        self.grid = grid
        self._determine_dimensions()

    def _determine_dimensions(self):
        """Determine if grid is 2D or 3D and set dimensions"""
        if isinstance(self.grid[0][0], list):
            # 3D grid
            self.is_3d = True
            self.depth = len(self.grid)
            self.rows = len(self.grid[0]) if self.depth > 0 else 0
            self.cols = len(self.grid[0][0]) if self.rows > 0 else 0
        else:
            # 2D grid
            self.is_3d = False
            self.rows = len(self.grid)
            self.cols = len(self.grid[0]) if self.rows > 0 else 0
            self.depth = None

    def heuristic(self, node1, node2):
        """Calculate heuristic distance (Manhattan distance)"""
        if self.is_3d:
            return abs(node1.x - node2.x) + abs(node1.y - node2.y) + abs(node1.z - node2.z)
        else:
            return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def get_neighbors(self, node):
        """Get valid neighboring nodes"""
        neighbors = []

        if self.is_3d:
            # 6-directional movement for 3D
            directions = [
                (1, 0, 0), (-1, 0, 0),  # x-axis
                (0, 1, 0), (0, -1, 0),  # y-axis
                (0, 0, 1), (0, 0, -1)  # z-axis
            ]

            for dx, dy, dz in directions:
                nx, ny, nz = node.x + dx, node.y + dy, node.z + dz

                if (0 <= nx < self.depth and
                        0 <= ny < self.rows and
                        0 <= nz < self.cols and
                        self.grid[nx][ny][nz] == 0):
                    neighbors.append(Node(nx, ny, nz))
        else:
            # 4-directional movement for 2D
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                nx, ny = node.x + dx, node.y + dy

                if (0 <= nx < self.rows and
                        0 <= ny < self.cols and
                        self.grid[nx][ny] == 0):
                    neighbors.append(Node(nx, ny))

        return neighbors

    def reconstruct_path(self, node):
        """Reconstruct path from start to goal"""
        path = []
        current = node
        while current:
            path.append(current.coords)
            current = current.parent
        return path[::-1]  # Reverse to get path from start to goal

    def find_path(self, start, goal):
        """
        Find shortest path from start to goal using A*
        start: tuple (x, y) or (x, y, z)
        goal: tuple (x, y) or (x, y, z)
        Returns: list of tuples representing the path
        """
        # Create start and goal nodes
        start_node = Node(*start)
        goal_node = Node(*goal)

        # Check if start and goal are valid
        if self.is_3d:
            if (self.grid[start[0]][start[1]][start[2]] == 1 or
                    self.grid[goal[0]][goal[1]][goal[2]] == 1):
                return None
        else:
            if (self.grid[start[0]][start[1]] == 1 or
                    self.grid[goal[0]][goal[1]] == 1):
                return None

        # Initialize start node
        start_node.g = 0
        start_node.h = self.heuristic(start_node, goal_node)
        start_node.f = start_node.g + start_node.h

        # Open set (nodes to be evaluated)
        open_set = []
        heapq.heappush(open_set, start_node)

        # Closed set (nodes already evaluated)
        closed_set = set()

        # Keep track of all nodes
        all_nodes = {start: start_node}

        while open_set:
            current = heapq.heappop(open_set)

            # Check if we reached the goal
            if current == goal_node:
                return self.reconstruct_path(current)

            closed_set.add(current.coords)

            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                neighbor_tuple = neighbor.coords

                # Skip if already evaluated
                if neighbor_tuple in closed_set:
                    continue

                # Calculate tentative g score
                tentative_g = current.g + 1  # Cost to move to neighbor is 1

                # Get or create neighbor node
                if neighbor_tuple not in all_nodes:
                    all_nodes[neighbor_tuple] = neighbor
                neighbor = all_nodes[neighbor_tuple]

                # Update neighbor if we found a better path
                if tentative_g < neighbor.g:
                    neighbor.parent = current
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor, goal_node)
                    neighbor.f = neighbor.g + neighbor.h

                    # Add to open set if not already there
                    if neighbor not in open_set:
                        heapq.heappush(open_set, neighbor)

        return None  # No path found
