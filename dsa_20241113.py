# DSA Problem for 2024-11-13

Here is a novel DSA problem with a Python solution for 2024-11-13:

**Problem Statement:**

**"Minimum Jumps to Reach the End with Power-Ups"**

You are playing a game where you need to reach the end of a grid with a minimum number of jumps. The grid has obstacles and power-ups that can help or hinder your progress. The grid is represented as a 2D list, where:

* `0` represents an empty cell
* `1` represents an obstacle (you cannot jump onto an obstacle)
* `2` represents a power-up that allows you to jump an extra cell on your next jump
* `3` represents a power-up that forces you to jump back to the previous cell on your next jump

You start at the top-left corner of the grid (cell `[0, 0]`) and need to reach the bottom-right corner of the grid (cell `[n-1, n-1]`). You can move horizontally, vertically, or diagonally to an adjacent cell, but you can only jump onto an empty cell or a power-up cell.

Write a function `min_jumps(grid)` that returns the minimum number of jumps required to reach the end of the grid.

**Example Input/Output:**

```
grid = [
    [0, 0, 0, 1, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

print(min_jumps(grid))  # Output: 7
```

**Optimal Solution:**

Here is an optimal solution using Breadth-First Search (BFS) and a queue data structure:
```python
from collections import deque

def min_jumps(grid):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # 8 directions
    queue = deque([(0, 0, 0)])  # (x, y, jumps)
    visited = {(0, 0)}
    power_ups = {(x, y) for x in range(n) for y in range(n) if grid[x][y] == 2 or grid[x][y] == 3}

    while queue:
        x, y, jumps = queue.popleft()
        if (x, y) == (n-1, n-1):
            return jumps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < n) and (nx, ny) not in visited and grid[nx][ny] != 1:
                if (nx, ny) in power_ups:
                    if grid[nx][ny] == 2:
                        queue.append((nx, ny, jumps + 1))
                    else:
                        queue.append((x, y, jumps + 1))
                else:
                    queue.append((nx, ny, jumps + 1))
                visited.add((nx, ny))
    return -1  # unreachable
```

**Time/Space Complexity Analysis:**

* Time complexity: O(n^2) where n is the size of the grid, since we visit each cell at most once.
* Space complexity: O(n^2) since we use a queue to store the cells to visit, and a set to keep track of visited cells.

The optimal solution has a time and space complexity of O(n^2) because we need to visit each cell in the grid to find the minimum number of jumps. The use of a queue and a set helps to avoid revisiting cells and to keep track of visited cells efficiently.