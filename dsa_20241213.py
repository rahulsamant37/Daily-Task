# DSA Problem for 2024-12-13

Here is a novel DSA problem with a Python solution for 2024-12-13:

**Problem Statement:**

Given a 2D array of integers representing a grid, where each cell can have one of three values:

* `0` representing an empty cell
* `1` representing a wall
* `2` representing a treasure

You are tasked with finding the maximum number of treasures that can be collected by a robot that starts at the top-left corner of the grid. The robot can move either down or right, and it cannot move into a cell with a wall.

Write a program to find the maximum number of treasures that can be collected by the robot.

**Example Input:**

```
grid = [
    [0, 0, 2, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2]
]
```

**Optimal Solution:**

Here is a Python solution using dynamic programming:
```python
def max_treasures(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0] == 2

    # Initialize first row
    for i in range(1, n):
        if grid[0][i] == 2:
            dp[0][i] = dp[0][i-1] + 1
        elif grid[0][i] == 0:
            dp[0][i] = dp[0][i-1]

    # Initialize first column
    for i in range(1, m):
        if grid[i][0] == 2:
            dp[i][0] = dp[i-1][0] + 1
        elif grid[i][0] == 0:
            dp[i][0] = dp[i-1][0]

    # Fill in the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 2:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
            elif grid[i][j] == 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = 0

    return dp[m-1][n-1]

grid = [
    [0, 0, 2, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2]
]

print(max_treasures(grid))  # Output: 3
```

**Time/Space Complexity Analysis:**

* Time complexity: O(m\*n), where m and n are the number of rows and columns in the grid, respectively. This is because we need to iterate over the entire grid to fill in the dp table.
* Space complexity: O(m\*n), where m and n are the number of rows and columns in the grid, respectively. This is because we need to store the dp table, which has the same size as the input grid.

Note that the solution has a linear time complexity because we only need to iterate over the grid once to fill in the dp table. The space complexity is also linear because we need to store the dp table, which has the same size as the input grid.