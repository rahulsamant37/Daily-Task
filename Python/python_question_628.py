# Python Question: Implement a Sudoku Solver using Backtracking
'''
Implement a function `solve_sudoku(board)` that solves a Sudoku puzzle represented as a 9x9 list of lists.
Empty cells are represented by the character '.'. The function should modify the input `board` in-place
to represent the solved Sudoku. Assume that the input Sudoku has a unique solution.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'
- It is guaranteed that the input board represents a valid Sudoku puzzle.
- It is guaranteed that the input Sudoku puzzle has a single unique solution.

Example:
Input:
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
Output:
board = [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]
'''

# Solution
def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking.

    Args:
        board: A 9x9 list of lists representing the Sudoku puzzle.
               Empty cells are represented by the character '.'.
    """

    def is_valid(board, row, col, num):
        """
        Checks if placing the number 'num' at (row, col) is valid.

        Args:
            board: The Sudoku board.
            row: The row index.
            col: The column index.
            num: The number to be placed.

        Returns:
            True if the placement is valid, False otherwise.
        """
        # Check row
        for i in range(9):
            if board[row][i] == str(num):
                return False

        # Check column
        for i in range(9):
            if board[i][col] == str(num):
                return False

        # Check 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == str(num):
                    return False

        return True

    def solve():
        """
        Recursive backtracking function to solve the Sudoku puzzle.

        Returns:
            True if the puzzle is solved, False otherwise.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = str(num)
                            if solve():  # Recursively try to solve the rest of the board
                                return True
                            else:
                                board[row][col] = '.'  # Backtrack: reset the cell if the solution is not found
                    return False  # No valid number can be placed at this cell

        return True  # All cells are filled, the puzzle is solved

    solve()  # Start the backtracking process


# Test cases
def test_solution():
    board1 = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    solve_sudoku(board1)
    expected1 = [["5","3","4","6","7","8","9","1","2"],
                 ["6","7","2","1","9","5","3","4","8"],
                 ["1","9","8","3","4","2","5","6","7"],
                 ["8","5","9","7","6","1","4","2","3"],
                 ["4","2","6","8","5","3","7","9","1"],
                 ["7","1","3","9","2","4","8","5","6"],
                 ["9","6","1","5","3","7","2","8","4"],
                 ["2","8","7","4","1","9","6","3","5"],
                 ["3","4","5","2","8","6","1","7","9"]]
    assert board1 == expected1, f"Test case 1 failed: Expected {expected1}, got {board1}"

    board2 = [[".",".","9","7","4","8",".",".","."],
              ["7",".",".",".",".",".",".",".","."],
              [".","2",".","1",".","9",".",".","."],
              [".",".","7",".",".",".","2","4","."],
              [".","6","4",".","1",".","5","9","."],
              [".","9","8",".",".",".","3",".","."],
              [".",".",".","8",".","3",".","2","."],
              [".",".",".",".",".",".",".",".","6"],
              [".",".",".","2","7","5","9",".","."]]
    solve_sudoku(board2)
    expected2 = [["5","1","9","7","4","8","6","3","2"],
                 ["7","8","3","6","5","2","4","1","9"],
                 ["4","2","6","1","3","9","8","5","7"],
                 ["3","5","7","9","8","6","2","4","1"],
                 ["2","6","4","3","1","7","5","9","8"],
                 ["1","9","8","5","2","4","3","7","6"],
                 ["9","7","5","8","6","3","1","2","4"],
                 ["8","3","2","4","9","1","7","5","6"],
                 ["6","4","1","2","7","5","9","8","3"]]
    assert board2 == expected2, f"Test case 2 failed: Expected {expected2}, got {board2}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()