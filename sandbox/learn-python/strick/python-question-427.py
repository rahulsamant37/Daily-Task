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
        The length of the longest increasing path.
    """

    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]  # dp[i][j] stores the length of the longest increasing path starting from (i, j)
    max_length = 0

    def dfs(i, j):
        """
        Performs Depth-First Search to find the length of the longest increasing path starting from (i, j).

        Args:
            i: The row index.
            j: The column index.

        Returns:
            The length of the longest increasing path starting from (i, j).
        """
        if dp[i][j] != 0:
            return dp[i][j]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move: right, left, down, up
        max_path = 1  # Minimum path length is 1 (the cell itself)

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                max_path = max(max_path, 1 + dfs(x, y))

        dp[i][j] = max_path  # Store the calculated length in dp for memoization
        return max_path

    # Iterate through each cell in the matrix and find the longest increasing path starting from that cell.
    for i in range(m):
        for j in range(n):
            max_length = max(max_length, dfs(i, j))

    return max_length

# Test cases
def test_longest_increasing_path():
    matrix1 = [[9,9,4],[6,6,8],[2,1,1]]
    assert longest_increasing_path(matrix1) == 4, "Test Case 1 Failed"

    matrix2 = [[3,4,5],[3,2,6],[2,2,1]]
    assert longest_increasing_path(matrix2) == 4, "Test Case 2 Failed"

    matrix3 = [[1]]
    assert longest_increasing_path(matrix3) == 1, "Test Case 3 Failed"

    matrix4 = [[1,2]]
    assert longest_increasing_path(matrix4) == 2, "Test Case 4 Failed"

    matrix5 = [[1,2,3],[4,5,6],[7,8,9]]
    assert longest_increasing_path(matrix5) == 9, "Test Case 5 Failed"

    matrix6 = [[1,2,3]]
    assert longest_increasing_path(matrix6) == 3, "Test Case 6 Failed"

    matrix7 = [[1,2],[3,4]]
    assert longest_increasing_path(matrix7) == 4, "Test Case 7 Failed"

    matrix8 = [[7,7,5],[2,4,6],[8,2,0]]
    assert longest_increasing_path(matrix8) == 4, "Test Case 8 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_path()