# Python Question: Implement a Sudoku Solver using Backtracking
'''
Implement a Sudoku solver using a backtracking algorithm.  The input will be a 9x9 grid represented as a list of lists, where empty cells are represented by 0. The solver should modify the input grid in-place to represent the solved Sudoku.

A Sudoku puzzle is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid contains all of the digits from 1 to 9.

Input:
grid = [
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
grid = [
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
def solve_sudoku(grid):
    """
    Solves a Sudoku puzzle using backtracking.

    Args:
        grid: A 9x9 grid represented as a list of lists, where 0 represents empty cells.
    """

    def find_empty_cell(grid):
        """
        Finds the first empty cell in the grid.

        Returns:
            A tuple (row, col) representing the coordinates of the empty cell, or None if no empty cell is found.
        """
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def is_valid(grid, num, pos):
        """
        Checks if placing the given number at the given position is valid according to Sudoku rules.

        Args:
            grid: The Sudoku grid.
            num: The number to place.
            pos: A tuple (row, col) representing the position to place the number.

        Returns:
            True if the placement is valid, False otherwise.
        """
        # Check row
        for i in range(9):
            if grid[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if grid[i][pos[1]] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if grid[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve():
        """
        Recursive backtracking function to solve the Sudoku puzzle.

        Returns:
            True if the puzzle is solved, False otherwise.
        """
        empty_cell = find_empty_cell(grid)
        if not empty_cell:
            return True  # No more empty cells, the puzzle is solved

        row, col = empty_cell

        for num in range(1, 10):
            if is_valid(grid, num, (row, col)):
                grid[row][col] = num

                if solve():
                    return True  # Puzzle solved with this number placed

                grid[row][col] = 0  # Backtrack: reset the cell to 0

        return False  # No valid number can be placed, trigger backtracking

    solve()


# Test cases
def test_solution():
    grid1 = [
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
    solve_sudoku(grid1)
    expected_grid1 = [
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
    assert grid1 == expected_grid1, f"Test Case 1 Failed: Expected {expected_grid1}, Got {grid1}"

    grid2 = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    #This grid has multiple solutions, so we just check if it solves
    solve_sudoku(grid2)
    is_valid_solution = True
    for i in range(9):
        row_values = set()
        col_values = set()
        for j in range(9):
            if grid2[i][j] == 0 or grid2[j][i] == 0:
                is_valid_solution = False
                break
            if grid2[i][j] in row_values or grid2[j][i] in col_values:
                is_valid_solution = False
                break
            row_values.add(grid2[i][j])
            col_values.add(grid2[j][i])

    if not is_valid_solution:
        print("Test Case 2 Failed: Invalid Solution")
    else:
        print("All test cases passed!")

if __name__ == "__main__":
    test_solution()