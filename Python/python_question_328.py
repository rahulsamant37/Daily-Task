# Python Question: Longest Increasing Path in a Matrix
'''
Given an `m x n` integer matrix `matrix`, find the length of the longest increasing path in the matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside of the boundary (i.e., wrap around).

Example:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Input: matrix = [[1]]
Output: 1
'''

# Solution
def longestIncreasingPath(matrix):
    """
    Finds the length of the longest increasing path in a matrix.

    Args:
        matrix: A list of lists of integers representing the matrix.

    Returns:
        The length of the longest increasing path in the matrix.
    """
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]  # dp[i][j] stores the length of the longest increasing path starting from cell (i, j)

    def dfs(row, col):
        """
        Performs Depth-First Search to find the length of the longest increasing path starting from cell (row, col).

        Args:
            row: The row index of the cell.
            col: The column index of the cell.

        Returns:
            The length of the longest increasing path starting from cell (row, col).
        """
        if dp[row][col] != 0:
            return dp[row][col]

        max_length = 1  # Initialize the length to 1 (the cell itself)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move (right, left, down, up)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new cell is within the bounds of the matrix and if its value is greater than the current cell's value
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                max_length = max(max_length, 1 + dfs(new_row, new_col))  # Update the maximum length if a longer path is found

        dp[row][col] = max_length  # Store the length in the dp table
        return max_length

    longest_path = 0
    for i in range(rows):
        for j in range(cols):
            longest_path = max(longest_path, dfs(i, j))  # Find the maximum length among all possible starting cells

    return longest_path

# Test cases
def test_solution():
    matrix1 = [[9,9,4],[6,6,8],[2,1,1]]
    assert longestIncreasingPath(matrix1) == 4

    matrix2 = [[3,4,5],[3,2,6],[2,2,1]]
    assert longestIncreasingPath(matrix2) == 4

    matrix3 = [[1]]
    assert longestIncreasingPath(matrix3) == 1

    matrix4 = [[1,2]]
    assert longestIncreasingPath(matrix4) == 2

    matrix5 = [[1,2,3],[4,5,6],[7,8,9]]
    assert longestIncreasingPath(matrix5) == 9

    matrix6 = [[7,7,5],[2,4,6],[8,2,0]]
    assert longestIncreasingPath(matrix6) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()