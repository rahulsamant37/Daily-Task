"""
Kosaraju's Algorithm for Strongly Connected Components (SCC)
============================================================

Finds all strongly connected components in a directed graph.
A strongly connected component is a maximal set of vertices 
where every vertex is reachable from every other vertex.

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Author: Converted from C++ implementation
"""

from collections import defaultdict, deque

class KosarajuSCC:
    """
    Implementation of Kosaraju's algorithm for finding SCCs
    """
    
    def __init__(self, n):
        """
        Initialize graph with n vertices
        
        Args:
            n: number of vertices
        """
        self.n = n
        self.adj = defaultdict(list)      # Original graph
        self.adj_t = defaultdict(list)    # Transpose graph
    
    def add_edge(self, u, v):
        """
        Add directed edge from u to v
        
        Args:
            u: source vertex
            v: destination vertex
        """
        self.adj[u].append(v)
        self.adj_t[v].append(u)
    
    def topo_sort(self, start, visited, topo):
        """
        DFS-based topological sort on original graph
        
        Args:
            start: starting vertex
            visited: visited array
            topo: stack to store finishing times
        """
        visited[start] = True
        
        for neighbor in self.adj[start]:
            if not visited[neighbor]:
                self.topo_sort(neighbor, visited, topo)
        
        topo.append(start)
    
    def get_component(self, start, visited, component):
        """
        DFS on transpose graph to get one SCC
        
        Args:
            start: starting vertex
            visited: visited array
            component: current component being built
        """
        component.append(start)
        visited[start] = True
        
        for neighbor in self.adj_t[start]:
            if not visited[neighbor]:
                self.get_component(neighbor, visited, component)
    
    def get_scc(self):
        """
        Find all strongly connected components using Kosaraju's algorithm
        
        Returns:
            List of SCCs, where each SCC is a list of vertices
        """
        # Step 1: Fill vertices in stack according to their finishing times
        visited = [False] * self.n
        topo = []
        
        for i in range(self.n):
            if not visited[i]:
                self.topo_sort(i, visited, topo)
        
        # Step 2: Process all vertices in order defined by stack
        visited = [False] * self.n
        scc_list = []
        
        for i in range(len(topo) - 1, -1, -1):
            if not visited[topo[i]]:
                component = []
                self.get_component(topo[i], visited, component)
                scc_list.append(component)
        
        return scc_list
    
    def count_scc(self):
        """
        Count number of strongly connected components
        
        Returns:
            Number of SCCs
        """
        return len(self.get_scc())
    
    def is_strongly_connected(self):
        """
        Check if the entire graph is strongly connected
        
        Returns:
            True if graph has exactly one SCC, False otherwise
        """
        return self.count_scc() == 1

def condensation_graph(n, edges):
    """
    Build condensation graph (SCC graph) from original graph
    
    Args:
        n: number of vertices
        edges: list of directed edges as (u, v) tuples
    
    Returns:
        tuple (scc_list, condensed_adj, scc_id)
        - scc_list: list of SCCs
        - condensed_adj: adjacency list of condensation graph
        - scc_id: mapping from vertex to its SCC index
    """
    # Build graph
    graph = KosarajuSCC(n)
    for u, v in edges:
        graph.add_edge(u, v)
    
    # Get SCCs
    scc_list = graph.get_scc()
    
    # Create mapping from vertex to SCC index
    scc_id = {}
    for i, scc in enumerate(scc_list):
        for vertex in scc:
            scc_id[vertex] = i
    
    # Build condensation graph
    condensed_adj = defaultdict(set)
    for u, v in edges:
        scc_u = scc_id[u]
        scc_v = scc_id[v]
        if scc_u != scc_v:
            condensed_adj[scc_u].add(scc_v)
    
    # Convert sets to lists
    condensed_adj = {k: list(v) for k, v in condensed_adj.items()}
    
    return scc_list, condensed_adj, scc_id

def find_bridges_using_scc(n, edges):
    """
    Find bridges in undirected graph using SCC concept
    Note: This is more for demonstration; Tarjan's algorithm is better for bridges
    
    Args:
        n: number of vertices
        edges: list of undirected edges as (u, v) tuples
    
    Returns:
        List of bridge edges
    """
    # Convert undirected to directed by adding both directions
    directed_edges = []
    for u, v in edges:
        directed_edges.append((u, v))
        directed_edges.append((v, u))
    
    bridges = []
    
    # Check each edge
    for u, v in edges:
        # Remove edge (u,v) and (v,u)
        temp_edges = [(x, y) for x, y in directed_edges if not ((x == u and y == v) or (x == v and y == u))]
        
        # Check if removing this edge increases number of SCCs
        graph = KosarajuSCC(n)
        for x, y in temp_edges:
            graph.add_edge(x, y)
        
        if graph.count_scc() > 1:
            bridges.append((u, v))
    
    return bridges

def test_kosaraju():
    """Test Kosaraju's algorithm implementation"""
    print("Testing Kosaraju's Algorithm for SCC")
    print("=" * 40)
    
    # Test 1: Basic SCC finding
    print("Test 1: Basic SCC Detection")
    graph = KosarajuSCC(5)
    
    # Add edges: 0->1, 1->2, 2->0, 2->3, 3->4
    edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)]
    for u, v in edges:
        graph.add_edge(u, v)
    
    scc_list = graph.get_scc()
    print(f"Edges: {edges}")
    print(f"SCCs: {scc_list}")
    print(f"Number of SCCs: {len(scc_list)}")
    print()
    
    # Test 2: Strongly connected graph
    print("Test 2: Strongly Connected Graph")
    graph2 = KosarajuSCC(3)
    edges2 = [(0, 1), (1, 2), (2, 0)]
    for u, v in edges2:
        graph2.add_edge(u, v)
    
    print(f"Edges: {edges2}")
    print(f"Is strongly connected: {graph2.is_strongly_connected()}")
    print(f"SCCs: {graph2.get_scc()}")
    print()
    
    # Test 3: Disconnected components
    print("Test 3: Disconnected Components")
    graph3 = KosarajuSCC(6)
    edges3 = [(0, 1), (1, 0), (2, 3), (3, 2), (4, 5)]
    for u, v in edges3:
        graph3.add_edge(u, v)
    
    scc_list3 = graph3.get_scc()
    print(f"Edges: {edges3}")
    print(f"SCCs: {scc_list3}")
    print()
    
    # Test 4: Condensation graph
    print("Test 4: Condensation Graph")
    edges4 = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3)]
    scc_list4, condensed_adj, scc_id = condensation_graph(6, edges4)
    
    print(f"Original edges: {edges4}")
    print(f"SCCs: {scc_list4}")
    print(f"SCC mapping: {scc_id}")
    print(f"Condensation graph: {dict(condensed_adj)}")
    print()
    
    # Test 5: Large example
    print("Test 5: Larger Graph")
    graph5 = KosarajuSCC(8)
    edges5 = [
        (0, 1), (1, 2), (2, 3), (3, 1),  # SCC: {1, 2, 3}
        (2, 4), (4, 5), (5, 6), (6, 4),  # SCC: {4, 5, 6}
        (6, 7)                            # SCC: {0}, {7}
    ]
    for u, v in edges5:
        graph5.add_edge(u, v)
    
    scc_list5 = graph5.get_scc()
    print(f"Large graph SCCs: {scc_list5}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_kosaraju()
