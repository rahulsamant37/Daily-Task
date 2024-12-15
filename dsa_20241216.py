# DSA Problem for 2024-12-16

Here is a novel DSA problem with a Python solution for 2024-12-16:

**Problem Statement:**

**"Island Hopper"**

You are given a 2D grid of size `M x N`, where `M` is the number of rows and `N` is the number of columns. The grid represents a map of islands, where each cell can be either:

* `0`: Water (you cannot hop to this cell)
* `1`: Land (you can hop to this cell)

You start at the top-left cell of the grid. Your goal is to hop from one land cell to another, moving either horizontally, vertically, or diagonally to an adjacent land cell. You want to maximize the number of distinct islands you can visit.

Given the grid, write a function `max_islands` that returns the maximum number of distinct islands you can visit.

**Example:**
```
grid = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]
```
The optimal solution would be to visit the islands in the following order: `(0, 0) -> (0, 2) -> (1, 1) -> (2, 0) -> (2, 2) -> (3, 1)`, visiting 5 distinct islands.

**Optimal Solution:**
```python
def max_islands(grid):
    M, N = len(grid), len(grid[0])
    visited = [[False] * N for _ in range(M)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def dfs(r, c):
        if visited[r][c] or grid[r][c] == 0:
            return 0
        visited[r][c] = True
        count = 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N:
                count += dfs(nr, nc)
        return count

    max_islands = 0
    for r in range(M):
        for c in range(N):
            if grid[r][c] == 1 and not visited[r][c]:
                max_islands += dfs(r, c)
    return max_islands
```
**Time/Space Complexity Analysis:**

* Time Complexity: `O(M * N)`
	+ The DFS function is called for each land cell, and each cell is visited at most once.
	+ The DFS function itself has a time complexity of `O(1)` since it only checks adjacent cells.
* Space Complexity: `O(M * N)`
	+ The `visited` grid has the same size as the input grid.

This problem is a variation of the "Island Counting" problem, where we not only count the number of islands but also want to maximize the number of distinct islands visited. The optimal solution uses a DFS approach to explore the land cells and mark them as visited to avoid revisiting the same island. The time and space complexities are linear with respect to the size of the input grid.