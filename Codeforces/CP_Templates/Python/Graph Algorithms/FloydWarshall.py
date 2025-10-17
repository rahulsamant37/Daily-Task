def floyd_warshall(n, edges):
    """
    Floyd-Warshall algorithm for all-pairs shortest paths
    Time complexity: O(n^3)
    
    Args:
        n: number of vertices (0 to n-1)
        edges: adjacency list {u: [(v, weight), ...]} or list of (u, v, weight)
        
    Returns:
        dist: 2D array where dist[i][j] is shortest distance from i to j
        next: 2D array for path reconstruction
    """
    INF = float('inf')
    
    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]
    next_node = [[-1] * n for _ in range(n)]
    
    # Distance from vertex to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Fill initial distances from edge list
    if isinstance(edges, dict):
        for u in edges:
            for v, weight in edges[u]:
                if dist[u][v] > weight:
                    dist[u][v] = weight
                    next_node[u][v] = v
    else:
        # Assume edges is list of (u, v, weight) tuples
        for u, v, weight in edges:
            if dist[u][v] > weight:
                dist[u][v] = weight
                next_node[u][v] = v
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]
    
    return dist, next_node

def has_negative_cycle(dist):
    """
    Check if graph has negative cycle using Floyd-Warshall result
    
    Args:
        dist: distance matrix from Floyd-Warshall
        
    Returns:
        True if negative cycle exists, False otherwise
    """
    n = len(dist)
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False

def reconstruct_path(next_node, start, end):
    """
    Reconstruct shortest path from start to end
    
    Args:
        next_node: next node matrix from Floyd-Warshall
        start: starting vertex
        end: ending vertex
        
    Returns:
        path from start to end, or empty list if no path exists
    """
    if next_node[start][end] == -1:
        return []
    
    path = [start]
    current = start
    
    while current != end:
        current = next_node[current][end]
        path.append(current)
    
    return path

def floyd_warshall_with_path_reconstruction(n, edges):
    """
    Floyd-Warshall with convenient path reconstruction
    
    Returns:
        (distances, get_path_function)
    """
    dist, next_node = floyd_warshall(n, edges)
    
    def get_path(start, end):
        return reconstruct_path(next_node, start, end)
    
    return dist, get_path

def detect_negative_cycles_floyd_warshall(n, edges):
    """
    Detect negative cycles and find affected vertices
    
    Returns:
        (has_negative_cycle, affected_vertices)
    """
    dist, _ = floyd_warshall(n, edges)
    
    # Run one more iteration to detect negative cycles
    affected = set()
    
    if isinstance(edges, dict):
        edge_list = []
        for u in edges:
            for v, weight in edges[u]:
                edge_list.append((u, v, weight))
    else:
        edge_list = edges
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        affected.add(i)
                        affected.add(j)
    
    return len(affected) > 0, affected

def transitive_closure(n, edges):
    """
    Compute transitive closure using Floyd-Warshall approach
    
    Returns:
        reachability matrix where reachable[i][j] = True if j is reachable from i
    """
    reachable = [[False] * n for _ in range(n)]
    
    # Initialize direct reachability
    for i in range(n):
        reachable[i][i] = True
    
    if isinstance(edges, dict):
        for u in edges:
            for v, _ in edges[u]:
                reachable[u][v] = True
    else:
        for u, v, _ in edges:
            reachable[u][v] = True
    
    # Floyd-Warshall for reachability
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
    
    return reachable

# Test functions
def test_floyd_warshall():
    """Test Floyd-Warshall algorithm"""
    print("Testing Floyd-Warshall Algorithm:")
    
    # Create test graph
    n = 4
    edges = [
        (0, 1, 3), (0, 3, 7),
        (1, 0, 8), (1, 2, 2),
        (2, 0, 5), (2, 3, 1),
        (3, 0, 2)
    ]
    
    print(f"Edges: {edges}")
    
    # Run Floyd-Warshall
    dist, get_path = floyd_warshall_with_path_reconstruction(n, edges)
    
    print("\nShortest distances:")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                print(f"  {i} -> {j}: INF")
            else:
                print(f"  {i} -> {j}: {dist[i][j]}")
    
    print("\nShortest paths:")
    for i in range(n):
        for j in range(n):
            if i != j:
                path = get_path(i, j)
                if path:
                    print(f"  {i} -> {j}: {' -> '.join(map(str, path))}")
                else:
                    print(f"  {i} -> {j}: No path")

if __name__ == "__main__":
    test_floyd_warshall()
