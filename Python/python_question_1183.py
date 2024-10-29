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
    Finds the length of the longest increasing path in a matrix.

    Args:
        matrix: A list of lists representing the matrix.

    Returns:
        The length of the longest increasing path.
    """
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]  # DP table to store the length of the longest increasing path starting from each cell
    max_length = 0

    def dfs(row, col):
        """
        Performs Depth-First Search to find the longest increasing path starting from a cell.

        Args:
            row: The row index of the current cell.
            col: The column index of the current cell.

        Returns:
            The length of the longest increasing path starting from the current cell.
        """
        if dp[row][col] != 0:
            return dp[row][col]  # Return the cached result if already computed

        length = 1  # Initialize the length to 1 (the current cell itself)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move (right, left, down, up)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new cell is within the matrix bounds and has a greater value
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                length = max(length, 1 + dfs(new_row, new_col))  # Recursively explore the new cell

        dp[row][col] = length  # Store the computed length in the DP table
        return length

    # Iterate through each cell in the matrix and find the longest increasing path starting from it
    for i in range(rows):
        for j in range(cols):
            max_length = max(max_length, dfs(i, j))

    return max_length


# Test cases
def test_longest_increasing_path():
    assert longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]]) == 4
    assert longest_increasing_path([[1]]) == 1
    assert longest_increasing_path([[1,2]]) == 2
    assert longest_increasing_path([[1],[2]]) == 2
    assert longest_increasing_path([[1,2,3],[4,5,6],[7,8,9]]) == 9
    assert longest_increasing_path([[1,2,3],[6,5,4],[7,8,9]]) == 6
    assert longest_increasing_path([[7,8,9],[6,5,4],[1,2,3]]) == 6
    assert longest_increasing_path([]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_path()