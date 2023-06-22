#!/usr/bin/python3
"""
Island perimeter module.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    height = len(grid)
    count = 0
    if grid is None:
        return 0
    width = len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is 1:
                if i - 1 >= 0:
                    if grid[i - 1][j] == 0:
                        count = count + 1
                else:
                    count = count + 1
                if i + 1 < height:
                    if grid[i + 1][j] == 0:
                        count = count + 1
                else:
                    count = count + 1
                if j - 1 >= 0:
                    if grid[i][j - 1] == 0:
                        count = count + 1
                else:
                    count = count + 1
                if j + 1 < width:
                    if grid[i][j + 1] == 0:
                        count = count + 1
                else:
                    count = count + 1
    return count
