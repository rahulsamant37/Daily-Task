# Python Question: Implement a Sudoku Solver using Backtracking
'''
Implement a Sudoku solver using a backtracking algorithm.
The input is a 9x9 Sudoku board represented as a list of lists, where empty cells are represented by the integer 0.
The function should modify the input board in-place to contain the solved Sudoku. If no solution exists, the function should return False. Otherwise, it should return True.

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
[
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
'''

# Solution
def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking.

    Args:
        board: A 9x9 Sudoku board represented as a list of lists.
               Empty cells are represented by 0.

    Returns:
        True if the Sudoku is solvable, False otherwise.
        Modifies the board in-place with the solution.
    """

    def find_empty_location(board):
        """
        Finds an empty cell (represented by 0) in the board.

        Returns:
            A tuple (row, col) representing the coordinates of the empty cell,
            or None if no empty cell is found.
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
            if board[row][i] == num and i != col:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num and i != row:
                return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve():
        """
        Recursive backtracking function to solve the Sudoku.

        Returns:
            True if a solution is found, False otherwise.
        """
        empty_location = find_empty_location(board)
        if not empty_location:
            return True  # No empty cells, board is solved

        row, col = empty_location

        for num in range(1, 10):
            if is_valid(board, num, (row, col)):
                board[row][col] = num

                if solve():
                    return True  # Solution found

                board[row][col] = 0  # Backtrack: Reset the cell

        return False  # No valid number found for this cell, backtrack

    return solve()


# Test cases
def test_solution():
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
    solved_board1 = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    solve_sudoku(board1)
    assert board1 == solved_board1, "Test Case 1 Failed"

    board2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # This is a very difficult board to solve, but it should still be solvable.
    # It will take a long time, but we expect it to return a solved board.
    solve_sudoku(board2)
    is_valid_sudoku = True
    for i in range(9):
        for j in range(9):
            if board2[i][j] == 0 or not (1 <= board2[i][j] <= 9):
                is_valid_sudoku = False
                break
        if not is_valid_sudoku:
            break

    if is_valid_sudoku:
        # Verify rows
        for i in range(9):
            nums = set()
            for j in range(9):
                if board2[i][j] in nums:
                    is_valid_sudoku = False
                    break
                nums.add(board2[i][j])
            if not is_valid_sudoku:
                break

        # Verify columns
        for j in range(9):
            nums = set()
            for i in range(9):
                if board2[i][j] in nums:
                    is_valid_sudoku = False
                    break
                nums.add(board2[i][j])
            if not is_valid_sudoku:
                break

        # Verify 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board2[x][y] in nums:
                            is_valid_sudoku = False
                            break
                        nums.add(board2[x][y])
                    if not is_valid_sudoku:
                        break
                if not is_valid_sudoku:
                    break

    assert is_valid_sudoku, "Test Case 2 Failed: Empty board test"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()