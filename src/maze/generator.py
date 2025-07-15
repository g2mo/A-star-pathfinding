"""Maze generation utilities"""

import random


class MazeGenerator:
    """Generate random mazes using recursive backtracking (2D) or sparse obstacles (3D)"""

    def __init__(self, width, height, depth=None):
        """
        Initialize maze generator
        width: maze width (should be odd for proper 2D generation)
        height: maze height (should be odd for proper 2D generation)
        depth: maze depth for 3D (None for 2D)
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.is_3d = depth is not None

        if self.is_3d:
            # Initialize 3D grid with all empty (0s) - we'll add obstacles
            self.grid = [[[0 for _ in range(width)] for _ in range(height)] for _ in range(depth)]
        else:
            # Initialize 2D grid with all walls (1s)
            self.grid = [[1 for _ in range(width)] for _ in range(height)]

    def generate(self):
        """Generate a random maze"""
        if self.is_3d:
            return self._generate_3d()
        else:
            return self._generate_2d()

    def _generate_2d(self):
        """Generate a 2D maze using recursive backtracking"""
        # Start from a random cell
        start_x = random.randint(0, self.height - 1)
        start_y = random.randint(0, self.width - 1)

        # Carve out the starting cell
        self.grid[start_x][start_y] = 0

        # Stack for backtracking
        stack = [(start_x, start_y)]

        while stack:
            current_x, current_y = stack[-1]

            # Get unvisited neighbors
            neighbors = self._get_unvisited_neighbors_2d(current_x, current_y)

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
        self._clear_area_2d(0, 0)
        self._clear_area_2d(self.height - 1, self.width - 1)

        return self.grid

    def _generate_3d(self):
        """Generate a simple 3D maze with sparse obstacles"""
        # Start with all empty space (done in __init__)

        # Add some pillar obstacles (vertical columns)
        num_pillars = min(8, (self.height * self.width) // 20)
        for _ in range(num_pillars):
            x = random.randint(2, self.depth - 3)
            y = random.randint(2, self.height - 3)
            # Create a pillar through multiple z levels
            pillar_height = random.randint(3, min(7, self.width - 2))
            start_z = random.randint(0, self.width - pillar_height)
            for z in range(start_z, start_z + pillar_height):
                self.grid[x][y][z] = 1

        # Add some floating blocks
        num_blocks = min(10, (self.depth * self.height * self.width) // 100)
        for _ in range(num_blocks):
            x = random.randint(1, self.depth - 2)
            y = random.randint(1, self.height - 2)
            z = random.randint(1, self.width - 2)
            # Create a small 2x2x2 or 3x3x3 block
            block_size = random.choice([2, 3])
            for dx in range(block_size):
                for dy in range(block_size):
                    for dz in range(block_size):
                        nx, ny, nz = x + dx, y + dy, z + dz
                        if (0 < nx < self.depth - 1 and
                                0 < ny < self.height - 1 and
                                0 < nz < self.width - 1):
                            self.grid[nx][ny][nz] = 1

        # Add some wall segments
        num_walls = min(6, (self.height + self.width) // 4)
        for _ in range(num_walls):
            if random.random() < 0.5:
                # Horizontal wall (along x)
                y = random.randint(1, self.height - 2)
                z = random.randint(1, self.width - 2)
                length = random.randint(3, self.depth // 2)
                start_x = random.randint(0, self.depth - length)
                for x in range(start_x, start_x + length):
                    self.grid[x][y][z] = 1
            else:
                # Horizontal wall (along y)
                x = random.randint(1, self.depth - 2)
                z = random.randint(1, self.width - 2)
                length = random.randint(3, self.height // 2)
                start_y = random.randint(0, self.height - length)
                for y in range(start_y, start_y + length):
                    self.grid[x][y][z] = 1

        # Ensure start and goal areas are clear
        self._clear_area_3d(0, 0, 0, radius=1)
        self._clear_area_3d(self.depth - 1, self.height - 1, self.width - 1, radius=1)

        return self.grid

    def _get_unvisited_neighbors_2d(self, x, y):
        """Get unvisited neighbors that are 2 cells away"""
        neighbors = []
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if neighbor is within bounds and unvisited (still a wall)
            if 0 <= nx < self.height and 0 <= ny < self.width and self.grid[nx][ny] == 1:
                neighbors.append((nx, ny))

        return neighbors

    def _clear_area_2d(self, x, y, radius=1):
        """Clear a small area around a point in 2D"""
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width:
                    self.grid[nx][ny] = 0

    def _clear_area_3d(self, x, y, z, radius=1):
        """Clear a small area around a point in 3D"""
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                for dz in range(-radius, radius + 1):
                    nx, ny, nz = x + dx, y + dy, z + dz
                    if (0 <= nx < self.depth and
                            0 <= ny < self.height and
                            0 <= nz < self.width):
                        self.grid[nx][ny][nz] = 0

    def add_random_paths(self, percentage=0.1):
        """Add some random paths to make the maze less perfect"""
        if self.is_3d:
            cells_to_clear = int(self.depth * self.height * self.width * percentage)

            for _ in range(cells_to_clear):
                x = random.randint(1, self.depth - 2)
                y = random.randint(1, self.height - 2)
                z = random.randint(1, self.width - 2)
                self.grid[x][y][z] = 0
        else:
            cells_to_clear = int(self.height * self.width * percentage)

            for _ in range(cells_to_clear):
                x = random.randint(1, self.height - 2)
                y = random.randint(1, self.width - 2)
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
