# DSA Problem for 2024-10-30

Here is a novel DSA problem with a Python solution for 2024-10-30:

**Problem Statement:**

**"Maximum Spanning Tree Queries"**

You are given an undirected weighted graph with `n` nodes and `m` edges. The graph is represented as an adjacency list `adj_list`, where `adj_list[i]` is a list of tuples `(j, w)` representing an edge from node `i` to node `j` with weight `w`.

You are also given a list of `q` queries, where each query is a pair `(u, v)` representing a pair of nodes. For each query, you need to find the maximum edge weight on the path from node `u` to node `v` in the maximum spanning tree of the graph.

**Constraints:**

* `1 <= n <= 10^5`
* `1 <= m <= 2*10^5`
* `1 <= q <= 10^5`
* `1 <= u, v <= n`
* `1 <= w <= 10^9`

**Optimal Solution:**

We can use the following approach to solve this problem:

1. First, we build the maximum spanning tree of the graph using Kruskal's algorithm.
2. Then, we use a union-find data structure to support queries. We initialize the union-find data structure with `n` disjoint sets, each representing a node in the graph.
3. For each query `(u, v)`, we find the maximum edge weight on the path from `u` to `v` in the maximum spanning tree by traversing up the tree from `u` to the LCA (lowest common ancestor) of `u` and `v`, and then traversing down from the LCA to `v`.

Here is the Python solution:
```python
def maximum_spanning_tree_queries(adj_list, queries):
    # Build maximum spanning tree using Kruskal's algorithm
    edges = []
    for i in range(len(adj_list)):
        for j, w in adj_list[i]:
            edges.append((w, i, j))
    edges.sort(reverse=True)

    mst_edges = []
    parent = list(range(len(adj_list)))
    rank = [0] * len(adj_list)

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1

    for w, u, v in edges:
        if find(u) != find(v):
            mst_edges.append((w, u, v))
            union(u, v)

    # Initialize union-find data structure
    parent = list(range(len(adj_list)))
    rank = [0] * len(adj_list)

    # Process queries
    results = []
    for u, v in queries:
        max_weight = 0
        while u != v:
            # Traverse up the tree from u to the LCA of u and v
            while find(u) != find(v):
                max_weight = max(max_weight, mst_edges[parent[u]][0])
                u = parent[u]
            # Traverse down from the LCA to v
            while find(u) != v:
                max_weight = max(max_weight, mst_edges[u][0])
                u = mst_edges[u][1]
        results.append(max_weight)
    return results
```
**Time/Space Complexity Analysis:**

* The time complexity of the Kruskal's algorithm is `O(m log m)`, where `m` is the number of edges.
* The time complexity of processing each query is `O(log n)`, where `n` is the number of nodes.
* Therefore, the total time complexity is `O(m log m + q log n)`.
* The space complexity is `O(m + n)`, which is required to store the maximum spanning tree and the union-find data structure.

Note that the solution has a good time complexity because we only process each edge once during the Kruskal's algorithm, and we use a union-find data structure to support fast queries.