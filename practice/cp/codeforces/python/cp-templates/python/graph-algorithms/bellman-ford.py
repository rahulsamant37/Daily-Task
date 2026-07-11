from collections import defaultdict

def bellman_ford(graph, n, src):
    """
    Bellman-Ford algorithm for single source shortest path
    Can detect negative cycles
    Time complexity: O(VE)
    
    Args:
        graph: adjacency list {u: [(v, weight), ...]} or list of edges
        n: number of vertices (0 to n-1)
        src: source vertex
    
    Returns:
        (distances, has_negative_cycle, negative_cycle_nodes)
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[src] = 0
    
    # Convert adjacency list to edge list if needed
    edges = []
    if isinstance(graph, dict) or isinstance(graph, defaultdict):
        for u in graph:
            for v, weight in graph[u]:
                edges.append((u, v, weight))
    else:
        edges = graph  # Assume it's already an edge list
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
    
    # Check for negative cycles
    negative_cycle_nodes = set()
    for u, v, weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            negative_cycle_nodes.add(v)
    
    # Find all nodes affected by negative cycles
    if negative_cycle_nodes:
        # BFS to find all nodes reachable from negative cycle nodes
        queue = list(negative_cycle_nodes)
        visited = set(negative_cycle_nodes)
        
        while queue:
            node = queue.pop(0)
            for u, v, weight in edges:
                if u == node and v not in visited:
                    visited.add(v)
                    queue.append(v)
                    negative_cycle_nodes.add(v)
    
    has_negative_cycle = len(negative_cycle_nodes) > 0
    
    return dist, has_negative_cycle, negative_cycle_nodes

def bellman_ford_with_path(graph, n, src, target):
    """
    Bellman-Ford with path reconstruction
    
    Returns:
        (distance, path, has_negative_cycle)
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[src] = 0
    
    # Convert to edge list
    edges = []
    if isinstance(graph, dict) or isinstance(graph, defaultdict):
        for u in graph:
            for v, weight in graph[u]:
                edges.append((u, v, weight))
    else:
        edges = graph
    
    # Relax edges
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
    
    # Check for negative cycles
    has_negative_cycle = False
    for u, v, weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            has_negative_cycle = True
            break
    
    # Reconstruct path
    path = []
    if dist[target] != INF and not has_negative_cycle:
        current = target
        while current != -1:
            path.append(current)
            current = parent[current]
        path.reverse()
    
    return dist[target], path, has_negative_cycle

def detect_negative_cycle(graph, n):
    """
    Detect if graph has any negative cycle
    
    Args:
        graph: adjacency list or edge list
        n: number of vertices
    
    Returns:
        True if negative cycle exists, False otherwise
    """
    # Run Bellman-Ford from vertex 0 (or any vertex)
    # If graph is disconnected, we might need to run from multiple sources
    
    for start in range(n):
        dist, has_cycle, _ = bellman_ford(graph, n, start)
        if has_cycle:
            return True
    
    return False

def find_negative_cycle(graph, n):
    """
    Find a negative cycle in the graph if one exists
    
    Returns:
        cycle: list of vertices forming the negative cycle, or empty list if none
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    
    # Add a virtual source connected to all vertices with weight 0
    # This ensures we can find negative cycles in disconnected components
    virtual_source = n
    edges = []
    
    # Convert to edge list and add virtual edges
    if isinstance(graph, dict) or isinstance(graph, defaultdict):
        for u in graph:
            for v, weight in graph[u]:
                edges.append((u, v, weight))
    else:
        edges = list(graph)
    
    # Add virtual source edges
    for i in range(n):
        edges.append((virtual_source, i, 0))
    
    dist.append(0)  # Distance to virtual source
    parent.append(-1)
    n += 1
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
    
    # Find a vertex in negative cycle
    negative_vertex = -1
    for u, v, weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            parent[v] = u
            negative_vertex = v
    
    if negative_vertex == -1:
        return []  # No negative cycle
    
    # Move n steps back to ensure we're in the cycle
    for _ in range(n):
        negative_vertex = parent[negative_vertex]
    
    # Extract the cycle
    cycle = []
    current = negative_vertex
    while True:
        cycle.append(current)
        current = parent[current]
        if current == negative_vertex:
            break
    
    cycle.reverse()
    return cycle

def bellman_ford_improved(graph, n, src):
    """
    Improved Bellman-Ford with early termination
    Stops early if no improvements are made in an iteration
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[src] = 0
    
    edges = []
    if isinstance(graph, dict) or isinstance(graph, defaultdict):
        for u in graph:
            for v, weight in graph[u]:
                edges.append((u, v, weight))
    else:
        edges = graph
    
    # Relax edges with early termination
    for iteration in range(n - 1):
        improved = False
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                improved = True
        
        if not improved:
            break  # No improvements, algorithm can terminate early
    
    # Check for negative cycles
    negative_cycle_nodes = set()
    for u, v, weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            negative_cycle_nodes.add(v)
    
    has_negative_cycle = len(negative_cycle_nodes) > 0
    
    return dist, has_negative_cycle, negative_cycle_nodes

def spfa(graph, n, src):
    """
    SPFA (Shortest Path Faster Algorithm) - optimized Bellman-Ford
    Uses queue to process only vertices that might be improved
    Average case: O(E), Worst case: O(VE)
    """
    from collections import deque
    
    INF = float('inf')
    dist = [INF] * n
    in_queue = [False] * n
    queue = deque()
    
    dist[src] = 0
    queue.append(src)
    in_queue[src] = True
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
    
    return dist

# Test functions
def create_test_graph_with_negative():
    """Create test graph with negative edges"""
    graph = defaultdict(list)
    
    # Graph with negative edges but no negative cycle
    edges = [
        (0, 1, 4), (0, 2, 2),
        (1, 2, -3), (1, 3, 2),
        (2, 3, 4), (3, 4, 1)
    ]
    
    for u, v, w in edges:
        graph[u].append((v, w))
    
    return graph

def create_graph_with_negative_cycle():
    """Create test graph with negative cycle"""
    graph = defaultdict(list)
    
    # Graph with negative cycle: 0 -> 1 -> 2 -> 0
    edges = [
        (0, 1, 1), (1, 2, -2), (2, 0, -2),
        (0, 3, 5), (3, 4, 1)
    ]
    
    for u, v, w in edges:
        graph[u].append((v, w))
    
    return graph

def test_bellman_ford():
    """Test Bellman-Ford algorithm"""
    print("Testing Bellman-Ford Algorithm:")
    
    # Test with negative edges (no cycle)
    print("\nGraph with negative edges (no cycle):")
    graph1 = create_test_graph_with_negative()
    n = 5
    src = 0
    
    dist, has_cycle, cycle_nodes = bellman_ford(graph1, n, src)
    print(f"Distances from {src}: {dist}")
    print(f"Has negative cycle: {has_cycle}")
    
    # Test with negative cycle
    print("\nGraph with negative cycle:")
    graph2 = create_graph_with_negative_cycle()
    
    dist, has_cycle, cycle_nodes = bellman_ford(graph2, n, src)
    print(f"Has negative cycle: {has_cycle}")
    print(f"Nodes affected by negative cycle: {cycle_nodes}")
    
    # Test cycle detection
    print(f"\nNegative cycle detection: {detect_negative_cycle(graph2, n)}")
    
    # Test cycle finding
    cycle = find_negative_cycle(graph2, n)
    print(f"Negative cycle: {cycle}")

if __name__ == "__main__":
    test_bellman_ford()
