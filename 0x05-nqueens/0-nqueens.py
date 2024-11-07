#!/usr/bin/python3
"""
This module solves the N Queens problem, where the goal is to place
N queens on an NxN chessboard such that no two queens can attack each other.
"""
import sys


def print_solution(board):
    """Prints a solution in the required format."""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row][col]."""
    for i in range(row):
        if (
                board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row
           ):
            return False
    return True


def solve_nqueens(board, row):
    """Solves the N Queens problem using backtracking."""
    n = len(board)
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1  # Backtrack


def main():
    """
    Main function to handle command-line arguments and initiate the solver
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

    board = [-1] * n
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
