# A* Pathfinding Algorithm

Implementation of the A* pathfinding algorithm to solve simple 2D mazes.

## Version 3.0

Added animated visualization showing the algorithm's exploration process in real-time.

### Algorithm Overview
A* is an informed search algorithm that finds the optimal path between nodes
by combining the actual distance from start (g-score) with a heuristic estimate
to the goal (h-score).

### New Features in V3
- **Live animated visualization** showing algorithm progression
- **Real-time statistics update** during exploration
- **Configurable animation speed** 
- **Save animations** as GIF or video files
- **Choice between static and animated** visualization

### Installation

```
git clone https://github.com/yourusername/a_star_pathfinding.git
cd a_star_pathfinding
pip install -r requirements.txt
```

### Performance metrics displayed
- Path Length: Steps in optimal path 
- Nodes Explored: Total cells examined 
- Nodes Evaluated: Nodes popped from priority queue 
- Max Frontier Size: Largest open set size 
- Efficiency: Path length / nodes explored ratio

### Usage

Generate, solve, and animate a maze (basic usage):

`python main.py`

Use static visualization:

`python main.py --static`

Save animation as GIF:

`python main.py --save-plot solution.gif`

Slower animation for better observation:

`python main.py --interval 200`

Large maze with fast animation:

`python main.py --width 71 --height 41 --interval 10`

### Command Line Options
- `--width`: Maze width (default: 45)
- `--height`: Maze height (default: 27)
- `--seed`: Random seed for reproducible mazes
- `--random-paths`: Percentage of random paths (0.0-1.0)
- `--sample-maze`: Use the fixed sample maze
- `--no-visualize`: Disable console visualization
- `--no-plot`: Disable matplotlib plot
- `--save-plot PATH`: Save plot to file

### Animation Formats
- PNG: Static plots (`--static --save-plot solution.png`)
- GIF: Animated plots (`--save-plot solution.gif`)
- MP4: Video animations (`--save-plot solution.mp4`) - requires ffmpeg
