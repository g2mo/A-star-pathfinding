"""Maze generation utilities"""

import random


class MazeGenerator:
    """Generate random mazes using recursive backtracking"""

    def __init__(self, width, height, depth=None):
        """
        Initialize maze generator
        width: maze width (should be odd for proper generation)
        height: maze height (should be odd for proper generation)
        depth: maze depth for 3D (should be odd, None for 2D)
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.is_3d = depth is not None

        if self.is_3d:
            # Initialize 3D grid with all walls (1s)
            self.grid = [[[1 for _ in range(width)] for _ in range(height)] for _ in range(depth)]
        else:
            # Initialize 2D grid with all walls (1s)
            self.grid = [[1 for _ in range(width)] for _ in range(height)]

    def generate(self):
        """Generate a random maze using recursive backtracking"""
        if self.is_3d:
            # 3D generation not implemented in V2
            raise NotImplementedError("3D maze generation not yet implemented")

        # Start from a random cell
        start_x = random.randint(0, self.height-1)
        start_y = random.randint(0, self.width-1)

        # Carve out the starting cell
        self.grid[start_x][start_y] = 0

        # Stack for backtracking
        stack = [(start_x, start_y)]

        while stack:
            current_x, current_y = stack[-1]

            # Get unvisited neighbors
            neighbors = self._get_unvisited_neighbors(current_x, current_y)

            if neighbors:
                # Choose a random neighbor
                next_x, next_y = random.choice(neighbors)

                # Remove wall between current and chosen neighbor
                wall_x = (current_x + next_x) // 2
                wall_y = (current_y + next_y) // 2
                self.grid[wall_x][wall_y] = 0
                self.grid[next_x][next_y] = 0

                # Add neighbor to stack
                stack.append((next_x, next_y))
            else:
                # Backtrack
                stack.pop()

        # Ensure start and goal areas are clear
        self._clear_area(0, 0)
        self._clear_area(self.height-1, self.width-1)

        return self.grid

    def _get_unvisited_neighbors(self, x, y):
        """Get unvisited neighbors that are 2 cells away"""
        neighbors = []
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if neighbor is within bounds and unvisited (still a wall)
            if 0 <= nx < self.height and 0 <= ny < self.width and self.grid[nx][ny] == 1:
                neighbors.append((nx, ny))

        return neighbors

    def _clear_area(self, x, y, radius=1):
        """Clear a small area around a point"""
        for dx in range(-radius, radius+1):
            for dy in range(-radius, radius+1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width:
                    self.grid[nx][ny] = 0

    def add_random_paths(self, percentage=0.1):
        """Add some random paths to make the maze less perfect"""
        cells_to_clear = int(self.height * self.width * percentage)

        for _ in range(cells_to_clear):
            x = random.randint(1, self.height-2)
            y = random.randint(1, self.width-2)
            self.grid[x][y] = 0

    @staticmethod
    def create_sample_maze():
        """Create a sample 2D maze for testing"""
        return [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
