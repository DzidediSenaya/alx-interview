#!/usr/bin/python3
"""Module to determine the winner of the prime game."""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if x <= 0 or not nums:
        return None

    wins_maria = 0
    wins_ben = 0

    for n in nums:
        primes_count = sum(1 for i in range(1, n+1) if is_prime(i))
        if primes_count % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1

    if wins_maria > wins_ben:
        return "Maria"
    elif wins_maria < wins_ben:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
