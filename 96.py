# Solution for Project Euler Problem 96
# Problem Statement: Solve a collection of Su Doku puzzles and find the sum of the 3-digit numbers in the top-left corner of each solution.

import numpy as np

def is_valid(board, row, col, num):
    """Check if placing num at board[row][col] is valid."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False

    return True

def parse_sudoku(file_path):
    """Parse the Sudoku puzzles from the given file."""
    puzzles = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 10):
            puzzle = []
            for j in range(1, 10):
                puzzle.append([int(x) for x in lines[i + j].strip()])
            puzzles.append(puzzle)
    return puzzles

if __name__ == "__main__":
    FILE_PATH = "sudoku.txt"  # Replace with the actual file path
    puzzles = parse_sudoku(FILE_PATH)
    total = 0

    for puzzle in puzzles:
        board = np.array(puzzle)
        solve_sudoku(board)
        total += int("".join(map(str, board[0, :3])))

    print("The sum of the 3-digit numbers in the top-left corner is:", total)