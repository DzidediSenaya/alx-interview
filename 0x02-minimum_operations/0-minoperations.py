#!/usr/bin/python3
"""
Calculates the minimum number of operations to reach
a given number of characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters.

    Args:
    - n: an integer (the target number of H characters)

    Returns:
    - an integer representing the minimum number of operations
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations


if __name__ == "__main__":
    # Example usage
    n1 = 4
    n2 = 12

    result1 = minOperations(n1)
    result2 = minOperations(n2)

    print("Min number of operations to reach {} characters: {}"
          .format(n1, result1))
    print("Min number of operations to reach {} characters: {}"
          .format(n2, result2))
