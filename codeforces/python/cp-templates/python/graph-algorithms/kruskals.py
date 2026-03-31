"""
Kruskal's Algorithm for Minimum Spanning Tree (MST)
====================================================

Finds the minimum spanning tree of a weighted undirected graph.
Uses Union-Find (Disjoint Set Union) data structure with path compression 
and union by rank for efficient cycle detection.

Time Complexity: O(E log E) for sorting edges + O(E α(V)) for union-find
Space Complexity: O(V + E)

Author: Converted from C++ implementation
"""

class UnionFind:
    """
    Union-Find data structure with path compression and union by rank
    """
    
    def __init__(self, n):
        """
        Initialize Union-Find for n elements
        
        Args:
            n: number of elements
        """
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """
        Find root of element x with path compression
        
        Args:
            x: element to find root of
        
        Returns:
            root of element x
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union two sets containing x and y
        
        Args:
            x: element from first set
            y: element from second set
        
        Returns:
            True if union performed, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
    def connected(self, x, y):
        """
        Check if x and y are in the same connected component
        
        Args:
            x: first element
            y: second element
        
        Returns:
            True if connected, False otherwise
        """
        return self.find(x) == self.find(y)

def kruskal_mst(n, edges):
    """
    Find Minimum Spanning Tree using Kruskal's algorithm
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of edges as (weight, u, v) tuples
    
    Returns:
        tuple (mst_edges, total_weight)
        - mst_edges: list of edges in MST as (u, v, weight)
        - total_weight: total weight of MST
    """
    # Sort edges by weight
    edges.sort()
    
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            # MST complete when we have n-1 edges
            if len(mst_edges) == n - 1:
                break
    
    return mst_edges, total_weight

def kruskal_mst_detailed(n, edges):
    """
    Kruskal's algorithm with detailed step-by-step information
    
    Args:
        n: number of vertices
        edges: list of edges as (weight, u, v) tuples
    
    Returns:
        dict containing MST details
    """
    edges.sort()
    
    uf = UnionFind(n)
    mst_edges = []
    rejected_edges = []
    total_weight = 0
    steps = []
    
    for i, (weight, u, v) in enumerate(edges):
        if uf.connected(u, v):
            rejected_edges.append((u, v, weight))
            steps.append(f"Step {i+1}: Edge ({u},{v}) weight {weight} - REJECTED (creates cycle)")
        else:
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            steps.append(f"Step {i+1}: Edge ({u},{v}) weight {weight} - ACCEPTED")
            
            if len(mst_edges) == n - 1:
                steps.append(f"MST completed with {n-1} edges")
                break
    
    return {
        'mst_edges': mst_edges,
        'total_weight': total_weight,
        'rejected_edges': rejected_edges,
        'steps': steps,
        'num_components': n - len(mst_edges)
    }

def is_connected_graph(n, edges):
    """
    Check if graph is connected using Union-Find
    
    Args:
        n: number of vertices
        edges: list of edges as (weight, u, v) or (u, v, weight)
    
    Returns:
        True if graph is connected, False otherwise
    """
    uf = UnionFind(n)
    
    for edge in edges:
        if len(edge) == 3:
            if len(edge) == 3 and isinstance(edge[0], (int, float)) and edge[0] < n:
                # Format: (u, v, weight)
                u, v = edge[0], edge[1]
            else:
                # Format: (weight, u, v)
                u, v = edge[1], edge[2]
        else:
            # Format: (u, v)
            u, v = edge[0], edge[1]
        
        uf.union(u, v)
    
    # Check if all vertices are in the same component
    root = uf.find(0)
    for i in range(1, n):
        if uf.find(i) != root:
            return False
    
    return True

def find_all_msts(n, edges):
    """
    Find all possible MSTs when there are multiple MSTs with same weight
    Note: This is exponential in worst case, use carefully
    
    Args:
        n: number of vertices
        edges: list of edges as (weight, u, v)
    
    Returns:
        list of all possible MSTs
    """
    edges.sort()
    all_msts = []
    
    def backtrack(edge_idx, current_mst, current_weight, uf):
        if len(current_mst) == n - 1:
            all_msts.append((current_mst.copy(), current_weight))
            return
        
        if edge_idx >= len(edges):
            return
        
        weight, u, v = edges[edge_idx]
        
        # Try including this edge if it doesn't create a cycle
        if not uf.connected(u, v):
            # Save state
            old_parent = uf.parent.copy()
            old_rank = uf.rank.copy()
            
            uf.union(u, v)
            current_mst.append((u, v, weight))
            backtrack(edge_idx + 1, current_mst, current_weight + weight, uf)
            current_mst.pop()
            
            # Restore state
            uf.parent = old_parent
            uf.rank = old_rank
        
        # Try not including this edge
        backtrack(edge_idx + 1, current_mst, current_weight, uf)
    
    uf = UnionFind(n)
    backtrack(0, [], 0, uf)
    
    # Filter MSTs with minimum weight
    if all_msts:
        min_weight = min(mst[1] for mst in all_msts)
        return [mst[0] for mst in all_msts if mst[1] == min_weight]
    
    return []

def test_kruskal():
    """Test Kruskal's algorithm implementation"""
    print("Testing Kruskal's Algorithm for MST")
    print("=" * 40)
    
    # Test 1: Basic MST
    print("Test 1: Basic MST")
    n1 = 4
    edges1 = [
        (1, 0, 1),  # weight, u, v
        (4, 0, 2),
        (2, 1, 2),
        (5, 1, 3),
        (3, 2, 3)
    ]
    
    mst_edges1, total_weight1 = kruskal_mst(n1, edges1.copy())
    print(f"Vertices: {n1}")
    print(f"Edges: {[(u, v, w) for w, u, v in edges1]}")
    print(f"MST edges: {mst_edges1}")
    print(f"Total weight: {total_weight1}")
    print()
    
    # Test 2: Detailed step-by-step
    print("Test 2: Detailed MST Construction")
    result = kruskal_mst_detailed(n1, edges1.copy())
    for step in result['steps']:
        print(step)
    print(f"Final MST weight: {result['total_weight']}")
    print()
    
    # Test 3: Disconnected graph
    print("Test 3: Disconnected Graph")
    n3 = 6
    edges3 = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 3, 4),
        (4, 4, 5)
    ]
    
    mst_edges3, total_weight3 = kruskal_mst(n3, edges3.copy())
    print(f"Vertices: {n3}")
    print(f"Edges: {[(u, v, w) for w, u, v in edges3]}")
    print(f"Is connected: {is_connected_graph(n3, edges3)}")
    print(f"MST edges found: {mst_edges3}")
    print(f"Number of components: {n3 - len(mst_edges3)}")
    print()
    
    # Test 4: Complete graph
    print("Test 4: Complete Graph (4 vertices)")
    n4 = 4
    edges4 = []
    weight = 1
    for i in range(n4):
        for j in range(i + 1, n4):
            edges4.append((weight, i, j))
            weight += 1
    
    mst_edges4, total_weight4 = kruskal_mst(n4, edges4.copy())
    print(f"Complete graph with {n4} vertices")
    print(f"Total edges: {len(edges4)}")
    print(f"MST edges: {mst_edges4}")
    print(f"MST weight: {total_weight4}")
    print()
    
    # Test 5: Graph with multiple MSTs
    print("Test 5: Multiple MSTs")
    n5 = 4
    edges5 = [
        (1, 0, 1),
        (1, 1, 2),  # Same weight
        (1, 2, 3),  # Same weight
        (2, 0, 2),
        (2, 1, 3)
    ]
    
    print(f"Edges with same weights: {[(u, v, w) for w, u, v in edges5]}")
    mst_edges5, total_weight5 = kruskal_mst(n5, edges5.copy())
    print(f"One possible MST: {mst_edges5}")
    print(f"MST weight: {total_weight5}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_kruskal()
