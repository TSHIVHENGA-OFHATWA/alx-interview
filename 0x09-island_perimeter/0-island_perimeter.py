#!/usr/bin/python3
"""
This module contains a function that calculates the perimeter
of an island represented in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list int): A 2D list where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for column in range(cols):
            if grid[row][column] == 1:
                if row == 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][column] == 0:
                    perimeter += 1
                if column == 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                if column == cols - 1 or grid[row][column + 1] == 0:
                    perimeter += 1

    return perimeter
