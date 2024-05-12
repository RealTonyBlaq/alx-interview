#!/usr/bin/python3
""" Interview prep """

def minOperations(n: int) -> int:
    """
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    H = 1
    while H < n:
        copy = H
        paste = H + copy
