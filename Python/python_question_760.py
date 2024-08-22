# Python Question: Largest Island
'''
Given a 2D grid of 0s and 1s, where 0 represents water and 1 represents land, find the size of the largest island. An island is a group of 1s that are connected 4-directionally (up, down, left, right).

You can perform at most one operation: change one 0 to a 1.

Return the maximum possible area of an island after performing at most one operation.

Example:

Input: grid = [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Input: grid = [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the grid become [[1, 1], [1, 1]].

Input: grid = [[1,1],[1,1]]
Output: 4
'''

# Solution
def largest_island():
    def maxAreaOfIsland(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, grid, island_id):
            """
            Depth-first search to explore the island and assign a unique ID.
            """
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = island_id  # Mark the cell with the island ID
            return (1 + dfs(i + 1, j, grid, island_id) +
                    dfs(i - 1, j, grid, island_id) +
                    dfs(i, j + 1, grid, island_id) +
                    dfs(i, j - 1, grid, island_id))
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_id = 2  # Start island ID from 2 to avoid conflict with 0 and 1
        island_sizes = {}  # Store the size of each island

        # Find all islands and their sizes
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = dfs(i, j, grid, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        max_area = 0
        for island_id in island_sizes:
            max_area = max(max_area, island_sizes[island_id])

        # Find the maximum island area after changing one 0 to 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    # Find the neighboring islands
                    neighbors = set()
                    if i > 0 and grid[i - 1][j] > 1:
                        neighbors.add(grid[i - 1][j])
                    if i < rows - 1 and grid[i + 1][j] > 1:
                        neighbors.add(grid[i + 1][j])
                    if j > 0 and grid[i][j - 1] > 1:
                        neighbors.add(grid[i][j - 1])
                    if j < cols - 1 and grid[i][j + 1] > 1:
                        neighbors.add(grid[i][j + 1])
                    
                    # Calculate the area of the new island
                    new_area = 1
                    for island_id in neighbors:
                        new_area += island_sizes[island_id]
                    max_area = max(max_area, new_area)
        
        return max_area

    # Test cases
    def test_solution():
        grid1 = [[1, 0], [0, 1]]
        assert maxAreaOfIsland(grid1) == 3

        grid2 = [[1, 1], [1, 0]]
        assert maxAreaOfIsland(grid2) == 4

        grid3 = [[1,1],[1,1]]
        assert maxAreaOfIsland(grid3) == 4

        grid4 = [[0,0],[0,0]]
        assert maxAreaOfIsland(grid4) == 1

        grid5 = [[0,1],[1,0]]
        assert maxAreaOfIsland(grid5) == 3

        grid6 = [[0,1,0,0,1],[0,1,0,1,1],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]
        assert maxAreaOfIsland(grid6) == 9
        print("All test cases passed!")

    if __name__ == "__main__":
        test_solution()