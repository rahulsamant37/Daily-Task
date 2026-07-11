"""
Heavy-Light Decomposition (HLD)
===============================

Heavy-Light Decomposition is a technique to decompose a tree into 
"heavy" and "light" edges, allowing efficient path queries and updates.

A heavy edge connects a node to its child with the largest subtree.
All other edges are light edges. This creates chains that can be 
efficiently queried using segment trees.

Time Complexity:
- Preprocessing: O(n log n)
- Path query/update: O(log² n)
Space Complexity: O(n log n)

Author: Converted from C++ implementation
"""

import math
from collections import defaultdict

class SegmentTree:
    """
    Segment tree for range queries and point updates
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr[:]
        self.build(0, self.n - 1, 1)
    
    def build(self, start, end, node):
        """Build the segment tree"""
        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2
        self.build(start, mid, 2 * node)
        self.build(mid + 1, end, 2 * node + 1)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
    
    def update(self, start, end, node, idx, val):
        """Update value at index idx"""
        if start == end:
            self.tree[node] = val
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(start, mid, 2 * node, idx, val)
        else:
            self.update(mid + 1, end, 2 * node + 1, idx, val)
        
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
    
    def query(self, start, end, node, l, r):
        """Query maximum in range [l, r]"""
        if start > r or end < l:
            return float('-inf')
        if start >= l and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_max = self.query(start, mid, 2 * node, l, r)
        right_max = self.query(mid + 1, end, 2 * node + 1, l, r)
        return max(left_max, right_max)
    
    def point_update(self, idx, val):
        """Public interface for point update"""
        self.update(0, self.n - 1, 1, idx, val)
    
    def range_query(self, l, r):
        """Public interface for range query"""
        return self.query(0, self.n - 1, 1, l, r)

class BinaryLifting:
    """
    Binary lifting for LCA queries
    """
    
    def __init__(self, n, adj, root=0):
        self.n = n
        self.max_log = int(math.log2(n)) + 1
        self.parent = [[-1] * self.max_log for _ in range(n)]
        self.depth = [0] * n
        self.build(adj, root)
    
    def build(self, adj, root):
        """Build binary lifting table"""
        # DFS to set parents and depths
        stack = [(root, -1, 0)]
        visited = [False] * self.n
        
        while stack:
            node, par, d = stack.pop()
            if visited[node]:
                continue
            
            visited[node] = True
            self.parent[node][0] = par
            self.depth[node] = d
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    stack.append((neighbor, node, d + 1))
        
        # Fill binary lifting table
        for j in range(1, self.max_log):
            for i in range(self.n):
                if self.parent[i][j-1] != -1:
                    self.parent[i][j] = self.parent[self.parent[i][j-1]][j-1]
    
    def kth_ancestor(self, node, k):
        """Find k-th ancestor of node"""
        for i in range(self.max_log):
            if (k >> i) & 1:
                if node == -1:
                    return -1
                node = self.parent[node][i]
        return node
    
    def lca(self, u, v):
        """Find LCA of u and v"""
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Bring u to same level as v
        diff = self.depth[u] - self.depth[v]
        u = self.kth_ancestor(u, diff)
        
        if u == v:
            return u
        
        # Binary search for LCA
        for i in range(self.max_log - 1, -1, -1):
            if self.parent[u][i] != self.parent[v][i]:
                u = self.parent[u][i]
                v = self.parent[v][i]
        
        return self.parent[u][0]

class HeavyLightDecomposition:
    """
    Heavy-Light Decomposition implementation
    """
    
    def __init__(self, n, adj, values, root=0):
        """
        Initialize HLD
        
        Args:
            n: number of nodes
            adj: adjacency list
            values: node values
            root: root of the tree
        """
        self.n = n
        self.adj = adj
        self.root = root
        self.values = values[:]
        
        # HLD specific arrays
        self.heavy_child = [-1] * n
        self.subtree_size = [0] * n
        self.chain_head = list(range(n))  # Each node is its own chain head initially
        self.position = [0] * n  # Position in DFS order
        self.parent = [-1] * n
        self.depth = [0] * n
        
        # Build HLD
        self.dfs_size(root, -1)
        self.dfs_hld(root, -1, 0)
        
        # Build segment tree on linearized tree
        self.seg_tree = SegmentTree([values[i] for i in range(n)])
        
        # Binary lifting for LCA
        self.bl = BinaryLifting(n, adj, root)
    
    def dfs_size(self, node, par):
        """
        First DFS to calculate subtree sizes and heavy children
        """
        self.subtree_size[node] = 1
        self.parent[node] = par
        
        max_subtree = 0
        for neighbor in self.adj[node]:
            if neighbor != par:
                self.depth[neighbor] = self.depth[node] + 1
                self.dfs_size(neighbor, node)
                self.subtree_size[node] += self.subtree_size[neighbor]
                
                if self.subtree_size[neighbor] > max_subtree:
                    max_subtree = self.subtree_size[neighbor]
                    self.heavy_child[node] = neighbor
    
    def dfs_hld(self, node, par, pos):
        """
        Second DFS to assign positions and chain heads
        """
        self.position[node] = pos
        
        # Process heavy child first
        if self.heavy_child[node] != -1:
            self.chain_head[self.heavy_child[node]] = self.chain_head[node]
            pos = self.dfs_hld(self.heavy_child[node], node, pos + 1)
        
        # Process light children
        for neighbor in self.adj[node]:
            if neighbor != par and neighbor != self.heavy_child[node]:
                pos = self.dfs_hld(neighbor, node, pos + 1)
        
        return pos
    
    def path_query(self, u, v):
        """
        Query maximum value on path from u to v
        """
        lca = self.bl.lca(u, v)
        
        # Query from u to lca
        result1 = self.query_up(u, lca)
        
        # Query from v to lca
        result2 = self.query_up(v, lca)
        
        # Include lca value
        lca_val = self.seg_tree.range_query(self.position[lca], self.position[lca])
        
        return max(result1, result2, lca_val)
    
    def query_up(self, node, ancestor):
        """
        Query maximum from node up to ancestor (exclusive)
        """
        result = float('-inf')
        
        while self.chain_head[node] != self.chain_head[ancestor]:
            # Query entire chain from node to chain head
            chain_top = self.chain_head[node]
            result = max(result, 
                        self.seg_tree.range_query(self.position[chain_top], 
                                                 self.position[node]))
            node = self.parent[chain_top]
        
        # Query partial chain
        if self.position[ancestor] < self.position[node]:
            result = max(result, 
                        self.seg_tree.range_query(self.position[ancestor] + 1, 
                                                 self.position[node]))
        
        return result
    
    def point_update(self, node, value):
        """
        Update value at a node
        """
        self.values[node] = value
        self.seg_tree.point_update(self.position[node], value)
    
    def subtree_query(self, node):
        """
        Query maximum in subtree of node
        """
        subtree_end = self.position[node] + self.subtree_size[node] - 1
        return self.seg_tree.range_query(self.position[node], subtree_end)
    
    def distance(self, u, v):
        """
        Find distance between two nodes
        """
        lca = self.bl.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca]

def build_tree_from_edges(n, edge_list):
    """
    Build adjacency list from edge list
    """
    adj = [[] for _ in range(n)]
    for u, v in edge_list:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def test_hld():
    """Test Heavy-Light Decomposition"""
    print("Testing Heavy-Light Decomposition")
    print("=" * 35)
    
    # Test 1: Simple tree
    print("Test 1: Simple Tree")
    #     0(5)
    #    /    \
    #   1(3)   2(7)
    #  /      / | \
    # 3(1)   4(2) 5(8) 6(4)
    
    n1 = 7
    edges1 = [(0, 1), (0, 2), (1, 3), (2, 4), (2, 5), (2, 6)]
    values1 = [5, 3, 7, 1, 2, 8, 4]
    adj1 = build_tree_from_edges(n1, edges1)
    
    hld1 = HeavyLightDecomposition(n1, adj1, values1, root=0)
    
    print(f"Tree structure: {edges1}")
    print(f"Node values: {values1}")
    print(f"Heavy children: {hld1.heavy_child}")
    print(f"Chain heads: {hld1.chain_head}")
    print(f"DFS positions: {hld1.position}")
    
    # Test path queries
    path_queries = [
        (3, 5),  # Path from leaf to leaf
        (1, 6),  # Another leaf to leaf path
        (3, 0),  # Leaf to root
        (4, 6),  # Within same subtree
    ]
    
    print("Path queries (maximum on path):")
    for u, v in path_queries:
        result = hld1.path_query(u, v)
        print(f"  Path({u}, {v}): {result}")
    print()
    
    # Test 2: Point updates
    print("Test 2: Point Updates")
    print(f"Original value at node 5: {values1[5]}")
    hld1.point_update(5, 15)
    print(f"Updated value at node 5: 15")
    
    # Re-test some path queries
    print("Path queries after update:")
    for u, v in [(3, 5), (0, 5)]:
        result = hld1.path_query(u, v)
        print(f"  Path({u}, {v}): {result}")
    print()
    
    # Test 3: Subtree queries
    print("Test 3: Subtree Queries")
    subtree_tests = [0, 1, 2]
    for node in subtree_tests:
        result = hld1.subtree_query(node)
        print(f"  Maximum in subtree of {node}: {result}")
    print()
    
    # Test 4: Linear tree (worst case for HLD)
    print("Test 4: Linear Tree")
    n4 = 6
    edges4 = [(i, i+1) for i in range(n4-1)]  # 0-1-2-3-4-5
    values4 = [10, 20, 5, 30, 15, 25]
    adj4 = build_tree_from_edges(n4, edges4)
    
    hld4 = HeavyLightDecomposition(n4, adj4, values4, root=0)
    
    print(f"Linear tree: 0-1-2-3-4-5")
    print(f"Values: {values4}")
    print(f"Heavy children: {hld4.heavy_child}")
    
    # Test path queries on linear tree
    linear_queries = [(0, 5), (1, 4), (2, 5)]
    for u, v in linear_queries:
        result = hld4.path_query(u, v)
        distance = hld4.distance(u, v)
        print(f"  Path({u}, {v}): max={result}, distance={distance}")
    print()
    
    # Test 5: Star graph
    print("Test 5: Star Graph")
    n5 = 6
    center = 0
    edges5 = [(center, i) for i in range(1, n5)]
    values5 = [10, 20, 5, 30, 15, 25]
    adj5 = build_tree_from_edges(n5, edges5)
    
    hld5 = HeavyLightDecomposition(n5, adj5, values5, root=center)
    
    print(f"Star graph with center {center}")
    print(f"Values: {values5}")
    print(f"Heavy children: {hld5.heavy_child}")
    
    # All paths in star graph go through center
    star_queries = [(1, 3), (2, 4), (1, 5)]
    for u, v in star_queries:
        result = hld5.path_query(u, v)
        print(f"  Path({u}, {v}): {result}")
    print()
    
    # Test 6: Complete binary tree
    print("Test 6: Complete Binary Tree")
    n6 = 7
    edges6 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    values6 = [15, 10, 20, 5, 8, 25, 12]
    adj6 = build_tree_from_edges(n6, edges6)
    
    hld6 = HeavyLightDecomposition(n6, adj6, values6, root=0)
    
    print(f"Binary tree edges: {edges6}")
    print(f"Values: {values6}")
    print(f"Heavy children: {hld6.heavy_child}")
    
    # Test various paths in binary tree
    binary_queries = [(3, 6), (4, 5), (3, 4)]
    for u, v in binary_queries:
        result = hld6.path_query(u, v)
        lca = hld6.bl.lca(u, v)
        print(f"  Path({u}, {v}): max={result}, LCA={lca}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_hld()
