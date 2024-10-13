# Python Question: Minimum Cost to Connect All Points
'''
You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Explanation:
We can connect the points as follows:
- Connect [0,0] to [2,2] with cost 4.
- Connect [2,2] to [5,2] with cost 3.
- Connect [5,2] to [7,0] with cost 4.
- Connect [2,2] to [3,10] with cost 9.
The total cost is 4 + 3 + 4 + 9 = 20.
'''

# Solution
def solution():
    import heapq

    def minCostConnectPoints(points):
        """
        Calculates the minimum cost to connect all points using Prim's algorithm.

        Args:
            points: A list of integer coordinate pairs representing points on a 2D-plane.

        Returns:
            The minimum cost to connect all points.
        """

        n = len(points)
        if n <= 1:
            return 0

        # Adjacency list to store edges and their costs
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((j, cost))
                adj[j].append((i, cost))

        # Prim's algorithm
        visited = set()
        min_cost = 0
        pq = [(0, 0)]  # (cost, node) - start from node 0 with cost 0

        while len(visited) < n:
            cost, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            min_cost += cost

            for neighbor, neighbor_cost in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (neighbor_cost, neighbor))

        return min_cost

    return minCostConnectPoints


# Test cases
def test_solution():
    sol = solution()
    minCostConnectPoints = sol()

    # Test case 1
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    expected1 = 20
    assert minCostConnectPoints(points1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {minCostConnectPoints(points1)}"

    # Test case 2
    points2 = [[3, 12], [-2, 5], [-4, 1]]
    expected2 = 18
    assert minCostConnectPoints(points2) == 18, f"Test Case 2 Failed: Expected {18}, Got {minCostConnectPoints(points2)}"

    # Test case 3
    points3 = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    expected3 = 4
    assert minCostConnectPoints(points3) == 4, f"Test Case 3 Failed: Expected {4}, Got {minCostConnectPoints(points3)}"

    # Test case 4: Single point
    points4 = [[0, 0]]
    expected4 = 0
    assert minCostConnectPoints(points4) == 0, f"Test Case 4 Failed: Expected {0}, Got {minCostConnectPoints(points4)}"

    # Test case 5: Two points
    points5 = [[0, 0], [1, 0]]
    expected5 = 1
    assert minCostConnectPoints(points5) == 1, f"Test Case 5 Failed: Expected {1}, Got {minCostConnectPoints(points5)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()