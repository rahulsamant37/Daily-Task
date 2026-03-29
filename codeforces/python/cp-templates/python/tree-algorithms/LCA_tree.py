import math
from collections import defaultdict, deque

class BinaryLifting:
    """
    Binary Lifting for fast ancestor queries
    Supports k-th ancestor queries in O(log k) time
    """
    
    def __init__(self, n, edges, root=0):
        """
        Initialize binary lifting
        
        Args:
            n: number of nodes
            edges: adjacency list representation of tree
            root: root of the tree
        """
        self.n = n
        self.max_log = int(math.log2(n)) + 1
        
        # parent[i][j] = 2^j-th parent of node i
        self.parent = [[-1] * self.max_log for _ in range(n)]
        
        self._build_parent_table(edges, root)
    
    def _build_parent_table(self, edges, root):
        """Build the binary lifting parent table"""
        visited = [False] * self.n
        self._dfs_binary_lifting(edges, root, visited)
        
        # Fill the binary lifting table
        for j in range(1, self.max_log):
            for i in range(self.n):
                if self.parent[i][j - 1] != -1:
                    self.parent[i][j] = self.parent[self.parent[i][j - 1]][j - 1]
    
    def _dfs_binary_lifting(self, edges, node, visited):
        """DFS to set immediate parents"""
        visited[node] = True
        
        for neighbor in edges[node]:
            if not visited[neighbor]:
                self.parent[neighbor][0] = node
                self._dfs_binary_lifting(edges, neighbor, visited)
    
    def kth_ancestor(self, node, k):
        """
        Find k-th ancestor of node
        
        Args:
            node: starting node
            k: number of steps up
            
        Returns:
            k-th ancestor, or -1 if doesn't exist
        """
        current = node
        
        for i in range(self.max_log):
            if k & (1 << i):
                current = self.parent[current][i]
                if current == -1:
                    return -1
        
        return current


class LCA:
    """
    Lowest Common Ancestor using Binary Lifting
    Preprocessing: O(n log n)
    Query: O(log n)
    """
    
    def __init__(self, n, edges, root=0):
        """
        Initialize LCA structure
        
        Args:
            n: number of nodes
            edges: adjacency list representation of tree
            root: root of the tree
        """
        self.n = n
        self.root = root
        self.level = [0] * n
        
        # Initialize binary lifting
        self.binary_lifting = BinaryLifting(n, edges, root)
        
        # Calculate levels
        self._calculate_levels(edges, root)
    
    def _calculate_levels(self, edges, root):
        """Calculate level of each node using BFS"""
        queue = deque([root])
        visited = [False] * self.n
        visited[root] = True
        self.level[root] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbor in edges[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    self.level[neighbor] = self.level[node] + 1
                    queue.append(neighbor)
    
    def get_lca(self, u, v):
        """
        Find LCA of nodes u and v
        
        Args:
            u, v: nodes to find LCA of
            
        Returns:
            LCA of u and v
        """
        # Make sure u is at higher or same level as v
        if self.level[u] > self.level[v]:
            u, v = v, u
        
        # Bring v to same level as u
        level_diff = self.level[v] - self.level[u]
        v = self.binary_lifting.kth_ancestor(v, level_diff)
        
        if u == v:
            return u
        
        # Binary search for LCA
        for i in range(self.binary_lifting.max_log - 1, -1, -1):
            parent_u = self.binary_lifting.parent[u][i]
            parent_v = self.binary_lifting.parent[v][i]
            
            if parent_u != parent_v and parent_u != -1 and parent_v != -1:
                u = parent_u
                v = parent_v
        
        return self.binary_lifting.parent[u][0]
    
    def distance(self, u, v):
        """
        Calculate distance between two nodes
        
        Args:
            u, v: nodes
            
        Returns:
            shortest distance between u and v
        """
        lca = self.get_lca(u, v)
        return self.level[u] + self.level[v] - 2 * self.level[lca]
    
    def is_ancestor(self, u, v):
        """
        Check if u is an ancestor of v
        
        Args:
            u: potential ancestor
            v: node
            
        Returns:
            True if u is ancestor of v, False otherwise
        """
        return self.get_lca(u, v) == u
    
    def path_exists(self, u, v):
        """Check if path exists between u and v (always True in tree)"""
        return True


class LCA_Optimized:
    """
    More space-efficient LCA implementation
    Uses the fact that we only need log(n) bits for binary lifting
    """
    
    def __init__(self, n, edges, root=0):
        self.n = n
        self.root = root
        self.LOG = int(math.log2(n)) + 1
        
        # up[i][j] = 2^j-th ancestor of node i
        self.up = [[-1] * self.LOG for _ in range(n)]
        self.depth = [0] * n
        
        self._preprocess(edges, root)
    
    def _preprocess(self, edges, root):
        """Preprocess the tree"""
        # DFS to set up immediate parents and depths
        stack = [(root, -1, 0)]
        
        while stack:
            node, parent, d = stack.pop()
            self.up[node][0] = parent
            self.depth[node] = d
            
            for neighbor in edges[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, d + 1))
        
        # Fill binary lifting table
        for j in range(1, self.LOG):
            for i in range(self.n):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]
    
    def lca(self, u, v):
        """Find LCA of u and v"""
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Bring u to same depth as v
        diff = self.depth[u] - self.depth[v]
        for i in range(self.LOG):
            if (diff >> i) & 1:
                u = self.up[u][i]
        
        if u == v:
            return u
        
        # Binary search
        for i in range(self.LOG - 1, -1, -1):
            if self.up[u][i] != self.up[v][i]:
                u = self.up[u][i]
                v = self.up[v][i]
        
        return self.up[u][0]
    
    def dist(self, u, v):
        """Distance between u and v"""
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]
    
    def kth_ancestor(self, node, k):
        """Find k-th ancestor of node"""
        for i in range(self.LOG):
            if (k >> i) & 1:
                node = self.up[node][i]
                if node == -1:
                    break
        return node


class HeavyLightDecomposition:
    """
    Heavy-Light Decomposition for path queries
    Can be used for LCA and path operations
    """
    
    def __init__(self, n, edges, root=0):
        self.n = n
        self.edges = edges
        self.root = root
        
        # HLD arrays
        self.parent = [-1] * n
        self.depth = [0] * n
        self.subtree_size = [0] * n
        self.heavy_child = [-1] * n
        self.head = [0] * n
        self.pos = [0] * n
        
        self.timer = 0
        
        self._dfs1(root, -1)
        self._dfs2(root, root)
    
    def _dfs1(self, node, par):
        """First DFS - calculate subtree sizes and heavy children"""
        self.parent[node] = par
        self.subtree_size[node] = 1
        
        max_child_size = 0
        for child in self.edges[node]:
            if child != par:
                self.depth[child] = self.depth[node] + 1
                self._dfs1(child, node)
                self.subtree_size[node] += self.subtree_size[child]
                
                if self.subtree_size[child] > max_child_size:
                    max_child_size = self.subtree_size[child]
                    self.heavy_child[node] = child
    
    def _dfs2(self, node, h):
        """Second DFS - decompose into heavy paths"""
        self.head[node] = h
        self.pos[node] = self.timer
        self.timer += 1
        
        # Process heavy child first
        if self.heavy_child[node] != -1:
            self._dfs2(self.heavy_child[node], h)
        
        # Process other children
        for child in self.edges[node]:
            if child != self.parent[node] and child != self.heavy_child[node]:
                self._dfs2(child, child)
    
    def lca(self, u, v):
        """Find LCA using HLD"""
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u = self.parent[self.head[u]]
            else:
                v = self.parent[self.head[v]]
        
        return u if self.depth[u] < self.depth[v] else v


# Utility functions and applications

def build_tree_from_edges(n, edge_list):
    """
    Build adjacency list from edge list
    
    Args:
        n: number of nodes
        edge_list: list of (u, v) edges
        
    Returns:
        adjacency list representation
    """
    edges = [[] for _ in range(n)]
    for u, v in edge_list:
        edges[u].append(v)
        edges[v].append(u)
    return edges

def find_path(lca_obj, u, v):
    """
    Find path between two nodes using LCA
    
    Args:
        lca_obj: LCA object
        u, v: nodes
        
    Returns:
        path from u to v
    """
    lca = lca_obj.get_lca(u, v)
    
    # Path from u to lca
    path_u_to_lca = []
    current = u
    while current != lca:
        path_u_to_lca.append(current)
        current = lca_obj.binary_lifting.parent[current][0]
    path_u_to_lca.append(lca)
    
    # Path from lca to v
    path_lca_to_v = []
    current = v
    while current != lca:
        path_lca_to_v.append(current)
        current = lca_obj.binary_lifting.parent[current][0]
    
    # Combine paths
    path = path_u_to_lca + path_lca_to_v[::-1]
    return path


# Test functions
def test_lca():
    """Test LCA implementations"""
    print("Testing LCA:")
    
    # Create a test tree
    n = 7
    edges = [
        (0, 1), (0, 2),
        (1, 3), (1, 4),
        (2, 5), (2, 6)
    ]
    
    tree = build_tree_from_edges(n, edges)
    print(f"Tree edges: {edges}")
    
    # Test LCA
    lca = LCA(n, tree, root=0)
    
    test_pairs = [(3, 4), (3, 5), (4, 6), (1, 2)]
    
    print("\nLCA queries:")
    for u, v in test_pairs:
        lca_node = lca.get_lca(u, v)
        dist = lca.distance(u, v)
        print(f"LCA({u}, {v}) = {lca_node}, distance = {dist}")
    
    # Test k-th ancestor
    print("\nK-th ancestor queries:")
    for node in range(n):
        for k in range(1, 4):
            ancestor = lca.binary_lifting.kth_ancestor(node, k)
            print(f"{k}-th ancestor of {node} = {ancestor}")

def test_optimized_lca():
    """Test optimized LCA implementation"""
    print("\nTesting Optimized LCA:")
    
    n = 7
    edges = build_tree_from_edges(n, [
        (0, 1), (0, 2),
        (1, 3), (1, 4),
        (2, 5), (2, 6)
    ])
    
    lca = LCA_Optimized(n, edges, root=0)
    
    test_pairs = [(3, 4), (3, 5), (4, 6), (1, 2)]
    
    for u, v in test_pairs:
        lca_node = lca.lca(u, v)
        dist = lca.dist(u, v)
        print(f"LCA({u}, {v}) = {lca_node}, distance = {dist}")


if __name__ == "__main__":
    test_lca()
    test_optimized_lca()
