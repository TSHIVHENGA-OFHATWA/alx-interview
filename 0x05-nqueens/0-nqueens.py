#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][1] == col or \
           board[i][1] - i == col - row or \
           board[i][1] + i == col + row:
            return False
    return True


def solve(board, row, N):
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = [row, col]
            solve(board, row + 1, N)
            board[row] = [-1, -1]


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[-1, -1] for _ in range(N)]
    solve(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
