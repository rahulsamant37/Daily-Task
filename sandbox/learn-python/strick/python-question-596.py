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
- Connect [0, 0] to [2, 2] with cost 4.
- Connect [2, 2] to [5, 2] with cost 3.
- Connect [5, 2] to [7, 0] with cost 4.
- Connect [2, 2] to [3, 10] with cost 9.
The total cost of this is 4 + 3 + 4 + 9 = 20.
'''

# Solution
import heapq

def min_cost_connect_points(points):
    """
    Calculates the minimum cost to connect all points using Prim's algorithm.

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

    # Initialize the minimum spanning tree (MST)
    mst_cost = 0
    edges = 0  # Number of edges in MST
    visited = [False] * n  # Track visited nodes

    # Start with the first point
    pq = []  # Priority queue to store edges (cost, point)
    heapq.heappush(pq, (0, 0))  # (cost, point index)

    while edges < n:  # Iterate until all points are in the MST
        cost, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        mst_cost += cost
        edges += 1

        # Add new edges to the priority queue
        for v in range(n):
            if not visited[v]:
                distance = manhattan_distance(points[u], points[v])
                heapq.heappush(pq, (distance, v))

    return mst_cost

# Test cases
def test_solution():
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    assert min_cost_connect_points(points1) == 20

    points2 = [[3,12],[-2,5],[-4,1]]
    assert min_cost_connect_points(points2) == 18

    points3 = [[0,0],[1,1],[1,0],[-1,1]]
    assert min_cost_connect_points(points3) == 4

    points4 = [[-100000,-100000],[100000,100000]]
    assert min_cost_connect_points(points4) == 400000

    points5 = [[0,0]]
    assert min_cost_connect_points(points5) == 0

    points6 = [[0,0],[0,0]]
    assert min_cost_connect_points(points6) == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()