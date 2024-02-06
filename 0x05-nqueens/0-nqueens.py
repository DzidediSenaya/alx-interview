#!/usr/bin/python3
"""
N Queens solved with Backtracing
"""
import sys


def nqueens(n, row, board):
    """
    Method: nqueens - place n queens
            on an n by n board so that
            no queens are attacking any
            others.
    Parameters:
        n (int): board size and # of queens
        row (int): current row
        board (list): current board state
    Returns: All possible solutions to
            placement, in list of lists form
    """
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            nqueens(n, row + 1, board)
            board.pop()


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for q_row, q_col in board:
        if col == q_col or row - col == q_row - q_col or row + col == q_row + q_col:
            return False
    return True


def main():
    """
    Main function to solve N Queens problem
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n, 0, [])


if __name__ == '__main__':
    main()
