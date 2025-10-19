"""
Ford-Fulkerson Algorithm for Maximum Flow
=========================================

Finds the maximum flow in a flow network from source to sink.
Uses DFS to find augmenting paths and updates residual capacities.

Time Complexity: O(E * max_flow) in worst case
                 O(VE²) with DFS
Space Complexity: O(V + E)

For better performance, use Edmonds-Karp (BFS) or Dinic's algorithm.

Author: Converted from C++ implementation
"""

from collections import defaultdict, deque
import sys

class Edge:
    """
    Represents an edge in the flow network
    """
    
    def __init__(self, src, dest, capacity, flow=0):
        """
        Initialize edge
        
        Args:
            src: source vertex
            dest: destination vertex
            capacity: maximum capacity
            flow: current flow (default 0)
        """
        self.src = src
        self.dest = dest
        self.capacity = capacity
        self.flow = flow
    
    def residual_capacity(self):
        """Get remaining capacity"""
        return self.capacity - self.flow
    
    def __repr__(self):
        return f"Edge({self.src}->{self.dest}, cap={self.capacity}, flow={self.flow})"

class FordFulkerson:
    """
    Ford-Fulkerson algorithm implementation for maximum flow
    """
    
    def __init__(self, n):
        """
        Initialize flow network
        
        Args:
            n: number of vertices
        """
        self.n = n
        self.adj = defaultdict(list)  # adjacency list of edge indices
        self.edges = []  # list of all edges
        self.iteration = 0
        self.visited = None
    
    def add_edge(self, src, dest, capacity):
        """
        Add edge to the flow network
        
        Args:
            src: source vertex
            dest: destination vertex
            capacity: edge capacity
        
        Returns:
            index of the added edge
        """
        # Forward edge
        forward_edge = Edge(src, dest, capacity)
        forward_idx = len(self.edges)
        self.edges.append(forward_edge)
        self.adj[src].append(forward_idx)
        
        # Backward edge (residual)
        backward_edge = Edge(dest, src, 0)
        backward_idx = len(self.edges)
        self.edges.append(backward_edge)
        self.adj[dest].append(backward_idx)
        
        return forward_idx
    
    def dfs(self, v, sink, min_capacity):
        """
        DFS to find augmenting path
        
        Args:
            v: current vertex
            sink: destination vertex
            min_capacity: minimum capacity along current path
        
        Returns:
            flow that can be pushed through this path
        """
        if v == sink:
            return min_capacity
        
        self.visited[v] = self.iteration
        
        for edge_idx in self.adj[v]:
            edge = self.edges[edge_idx]
            
            if (self.visited[edge.dest] != self.iteration and 
                edge.residual_capacity() > 0):
                
                flow = self.dfs(edge.dest, sink, 
                              min(min_capacity, edge.residual_capacity()))
                
                if flow > 0:
                    # Update forward edge
                    self.edges[edge_idx].flow += flow
                    
                    # Update backward edge
                    backward_idx = edge_idx ^ 1  # XOR to get pair
                    self.edges[backward_idx].flow -= flow
                    
                    return flow
        
        return 0
    
    def max_flow(self, source, sink):
        """
        Find maximum flow from source to sink
        
        Args:
            source: source vertex
            sink: sink vertex
        
        Returns:
            maximum flow value
        """
        max_flow_value = 0
        self.visited = [0] * self.n
        self.iteration = 1
        
        while True:
            # Find augmenting path using DFS
            flow = self.dfs(source, sink, float('inf'))
            
            if flow == 0:
                break
            
            max_flow_value += flow
            self.iteration += 1
        
        return max_flow_value
    
    def get_min_cut(self, source, sink):
        """
        Find minimum cut after computing maximum flow
        
        Args:
            source: source vertex
            sink: sink vertex
        
        Returns:
            tuple (cut_edges, cut_vertices_s, cut_vertices_t)
        """
        # First compute max flow
        self.max_flow(source, sink)
        
        # Find vertices reachable from source in residual graph
        reachable = [False] * self.n
        stack = [source]
        reachable[source] = True
        
        while stack:
            v = stack.pop()
            for edge_idx in self.adj[v]:
                edge = self.edges[edge_idx]
                if not reachable[edge.dest] and edge.residual_capacity() > 0:
                    reachable[edge.dest] = True
                    stack.append(edge.dest)
        
        # Find cut edges
        cut_edges = []
        for i in range(0, len(self.edges), 2):  # Only forward edges
            edge = self.edges[i]
            if reachable[edge.src] and not reachable[edge.dest]:
                cut_edges.append((edge.src, edge.dest, edge.capacity))
        
        # Partition vertices
        s_vertices = [i for i in range(self.n) if reachable[i]]
        t_vertices = [i for i in range(self.n) if not reachable[i]]
        
        return cut_edges, s_vertices, t_vertices
    
    def get_flow_details(self):
        """
        Get detailed flow information
        
        Returns:
            list of edges with their flows
        """
        flow_details = []
        for i in range(0, len(self.edges), 2):  # Only forward edges
            edge = self.edges[i]
            if edge.flow > 0:
                flow_details.append({
                    'from': edge.src,
                    'to': edge.dest,
                    'flow': edge.flow,
                    'capacity': edge.capacity
                })
        return flow_details

class EdmondsKarp:
    """
    Edmonds-Karp algorithm (Ford-Fulkerson with BFS)
    Better time complexity: O(VE²)
    """
    
    def __init__(self, n):
        self.n = n
        self.capacity = [[0] * n for _ in range(n)]
        self.flow = [[0] * n for _ in range(n)]
    
    def add_edge(self, src, dest, cap):
        """Add edge with capacity"""
        self.capacity[src][dest] += cap
    
    def bfs(self, source, sink, parent):
        """
        BFS to find augmenting path
        
        Returns:
            True if path exists, False otherwise
        """
        visited = [False] * self.n
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v in range(self.n):
                if (not visited[v] and 
                    self.capacity[u][v] - self.flow[u][v] > 0):
                    
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        
        return False
    
    def max_flow(self, source, sink):
        """
        Find maximum flow using Edmonds-Karp algorithm
        
        Returns:
            maximum flow value
        """
        parent = [-1] * self.n
        max_flow_value = 0
        
        while self.bfs(source, sink, parent):
            # Find minimum residual capacity along the path
            path_flow = float('inf')
            s = sink
            
            while s != source:
                path_flow = min(path_flow, 
                              self.capacity[parent[s]][s] - self.flow[parent[s]][s])
                s = parent[s]
            
            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                self.flow[u][v] += path_flow
                self.flow[v][u] -= path_flow
                v = parent[v]
            
            max_flow_value += path_flow
        
        return max_flow_value

def test_ford_fulkerson():
    """Test Ford-Fulkerson algorithm"""
    print("Testing Ford-Fulkerson Algorithm for Maximum Flow")
    print("=" * 50)
    
    # Test 1: Basic flow network
    print("Test 1: Basic Flow Network")
    graph1 = FordFulkerson(6)
    
    # Add edges: (src, dest, capacity)
    edges1 = [
        (0, 1, 16), (0, 2, 13),
        (1, 2, 10), (1, 3, 12),
        (2, 1, 4), (2, 4, 14),
        (3, 2, 9), (3, 5, 20),
        (4, 3, 7), (4, 5, 4)
    ]
    
    for src, dest, cap in edges1:
        graph1.add_edge(src, dest, cap)
    
    source, sink = 0, 5
    max_flow1 = graph1.max_flow(source, sink)
    
    print(f"Edges: {edges1}")
    print(f"Source: {source}, Sink: {sink}")
    print(f"Maximum flow: {max_flow1}")
    
    # Get flow details
    flow_details = graph1.get_flow_details()
    print("Flow details:")
    for detail in flow_details:
        print(f"  {detail['from']} -> {detail['to']}: {detail['flow']}/{detail['capacity']}")
    
    # Get min cut
    cut_edges, s_vertices, t_vertices = graph1.get_min_cut(source, sink)
    print(f"Min cut edges: {cut_edges}")
    print(f"S vertices: {s_vertices}")
    print(f"T vertices: {t_vertices}")
    print()
    
    # Test 2: Compare with Edmonds-Karp
    print("Test 2: Edmonds-Karp Comparison")
    graph2 = EdmondsKarp(6)
    
    for src, dest, cap in edges1:
        graph2.add_edge(src, dest, cap)
    
    max_flow2 = graph2.max_flow(source, sink)
    print(f"Ford-Fulkerson result: {max_flow1}")
    print(f"Edmonds-Karp result: {max_flow2}")
    print(f"Results match: {max_flow1 == max_flow2}")
    print()
    
    # Test 3: Simple path
    print("Test 3: Simple Path")
    graph3 = FordFulkerson(4)
    edges3 = [(0, 1, 20), (1, 2, 30), (2, 3, 10)]
    
    for src, dest, cap in edges3:
        graph3.add_edge(src, dest, cap)
    
    max_flow3 = graph3.max_flow(0, 3)
    print(f"Linear path: {edges3}")
    print(f"Maximum flow: {max_flow3}")  # Should be 10 (bottleneck)
    print()
    
    # Test 4: Disconnected graph
    print("Test 4: Disconnected Graph")
    graph4 = FordFulkerson(4)
    edges4 = [(0, 1, 10), (2, 3, 20)]  # No path from 0 to 3
    
    for src, dest, cap in edges4:
        graph4.add_edge(src, dest, cap)
    
    max_flow4 = graph4.max_flow(0, 3)
    print(f"Disconnected edges: {edges4}")
    print(f"Maximum flow from 0 to 3: {max_flow4}")  # Should be 0
    print()
    
    # Test 5: Multiple paths
    print("Test 5: Multiple Paths")
    graph5 = FordFulkerson(4)
    edges5 = [
        (0, 1, 10), (0, 2, 10),
        (1, 3, 25), (2, 3, 6)
    ]
    
    for src, dest, cap in edges5:
        graph5.add_edge(src, dest, cap)
    
    max_flow5 = graph5.max_flow(0, 3)
    print(f"Multiple paths: {edges5}")
    print(f"Maximum flow: {max_flow5}")
    
    flow_details5 = graph5.get_flow_details()
    print("Flow distribution:")
    for detail in flow_details5:
        print(f"  {detail['from']} -> {detail['to']}: {detail['flow']}")
    print()
    
    # Test 6: Star graph
    print("Test 6: Star Graph")
    graph6 = FordFulkerson(5)
    center = 2
    edges6 = [(0, center, 5), (1, center, 3), (center, 3, 4), (center, 4, 6)]
    
    for src, dest, cap in edges6:
        graph6.add_edge(src, dest, cap)
    
    # Multiple source-sink pairs
    flows = []
    for source in [0, 1]:
        for sink in [3, 4]:
            graph_copy = FordFulkerson(5)
            for src, dest, cap in edges6:
                graph_copy.add_edge(src, dest, cap)
            flow = graph_copy.max_flow(source, sink)
            flows.append((source, sink, flow))
    
    print(f"Star graph edges: {edges6}")
    for source, sink, flow in flows:
        print(f"Flow from {source} to {sink}: {flow}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_ford_fulkerson()
