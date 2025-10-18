"""
Binary Lifting Algorithm
========================

Binary lifting is a technique used to preprocess a tree to answer
queries about ancestors in O(log n) time. It's commonly used for:
- Finding k-th ancestor of a node
- Lowest Common Ancestor (LCA) queries
- Tree path queries

Time Complexity: 
- Preprocessing: O(n log n)
- Query: O(log n)
Space Complexity: O(n log n)

Author: Converted from C++ implementation
"""

import math
from collections import defaultdict, deque

class BinaryLifting:
    """
    Binary lifting implementation for tree queries
    """
    
    def __init__(self, n, edges=None, root=0):
        """
        Initialize binary lifting structure
        
        Args:
            n: number of nodes in tree
            edges: adjacency list representation of tree
            root: root of the tree (default 0)
        """
        self.n = n
        self.max_log = int(math.log2(n)) + 1
        self.parent = [[-1] * self.max_log for _ in range(n)]
        self.depth = [0] * n
        
        if edges is not None:
            self.build(edges, root)
    
    def build(self, edges, root):
        """
        Build the binary lifting table
        
        Args:
            edges: adjacency list of the tree
            root: root node
        """
        # First DFS to set immediate parents and depths
        self._dfs(root, -1, 0, edges)
        
        # Fill the binary lifting table
        for j in range(1, self.max_log):
            for i in range(self.n):
                if self.parent[i][j-1] != -1:
                    self.parent[i][j] = self.parent[self.parent[i][j-1]][j-1]
    
    def _dfs(self, node, par, d, edges):
        """
        DFS to set immediate parents and depths
        
        Args:
            node: current node
            par: parent of current node
            d: depth of current node
            edges: adjacency list
        """
        self.parent[node][0] = par
        self.depth[node] = d
        
        for neighbor in edges[node]:
            if neighbor != par:
                self._dfs(neighbor, node, d + 1, edges)
    
    def kth_ancestor(self, node, k):
        """
        Find k-th ancestor of a node
        
        Args:
            node: starting node
            k: number of steps up
        
        Returns:
            k-th ancestor, or -1 if doesn't exist
        """
        if k > self.depth[node]:
            return -1
        
        for i in range(self.max_log):
            if (k >> i) & 1:
                if node == -1:
                    return -1
                node = self.parent[node][i]
        
        return node
    
    def lca(self, u, v):
        """
        Find Lowest Common Ancestor of two nodes
        
        Args:
            u: first node
            v: second node
        
        Returns:
            LCA of u and v
        """
        # Make sure u is deeper than v
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Bring u to the same level as v
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
    
    def distance(self, u, v):
        """
        Find distance between two nodes
        
        Args:
            u: first node
            v: second node
        
        Returns:
            distance between u and v
        """
        lca_node = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca_node]
    
    def is_ancestor(self, u, v):
        """
        Check if u is an ancestor of v
        
        Args:
            u: potential ancestor
            v: node to check
        
        Returns:
            True if u is ancestor of v
        """
        return self.lca(u, v) == u and self.depth[u] <= self.depth[v]
    
    def path_to_root(self, node):
        """
        Get path from node to root
        
        Args:
            node: starting node
        
        Returns:
            list of nodes from node to root
        """
        path = []
        current = node
        
        while current != -1:
            path.append(current)
            current = self.parent[current][0]
        
        return path
    
    def node_at_distance(self, u, v, k):
        """
        Find node at distance k from u towards v
        
        Args:
            u: starting node
            v: target node
            k: distance from u
        
        Returns:
            node at distance k from u on path to v, or -1 if invalid
        """
        lca_node = self.lca(u, v)
        dist_to_lca = self.depth[u] - self.depth[lca_node]
        
        if k <= dist_to_lca:
            # Node is between u and lca
            return self.kth_ancestor(u, k)
        else:
            # Node is between lca and v
            remaining = k - dist_to_lca
            dist_lca_to_v = self.depth[v] - self.depth[lca_node]
            
            if remaining > dist_lca_to_v:
                return -1
            
            return self.kth_ancestor(v, dist_lca_to_v - remaining)

def build_tree_from_edges(n, edges_list):
    """
    Build adjacency list from edge list
    
    Args:
        n: number of nodes
        edges_list: list of (u, v) edges
    
    Returns:
        adjacency list representation
    """
    adj = [[] for _ in range(n)]
    for u, v in edges_list:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def test_binary_lifting():
    """Test binary lifting implementation"""
    print("Testing Binary Lifting Algorithm")
    print("=" * 35)
    
    # Test 1: Simple tree
    print("Test 1: Simple Tree")
    #     0
    #    / \
    #   1   2
    #  /   / \
    # 3   4   5
    
    n1 = 6
    edges1 = [(0, 1), (0, 2), (1, 3), (2, 4), (2, 5)]
    adj1 = build_tree_from_edges(n1, edges1)
    
    bl1 = BinaryLifting(n1, adj1, root=0)
    
    print(f"Tree edges: {edges1}")
    print(f"Depths: {bl1.depth}")
    
    # Test k-th ancestor queries
    test_cases = [
        (3, 1),  # 1st ancestor of 3 should be 1
        (3, 2),  # 2nd ancestor of 3 should be 0
        (5, 1),  # 1st ancestor of 5 should be 2
        (4, 2),  # 2nd ancestor of 4 should be 0
        (0, 1),  # 1st ancestor of 0 should be -1 (doesn't exist)
    ]
    
    print("K-th ancestor queries:")
    for node, k in test_cases:
        ancestor = bl1.kth_ancestor(node, k)
        print(f"  {k}-th ancestor of {node}: {ancestor}")
    print()
    
    # Test 2: LCA queries
    print("Test 2: LCA Queries")
    lca_cases = [
        (3, 4),  # LCA of 3 and 4
        (3, 5),  # LCA of 3 and 5
        (1, 2),  # LCA of 1 and 2
        (4, 5),  # LCA of 4 and 5
        (0, 3),  # LCA of 0 and 3
    ]
    
    for u, v in lca_cases:
        lca_result = bl1.lca(u, v)
        distance = bl1.distance(u, v)
        print(f"  LCA({u}, {v}) = {lca_result}, distance = {distance}")
    print()
    
    # Test 3: Path queries
    print("Test 3: Path Queries")
    path_cases = [
        (3, 5, 0),  # Node at distance 0 from 3 towards 5
        (3, 5, 1),  # Node at distance 1 from 3 towards 5
        (3, 5, 2),  # Node at distance 2 from 3 towards 5
        (3, 5, 3),  # Node at distance 3 from 3 towards 5
        (4, 1, 2),  # Node at distance 2 from 4 towards 1
    ]
    
    for u, v, k in path_cases:
        node = bl1.node_at_distance(u, v, k)
        print(f"  Node at distance {k} from {u} towards {v}: {node}")
    print()
    
    # Test 4: Larger tree (binary tree)
    print("Test 4: Complete Binary Tree")
    #       0
    #      / \
    #     1   2
    #    / \ / \
    #   3 4 5  6
    
    n4 = 7
    edges4 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    adj4 = build_tree_from_edges(n4, edges4)
    
    bl4 = BinaryLifting(n4, adj4, root=0)
    
    print(f"Binary tree edges: {edges4}")
    
    # Test all LCA combinations for leaves
    leaves = [3, 4, 5, 6]
    print("LCA between all leaf pairs:")
    for i in range(len(leaves)):
        for j in range(i + 1, len(leaves)):
            u, v = leaves[i], leaves[j]
            lca_result = bl4.lca(u, v)
            print(f"  LCA({u}, {v}) = {lca_result}")
    print()
    
    # Test 5: Linear tree (worst case)
    print("Test 5: Linear Tree")
    n5 = 8
    edges5 = [(i, i+1) for i in range(n5-1)]  # 0-1-2-3-4-5-6-7
    adj5 = build_tree_from_edges(n5, edges5)
    
    bl5 = BinaryLifting(n5, adj5, root=0)
    
    print(f"Linear tree: 0-1-2-3-4-5-6-7")
    
    # Test ancestor queries on linear tree
    for k in [1, 2, 4, 7]:
        ancestor = bl5.kth_ancestor(7, k)
        print(f"  {k}-th ancestor of 7: {ancestor}")
    
    # Test LCA on linear tree
    print(f"  LCA(2, 6) = {bl5.lca(2, 6)}")
    print(f"  Distance(1, 5) = {bl5.distance(1, 5)}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_binary_lifting()
