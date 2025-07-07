# A* Pathfinding Algorithm

Implementation of the A* pathfinding algorithm to solve simple 2D mazes.

## Version 1.0

Basic implementation of A* pathfinding for 2D grids with text-based visualization.

### Algorithm Overview
A* is an informed search algorithm that finds the optimal path between nodes
by combining the actual distance from start (g-score) with a heuristic estimate
to the goal (h-score).

### Features
- A* pathfinding algorithm for 2D grids
- Text-based console visualization
- Configurable via command-line arguments

### Installation

```
git clone https://github.com/yourusername/a_star_pathfinding.git
cd a_star_pathfinding
```

### Usage
Basic usage: `python main.py`; 
with options: `python main.py --width 10 --height 10 --no-visualize`
