# Python Question: Minimum Cost to Connect All Points
'''
You are given an array `points` representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the Manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Explanation:

We can connect the points as follows:
- Connect [0,0] with [2,2] at cost 2 + 2 = 4.
- Connect [2,2] with [5,2] at cost 3 + 0 = 3.
- Connect [5,2] with [7,0] at cost 2 + 2 = 4.
- Connect [2,2] with [3,10] at cost 1 + 8 = 9.
The total cost of this connection is 4 + 3 + 4 + 9 = 20.

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
'''

# Solution
import heapq

def minimum_cost_to_connect_all_points(points):
    """
    Finds the minimum cost to connect all points using Prim's algorithm.

    Args:
        points: A list of lists, where each inner list represents the coordinates of a point [x, y].

    Returns:
        The minimum cost to connect all points.
    """

    n = len(points)
    if n <= 1:
        return 0

    # Calculate Manhattan distance between two points
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # Adjacency list to store edges and their weights
    adj = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            dist = manhattan_distance(points[i], points[j])
            adj[i].append((j, dist))
            adj[j].append((i, dist))

    # Prim's algorithm
    visited = set()
    min_cost = 0
    pq = [(0, 0)]  # (cost, node) - Start from node 0 with cost 0

    while pq and len(visited) < n:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        min_cost += cost

        for neighbor, weight in adj[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor))

    return min_cost

# Test cases
def test_minimum_cost_to_connect_all_points():
    assert minimum_cost_to_connect_all_points([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
    assert minimum_cost_to_connect_all_points([[3,12],[-2,5],[-4,1]]) == 18
    assert minimum_cost_to_connect_all_points([[0,0]]) == 0
    assert minimum_cost_to_connect_all_points([[0,0],[1,1]]) == 2
    assert minimum_cost_to_connect_all_points([[0,0],[1,1],[2,2]]) == 4
    assert minimum_cost_to_connect_all_points([[0,0],[1,1],[100,100]]) == 200

if __name__ == "__main__":
    test_minimum_cost_to_connect_all_points()