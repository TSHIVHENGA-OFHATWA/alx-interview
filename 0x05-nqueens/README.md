Overview

The N Queens problem is a classic backtracking challenge that involves placing N queens on an N×N chessboard such that no two queens threaten each other. This means:

1. No two queens can be in the same row.
2. No two queens can be in the same column.
3. No two queens can be on the same diagonal.

This repository contains a Python program that solves the N Queens problem for any value of N ≥ 4 and outputs all possible solutions.

Usage

Command
./0-nqueens.py N

Arguments

N: The size of the chessboard and the number of queens to place.

Requirements

N must be an integer.

N must be greater than or equal to 4.

Output

Each solution is printed on a new line, represented as a list of queen positions. Each position is denoted by [row, column], where row and column are 0-indexed.

Example

Input
./0-nqueens.py 4

Output
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]