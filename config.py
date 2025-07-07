"""Configuration settings for A* Pathfinding"""

# Grid dimensions
DEFAULT_WIDTH = 8
DEFAULT_HEIGHT = 8
DEFAULT_DEPTH = 8  # For 3D mode

# Start and goal positions
DEFAULT_START_2D = (0, 0)
DEFAULT_GOAL_2D = (7, 7)
DEFAULT_START_3D = (0, 0, 0)
DEFAULT_GOAL_3D = (7, 7, 7)

# Visualization settings
SHOW_VISUALIZATION = True
CONSOLE_SYMBOLS = {
    'walkable': '.',
    'obstacle': '#',
    'path': '*',
    'start': 'S',
    'goal': 'G'
}
