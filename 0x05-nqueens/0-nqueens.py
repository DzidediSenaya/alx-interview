#!/usr/bin/python3
"""
N Queens problem solved
"""
import sys


def backtrack(row, n, cols, pos_diag, neg_diag, board):
    """
    Backtrack
    """
    if row == n:
        res = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    res.append([i, j])
        print(res)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    N queens problem
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
