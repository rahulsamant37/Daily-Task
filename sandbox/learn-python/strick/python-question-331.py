# Python Question: Implement a Sudoku Solver
'''
Implement a Sudoku solver that takes a partially filled Sudoku board as input and returns the solved board. The input board will be a 9x9 2D list of integers, where 0 represents an empty cell.
The solution should fill all the empty cells such that the Sudoku rules are satisfied:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 subgrids must contain the digits 1-9 without repetition.

If a solution exists, return the solved board. If no solution exists, return the original board (or any other indication of failure).

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
        board: A 9x9 2D list representing the Sudoku board. 0 represents an empty cell.

    Returns:
        True if the Sudoku is solved, False otherwise. Modifies the board in-place.
    """

    def find_empty_location(board):
        """
        Finds the next empty cell (represented by 0) in the board.

        Returns:
            A tuple (row, col) representing the coordinates of the empty cell, or None if no empty cell is found.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(board, num, pos):
        """
        Checks if placing a number at a given position is valid according to Sudoku rules.

        Args:
            board: The Sudoku board.
            num: The number to be placed.
            pos: A tuple (row, col) representing the position to place the number.

        Returns:
            True if the placement is valid, False otherwise.
        """
        row, col = pos

        # Check row
        for i in range(9):
            if board[row][i] == num and i != col:  # Check if num exists in row, excluding the current cell
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num and i != row:  # Check if num exists in column, excluding the current cell
                return False

        # Check 3x3 box
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos: # Check if num exists in the box, excluding the current cell
                    return False

        return True

    def solve():
        """
        Recursive backtracking function to solve the Sudoku puzzle.
        """
        empty_location = find_empty_location(board)
        if not empty_location:
            return True  # No more empty cells, puzzle is solved

        row, col = empty_location

        for num in range(1, 10):
            if is_valid(board, num, (row, col)):
                board[row][col] = num  # Try placing the number

                if solve():  # Recursively attempt to solve the puzzle
                    return True

                board[row][col] = 0  # Backtrack: reset the cell if the solution is not found

        return False  # No valid number can be placed, backtrack

    return solve()

# Test cases
def test_solution():
    # Test case 1: Simple Sudoku
    board1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solved1 = solve_sudoku(board1)
    if solved1:
        print("Test Case 1: Solved")
        # for row in board1:
        #     print(row)
    else:
        print("Test Case 1: Failed to solve")

    # Test case 2: Empty Sudoku
    board2 = [[0 for _ in range(9)] for _ in range(9)]
    solved2 = solve_sudoku(board2)
    if solved2:
        print("Test Case 2: Solved")
        # for row in board2:
        #     print(row)
    else:
        print("Test Case 2: Failed to solve")

    # Test case 3: Sudoku with no solution (example adapted from online)
    board3 = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]
    solved3 = solve_sudoku(board3)
    if solved3:
        print("Test Case 3: Solved (Unexpectedly)")
        # for row in board3:
        #     print(row)
    else:
        print("Test Case 3: Failed to solve (Correctly)")

if __name__ == "__main__":
    test_solution()