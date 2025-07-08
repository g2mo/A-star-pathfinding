# A* Pathfinding Algorithm

Implementation of the A* pathfinding algorithm to solve simple 2D mazes.

## Version 2.0

Added random maze generation using recursive backtracking algorithm + matplotlib 
visualization showing the solution, explored areas, and performance statistics.

### Algorithm Overview
A* is an informed search algorithm that finds the optimal path between nodes
by combining the actual distance from start (g-score) with a heuristic estimate
to the goal (h-score).

### New Features in V2
- **Random maze generation** using recursive backtracking
- **Adjustable maze complexity** with random path addition
- **Seeded generation** for reproducible mazes
- **Maze statistics** display
- **Matplotlib visualization** with color-coded elements
- **Performance metrics display** in the plot
- **Algorithm exploration tracking** showing which nodes were explored
- **Save plot to file** option
- **Clean, minimalistic visual design**

### Installation

```
git clone https://github.com/yourusername/a_star_pathfinding.git
cd a_star_pathfinding
pip install -r requirements.txt
```

### Usage
Basic usage: `python main.py`; with options: `python main.py --width 10 --height 10 --no-visualize`

### Performance metrics displayed
- Path Length: Steps in optimal path 
- Nodes Explored: Total cells examined 
- Nodes Evaluated: Nodes popped from priority queue 
- Max Frontier Size: Largest open set size 
- Efficiency: Path length / nodes explored ratio

### Command Line Options
- `--width`: Maze width (default: 25)
- `--height`: Maze height (default: 15)
- `--seed`: Random seed for reproducible mazes
- `--random-paths`: Percentage of random paths (0.0-1.0)
- `--sample-maze`: Use the fixed sample maze
- `--no-visualize`: Disable console visualization
- `--no-plot`: Disable matplotlib plot
- `--save-plot PATH`: Save plot to file
