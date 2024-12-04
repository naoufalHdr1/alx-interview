#!/usr/bin/env python3
""" Island Perimeter Module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list): A 2D grid representing water (0) and land (1).

    Returns:
        int: The perimeter of the island.
    """
    # Initialize the perimeter count
    perimeter = 0

    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell contributes 4 sides initially
                perimeter += 4

                # Check for adjacent land cells and subtract shared edges
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
