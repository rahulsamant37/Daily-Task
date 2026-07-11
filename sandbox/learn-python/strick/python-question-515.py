# Python Question: Longest Increasing Path in a Matrix
'''
Given an `m x n` integer matrix `matrix`, find the length of the longest increasing path in the matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap around).

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
def longest_increasing_path(matrix):
    """
    Finds the length of the longest increasing path in the given matrix.

    Args:
        matrix: A list of lists representing the integer matrix.

    Returns:
        The length of the longest increasing path in the matrix.
    """

    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]  # dp[i][j] stores the length of the longest increasing path starting from matrix[i][j]
    max_length = 0

    def dfs(row, col):
        """
        Performs Depth-First Search to find the longest increasing path starting from (row, col).

        Args:
            row: The row index of the starting cell.
            col: The column index of the starting cell.

        Returns:
            The length of the longest increasing path starting from (row, col).
        """
        if dp[row][col] != 0:
            return dp[row][col]  # Return cached result if available

        length = 1  # Initialize path length to 1 (the current cell itself)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new cell is within bounds and has a larger value
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                length = max(length, 1 + dfs(new_row, new_col))  # Update length with the longest path from the neighbor

        dp[row][col] = length  # Cache the result
        return length

    # Iterate through each cell in the matrix and find the longest path starting from it
    for i in range(rows):
        for j in range(cols):
            max_length = max(max_length, dfs(i, j))  # Update the overall maximum length

    return max_length

# Test cases
def test_longest_increasing_path():
    matrix1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    assert longest_increasing_path(matrix1) == 4

    matrix2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    assert longest_increasing_path(matrix2) == 4

    matrix3 = [[1]]
    assert longest_increasing_path(matrix3) == 1

    matrix4 = [[1,2]]
    assert longest_increasing_path(matrix4) == 2

    matrix5 = [[1,2,3],[4,5,6],[7,8,9]]
    assert longest_increasing_path(matrix5) == 9

    matrix6 = []
    assert longest_increasing_path(matrix6) == 0

    matrix7 = [[7,8,9],[9,7,6],[7,2,3]]
    assert longest_increasing_path(matrix7) == 6

if __name__ == "__main__":
    test_longest_increasing_path()