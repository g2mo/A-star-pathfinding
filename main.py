#!/usr/bin/env python3
"""
A* Pathfinding Algorithm - Main Entry Point

This script implements the A* pathfinding algorithm for 2D grid-based navigation.
A* is an informed search algorithm that finds the optimal path between nodes
by combining the actual distance from start (g-score) with a heuristic estimate
to the goal (h-score).

Usage:
    python main.py [options]

Options:
    --width WIDTH       Grid width (default: from config)
    --height HEIGHT     Grid height (default: from config)
    --no-visualize      Disable console visualization
    --no-plot           Disable matplotlib plot
    --static            Use static plot instead of animated
    --save-plot PATH    Save plot to file (png for static, gif/mp4 for animated)
    --interval MS       Animation interval in milliseconds (default: 50)
    --mode {2d,3d}      Choose between 2D and 3D mode (default: 2d)
    --seed SEED         Random seed for maze generation
    --sample-maze       Use the sample maze instead of generating random
    --random-paths PCT  Percentage of random paths to add (0.0-1.0)

Author: Guglielmo Cimolai
Date: 09/07/2025
Version: 3
"""

import argparse
import random
import sys

from src.core import AStar
from src.maze import MazeGenerator
from src.visualization import ConsoleVisualizer, MatplotlibVisualizer
import config


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='A* Pathfinding Algorithm Implementation'
    )
    parser.add_argument(
        '--width', type=int, default=config.DEFAULT_WIDTH,
        help='Grid width (should be odd for proper maze generation)'
    )
    parser.add_argument(
        '--height', type=int, default=config.DEFAULT_HEIGHT,
        help='Grid height (should be odd for proper maze generation)'
    )
    parser.add_argument(
        '--no-visualize', action='store_true',
        help='Disable console visualization'
    )
    parser.add_argument(
        '--no-plot', action='store_true',
        help='Disable matplotlib plot'
    )
    parser.add_argument(
        '--static', action='store_true',
        help='Use static plot instead of animated'
    )
    parser.add_argument(
        '--save-plot', type=str, default=config.PLOT_SAVE_PATH,
        help='Save plot to file (png for static, gif/mp4 for animated)'
    )
    parser.add_argument(
        '--interval', type=int, default=config.ANIMATION_INTERVAL,
        help='Animation interval in milliseconds'
    )
    parser.add_argument(
        '--mode', choices=['2d', '3d'], default='2d',
        help='Choose between 2D and 3D mode'
    )
    parser.add_argument(
        '--seed', type=int, default=config.MAZE_RANDOM_SEED,
        help='Random seed for maze generation'
    )
    parser.add_argument(
        '--sample-maze', action='store_true',
        help='Use the sample maze instead of generating random'
    )
    parser.add_argument(
        '--random-paths', type=float, default=config.MAZE_RANDOM_PATHS_PERCENTAGE,
        help='Percentage of random paths to add (0.0-1.0)'
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_arguments()

    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
        print(f"Using random seed: {args.seed}")

    # For V4, we only support 2D visualization
    if args.mode == '3d':
        print("3D visualization not yet implemented in V4. Using 2D mode.")
        args.mode = '2d'

    # Create or generate maze
    if args.sample_maze:
        print("Using sample maze...")
        grid = MazeGenerator.create_sample_maze()
        height, width = len(grid), len(grid[0])
    else:
        # Ensure odd dimensions for proper maze generation
        width = args.width if args.width % 2 == 1 else args.width + 1
        height = args.height if args.height % 2 == 1 else args.height + 1

        print(f"Generating random maze ({height}x{width})...")
        maze_gen = MazeGenerator(width, height)
        grid = maze_gen.generate()

        # Add random paths if specified
        if args.random_paths > 0:
            print(f"Adding random paths ({args.random_paths * 100:.1f}% of cells)...")
            maze_gen.add_random_paths(args.random_paths)

    # Define start and goal
    start = config.DEFAULT_START_2D
    goal = config.DEFAULT_GOAL_2D if config.DEFAULT_GOAL_2D else (height - 1, width - 1)

    # Create pathfinder and find path with statistics
    print("\nFinding path with A* algorithm...")
    astar = AStar(grid)
    path, explored_nodes, max_frontier, nodes_evaluated = astar.find_path_with_stats(start, goal)

    # Calculate statistics
    if path:
        path_length = len(path)
        nodes_explored = len(explored_nodes)
        efficiency = (path_length / nodes_explored) * 100 if nodes_explored > 0 else 0

        print(f"Path found! Length: {path_length}")
        print(f"Nodes explored: {nodes_explored}")
        print(f"Nodes evaluated: {nodes_evaluated}")
        print(f"Max frontier size: {max_frontier}")
        print(f"Efficiency: {efficiency:.1f}%")
    else:
        print("No path found!")
        path_length = 0
        nodes_explored = len(explored_nodes)
        efficiency = 0

    # Show maze statistics
    total_cells = width * height
    walkable_cells = sum(row.count(0) for row in grid)
    print(f"\nMaze statistics:")
    print(f"- Size: {height}x{width}")
    print(f"- Total cells: {total_cells}")
    print(f"- Walkable cells: {walkable_cells} ({walkable_cells / total_cells * 100:.1f}%)")
    print(f"- Obstacles: {total_cells - walkable_cells} ({(total_cells - walkable_cells) / total_cells * 100:.1f}%)")

    # Console visualization
    if not args.no_visualize:
        print("\nConsole visualization:")
        print("Legend: S=Start, G=Goal, #=Wall, .=Empty, *=Path")
        print("-" * (width * 2 - 1))
        ConsoleVisualizer.visualize_path(grid, path, start, goal)

    # Matplotlib visualization
    if not args.no_plot and config.SHOW_PLOT:
        if MatplotlibVisualizer.is_available():
            stats = {
                'path_length': path_length,
                'nodes_explored': nodes_explored,
                'nodes_evaluated': nodes_evaluated,
                'max_frontier': max_frontier,
                'efficiency': efficiency
            }

            if args.static:
                print("\nGenerating static visualization plot...")
                MatplotlibVisualizer.plot_solution(
                    grid, path, explored_nodes, start, goal, stats,
                    save_path=args.save_plot
                )
            else:
                print("\nGenerating animated visualization...")
                print(f"Animation speed: {args.interval}ms per frame")
                MatplotlibVisualizer.plot_solution_animated(
                    grid, path, explored_nodes, start, goal, stats,
                    interval=args.interval, save_path=args.save_plot
                )
        else:
            print("\nMatplotlib not available. Install with: pip install matplotlib numpy")


if __name__ == "__main__":
    main()
