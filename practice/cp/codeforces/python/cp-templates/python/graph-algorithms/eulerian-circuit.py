"""
Eulerian Circuit and Path Algorithms
====================================

An Eulerian circuit is a circuit that visits every edge exactly once.
An Eulerian path is a path that visits every edge exactly once.

For undirected graphs:
- Eulerian circuit exists if all vertices have even degree
- Eulerian path exists if exactly 0 or 2 vertices have odd degree

For directed graphs:
- Eulerian circuit exists if all vertices have equal in-degree and out-degree
- Eulerian path exists if at most one vertex has (out-degree - in-degree = 1)
  and at most one vertex has (in-degree - out-degree = 1)

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Author: Converted from C++ implementation
"""

from collections import defaultdict, deque

class EulerianGraph:
    """
    Class for finding Eulerian circuits and paths
    """
    
    def __init__(self, n, directed=False):
        """
        Initialize graph
        
        Args:
            n: number of vertices
            directed: whether graph is directed
        """
        self.n = n
        self.directed = directed
        self.adj = defaultdict(list)
        self.edge_count = defaultdict(int)  # For tracking used edges
        self.total_edges = 0
    
    def add_edge(self, u, v):
        """
        Add edge to the graph
        
        Args:
            u: source vertex
            v: destination vertex
        """
        self.adj[u].append((v, self.total_edges))
        if not self.directed:
            self.adj[v].append((u, self.total_edges))
        self.total_edges += 1
    
    def get_degrees(self):
        """
        Get degree information for vertices
        
        Returns:
            tuple (in_degree, out_degree) for directed graphs
            or (degree, degree) for undirected graphs
        """
        in_degree = [0] * self.n
        out_degree = [0] * self.n
        
        if self.directed:
            for u in range(self.n):
                out_degree[u] = len(self.adj[u])
                for v, _ in self.adj[u]:
                    in_degree[v] += 1
        else:
            for u in range(self.n):
                in_degree[u] = out_degree[u] = len(self.adj[u])
        
        return in_degree, out_degree
    
    def has_eulerian_circuit(self):
        """
        Check if graph has Eulerian circuit
        
        Returns:
            True if Eulerian circuit exists
        """
        in_deg, out_deg = self.get_degrees()
        
        if self.directed:
            # All vertices must have equal in-degree and out-degree
            for i in range(self.n):
                if in_deg[i] != out_deg[i]:
                    return False
        else:
            # All vertices must have even degree
            for i in range(self.n):
                if out_deg[i] % 2 != 0:
                    return False
        
        return True
    
    def has_eulerian_path(self):
        """
        Check if graph has Eulerian path
        
        Returns:
            tuple (has_path, start_vertex, end_vertex)
        """
        in_deg, out_deg = self.get_degrees()
        
        if self.directed:
            start_vertex = end_vertex = -1
            
            for i in range(self.n):
                diff = out_deg[i] - in_deg[i]
                if diff == 1:
                    if start_vertex == -1:
                        start_vertex = i
                    else:
                        return False, -1, -1  # More than one start vertex
                elif diff == -1:
                    if end_vertex == -1:
                        end_vertex = i
                    else:
                        return False, -1, -1  # More than one end vertex
                elif diff != 0:
                    return False, -1, -1
            
            # Either both are -1 (circuit) or both are valid (path)
            if start_vertex == -1 and end_vertex == -1:
                return True, 0, 0  # Circuit exists, can start anywhere
            elif start_vertex != -1 and end_vertex != -1:
                return True, start_vertex, end_vertex
            else:
                return False, -1, -1
        
        else:  # Undirected graph
            odd_vertices = []
            for i in range(self.n):
                if out_deg[i] % 2 == 1:
                    odd_vertices.append(i)
            
            if len(odd_vertices) == 0:
                return True, 0, 0  # Circuit exists
            elif len(odd_vertices) == 2:
                return True, odd_vertices[0], odd_vertices[1]
            else:
                return False, -1, -1
    
    def find_eulerian_circuit_hierholzer(self, start=0):
        """
        Find Eulerian circuit using Hierholzer's algorithm
        
        Args:
            start: starting vertex
        
        Returns:
            list representing Eulerian circuit
        """
        if not self.has_eulerian_circuit():
            return []
        
        # Create a copy of adjacency list
        curr_adj = defaultdict(list)
        for u in self.adj:
            curr_adj[u] = self.adj[u].copy()
        
        circuit = []
        stack = [start]
        
        while stack:
            v = stack[-1]
            if curr_adj[v]:
                u, edge_id = curr_adj[v].pop()
                # Remove reverse edge for undirected graph
                if not self.directed:
                    curr_adj[u] = [(x, eid) for x, eid in curr_adj[u] if eid != edge_id]
                stack.append(u)
            else:
                circuit.append(stack.pop())
        
        return circuit[::-1]
    
    def find_eulerian_path_hierholzer(self):
        """
        Find Eulerian path using Hierholzer's algorithm
        
        Returns:
            list representing Eulerian path
        """
        has_path, start, end = self.has_eulerian_path()
        if not has_path:
            return []
        
        # Use circuit algorithm starting from appropriate vertex
        return self.find_eulerian_circuit_hierholzer(start)
    
    def dfs_eulerian(self, v, curr_adj, path):
        """
        DFS-based Eulerian path finding (recursive)
        
        Args:
            v: current vertex
            curr_adj: current adjacency list
            path: path being constructed
        """
        while curr_adj[v]:
            u, edge_id = curr_adj[v].pop()
            # Remove reverse edge for undirected graph
            if not self.directed:
                curr_adj[u] = [(x, eid) for x, eid in curr_adj[u] if eid != edge_id]
            self.dfs_eulerian(u, curr_adj, path)
        path.append(v)
    
    def find_all_eulerian_circuits(self):
        """
        Find all Eulerian circuits in the graph
        
        Returns:
            list of all Eulerian circuits
        """
        if not self.has_eulerian_circuit():
            return []
        
        circuits = []
        
        # Find connected components with edges
        visited_vertices = set()
        
        for start in range(self.n):
            if start not in visited_vertices and self.adj[start]:
                # Create copy of adjacency list
                curr_adj = defaultdict(list)
                for u in self.adj:
                    curr_adj[u] = self.adj[u].copy()
                
                path = []
                self.dfs_eulerian(start, curr_adj, path)
                
                if len(path) > 1:  # Valid circuit
                    circuits.append(path[::-1])
                
                # Mark all vertices in this component as visited
                for v in path:
                    visited_vertices.add(v)
        
        return circuits

def fleury_algorithm(n, edges, directed=False):
    """
    Fleury's algorithm for finding Eulerian path/circuit
    (Alternative implementation - less efficient than Hierholzer's)
    
    Args:
        n: number of vertices
        edges: list of edges
        directed: whether graph is directed
    
    Returns:
        Eulerian path/circuit
    """
    graph = EulerianGraph(n, directed)
    for u, v in edges:
        graph.add_edge(u, v)
    
    # Check if Eulerian path exists
    has_path, start, end = graph.has_eulerian_path()
    if not has_path:
        return []
    
    # Use Hierholzer's algorithm (more efficient)
    return graph.find_eulerian_path_hierholzer()

def test_eulerian():
    """Test Eulerian algorithms"""
    print("Testing Eulerian Circuit and Path Algorithms")
    print("=" * 45)
    
    # Test 1: Eulerian circuit in undirected graph
    print("Test 1: Eulerian Circuit (Undirected)")
    graph1 = EulerianGraph(5, directed=False)
    edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2)]
    for u, v in edges1:
        graph1.add_edge(u, v)
    
    print(f"Edges: {edges1}")
    print(f"Has Eulerian circuit: {graph1.has_eulerian_circuit()}")
    
    circuit = graph1.find_eulerian_circuit_hierholzer()
    print(f"Eulerian circuit: {circuit}")
    print()
    
    # Test 2: Eulerian path in undirected graph
    print("Test 2: Eulerian Path (Undirected)")
    graph2 = EulerianGraph(4, directed=False)
    edges2 = [(0, 1), (1, 2), (2, 3)]
    for u, v in edges2:
        graph2.add_edge(u, v)
    
    print(f"Edges: {edges2}")
    has_path, start, end = graph2.has_eulerian_path()
    print(f"Has Eulerian path: {has_path}")
    if has_path:
        print(f"Start: {start}, End: {end}")
        path = graph2.find_eulerian_path_hierholzer()
        print(f"Eulerian path: {path}")
    print()
    
    # Test 3: Directed graph with Eulerian circuit
    print("Test 3: Eulerian Circuit (Directed)")
    graph3 = EulerianGraph(3, directed=True)
    edges3 = [(0, 1), (1, 2), (2, 0)]
    for u, v in edges3:
        graph3.add_edge(u, v)
    
    print(f"Directed edges: {edges3}")
    print(f"Has Eulerian circuit: {graph3.has_eulerian_circuit()}")
    circuit3 = graph3.find_eulerian_circuit_hierholzer()
    print(f"Eulerian circuit: {circuit3}")
    print()
    
    # Test 4: Graph with no Eulerian path/circuit
    print("Test 4: No Eulerian Path/Circuit")
    graph4 = EulerianGraph(4, directed=False)
    edges4 = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]  # Vertex 1 and 3 have odd degree
    for u, v in edges4:
        graph4.add_edge(u, v)
    
    print(f"Edges: {edges4}")
    print(f"Has Eulerian circuit: {graph4.has_eulerian_circuit()}")
    has_path, start, end = graph4.has_eulerian_path()
    print(f"Has Eulerian path: {has_path}")
    print()
    
    # Test 5: Disconnected graph with multiple circuits
    print("Test 5: Multiple Eulerian Circuits")
    graph5 = EulerianGraph(6, directed=False)
    edges5 = [(0, 1), (1, 0), (2, 3), (3, 2), (4, 5), (5, 4)]
    for u, v in edges5:
        graph5.add_edge(u, v)
    
    print(f"Edges: {edges5}")
    circuits5 = graph5.find_all_eulerian_circuits()
    print(f"All Eulerian circuits: {circuits5}")
    print()
    
    # Test 6: Complete graph K4
    print("Test 6: Complete Graph K4")
    graph6 = EulerianGraph(4, directed=False)
    edges6 = []
    for i in range(4):
        for j in range(i + 1, 4):
            edges6.append((i, j))
    
    for u, v in edges6:
        graph6.add_edge(u, v)
    
    print(f"K4 edges: {edges6}")
    print(f"Has Eulerian circuit: {graph6.has_eulerian_circuit()}")
    has_path, start, end = graph6.has_eulerian_path()
    print(f"Has Eulerian path: {has_path}")
    print()
    
    # Test 7: Bridge example (Königsberg bridge problem)
    print("Test 7: Königsberg Bridge Problem")
    graph7 = EulerianGraph(4, directed=False)
    # 4 landmasses, 7 bridges - famous problem that has no solution
    bridges = [(0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (2, 3), (2, 3)]
    for u, v in bridges:
        graph7.add_edge(u, v)
    
    print(f"Königsberg bridges: {bridges}")
    print(f"Has Eulerian path: {graph7.has_eulerian_path()[0]}")
    print("This is the famous problem that Euler proved has no solution!")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_eulerian()
