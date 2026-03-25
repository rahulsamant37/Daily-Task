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
- Connect (0, 0) with (2, 2) at cost 4.
- Connect (2, 2) with (5, 2) at cost 3.
- Connect (5, 2) with (7, 0) at cost 4.
- Connect (2, 2) with (3, 10) at cost 9.
The total cost of this graph is 4 + 3 + 4 + 9 = 20.
'''

# Solution
import heapq

def solution():
    def minCostConnectPoints(points):
        """
        Finds the minimum cost to connect all points using Prim's algorithm.

        Args:
            points: A list of lists, where each inner list represents a point [x, y].

        Returns:
            The minimum cost to connect all points.
        """
        n = len(points)
        if n <= 1:
            return 0

        # Calculate Manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Adjacency list to store edges and their weights (Manhattan distances)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhattan_distance(points[i], points[j])
                adj[i].append((j, dist))
                adj[j].append((i, dist))

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

            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, neighbor))

        return min_cost
    return minCostConnectPoints

# Test cases
def test_solution():
    minCostConnectPoints = solution()

    # Test case 1
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    expected1 = 20
    assert minCostConnectPoints(points1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {minCostConnectPoints(points1)}"

    # Test case 2
    points2 = [[3,12],[-2,5],[-4,1]]
    expected2 = 18
    assert minCostConnectPoints(points2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {minCostConnectPoints(points2)}"

    # Test case 3
    points3 = [[0,0],[1,1],[1,0],[-1,1]]
    expected3 = 4
    assert minCostConnectPoints(points3) == 4, f"Test Case 3 Failed: Expected {expected3}, Got {minCostConnectPoints(points3)}"

    # Test case 4
    points4 = [[-13, -16], [-14, -13], [-5, -15], [-2, -1], [-14, -5], [-10, -18], [-19, 1], [12, -18], [-4, -12], [-16, -7]]
    expected4 = 137
    assert minCostConnectPoints(points4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {minCostConnectPoints(points4)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()