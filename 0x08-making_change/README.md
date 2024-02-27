# Coin Change Problem Solver

This project aims to solve the classic problem of finding the minimum number of coins needed to make up a given total amount, known as the coin change problem. The solution is implemented in Python, utilizing dynamic programming to efficiently compute the result.

## Problem Description

Given a pile of coins with different denominations and a target total amount, the objective is to determine the fewest number of coins required to meet the target amount. If the total amount cannot be met using the available coins, the function returns -1.

## Solution Approach

### Dynamic Programming

Dynamic programming is employed to solve this problem efficiently. The approach involves breaking down the problem into smaller subproblems and storing the solutions to these subproblems in a table to avoid redundant computations. By iteratively updating the table, we can determine the minimum number of coins needed for increasing amounts until reaching the target total.

### Algorithm Steps

1. Initialize an array `dp` to store the minimum number of coins needed for each amount from 0 to the target total.
2. Set `dp[0] = 0` since no coins are needed to make up amount 0.
3. Iterate through each coin denomination:
   - For each coin denomination, update `dp[i]` if using the current coin reduces the number of coins needed for amount `i`.
4. Return `dp[total]` if a solution is found, otherwise return -1 if the target total cannot be met.

## Usage

To use the `makeChange` function:

```python
print(makeChange([1, 2, 25], 37))               # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453)) # Output: -1
```

## Project Structure

- `0-making_change.py`: Python script containing the implementation of the `makeChange` function.
- `README.md`: This file, providing an overview of the project, problem description, solution approach, usage instructions, and project structure.

## Requirements

- Python 3.x
- PEP 8 style compliance
- All files must be executable
- Ubuntu 20.04 LTS environment

## Author

This project is authored by Dzidedi Senaya. 

Feel free to contribute, suggest improvements, or report any issues via GitHub. Thank you for using our coin change problem solver!
