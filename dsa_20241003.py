# DSA Problem for 2024-10-03

Here is a novel DSA problem with a Python solution for 2024-10-03:

**Problem Statement:**

**"Maximum Sum of Connected Components"**

Given a weighted undirected graph with `n` nodes and `m` edges, where each node has a weight associated with it, find the maximum sum of weights of connected components in the graph.

**Formal Definition:**

* The graph is represented as an adjacency list `graph`, where `graph[i]` is a list of neighboring nodes of node `i`.
* Each node `i` has a weight `weights[i]` associated with it.
* A connected component is a subset of nodes that are reachable from each other through edges.

**Example Input:**

```
graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
weights = [5, 3, 2, 7]
```

**Expected Output:**

```
14
```

**Explanation:**

The graph has 4 nodes and 4 edges. The weights of the nodes are `[5, 3, 2, 7]`. The connected components are `{0, 1, 2}` and `{3}`. The maximum sum of weights of connected components is `5 + 3 + 2 = 10` for the first component and `7` for the second component. The maximum sum is `10 + 7 = 14`.

**Optimal Solution:**
```python
def max_sum_of_connected_components(graph, weights):
    n = len(graph)
    visited = [False] * n
    max_sum = 0

    def dfs(node):
        nonlocal max_sum
        if visited[node]:
            return 0
        visited[node] = True
        curr_sum = weights[node]
        for neighbor in graph[node]:
            curr_sum += dfs(neighbor)
        max_sum = max(max_sum, curr_sum)
        return curr_sum

    for node in range(n):
        if not visited[node]:
            dfs(node)

    return max_sum
```

**Time Complexity Analysis:**

The time complexity of the solution is O(n + m), where n is the number of nodes and m is the number of edges. The reason is that we visit each node and edge exactly once during the DFS traversal.

**Space Complexity Analysis:**

The space complexity of the solution is O(n), where n is the number of nodes. We use a boolean array `visited` of size n to keep track of visited nodes, and a recursive function call stack that can grow up to a maximum depth of n in the worst case.

I hope you find this problem and solution helpful!