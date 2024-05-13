#!/usr/bin/env python3
""" pascal_triangle - Returns a list of lists of integers
                    representing the Pascals triangle of n
"""

from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """ Returns the Pascal Triangle of n """
    if n <= 0:
        return []

    pasc = [[1]]
    k = 1
    while k < n:
        new = [1]
        i = 0
        while i < len(pasc[k - 1]):
            try:
                new.append(pasc[k - 1][i] + pasc[k - 1][i + 1])
            except IndexError:
                new.append(1)
            finally:
                i += 1
        pasc.append(new)
        k += 1

    return pasc
