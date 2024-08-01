#!/usr/bin/python3
""" Script returns the perimeter of the island described in grid """

def island_perimeter(grid):
    """
    grid is a list of list of integers:
    
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn't have “lakes” (water inside that isn't connected to the water surrounding the island).
    """

    if not check_surroundings(grid):
        return 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four directions
                if r == 0 or grid[r-1][c] == 0:  # Up
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # Down
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Left
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # Right
                    perimeter += 1

    return perimeter

def check_surroundings(grid):
    """ Checks that the grid is surrounded by water """
    if not grid or grid == []:
        return False

    size = len(grid[0])
    for cell in range(size):
        if grid[0][cell] != 0 and grid[-1][cell] != 0:
            return False

    for square in grid:
        if square[0] != 0 and square[-1] != 0:
            return False

    return True
