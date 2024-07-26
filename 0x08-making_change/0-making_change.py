#!/usr/bin/python3
""" Interview prep """

from collections import deque

def makeChange(coins, total):
    """
    Making change
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to potentially reach the solution faster
    coins.sort(reverse=True)
    
    # Initialize a queue for BFS
    queue = deque([(0, 0)])  # (current_sum, number_of_coins_used)
    visited = set([0])  # To avoid revisiting the same sum

    while queue:
        current_sum, num_coins = queue.popleft()

        for coin in coins:
            new_sum = current_sum + coin
            if new_sum == total:
                return num_coins + 1
            if new_sum < total and new_sum not in visited:
                visited.add(new_sum)
                queue.append((new_sum, num_coins + 1))

    return -1
