# DSA Problem for 2024-11-07

Here is a novel DSA problem with a Python solution for 2024-11-07:

**Problem Statement:**

You are given a 2D grid of characters, where each cell can be either 'W' (water), 'L' (land), or 'T' (tree). A group of connected trees (horizontally, vertically, or diagonally) is considered a forest. Your task is to find the largest forest in the grid and return its size.

**Example Input:**

```
grid = [
    ['W', 'L', 'T', 'W', 'W'],
    ['W', 'T', 'T', 'L', 'W'],
    ['W', 'W', 'W', 'L', 'T'],
    ['W', 'T', 'W', 'W', 'L'],
    ['W', 'W', 'W', 'W', 'W']
]
```

**Example Output:**

```
3
```

**Explanation:**

The largest forest in the given grid has a size of 3, which can be found in the second row (two connected trees) and the fifth column (one tree).

**Optimal Solution:**

```python
def largest_forest(grid):
    def dfs(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 'T':
            grid[i][j] = 'W'  # mark as visited
            return 1 + dfs(i-1, j-1) + dfs(i-1, j) + dfs(i-1, j+1) + dfs(i, j-1) + dfs(i, j+1) + dfs(i+1, j-1) + dfs(i+1, j) + dfs(i+1, j+1)
        return 0

    max_forest_size = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'T':
                max_forest_size = max(max_forest_size, dfs(i, j))
    return max_forest_size
```

**Time/Space Complexity Analysis:**

* Time complexity: O(m \* n), where m is the number of rows and n is the number of columns in the grid. This is because in the worst-case scenario, we need to perform a DFS on each cell in the grid.
* Space complexity: O(m \* n), which is the maximum depth of the recursion stack in the DFS function. This occurs when all cells in the grid are connected trees.

Note: This problem can also be solved using union-find data structure, but the DFS approach is more straightforward and easier to implement.