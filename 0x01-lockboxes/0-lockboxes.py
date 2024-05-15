#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ Checks if all the boxes are unlocked """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)
    
    return all(visited)
