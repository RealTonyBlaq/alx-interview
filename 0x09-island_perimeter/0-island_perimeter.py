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

    if grid == []:
        return 0


def check_surroundings(grid):
    """ Checks that the grid is surrounded by water """
    size = len(grid[0])
    for cell in range(len(grid[0])):
        if cell != 0:
            return False
    
