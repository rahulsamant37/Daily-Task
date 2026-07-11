# Python Question: Find the Largest Island
'''
You are given a 2D grid of 0s and 1s, where 0 represents water and 1 represents land. An island is a group of 1s connected 4-directionally (horizontal or vertical). You may change one 0 to a 1 to form one bigger island.

Find the maximum area of an island in the grid after performing at most one such operation.

Example:
Input:
grid = [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect the two islands, then we get an island with area 3.

Input:
grid = [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island in the grid.

Input:
grid = [[1, 1], [1, 1]]
Output: 4
Explanation: There is no 0, the grid is all 1, the area of the island is 4.
'''

# Solution
def solution():
    def largestIsland(grid):
        """
        Finds the maximum area of an island in the grid after changing one 0 to 1.

        Args:
            grid: A 2D list of integers representing the grid.

        Returns:
            The maximum area of an island after changing one 0 to 1.
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        
        # Function to perform Depth First Search to find the area of an island
        def dfs(i, j, island_id):
            """
            Performs Depth First Search to find the area of an island.

            Args:
                i: The row index of the current cell.
                j: The column index of the current cell.
                island_id: The ID of the current island.

            Returns:
                The area of the current island.
            """
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
                return 0
            
            grid[i][j] = island_id # Mark the island with a unique ID
            area = 1
            area += dfs(i + 1, j, island_id)  # Explore downward
            area += dfs(i - 1, j, island_id)  # Explore upward
            area += dfs(i, j + 1, island_id)  # Explore rightward
            area += dfs(i, j - 1, island_id)  # Explore leftward
            return area

        # Assign island IDs and calculate areas
        island_id = 2
        island_areas = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = dfs(i, j, island_id)
                    island_areas[island_id] = area
                    island_id += 1

        # Find the maximum area after changing one 0 to 1
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    neighboring_islands = set()
                    if i > 0 and grid[i - 1][j] > 1:
                        neighboring_islands.add(grid[i - 1][j])
                    if i < n - 1 and grid[i + 1][j] > 1:
                        neighboring_islands.add(grid[i + 1][j])
                    if j > 0 and grid[i][j - 1] > 1:
                        neighboring_islands.add(grid[i][j - 1])
                    if j < m - 1 and grid[i][j + 1] > 1:
                        neighboring_islands.add(grid[i][j + 1])

                    area = 1  # Start with the area of the flipped 0
                    for island in neighboring_islands:
                        area += island_areas[island]
                    max_area = max(max_area, area)
        
        # If the grid has no 0, return the total area of the existing island.
        if not island_areas:
            return 0

        # If no 0 was found, it means the grid is all 1s
        if max_area == 0:
            return max(island_areas.values())
            
        return max_area

    return largestIsland

# Test cases
def test_solution():
    grid1 = [[1, 0], [0, 1]]
    assert solution()(grid1) == 3

    grid2 = [[1, 1], [1, 0]]
    assert solution()(grid2) == 4

    grid3 = [[1, 1], [1, 1]]
    assert solution()(grid3) == 4

    grid4 = [[0, 0], [0, 0]]
    assert solution()(grid4) == 1

    grid5 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    assert solution()(grid5) == 5
    
    grid6 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert solution()(grid6) == 1
    
    grid7 = [[1]]
    assert solution()(grid7) == 1
    
    grid8 = [[0]]
    assert solution()(grid8) == 1
    
    grid9 = [[1,1,0,1,1],
             [1,0,1,0,1],
             [1,1,0,1,1]]
    assert solution()(grid9) == 14
    
    grid10 = [[0,1,1],[1,0,1],[1,1,0]]
    assert solution()(grid10) == 8
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()