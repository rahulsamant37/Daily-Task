# Python Question: Minimum Cost Path in a Grid
'''
Given a grid represented by a 2D list `cost`, where `cost[i][j]` represents the cost to enter cell (i, j), find the minimum cost to reach the bottom-right cell (m-1, n-1) from the top-left cell (0, 0). You can only move down or right.

Example:
Input:
cost = [[1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]]
Output:
12

Explanation:
The minimum cost path is 1 -> 4 -> 4 -> 3 -> 2 -> 3, with a total cost of 12.
'''

# Solution
def solution():
    def min_cost_path(cost):
        """
        Calculates the minimum cost path from the top-left to the bottom-right cell in a grid.

        Args:
            cost: A 2D list representing the cost of each cell in the grid.

        Returns:
            The minimum cost to reach the bottom-right cell.
        """
        m = len(cost)
        n = len(cost[0])

        # Create a DP table to store the minimum cost to reach each cell
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Initialize the top-left cell
        dp[0][0] = cost[0][0]

        # Initialize the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + cost[0][j]

        # Initialize the first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + cost[i][0]

        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost[i][j]

        # Return the minimum cost to reach the bottom-right cell
        return dp[m-1][n-1]
    return min_cost_path

# Test cases
def test_solution():
    cost1 = [[1, 3, 5, 8],
             [4, 2, 1, 7],
             [4, 3, 2, 3]]
    assert solution()(cost1) == 12

    cost2 = [[1, 2, 3],
             [4, 5, 6]]
    assert solution()(cost2) == 8

    cost3 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    assert solution()(cost3) == 5

    cost4 = [[5]]
    assert solution()(cost4) == 5

    cost5 = [[1, 10, 100],
             [1, 1, 10],
             [1, 1, 1]]
    assert solution()([[1, 10, 100], [1, 1, 10], [1, 1, 1]]) == 7
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()