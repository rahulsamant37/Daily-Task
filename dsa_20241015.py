# DSA Problem for 2024-10-15

Here's a novel DSA problem with a Python solution for 2024-10-15:

**Problem Statement:**

You are given a 2D matrix `grid` of size `m x n`, where each cell can have one of the following values:

* `0`: Empty cell
* `1`: Wall
* `2`: Teleporter

A teleporter can transport you to any other teleporter in the grid instantaneously. You start at the top-left cell of the grid.

Your task is to find the minimum number of steps required to reach the bottom-right cell of the grid. You can move up, down, left, or right by one cell at a time, but you cannot move through walls. If you reach a teleporter, you can instantly move to any other teleporter in the grid.

**Example Input:**

```
grid = [
    [0, 0, 0, 2, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
```

**Expected Output:**

`5`

**Explanation:**

* Start at the top-left cell (0, 0)
* Move right to the teleporter at (0, 3)
* Teleport to the teleporter at (3, 1)
* Move right to the cell at (3, 2)
* Move down to the cell at (4, 2)
* Move right to the bottom-right cell at (4, 4)

Total steps: 5

**Optimal Solution:**

```python
from collections import deque

def min_steps_to_reach_bottom_right(grid):
    m, n = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = {(0, 0)}
    teleporters = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                teleporters.append((i, j))

    while queue:
        row, col, steps = queue.popleft()
        if row == m - 1 and col == n - 1:
            return steps

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] != 1:
                if grid[nr][nc] == 2:
                    for teleporter in teleporters:
                        tr, tc = teleporter
                        if (tr, tc) not in visited:
                            queue.append((tr, tc, steps + 1))
                            visited.add((tr, tc))
                else:
                    queue.append((nr, nc, steps + 1))
                    visited.add((nr, nc))

    return -1  # If it's not possible to reach the bottom-right cell
```

**Time/Space Complexity Analysis:**

* Time complexity: O(m \* n + t), where `t` is the number of teleporters. This is because we visit each cell at most once and process each teleporter once.
* Space complexity: O(m \* n + t), where `t` is the number of teleporters. This is because we store the visited cells and teleporters in the `visited` and `teleporters` data structures.

Note that the time and space complexities can be improved by using a more efficient data structure, such as a hash set, to store the visited cells and teleporters.