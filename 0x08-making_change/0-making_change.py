#!/usr/bin/python3
"""
Module for solving the coin change problem
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to
    meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of
    # coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp[i] if using the current coin reduces
        # the number of coins needed for amount i
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Test cases
    print(makeChange([1, 2, 25], 37))    # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))    # Output: -1
