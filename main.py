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
    --no-visualize      Disable visualization
    --mode {2d,3d}      Choose between 2D and 3D mode (default: 2d)

Author: Guglielmo Cimolai
Date: 07/07/2025
Version: 1
"""

import argparse
import sys

from src.core import AStar
from src.maze import MazeGenerator
from src.visualization import ConsoleVisualizer
import config


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='A* Pathfinding Algorithm Implementation'
    )
    parser.add_argument(
        '--width', type=int, default=config.DEFAULT_WIDTH,
        help='Grid width'
    )
    parser.add_argument(
        '--height', type=int, default=config.DEFAULT_HEIGHT,
        help='Grid height'
    )
    parser.add_argument(
        '--no-visualize', action='store_true',
        help='Disable visualization'
    )
    parser.add_argument(
        '--mode', choices=['2d', '3d'], default='2d',
        help='Choose between 2D and 3D mode'
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_arguments()

    # For V1, we only support the sample 2D maze
    if args.mode == '3d':
        print("3D mode not yet implemented in V1. Using 2D mode.")
        args.mode = '2d'

    # Create maze
    print("Creating sample maze...")
    grid = MazeGenerator.create_sample_maze()

    # Define start and goal
    start = config.DEFAULT_START_2D
    goal = config.DEFAULT_GOAL_2D

    # Create pathfinder and find path
    print("\nFinding path with A* algorithm...")
    astar = AStar(grid)
    path = astar.find_path(start, goal)

    # Display results
    if path:
        print(f"Path found! Length: {len(path)}")
        print(f"Path: {path}")
    else:
        print("No path found!")

    # Visualize if enabled
    if not args.no_visualize:
        print("\nVisualization:")
        print("Legend: S=Start, G=Goal, #=Wall, .=Empty, *=Path")
        ConsoleVisualizer.visualize_path(grid, path, start, goal)


if __name__ == "__main__":
    main()
