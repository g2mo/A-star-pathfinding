# A* Pathfinding Algorithm
Implementation of the A* pathfinding algorithm to solve simple 2D mazes.

## Version 4.0
Added "Learning Mode" to visualize the algorithm's decision-making process by displaying cost values (g and h) in real-time.

### Algorithm Overview
A* is an informed search algorithm that finds the optimal path between nodes
by combining the actual distance from start (g-score) with a heuristic estimate
to the goal (h-score).

### New Features in V4
- **Learning Mode visualization** showing g and h values on frontier nodes
- **Enhanced animation states** with frontier and current node highlighting
- **Automatic maze size adjustment** for better learning mode visibility
- **Cost value display** showing how A* makes decisions
- **Visual distinction** between explored, frontier, and current nodes

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

### Learning Mode
Learning mode helps visualize how A* makes decisions:
- g value (top): Cost from start to this node
- h value (bottom): Heuristic estimate to goal
- Yellow cells: Frontier nodes being considered
- Green cell: Current node being evaluated
- f = g + h: Node with lowest f value is chosen next

### Outputs
<img width="800" alt="PLot1" src="https://github.com/user-attachments/assets/0aff24ce-7161-42e0-a79a-de91fbe336db" />
<img width="800" alt="Plot2" src="https://github.com/user-attachments/assets/d3f55fd0-4324-4623-8bed-6442cf853177" />


### Usage

Generate, solve, and animate a maze (basic usage):

`python main.py`

Enable learning mode:

`python main.py --learning-mode`

Learning mode with custom maze size:

`python main.py --learning-mode --width 15 --height 15`

Use static visualization:

`python main.py --static`

Save animation as GIF:

`python main.py --save-plot solution.gif`

Save learning mode animation:

`python main.py --learning-mode --save-plot learning.gif`

Slower animation for better observation:

`python main.py --interval 200`

Large maze with fast animation:

`python main.py --width 71 --height 41 --interval 10`

### Command Line Options
- `--width`: Maze width (default: 25)
- `--height`: Maze height (default: 15)
- `--seed`: Random seed for reproducible mazes
- `--random-paths`: Percentage of random paths (0.0-1.0)
- `--sample-maze`: Use the fixed sample maze
- `--no-visualize`: Disable console visualization
- `--no-plot`: Disable matplotlib plot
- `--static`: Use static plot instead of animated
- `--learning-mode`: Enable learning mode with cost display
- `--save-plot PATH`: Save plot to file
- `--interval MS`: Animation speed in milliseconds

### Animation Formats
- PNG: Static plots (`--static --save-plot solution.png`)
- GIF: Animated plots (`--save-plot solution.gif`)
- MP4: Video animations (`--save-plot solution.mp4`) - requires ffmpeg
