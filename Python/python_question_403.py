# Python Question: Minimum Cost Path in a Grid
'''
You are given a grid represented by a 2D list of integers `grid`, where each cell `grid[i][j]` represents the cost to enter that cell. You start at the top-left cell `(0, 0)` and want to reach the bottom-right cell `(m-1, n-1)`. You can only move down or right.

Your task is to find the minimum cost path from the top-left cell to the bottom-right cell.

Example:

Input:
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
Output: 7

Explanation: The path 1 -> 1 -> 5 -> 2 -> 1 has the minimum cost of 7.
'''

# Solution
def solution():
    def min_cost_path(grid):
        """
        Calculates the minimum cost path from the top-left cell to the bottom-right cell in a grid.

        Args:
            grid: A 2D list of integers representing the cost of each cell.

        Returns:
            The minimum cost to reach the bottom-right cell.
        """
        m = len(grid)
        n = len(grid[0])

        # Create a DP table to store the minimum cost to reach each cell.
        dp = [[0] * n for _ in range(m)]

        # Initialize the top-left cell with its cost.
        dp[0][0] = grid[0][0]

        # Fill the first row. The only way to reach a cell in the first row is from the left.
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Fill the first column. The only way to reach a cell in the first column is from above.
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill the rest of the table. The minimum cost to reach a cell is the minimum of the cost to reach it from above or from the left, plus the cost of the cell itself.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        # The minimum cost to reach the bottom-right cell is stored in dp[m-1][n-1].
        return dp[m-1][n-1]
    
    return min_cost_path

# Test cases
def test_solution():
    min_cost_path = solution()
    # Test case 1
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert min_cost_path(grid1) == 7, "Test Case 1 Failed"

    # Test case 2
    grid2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert min_cost_path(grid2) == 12, "Test Case 2 Failed"

    # Test case 3
    grid3 = [
        [1, 2],
        [1, 2]
    ]
    assert min_cost_path(grid3) == 5, "Test Case 3 Failed"

    # Test case 4: Single cell grid
    grid4 = [[5]]
    assert min_cost_path(grid4) == 5, "Test Case 4 Failed"

    # Test case 5: Large grid with varying costs
    grid5 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    assert min_cost_path(grid5) == 76, "Test Case 5 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()