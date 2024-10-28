# Python Question: Find the Longest Increasing Path in a Matrix
'''
Given an m x n integers matrix, find the length of the longest increasing path in the matrix.

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
def longestIncreasingPath(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_length = 0

    def dfs(row, col):
        # If the length is already calculated, return it
        if dp[row][col] != 0:
            return dp[row][col]

        # Possible directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_path = 1  # Minimum path length is 1 (the cell itself)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new cell is within the bounds and has a larger value
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                max_path = max(max_path, 1 + dfs(new_row, new_col))

        dp[row][col] = max_path  # Store the calculated length in dp
        return max_path

    # Iterate through each cell in the matrix and calculate the longest increasing path starting from that cell
    for row in range(rows):
        for col in range(cols):
            max_length = max(max_length, dfs(row, col))

    return max_length

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

    matrix5 = [[1,2,3],[6,5,4],[7,8,9]]
    assert longestIncreasingPath(matrix5) == 9

    matrix6 = [[7,7,5],[2,4,6],[8,2,0]]
    assert longestIncreasingPath(matrix6) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()