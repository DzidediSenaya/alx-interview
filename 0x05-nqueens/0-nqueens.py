#!/usr/bin/python3
"""
NQueens Problem Solver
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursive function to solve N Queens problem
    """
    if row == n:
        res = []
        for i in range(len(board)):
            res.append([i, board[i]])
        print(res)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """
    Main function to solve N Queens problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
