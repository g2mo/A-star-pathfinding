"""
A* Pathfinding Algorithm - Basic Implementation

This script implements the A* pathfinding algorithm for 2D grid-based navigation.
A* is an informed search algorithm that finds the optimal path between nodes
by combining the actual distance from start (g-score) with a heuristic estimate
to the goal (h-score).

Algorithm Overview:
    1. Maintain a priority queue (open set) of nodes to explore
    2. For each node, calculate f(n) = g(n) + h(n)
    3. Always explore the node with lowest f-score first
    4. Stop when goal is reached or no path exists

Author: Guglielmo Cimolai
Date: 03/07/2025
Version: 1
"""

import heapq
import math


class Node:
    """Represents a cell in the grid"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = float('inf') # Cost from start to this node
        self.h = 0 # Heuristic cost from this node to goal
        self.f = float('inf') # Total cost (g + h)
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class AStar:
    def __init__(self, grid):
        """
        Initialize A* pathfinder
        grid: 2D list where 0 = walkable, 1 = obstacle
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def heuristic(self, node1, node2):
        """Calculate heuristic distance (Manhattan distance)"""
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def get_neighbors(self, node):
        """Get valid neighboring nodes"""
        neighbors = []
        # 4-directional movement (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            nx, ny = node.x + dx, node.y + dy

            # Check if neighbor is within bounds and walkable
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0:
                neighbors.append(Node(nx, ny))

        return neighbors

    def reconstruct_path(self, node):
        """Reconstruct path from start to goal"""
        path = []
        current = node
        while current:
            path.append((current.x, current.y))
            current = current.parent
        return path[::-1] # Reverse to get path from start to goal

    def find_path(self, start, goal):
        """
        Find shortest path from start to goal using A*
        start: tuple (x, y)
        goal: tuple (x, y)
        Returns: list of tuples representing the path
        """
        # Create start and goal nodes
        start_node = Node(start[0], start[1])
        goal_node = Node(goal[0], goal[1])

        # Check if start and goal are valid
        if self.grid[start[0]][start[1]] == 1 or self.grid[goal[0]][goal[1]] == 1:
            return None # Start or goal is an obstacle

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
        all_nodes = {(start[0], start[1]): start_node}

        while open_set:
            current = heapq.heappop(open_set)

            # Check if we reached the goal
            if current == goal_node:
                return self.reconstruct_path(current)

            closed_set.add((current.x, current.y))

            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                neighbor_tuple = (neighbor.x, neighbor.y)

                # Skip if already evaluated
                if neighbor_tuple in closed_set:
                    continue

                # Calculate tentative g score
                tentative_g = current.g + 1 # Cost to move to neighbor is 1

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

        return None # No path found


def visualize_path(grid, path, start, goal):
    """Visualize the grid and path"""
    # Create a copy of the grid for visualization
    visual = [row[:] for row in grid]

    # Mark the path
    if path:
        for x, y in path:
            if (x, y) != start and (x, y) != goal:
                visual[x][y] = 2 # Path marker

    # Mark start and goal
    visual[start[0]][start[1]] = 3 # Start marker
    visual[goal[0]][goal[1]] = 4 # Goal marker

    # Print the grid
    symbols = {
        0: '.', # Walkable
        1: '#', # Obstacle
        2: '*', # Path
        3: 'S', # Start
        4: 'G'  # Goal
    }

    for row in visual:
        print(' '.join(symbols.get(cell, '?') for cell in row))


# Example usage
if __name__ == "__main__":
    # Create a sample grid (0 = walkable, 1 = obstacle)
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Define start and goal positions
    start = (0, 0)
    goal = (7, 7)

    # Create A* pathfinder and find path
    astar = AStar(grid)
    path = astar.find_path(start, goal)

    # Display results
    if path:
        print(f"Path found! Length: {len(path)}")
        print(f"Path: {path}")
    else:
        print("No path found!")

    print("\nVisualization:")
    visualize_path(grid, path, start, goal)
