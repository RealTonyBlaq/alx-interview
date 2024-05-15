#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ Checks if all the boxes are unlocked """
    box_size = len(boxes)
    if box_size == 0:
        return False

    visited = [False] * box_size
    visited[0] = True

    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key < box_size and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
