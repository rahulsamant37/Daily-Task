class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure
    Time complexity: O(α(n)) per operation where α is inverse Ackermann function
    For practical purposes, this is nearly O(1)
    """
    
    def __init__(self, n):
        """
        Initialize Union-Find structure with n elements
        
        Args:
            n: number of elements (0 to n-1)
        """
        self.n = n
        self.parent = list(range(n))  # Initially, each element is its own parent
        self.rank = [0] * n  # Rank for union by rank optimization
        self.size = [1] * n  # Size of each component
        self.components = n  # Number of connected components
    
    def find(self, x):
        """
        Find the root of element x with path compression
        
        Args:
            x: element to find root of
            
        Returns:
            root of the component containing x
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union two elements x and y
        
        Args:
            x, y: elements to union
            
        Returns:
            True if union was performed (x and y were in different components)
            False if x and y were already in the same component
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same component
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        """
        Check if two elements are in the same component
        
        Args:
            x, y: elements to check
            
        Returns:
            True if x and y are connected, False otherwise
        """
        return self.find(x) == self.find(y)
    
    def component_size(self, x):
        """
        Get the size of the component containing x
        
        Args:
            x: element
            
        Returns:
            size of component containing x
        """
        return self.size[self.find(x)]
    
    def get_components(self):
        """
        Get all connected components
        
        Returns:
            list of lists, where each inner list contains elements of one component
        """
        components = {}
        for i in range(self.n):
            root = self.find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        
        return list(components.values())
    
    def num_components(self):
        """
        Get the number of connected components
        
        Returns:
            number of connected components
        """
        return self.components


class WeightedUnionFind:
    """
    Weighted Union-Find for problems where we need to track relationships
    between elements (like relative distances, differences, etc.)
    """
    
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weight = [0] * n  # weight[x] = weight relative to parent
    
    def find(self, x):
        """Find with path compression and weight update"""
        if self.parent[x] != x:
            original_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] += self.weight[original_parent]
        return self.parent[x]
    
    def union(self, x, y, w):
        """
        Union x and y with relative weight w
        Meaning: weight[y] - weight[x] = w
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
            x, y = y, x
            w = -w
        
        self.parent[root_y] = root_x
        self.weight[root_y] = self.weight[x] - self.weight[y] + w
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True
    
    def diff(self, x, y):
        """Get the difference weight[y] - weight[x]"""
        if self.find(x) != self.find(y):
            return None  # Not connected
        return self.weight[y] - self.weight[x]


class PersistentUnionFind:
    """
    Union-Find that supports rollback operations
    Useful for offline algorithms and backtracking
    """
    
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
        self.history = []  # Stack of operations for rollback
    
    def find(self, x):
        """Find without path compression (to support rollback)"""
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        """Union with ability to rollback"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            self.history.append(None)  # No change
            return False
        
        # Always attach smaller rank to larger rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        # Save state for rollback
        self.history.append((root_y, self.parent[root_y], self.rank[root_x]))
        
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        self.components -= 1
        return True
    
    def rollback(self):
        """Rollback the last union operation"""
        if not self.history:
            return False
        
        last_op = self.history.pop()
        if last_op is None:
            return True  # Nothing to rollback
        
        node, old_parent, old_rank = last_op
        self.parent[node] = old_parent
        
        # Find the root that was modified and restore its rank
        root = self.find(node)
        if root != node:  # If node was not root
            other_root = self.parent[node]
            if self.rank[other_root] != old_rank:
                self.rank[other_root] = old_rank
        
        self.components += 1
        return True


# Applications and examples

def kruskal_mst(edges, n):
    """
    Kruskal's algorithm for Minimum Spanning Tree using Union-Find
    
    Args:
        edges: list of (weight, u, v) tuples
        n: number of vertices
        
    Returns:
        (mst_weight, mst_edges)
    """
    edges.sort()  # Sort edges by weight
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break
    
    return mst_weight, mst_edges

def detect_cycle_undirected(edges, n):
    """
    Detect cycle in undirected graph using Union-Find
    
    Args:
        edges: list of (u, v) tuples
        n: number of vertices
        
    Returns:
        True if cycle exists, False otherwise
    """
    uf = UnionFind(n)
    
    for u, v in edges:
        if not uf.union(u, v):
            return True  # Cycle detected
    
    return False

def count_connected_components(edges, n):
    """
    Count connected components in undirected graph
    
    Args:
        edges: list of (u, v) tuples
        n: number of vertices
        
    Returns:
        number of connected components
    """
    uf = UnionFind(n)
    
    for u, v in edges:
        uf.union(u, v)
    
    return uf.num_components()

# Test functions
def test_union_find():
    """Test basic Union-Find operations"""
    print("Testing Union-Find:")
    
    uf = UnionFind(6)
    print(f"Initial components: {uf.num_components()}")
    
    # Union some elements
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    
    print(f"After unions: {uf.num_components()}")
    print(f"0 and 2 connected: {uf.connected(0, 2)}")
    print(f"2 and 3 connected: {uf.connected(2, 3)}")
    print(f"Component size of 0: {uf.component_size(0)}")
    
    components = uf.get_components()
    print(f"All components: {components}")

def test_kruskal():
    """Test Kruskal's MST algorithm"""
    print("\nTesting Kruskal's MST:")
    
    # Example graph
    edges = [
        (1, 0, 1), (3, 0, 2), (2, 1, 2),
        (4, 1, 3), (5, 2, 3), (1, 3, 4)
    ]
    n = 5
    
    mst_weight, mst_edges = kruskal_mst(edges, n)
    print(f"MST weight: {mst_weight}")
    print(f"MST edges: {mst_edges}")

def test_cycle_detection():
    """Test cycle detection"""
    print("\nTesting Cycle Detection:")
    
    # Graph with cycle
    edges_with_cycle = [(0, 1), (1, 2), (2, 0), (3, 4)]
    print(f"Edges with cycle: {detect_cycle_undirected(edges_with_cycle, 5)}")
    
    # Graph without cycle
    edges_no_cycle = [(0, 1), (1, 2), (3, 4)]
    print(f"Edges without cycle: {detect_cycle_undirected(edges_no_cycle, 5)}")

if __name__ == "__main__":
    test_union_find()
    test_kruskal()
    test_cycle_detection()
