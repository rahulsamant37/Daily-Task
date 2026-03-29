import heapq
from collections import defaultdict

def dijkstra(graph, start, n):
    """
    Dijkstra's algorithm for single source shortest path
    Time complexity: O(V log V + E log V)
    
    Args:
        graph: adjacency list representation {u: [(v, weight), ...]}
        start: starting vertex
        n: number of vertices (0 to n-1)
    
    Returns:
        dist: list of shortest distances from start
        parent: list of parent nodes for path reconstruction
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    
    while pq:
        d_v, v = heapq.heappop(pq)
        
        # Skip if we've already found a better path
        if d_v != dist[v]:
            continue
        
        # Check all neighbors
        for neighbor, weight in graph[v]:
            if dist[v] + weight < dist[neighbor]:
                dist[neighbor] = dist[v] + weight
                parent[neighbor] = v
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    return dist, parent

def reconstruct_path(parent, start, end):
    """Reconstruct shortest path from start to end using parent array"""
    if parent[end] == -1 and start != end:
        return []  # No path exists
    
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    
    path.reverse()
    return path

def dijkstra_with_path(graph, start, end, n):
    """
    Dijkstra's algorithm that returns both distance and path
    
    Returns:
        distance: shortest distance from start to end
        path: shortest path from start to end
    """
    dist, parent = dijkstra(graph, start, n)
    path = reconstruct_path(parent, start, end)
    return dist[end], path

def dijkstra_all_pairs(graph, n):
    """
    Run Dijkstra from all vertices to get all-pairs shortest paths
    Time complexity: O(V^2 log V + VE log V)
    
    Returns:
        distances: 2D array where distances[i][j] is shortest path from i to j
    """
    distances = []
    for i in range(n):
        dist, _ = dijkstra(graph, i, n)
        distances.append(dist)
    return distances

def dijkstra_early_termination(graph, start, target, n):
    """
    Dijkstra's algorithm with early termination when target is reached
    
    Returns:
        distance to target, parent array for path reconstruction
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        d_v, v = heapq.heappop(pq)
        
        # Early termination
        if v == target:
            return dist[target], parent
        
        if d_v != dist[v]:
            continue
        
        for neighbor, weight in graph[v]:
            if dist[v] + weight < dist[neighbor]:
                dist[neighbor] = dist[v] + weight
                parent[neighbor] = v
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    return dist[target], parent

# Example usage and testing
def create_test_graph():
    """Create a test graph for demonstration"""
    # Graph representation: {vertex: [(neighbor, weight), ...]}
    graph = defaultdict(list)
    
    # Add edges
    edges = [
        (0, 1, 4), (0, 2, 2),
        (1, 2, 1), (1, 3, 5),
        (2, 3, 8), (2, 4, 10),
        (3, 4, 2)
    ]
    
    for u, v, w in edges:
        graph[u].append((v, w))
        # For undirected graph, add reverse edge
        # graph[v].append((u, w))
    
    return graph

def test_dijkstra():
    """Test Dijkstra's algorithm"""
    graph = create_test_graph()
    n = 5  # vertices 0, 1, 2, 3, 4
    start = 0
    
    print("Testing Dijkstra's Algorithm:")
    print(f"Graph: {dict(graph)}")
    
    # Test single source shortest path
    distances, parents = dijkstra(graph, start, n)
    print(f"\nShortest distances from vertex {start}:")
    for i in range(n):
        if distances[i] == float('inf'):
            print(f"  To vertex {i}: INFINITY (no path)")
        else:
            print(f"  To vertex {i}: {distances[i]}")
    
    # Test path reconstruction
    print(f"\nShortest paths from vertex {start}:")
    for i in range(n):
        path = reconstruct_path(parents, start, i)
        if path:
            print(f"  To vertex {i}: {' -> '.join(map(str, path))}")
        else:
            print(f"  To vertex {i}: No path")
    
    # Test specific path query
    target = 4
    distance, path = dijkstra_with_path(graph, start, target, n)
    print(f"\nSpecific query from {start} to {target}:")
    print(f"  Distance: {distance}")
    print(f"  Path: {' -> '.join(map(str, path))}")

# Utility functions for common graph problems

def dijkstra_modified_for_problem(graph, start, n, special_condition=None):
    """
    Modified Dijkstra for specific problem requirements
    Add custom logic as needed
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        d_v, v = heapq.heappop(pq)
        
        if d_v != dist[v]:
            continue
        
        for neighbor, weight in graph[v]:
            new_dist = dist[v] + weight
            
            # Add special condition here if needed
            if special_condition:
                new_dist = special_condition(v, neighbor, new_dist)
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = v
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    return dist, parent

def dijkstra_with_node_weights(graph, node_weights, start, n):
    """
    Dijkstra's algorithm where both edges and nodes have weights
    Total cost = edge_weight + destination_node_weight
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = node_weights[start]  # Include starting node weight
    
    pq = [(node_weights[start], start)]
    
    while pq:
        d_v, v = heapq.heappop(pq)
        
        if d_v != dist[v]:
            continue
        
        for neighbor, edge_weight in graph[v]:
            new_dist = dist[v] + edge_weight + node_weights[neighbor]
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = v
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    return dist, parent

if __name__ == "__main__":
    test_dijkstra()
