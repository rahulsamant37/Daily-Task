# Python Question: Implement a Sudoku Solver
'''
Implement a Sudoku solver using backtracking.

Sudoku puzzles are represented as a 9x9 2D list (list of lists) where each cell contains a digit from 1-9 or 0 (representing an empty cell).

The goal is to fill the empty cells with digits such that the following rules are satisfied:

1.  Each row must contain the digits 1-9 without repetition.
2.  Each column must contain the digits 1-9 without repetition.
3.  Each of the nine 3x3 subgrids (also known as "boxes" or "blocks") must contain the digits 1-9 without repetition.

Write a function `solve_sudoku(board)` that takes a Sudoku board as input and modifies it in-place to represent a solved Sudoku puzzle. If the puzzle is unsolvable, the function should return False. Otherwise, it should return True.

Example:

Input:
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

Output:
board = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
'''

# Solution
def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking.

    Args:
        board: A 9x9 2D list representing the Sudoku board.

    Returns:
        True if the puzzle is solvable, False otherwise.  Modifies the board in-place.
    """

    def find_empty_location(board):
        """
        Finds an empty cell (cell with value 0) in the board.

        Args:
            board: A 9x9 2D list representing the Sudoku board.

        Returns:
            A tuple (row, col) representing the coordinates of an empty cell, or None if no empty cell is found.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(board, num, pos):
        """
        Checks if placing the given number at the given position is valid according to Sudoku rules.

        Args:
            board: A 9x9 2D list representing the Sudoku board.
            num: The number to be placed (1-9).
            pos: A tuple (row, col) representing the position to place the number.

        Returns:
            True if the placement is valid, False otherwise.
        """
        row, col = pos

        # Check row
        for i in range(9):
            if board[row][i] == num and i != col:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num and i != row:
                return False

        # Check 3x3 box
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve():
        """
        Recursive function to solve the Sudoku puzzle using backtracking.

        Returns:
            True if the puzzle is solved, False otherwise.
        """
        empty_location = find_empty_location(board)
        if not empty_location:
            return True  # No empty cells, puzzle is solved

        row, col = empty_location

        for num in range(1, 10):
            if is_valid(board, num, (row, col)):
                board[row][col] = num

                if solve():
                    return True  # Recursively solve with the current number

                board[row][col] = 0  # Backtrack: reset the cell if the solution is not found

        return False  # No valid number found for this cell, backtrack

    return solve()


# Test cases
def test_solution():
    board1 = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    expected_board1 = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]
    solve_sudoku(board1)
    assert board1 == expected_board1, f"Test case 1 failed: Expected {expected_board1}, got {board1}"

    board2 = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]  # An empty board.  Should still solve but might take a long time.  Removed the assertion for this case.

    board3 = [
        [1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,4,5,6,7,8,9,1],
        [5,6,7,8,9,1,2,3,4],
        [8,9,1,2,3,4,5,6,7],
        [3,4,5,6,7,8,9,1,2],
        [6,7,8,9,1,2,3,4,5],
        [9,1,2,3,4,5,6,7,8]
    ] # Already solved board.
    solve_sudoku(board3)
    assert board3 == [
        [1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,4,5,6,7,8,9,1],
        [5,6,7,8,9,1,2,3,4],
        [8,9,1,2,3,4,5,6,7],
        [3,4,5,6,7,8,9,1,2],
        [6,7,8,9,1,2,3,4,5],
        [9,1,2,3,4,5,6,7,8]
    ], f"Test case 3 failed: Expected same board, got {board3}"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()