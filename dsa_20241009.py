# DSA Problem for 2024-10-09

Here's a novel DSA problem for 2024-10-09:

**Problem Statement:**

Given a 2D grid of size `m x n`, where each cell can have one of three values:

* 0: Empty cell
* 1: Wall cell
* 2: Gate cell

You are standing at the top-left corner of the grid, and you need to find the minimum number of steps to reach each cell in the grid, considering the following rules:

* You can move in any of the four directions (up, down, left, right) from an empty cell.
* You cannot move through wall cells.
* When you reach a gate cell, you can move through it, and the gate cell becomes an empty cell.

Write an algorithm to find the minimum number of steps to reach each cell in the grid.

**Optimal Solution:**
```python
from collections import deque

def min_steps_to_reach_all_cells(grid):
    m, n = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = [[False] * n for _ in range(m)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        row, col, steps = queue.popleft()
        if visited[row][col]:
            continue
        visited[row][col] = True

        if grid[row][col] == 2:  # Gate cell
            grid[row][col] = 0  # Mark as empty cell

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 1:
                queue.append((nr, nc, steps + 1))

    return [[steps for _, _, steps in row] for row in queue]
```
**Time/Space Complexity Analysis:**

* Time complexity: O(m \* n), where `m` and `n` are the dimensions of the grid. This is because we visit each cell at most once.
* Space complexity: O(m \* n), where `m` and `n` are the dimensions of the grid. This is because we need to store the visited cells and the queue of cells to process.

Note: The `deque` data structure from the `collections` module is used to implement the queue, which provides an efficient way to add and remove elements from both ends.

This problem combines elements of Breadth-First Search (BFS) and graph traversal, and the solution uses a queue to keep track of cells to process. The key insight is to mark gate cells as empty cells when we reach them, so that we can move through them in subsequent iterations.