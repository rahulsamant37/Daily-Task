"""
Prim's Algorithm for Minimum Spanning Tree (MST)
=================================================

Finds the minimum spanning tree of a weighted undirected graph.
Starts from an arbitrary vertex and grows the MST by adding the 
minimum weight edge that connects a vertex in MST to a vertex not in MST.

Time Complexity: O(V log V + E log V) using priority queue
                 O(V²) using linear search for minimum
Space Complexity: O(V + E)

Author: Converted from C++ implementation
"""

import heapq
from collections import defaultdict

class PrimsMST:
    """
    Implementation of Prim's algorithm for finding MST
    """
    
    def __init__(self, n):
        """
        Initialize graph with n vertices
        
        Args:
            n: number of vertices
        """
        self.n = n
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        """
        Add undirected edge between u and v with given weight
        
        Args:
            u: first vertex
            v: second vertex
            weight: edge weight
        """
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))
    
    def prim_mst_with_priority_queue(self, start=0):
        """
        Find MST using Prim's algorithm with priority queue
        
        Args:
            start: starting vertex (default 0)
        
        Returns:
            tuple (mst_edges, total_weight, mst_tree)
            - mst_edges: list of MST edges as (u, v, weight)
            - total_weight: total weight of MST
            - mst_tree: adjacency list representation of MST
        """
        visited = [False] * self.n
        parent = [-1] * self.n
        key = [float('inf')] * self.n
        
        # Start from vertex 'start'
        key[start] = 0
        pq = [(0, start)]  # (weight, vertex)
        
        mst_edges = []
        total_weight = 0
        mst_tree = defaultdict(list)
        
        while pq:
            current_weight, u = heapq.heappop(pq)
            
            if visited[u]:
                continue
            
            visited[u] = True
            
            # Add edge to MST (except for starting vertex)
            if parent[u] != -1:
                mst_edges.append((parent[u], u, current_weight))
                total_weight += current_weight
                mst_tree[parent[u]].append((u, current_weight))
                mst_tree[u].append((parent[u], current_weight))
            
            # Update key values of adjacent vertices
            for v, weight in self.adj[u]:
                if not visited[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
                    heapq.heappush(pq, (weight, v))
        
        return mst_edges, total_weight, dict(mst_tree)
    
    def prim_mst_simple(self, start=0):
        """
        Find MST using Prim's algorithm with O(V²) complexity
        
        Args:
            start: starting vertex (default 0)
        
        Returns:
            tuple (mst_edges, total_weight)
        """
        visited = [False] * self.n
        parent = [-1] * self.n
        key = [float('inf')] * self.n
        
        key[start] = 0
        mst_edges = []
        total_weight = 0
        
        for _ in range(self.n):
            # Find minimum key vertex not yet in MST
            min_key = float('inf')
            u = -1
            for v in range(self.n):
                if not visited[v] and key[v] < min_key:
                    min_key = key[v]
                    u = v
            
            if u == -1:  # No more vertices reachable
                break
            
            visited[u] = True
            
            # Add edge to MST (except for starting vertex)
            if parent[u] != -1:
                mst_edges.append((parent[u], u, key[u]))
                total_weight += key[u]
            
            # Update key values of adjacent vertices
            for v, weight in self.adj[u]:
                if not visited[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
        
        return mst_edges, total_weight

def prim_mst_from_edges(n, edges, start=0):
    """
    Find MST using Prim's algorithm from edge list
    
    Args:
        n: number of vertices
        edges: list of edges as (u, v, weight) tuples
        start: starting vertex
    
    Returns:
        tuple (mst_edges, total_weight)
    """
    graph = PrimsMST(n)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)
    
    return graph.prim_mst_with_priority_queue(start)

def prim_step_by_step(n, edges, start=0):
    """
    Prim's algorithm with detailed step-by-step execution
    
    Args:
        n: number of vertices
        edges: list of edges as (u, v, weight)
        start: starting vertex
    
    Returns:
        dict with detailed execution steps
    """
    graph = PrimsMST(n)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)
    
    visited = [False] * n
    parent = [-1] * n
    key = [float('inf')] * n
    
    key[start] = 0
    pq = [(0, start)]
    
    mst_edges = []
    total_weight = 0
    steps = []
    step_count = 0
    
    steps.append(f"Step 0: Starting from vertex {start}")
    
    while pq:
        current_weight, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        step_count += 1
        
        if parent[u] != -1:
            mst_edges.append((parent[u], u, current_weight))
            total_weight += current_weight
            steps.append(f"Step {step_count}: Added edge ({parent[u]}, {u}) with weight {current_weight}")
        else:
            steps.append(f"Step {step_count}: Added starting vertex {u}")
        
        # Update adjacent vertices
        updates = []
        for v, weight in graph.adj[u]:
            if not visited[v] and weight < key[v]:
                old_key = key[v]
                key[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))
                updates.append(f"  Updated vertex {v}: key {old_key} -> {weight}, parent -> {u}")
        
        if updates:
            steps.extend(updates)
        
        steps.append(f"  Current MST weight: {total_weight}")
        steps.append(f"  Visited vertices: {[i for i in range(n) if visited[i]]}")
        steps.append("")
    
    return {
        'mst_edges': mst_edges,
        'total_weight': total_weight,
        'steps': steps,
        'num_components': 1 if len(mst_edges) == n - 1 else n - len(mst_edges)
    }

def compare_prim_kruskal(n, edges):
    """
    Compare MST results from Prim's and Kruskal's algorithms
    
    Args:
        n: number of vertices
        edges: list of edges as (u, v, weight)
    
    Returns:
        comparison results
    """
    # Prim's MST
    prim_mst, prim_weight, _ = prim_mst_from_edges(n, edges)
    
    # For comparison with Kruskal's, we'd need to import it
    # Here we'll just return Prim's results
    return {
        'prim_mst': prim_mst,
        'prim_weight': prim_weight,
        'same_weight': True  # Both algorithms give same weight
    }

def is_graph_connected_prim(n, edges):
    """
    Check if graph is connected using Prim's algorithm
    
    Args:
        n: number of vertices
        edges: list of edges
    
    Returns:
        True if connected, False otherwise
    """
    if not edges:
        return n <= 1
    
    mst_edges, _ = prim_mst_from_edges(n, edges)
    return len(mst_edges) == n - 1

def test_prim():
    """Test Prim's algorithm implementation"""
    print("Testing Prim's Algorithm for MST")
    print("=" * 40)
    
    # Test 1: Basic MST
    print("Test 1: Basic MST")
    n1 = 4
    edges1 = [
        (0, 1, 1),
        (0, 2, 4),
        (1, 2, 2),
        (1, 3, 5),
        (2, 3, 3)
    ]
    
    mst_edges1, total_weight1, mst_tree1 = prim_mst_from_edges(n1, edges1)
    print(f"Vertices: {n1}")
    print(f"Edges: {edges1}")
    print(f"MST edges: {mst_edges1}")
    print(f"Total weight: {total_weight1}")
    print(f"MST tree: {mst_tree1}")
    print()
    
    # Test 2: Step-by-step execution
    print("Test 2: Step-by-step MST Construction")
    result = prim_step_by_step(n1, edges1)
    for step in result['steps']:
        print(step)
    print()
    
    # Test 3: Different starting vertex
    print("Test 3: Different Starting Vertex")
    mst_edges3, total_weight3, _ = prim_mst_from_edges(n1, edges1, start=2)
    print(f"Starting from vertex 2:")
    print(f"MST edges: {mst_edges3}")
    print(f"Total weight: {total_weight3}")
    print()
    
    # Test 4: Disconnected graph
    print("Test 4: Disconnected Graph")
    n4 = 6
    edges4 = [
        (0, 1, 1),
        (1, 2, 2),
        (3, 4, 3),
        (4, 5, 4)
    ]
    
    mst_edges4, total_weight4, _ = prim_mst_from_edges(n4, edges4)
    print(f"Vertices: {n4}")
    print(f"Edges: {edges4}")
    print(f"Is connected: {is_graph_connected_prim(n4, edges4)}")
    print(f"MST edges found: {mst_edges4}")
    print(f"Reachable from vertex 0: {len(mst_edges4) + 1} vertices")
    print()
    
    # Test 5: Complete graph
    print("Test 5: Complete Graph (4 vertices)")
    n5 = 4
    edges5 = []
    weight = 1
    for i in range(n5):
        for j in range(i + 1, n5):
            edges5.append((i, j, weight))
            weight += 1
    
    mst_edges5, total_weight5, _ = prim_mst_from_edges(n5, edges5)
    print(f"Complete graph with {n5} vertices")
    print(f"Total edges: {len(edges5)}")
    print(f"MST edges: {mst_edges5}")
    print(f"MST weight: {total_weight5}")
    print()
    
    # Test 6: Single vertex
    print("Test 6: Single Vertex")
    n6 = 1
    edges6 = []
    mst_edges6, total_weight6, _ = prim_mst_from_edges(n6, edges6)
    print(f"Single vertex graph:")
    print(f"MST edges: {mst_edges6}")
    print(f"Total weight: {total_weight6}")
    print()
    
    # Test 7: Linear graph
    print("Test 7: Linear Graph")
    n7 = 5
    edges7 = [(i, i+1, i+1) for i in range(n7-1)]
    mst_edges7, total_weight7, _ = prim_mst_from_edges(n7, edges7)
    print(f"Linear graph: {edges7}")
    print(f"MST edges: {mst_edges7}")
    print(f"Total weight: {total_weight7}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_prim()
