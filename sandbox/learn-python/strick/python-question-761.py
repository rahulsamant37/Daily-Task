# Python Question: Longest Increasing Path in a Matrix
'''
Given an m x n integers matrix, find the length of the longest increasing path in the matrix.

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
    dp = [[0] * cols for _ in range(rows)]  # DP table to store the length of the longest increasing path starting from each cell

    def dfs(row, col):
        """
        Performs Depth-First Search to find the length of the longest increasing path starting from a given cell.

        Args:
            row: The row index of the cell.
            col: The column index of the cell.

        Returns:
            The length of the longest increasing path starting from the given cell.
        """
        if dp[row][col] != 0:
            return dp[row][col]  # If the length is already calculated, return it

        max_length = 1  # Initialize the length to 1 (the current cell itself)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new cell is within the bounds of the matrix and if its value is greater than the current cell
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                max_length = max(max_length, 1 + dfs(new_row, new_col))  # Update the maximum length

        dp[row][col] = max_length  # Store the calculated length in the DP table
        return max_length

    longest_path = 0
    for row in range(rows):
        for col in range(cols):
            longest_path = max(longest_path, dfs(row, col))  # Find the maximum length across all cells

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

    matrix6 = [[1,2,3],[6,5,4],[7,8,9]]
    assert longestIncreasingPath(matrix6) == 6

    matrix7 = [[7,7,5],[7,6,4],[7,5,3]]
    assert longestIncreasingPath(matrix7) == 6

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()