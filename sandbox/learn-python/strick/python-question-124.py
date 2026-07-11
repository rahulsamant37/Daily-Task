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
- Connect [2,2] to [3,10] with cost 11.
The total cost is 4 + 3 + 4 + 11 = 22.
Another way to connect the points is:
- Connect [0,0] to [7,0] with cost 7.
- Connect [2,2] to [5,2] with cost 3.
- Connect [2,2] to [3,10] with cost 11.
The total cost is 7 + 3 + 11 = 21.
But the minimum cost to connect all the points is 20.
'''

# Solution
import heapq

def solution():
    def minCostConnectPoints(points):
        """
        Implements Prim's algorithm to find the minimum cost to connect all points.

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

        # Adjacency list to store edges and their weights (distances).  Not explicitly needed with heap.
        # adj = {i: [] for i in range(n)}  # i: [(neighbor, weight)]

        # Start with an arbitrary point (e.g., point 0)
        visited = {0}
        min_heap = []  # (cost, point) -  point is the index
        for j in range(1, n):
            heapq.heappush(min_heap, (manhattan_distance(points[0], points[j]), j))  # Cost to connect point 0 to all other points

        total_cost = 0
        edges_used = 0

        while min_heap and edges_used < n - 1:
            cost, next_point = heapq.heappop(min_heap)

            if next_point in visited:
                continue

            visited.add(next_point)
            total_cost += cost
            edges_used += 1

            # Update the min_heap with costs to connect the new point to all unvisited points
            for j in range(n):
                if j not in visited:
                    heapq.heappush(min_heap, (manhattan_distance(points[next_point], points[j]), j))

        return total_cost
    return minCostConnectPoints

# Test cases
def test_solution():
    minCostConnectPoints = solution()
    assert minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
    assert minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
    assert minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]) == 4
    assert minCostConnectPoints([[0,0]]) == 0
    assert minCostConnectPoints([[0,0],[1,0]]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()