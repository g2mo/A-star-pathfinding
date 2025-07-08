"""Visualization utilities for pathfinding"""

# Try to import matplotlib
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np

    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


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


class MatplotlibVisualizer:
    """Matplotlib-based visualization for grids and paths"""

    @staticmethod
    def is_available():
        """Check if matplotlib is available"""
        return MATPLOTLIB_AVAILABLE

    @staticmethod
    def plot_solution(grid, path, explored_nodes, start, goal, stats, save_path=None):
        """Create a plot showing the solution and algorithm evolution"""
        if not MATPLOTLIB_AVAILABLE:
            print("Warning: matplotlib not available. Install with: pip install matplotlib numpy")
            return

        # Convert grid to numpy array
        maze = np.array(grid)
        height, width = maze.shape

        # Create figure with proper size
        fig, ax = plt.subplots(figsize=(10, 7))

        # Create display array
        display = np.ones((height, width, 3))  # RGB array

        # Define colors (RGB)
        colors = {
            'wall': [0.2, 0.2, 0.2],  # Dark gray
            'empty': [0.95, 0.95, 0.95],  # White
            'explored': [0.8, 0.9, 1.0],  # Light blue
            'path': [1.0, 0.3, 0.3],  # Red
            'start': [0, 0.8, 0],  # Green
            'goal': [0.5, 0.2, 0.8]  # Purple
        }

        # Fill maze structure
        for i in range(height):
            for j in range(width):
                if maze[i][j] == 1:  # Wall
                    display[i, j] = colors['wall']
                else:  # Empty
                    display[i, j] = colors['empty']

        # Mark explored nodes
        for coords in explored_nodes:
            x, y = coords[:2]  # Handle both 2D and 3D
            if (x, y) != start[:2] and (x, y) != goal[:2]:
                display[x, y] = colors['explored']

        # Mark path
        if path:
            for coords in path:
                x, y = coords[:2]  # Handle both 2D and 3D
                if (x, y) != start[:2] and (x, y) != goal[:2]:
                    display[x, y] = colors['path']

        # Mark start and goal
        display[start[0], start[1]] = colors['start']
        display[goal[0], goal[1]] = colors['goal']

        # Display the image
        ax.imshow(display, interpolation='nearest', aspect='equal')

        # Remove axes
        ax.axis('off')

        # Add title
        ax.set_title('A* Pathfinding Solution', fontsize=16, fontweight='bold', pad=20)

        # Add statistics text
        stats_text = f"Path Length: {stats['path_length']}\n"
        stats_text += f"Nodes Explored: {stats['nodes_explored']}\n"
        stats_text += f"Nodes Evaluated: {stats['nodes_evaluated']}\n"
        stats_text += f"Max Frontier Size: {stats['max_frontier']}\n"
        stats_text += f"Efficiency: {stats['efficiency']:.1f}%"

        # Add statistics box
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
        ax.text(1.02, 0.95, stats_text, transform=ax.transAxes, fontsize=12,
                verticalalignment='top', bbox=props)

        # Add legend
        legend_elements = [
            patches.Rectangle((0, 0), 1, 1, facecolor=colors['wall'], label='Wall'),
            patches.Rectangle((0, 0), 1, 1, facecolor=colors['empty'], label='Empty'),
            patches.Rectangle((0, 0), 1, 1, facecolor=colors['explored'], label='Explored'),
            patches.Rectangle((0, 0), 1, 1, facecolor=colors['path'], label='Path'),
            patches.Rectangle((0, 0), 1, 1, facecolor=colors['start'], label='Start'),
            patches.Rectangle((0, 0), 1, 1, facecolor=colors['goal'], label='Goal')
        ]

        ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1.02, 0.5),
                  frameon=True, fancybox=True, shadow=True)

        # Adjust layout to prevent legend cutoff
        plt.tight_layout()

        # Save or show plot
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Plot saved to: {save_path}")
        else:
            plt.show()
