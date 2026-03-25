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
- Connect (0, 0) with (2, 2) with cost 4.
- Connect (2, 2) with (5, 2) with cost 3.
- Connect (5, 2) with (7, 0) with cost 4.
- Connect (2, 2) with (3, 10) with cost 9.

The total cost of the path is 4 + 3 + 4 + 9 = 20.
'''

# Solution
import heapq

def solution():
    def minCostConnectPoints(points):
        """
        Finds the minimum cost to connect all points using Prim's algorithm.

        Args:
            points: A list of lists representing the coordinates of points.

        Returns:
            The minimum cost to connect all points.
        """

        n = len(points)
        visited = [False] * n
        min_cost = 0
        edges = []  # Priority queue to store edges with their costs
        heapq.heappush(edges, (0, 0))  # Start from the first point (index 0) with cost 0

        num_visited = 0
        while num_visited < n:
            cost, u = heapq.heappop(edges)

            if visited[u]:
                continue

            visited[u] = True
            min_cost += cost
            num_visited += 1

            for v in range(n):
                if not visited[v]:
                    # Calculate Manhattan distance between u and v
                    manhattan_distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(edges, (manhattan_distance, v))

        return min_cost
    return minCostConnectPoints

# Test cases
def test_solution():
    minCostConnectPoints = solution()

    # Test case 1
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    expected1 = 20
    actual1 = minCostConnectPoints(points1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {actual1}"

    # Test case 2
    points2 = [[3,12],[-2,5],[-4,1]]
    expected2 = 18
    actual2 = minCostConnectPoints(points2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {actual2}"

    # Test case 3
    points3 = [[0,0],[1,1],[1,0],[-1,1]]
    expected3 = 4
    actual3 = minCostConnectPoints(points3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {actual3}"

    # Test case 4
    points4 = [[-100000, -100000], [100000, 100000]]
    expected4 = 400000
    actual4 = minCostConnectPoints(points4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {actual4}"
    
    # Test case 5: Single point
    points5 = [[0, 0]]
    expected5 = 0
    actual5 = minCostConnectPoints(points5)
    assert actual5 == 0, f"Test Case 5 Failed: Expected {expected5}, Got {actual5}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()