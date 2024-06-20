#!/usr/bin/python3
""" Interview prep """


def makeChange(coins, total):
    """ Making change """
    if total <= 0:
        return 0
    
    # Initialize the DP table with "infinity" (a large number)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Populate the DP table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means it's not possible
    # to make the total
    return dp[total] if dp[total] != float('inf') else -1
