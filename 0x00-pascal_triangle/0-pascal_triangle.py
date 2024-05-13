#!/usr/bin/python3
"""
pascal_triangle - Returns a list of lists of integers
representing the Pascals triangle of n
"""

from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """ Returns the Pascal Triangle of n """
    if n <= 0:
        return []

    pasc = [[1]]
    for _ in range(1, n):
        new, prev = [1], pasc[-1]
        for i in range(len(prev) - 1):
            new.append(prev[i] + prev[i + 1])
        new.append(1)
        pasc.append(new)

    return pasc
