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
def longest_increasing_path(matrix):
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
            return dp[row][col]  # Return the cached value if it exists

        max_length = 1  # Initialize the length to 1 (the cell itself)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move: right, left, down, up

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                max_length = max(max_length, 1 + dfs(new_row, new_col))  # Recursively explore the neighbor and update the max_length

        dp[row][col] = max_length  # Cache the result
        return max_length

    longest_path = 0
    for i in range(rows):
        for j in range(cols):
            longest_path = max(longest_path, dfs(i, j))  # Iterate through all cells and find the maximum length

    return longest_path


# Test cases
def test_longest_increasing_path():
    assert longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]]) == 4
    assert longest_increasing_path([[1]]) == 1
    assert longest_increasing_path([[1,2]]) == 2
    assert longest_increasing_path([[1],[2]]) == 2
    assert longest_increasing_path([[7,7,5],[2,4,6],[8,2,0]]) == 4
    assert longest_increasing_path([]) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_increasing_path()