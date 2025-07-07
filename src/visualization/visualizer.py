"""Visualization utilities for pathfinding"""


class ConsoleVisualizer:
    """Text-based visualization for grids and paths"""

    @staticmethod
    def visualize_path(grid, path, start, goal):
        """Visualize the grid and path in console"""
        # Create a copy of the grid for visualization
        visual = [row[:] for row in grid]

        # Mark the path
        if path:
            for coords in path:
                if len(coords) == 2:  # 2D
                    x, y = coords
                    if (x, y) != start and (x, y) != goal:
                        visual[x][y] = 2  # Path marker
                else:  # 3D - for now just print coordinates
                    pass

        # Mark start and goal for 2D
        if len(start) == 2:
            visual[start[0]][start[1]] = 3  # Start marker
            visual[goal[0]][goal[1]] = 4  # Goal marker

        # Print the grid
        symbols = {
            0: '.',  # Walkable
            1: '#',  # Obstacle
            2: '*',  # Path
            3: 'S',  # Start
            4: 'G'  # Goal
        }

        for row in visual:
            print(' '.join(symbols.get(cell, '?') for cell in row))
