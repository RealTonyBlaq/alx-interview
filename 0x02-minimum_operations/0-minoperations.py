#!/usr/bin/python3
""" Interview prep """


def copy_H() -> str:
    with open('test') as f:
        return f.read()

def minOperations(n: int) -> int:
    """
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    H, ops, copy = 1, 0, 0
    while H < n:
        if copy + H <= n:
            copy = H
            ops += 1
        paste = H + copy
        ops += 1
        H = paste

    return ops
