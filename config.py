"""Configuration settings for A* Pathfinding"""

# Grid dimensions
DEFAULT_WIDTH = 25
DEFAULT_HEIGHT = 15
DEFAULT_DEPTH = 8  # For 3D mode

# Default dimensions for 3D mode (smaller for performance)
DEFAULT_WIDTH_3D = 8
DEFAULT_HEIGHT_3D = 8
DEFAULT_DEPTH_3D = 8

# Maze generation settings
MAZE_RANDOM_SEED = None  # Set to integer for reproducible mazes
MAZE_RANDOM_PATHS_PERCENTAGE = 0.25  # Percentage of additional paths (0.0-1.0)

# Start and goal positions
DEFAULT_START_2D = (0, 0)
DEFAULT_GOAL_2D = None  # Will be set to (height-1, width-1) if None
DEFAULT_START_3D = (0, 0, 0)
DEFAULT_GOAL_3D = None  # Will be set to (depth-1, height-1, width-1) if None

# Visualization settings
SHOW_VISUALIZATION = True
SHOW_PLOT = True  # Show matplotlib plot if available
PLOT_SAVE_PATH = None  # Set to filename to save plot instead of showing

# Animation settings
ANIMATE_PLOT = True  # Show animated visualization by default
ANIMATION_INTERVAL = 50  # Milliseconds between frames (50ms = 20fps)
ANIMATION_INTERVAL_3D = 10  # Faster for 3D to handle more frames

# Learning mode settings
LEARNING_MODE = False  # Set to True to show g/h values during animation
LEARNING_MODE_INTERVAL = 250  # Slower animation for learning mode
LEARNING_MODE_INTERVAL_3D = 500  # Even slower for 3D learning mode

# Console visualization
CONSOLE_SYMBOLS = {
    'walkable': '.',
    'obstacle': '#',
    'path': '*',
    'start': 'S',
    'goal': 'G'
}

# Plot colors (RGB values 0-1)
PLOT_COLORS = {
    'wall': [0.2, 0.2, 0.2],  # Dark gray
    'empty': [0.95, 0.95, 0.95],  # White
    'explored': [0.8, 0.9, 1.0],  # Light blue
    'frontier': [1.0, 1.0, 0.6],  # Light yellow
    'current': [0.4, 1.0, 0.4],  # Light green
    'path': [1.0, 0.3, 0.3],  # Red
    'start': [0, 0.8, 0],  # Green
    'goal': [0.5, 0.2, 0.8]  # Purple
}

# 3D specific settings
VOXEL_SIZE = 0.9  # Size of voxels in 3D visualization
VOXEL_EDGE_WIDTH = 0.5  # Edge width for voxels
