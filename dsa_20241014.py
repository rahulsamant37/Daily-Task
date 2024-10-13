# DSA Problem for 2024-10-14

Here is a novel DSA problem with a Python solution for 2024-10-14:

**Problem Statement:**

**Minimum Cost to Connect Islands with Bridges**

You are given a 2D grid where some cells represent islands (denoted by 1) and others represent water (denoted by 0). You need to connect all the islands with bridges such that the total cost of building the bridges is minimized. The cost of building a bridge between two adjacent islands is equal to the Manhattan distance between them. Find the minimum cost required to connect all the islands.

Example:
```
Input:
grid = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0]
]

Output: 10
```
In this example, the minimum cost to connect all the islands is 10, which can be achieved by building bridges between the islands as follows:

```
 Island 1 --3--> Island 2
 Island 2 --2--> Island 3
 Island 3 --3--> Island 4
 Island 4 --2--> Island 5
```

**Optimal Solution:**
```
from heapq import heapify, heappop
from collections import defaultdict

def min_cost_to_connect_islands(grid):
    m, n = len(grid), len(grid[0])
    islands = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                islands.append((i, j))

    adj_list = defaultdict(list)
    for i in range(len(islands)):
        for j in range(i + 1, len(islands)):
            x1, y1 = islands[i]
            x2, y2 = islands[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            adj_list[i].append((cost, j))
            adj_list[j].append((cost, i))

    mst_cost = 0
    visited = set()
    heap = [(0, 0)]
    heapify(heap)

    while heap:
        cost, node = heappop(heap)
        if node not in visited:
            visited.add(node)
            mst_cost += cost
            for edge_cost, neighbor in adj_list[node]:
                if neighbor not in visited:
                    heappush(heap, (edge_cost, neighbor))

    return mst_cost
```
**Time/Space Complexity Analysis:**

* Time complexity: O(E log V), where E is the number of edges and V is the number of vertices (islands). In the worst case, E = V*(V-1)/2 and V = number of islands.
* Space complexity: O(V + E), where V is the number of vertices (islands) and E is the number of edges.

The time complexity is dominated by the heap operations (O(log V)) and the number of edges (E). The space complexity is dominated by the adjacency list (O(V + E)).

Note: This problem is a variation of the classic Minimum Spanning Tree (MST) problem, which is a well-known problem in graph theory. The solution uses a priority queue (heap) to efficiently select the minimum-cost edges to add to the MST.