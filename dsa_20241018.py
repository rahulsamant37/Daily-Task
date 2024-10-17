# DSA Problem for 2024-10-18

Here is a novel DSA problem with a Python solution for 2024-10-18:

**Problem Statement:**

Given a 2D grid of integers, where each cell can have one of three values: 0 (empty), 1 (start), or 2 (end). Find the minimum number of steps required to reach the end cell from the start cell, where you can only move up, down, left, or right one cell at a time, and you cannot move into an empty cell. If there is no possible path, return -1.

**Example:**

```
Input:
grid = [[1, 0, 0],
        [0, 0, 0],
        [0, 0, 2]]

Output: 4

Explanation: The shortest path from the start cell (1) to the end cell (2) is: right -> down -> right -> right, which takes 4 steps.
```

**Optimal Solution:**
```
from collections import deque

def min_steps_to_reach_end(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    start, end = None, None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                start = (i, j)
            elif grid[i][j] == 2:
                end = (i, j)

    if start is None or end is None:
        return -1

    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))

    return -1
```

**Time/Space Complexity Analysis:**

* Time complexity: O(rows \* cols), where rows and cols are the number of rows and columns in the grid, respectively. This is because in the worst case, we need to visit every cell in the grid.
* Space complexity: O(rows \* cols), which is the maximum size of the queue and the visited set.

Note: This problem is a variation of the classic Breadth-First Search (BFS) problem, which is a fundamental algorithm in graph theory. The key insight is to use a queue to keep track of the cells to visit, and a set to keep track of the cells that have already been visited. This ensures that we don't get stuck in an infinite loop and that we find the shortest path to the end cell.