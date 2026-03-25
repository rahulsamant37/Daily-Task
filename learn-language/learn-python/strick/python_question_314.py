# Python Question: Largest Island
'''
You are given an n x n binary matrix grid.  An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may change one 0 to a 1 to form one bigger island.

Return the maximum possible area of an island after changing at most one 0 to 1.

If there are no 0's in the grid, return the area of the largest island.
If there are no 1's in the grid, return 1.

Example:
Input: grid = [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect the two islands to form an island with area = 3.

Input: grid = [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island.

Input: grid = [[1, 1], [1, 1]]
Output: 4
Explanation: There are no 0's, return the area of the largest island.
'''

# Solution
def largest_island(grid):
    """
    Finds the largest possible island area after changing at most one 0 to 1.

    Args:
      grid: A list of lists representing the binary matrix.

    Returns:
      The maximum possible island area.
    """
    n = len(grid)
    island_id = 2  # Start island IDs from 2 to avoid confusion with 0 and 1
    island_sizes = {}  # Dictionary to store the size of each island
    max_area = 0

    def dfs(i, j, island_id):
        """
        Depth-first search to explore and mark an island with a given ID.
        """
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return 0

        grid[i][j] = island_id  # Mark the cell with the island ID
        area = 1
        area += dfs(i + 1, j, island_id)  # Explore down
        area += dfs(i - 1, j, island_id)  # Explore up
        area += dfs(i, j + 1, island_id)  # Explore right
        area += dfs(i, j - 1, island_id)  # Explore left
        return area

    # First, find all islands and their sizes
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                area = dfs(i, j, island_id)
                island_sizes[island_id] = area
                max_area = max(max_area, area)
                island_id += 1

    # If there are no 0's, return the area of the largest island
    if 0 not in [val for row in grid for val in row]:
        return max_area

    # If there are no 1's, return 1
    if 1 not in [val for row in grid for val in row]:
        return 1

    # Now, try changing each 0 to 1 and see if we can form a larger island
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                neighbor_islands = set()  # Use a set to avoid counting the same island multiple times
                if i > 0 and grid[i - 1][j] > 1:
                    neighbor_islands.add(grid[i - 1][j])
                if i < n - 1 and grid[i + 1][j] > 1:
                    neighbor_islands.add(grid[i + 1][j])
                if j > 0 and grid[i][j - 1] > 1:
                    neighbor_islands.add(grid[i][j - 1])
                if j < n - 1 and grid[i][j + 1] > 1:
                    neighbor_islands.add(grid[i][j + 1])

                new_area = 1  # Start with 1 (the 0 we're changing to 1)
                for island_id in neighbor_islands:
                    new_area += island_sizes[island_id]

                max_area = max(max_area, new_area)

    return max_area

# Test cases
def test_largest_island():
    assert largest_island([[1, 0], [0, 1]]) == 3
    assert largest_island([[1, 1], [1, 0]]) == 4
    assert largest_island([[1, 1], [1, 1]]) == 4
    assert largest_island([[0, 0], [0, 0]]) == 1
    assert largest_island([[0, 1], [1, 0]]) == 3
    assert largest_island([[1, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]]) == 8
    assert largest_island([[0]]) == 1
    assert largest_island([[1]]) == 1
    assert largest_island([[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]]) == 13
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_island()