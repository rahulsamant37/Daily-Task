# DSA Problem generated on 2024-12-27

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a 2D grid of characters, where each cell can be either '0' (representing an empty space) or '1' (representing a wall), find the number of islands that can be formed by connecting adjacent '1's (horizontally or vertically). An island is a group of connected '1's.

**Example Input:**
```
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
```
**Expected Output:** 3 (There are three islands in the given grid)

**Solution Code:**
```
def numIslands(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(numIslands(grid))  # Output: 3
```
**Time Complexity Analysis:**

The time complexity of the solution is O(M\*N), where M is the number of rows in the grid and N is the number of columns. This is because we are traversing each cell in the grid once.

The DFS function has a recursive depth of at most M+N, since we are exploring at most M rows and N columns from each starting point. However, since we are marking visited cells as '#', we only visit each cell once, so the overall time complexity remains O(M\*N).

The space complexity is O(M\*N) as well, since in the worst case, we might need to store all cells in the call stack during the DFS traversal.