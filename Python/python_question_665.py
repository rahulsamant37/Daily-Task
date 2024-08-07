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
- Connect [2,2] to [3,10] with cost 9.
- Connect [2,2] to [5,2] with cost 3.
- Connect [5,2] to [7,0] with cost 4.
The total cost of this connection is 4 + 9 + 3 + 4 = 20.

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
1 <= points.length <= 1000
-10^6 <= xi, yi <= 10^6
All (xi, yi) are distinct.
'''

# Solution
import heapq

def solution():
    def minCostConnectPoints(points):
        """
        Kruskal's Algorithm using Prim's Algorithm approach.

        Args:
            points: A list of (x, y) coordinates.

        Returns:
            The minimum cost to connect all points.
        """
        n = len(points)
        if n <= 1:
            return 0

        # Calculate Manhattan distances between all pairs of points.
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        # Prim's Algorithm
        visited = set()
        min_cost = 0
        pq = [(0, 0)]  # (cost, point)
        
        while len(visited) < n:
            cost, point = heapq.heappop(pq)
            
            if point in visited:
                continue
            
            visited.add(point)
            min_cost += cost
            
            for neighbor_cost, neighbor in adj[point]:
                if neighbor not in visited:
                    heapq.heappush(pq, (neighbor_cost, neighbor))

        return min_cost
    return minCostConnectPoints

# Test cases
def test_solution():
    minCostConnectPoints = solution()
    # Test case 1
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    assert minCostConnectPoints(points1) == 20

    # Test case 2
    points2 = [[3,12],[-2,5],[-4,1]]
    assert minCostConnectPoints(points2) == 18

    # Test case 3
    points3 = [[0,0]]
    assert minCostConnectPoints(points3) == 0

    # Test case 4
    points4 = [[0,0],[1,1],[1,0],[0,1]]
    assert minCostConnectPoints(points4) == 4

    # Test case 5
    points5 = [[-1000000,-1000000],[1000000,1000000]]
    assert minCostConnectPoints(points5) == 4000000

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()