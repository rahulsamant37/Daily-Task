# DSA Problem for 2024-11-06

Here's a novel DSA problem for 2024-11-06:

**Problem Statement:**

Given a 2D grid of 1s and 0s, where 1s represent buildings and 0s represent empty space, find the maximum number of buildings that can be seen from a particular direction (north, south, east, or west) from any cell in the grid.

For example, given the following grid:
```
[[1, 0, 0, 1],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [1, 0, 0, 1]]
```
From the north direction, the maximum number of buildings that can be seen is 3 (from the top-left cell). From the east direction, the maximum number of buildings that can be seen is 2 (from the bottom-right cell).

**Optimal Solution:**
```python
def max_buildings_visible(grid, direction):
    rows, cols = len(grid), len(grid[0])
    max_visible = [[0] * cols for _ in range(rows)]

    if direction == 'north':
        for col in range(cols):
            count = 0
            for row in range(rows):
                if grid[row][col] == 1:
                    count += 1
                    max_visible[row][col] = count
    elif direction == 'south':
        for col in range(cols):
            count = 0
            for row in range(rows - 1, -1, -1):
                if grid[row][col] == 1:
                    count += 1
                    max_visible[row][col] = count
    elif direction == 'east':
        for row in range(rows):
            count = 0
            for col in range(cols - 1, -1, -1):
                if grid[row][col] == 1:
                    count += 1
                    max_visible[row][col] = count
    elif direction == 'west':
        for row in range(rows):
            count = 0
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1
                    max_visible[row][col] = count

    return max(max(row) for row in max_visible)
```
**Time/Space Complexity Analysis:**

* Time complexity: O(rows \* cols), where rows and cols are the dimensions of the grid. This is because we iterate over each cell in the grid once for each direction.
* Space complexity: O(rows \* cols), where rows and cols are the dimensions of the grid. This is because we store the maximum number of visible buildings for each cell in the grid.

Note that the time and space complexity can be improved by using a more efficient data structure, such as a priority queue, to keep track of the maximum number of visible buildings. However, the above solution has a simple and easy-to-understand implementation.