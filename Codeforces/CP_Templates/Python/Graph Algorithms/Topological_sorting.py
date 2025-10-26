from collections import defaultdict, deque

def topological_sort_dfs(n, edges):
    """
    Topological sorting using DFS
    Time complexity: O(V + E)
    
    Args:
        n: number of vertices (0 to n-1)
        edges: adjacency list representation
        
    Returns:
        topologically sorted order, or empty list if cycle exists
    """
    # Convert edges to adjacency list if needed
    if isinstance(edges, list):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
    else:
        adj = edges
    
    visited = [False] * n
    rec_stack = [False] * n  # Recursion stack for cycle detection
    result = []
    
    def dfs(node):
        visited[node] = True
        rec_stack[node] = True
        
        for neighbor in adj[node]:
            if rec_stack[neighbor]:  # Back edge found - cycle detected
                return False
            if not visited[neighbor] and not dfs(neighbor):
                return False
        
        rec_stack[node] = False
        result.append(node)
        return True
    
    # Process all vertices
    for i in range(n):
        if not visited[i]:
            if not dfs(i):
                return []  # Cycle detected
    
    result.reverse()
    return result

def topological_sort_kahn(n, edges):
    """
    Topological sorting using Kahn's algorithm (BFS-based)
    Time complexity: O(V + E)
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of edges [(u, v), ...] or adjacency list
        
    Returns:
        topologically sorted order, or empty list if cycle exists
    """
    # Build adjacency list and in-degree array
    adj = defaultdict(list)
    in_degree = [0] * n
    
    if isinstance(edges, list) and edges and len(edges[0]) == 2:
        # Edge list format
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
    else:
        # Adjacency list format
        for u in edges:
            for v in edges[u]:
                adj[u].append(v)
                in_degree[v] += 1
    
    # Initialize queue with vertices having 0 in-degree
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Reduce in-degree of neighbors
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all vertices are processed (no cycle)
    if len(result) != n:
        return []  # Cycle detected
    
    return result

def has_cycle_directed(n, edges):
    """
    Check if directed graph has a cycle
    
    Returns:
        True if cycle exists, False otherwise
    """
    topo_order = topological_sort_dfs(n, edges)
    return len(topo_order) == 0

def find_cycle_directed(n, edges):
    """
    Find a cycle in directed graph if one exists
    
    Returns:
        cycle as list of vertices, or empty list if no cycle
    """
    if isinstance(edges, list):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
    else:
        adj = edges
    
    visited = [False] * n
    rec_stack = [False] * n
    parent = [-1] * n
    
    def dfs(node, path):
        visited[node] = True
        rec_stack[node] = True
        path.append(node)
        
        for neighbor in adj[node]:
            if rec_stack[neighbor]:
                # Cycle found - extract cycle
                cycle_start = path.index(neighbor)
                return path[cycle_start:] + [neighbor]
            
            if not visited[neighbor]:
                cycle = dfs(neighbor, path)
                if cycle:
                    return cycle
        
        rec_stack[node] = False
        path.pop()
        return []
    
    for i in range(n):
        if not visited[i]:
            cycle = dfs(i, [])
            if cycle:
                return cycle
    
    return []

def all_topological_orders(n, edges):
    """
    Generate all possible topological orderings
    
    Returns:
        list of all topological orders
    """
    if isinstance(edges, list):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
    else:
        adj = edges
    
    in_degree = [0] * n
    for u in adj:
        for v in adj[u]:
            in_degree[v] += 1
    
    def backtrack(current_order, remaining_in_degree):
        if len(current_order) == n:
            return [current_order[:]]
        
        results = []
        for i in range(n):
            if remaining_in_degree[i] == 0 and i not in current_order:
                # Choose this vertex
                current_order.append(i)
                new_in_degree = remaining_in_degree[:]
                new_in_degree[i] = -1  # Mark as used
                
                # Update in-degrees
                for neighbor in adj[i]:
                    new_in_degree[neighbor] -= 1
                
                # Recurse
                results.extend(backtrack(current_order, new_in_degree))
                
                # Backtrack
                current_order.pop()
        
        return results
    
    return backtrack([], in_degree)

def lexicographically_smallest_topological_order(n, edges):
    """
    Find lexicographically smallest topological ordering
    
    Returns:
        lexicographically smallest topological order
    """
    import heapq
    
    if isinstance(edges, list):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
    else:
        adj = edges
    
    in_degree = [0] * n
    for u in adj:
        for v in adj[u]:
            in_degree[v] += 1
    
    # Use min-heap instead of queue
    heap = []
    for i in range(n):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)
    
    result = []
    
    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)
    
    return result if len(result) == n else []

def longest_path_dag(n, edges, weights=None):
    """
    Find longest path in DAG using topological sorting
    
    Args:
        n: number of vertices
        edges: edge list or adjacency list
        weights: edge weights (if None, all weights are 1)
        
    Returns:
        (longest_distances, predecessors)
    """
    if isinstance(edges, list):
        adj = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            weight = weights[i] if weights else 1
            adj[u].append((v, weight))
    else:
        adj = edges
    
    topo_order = topological_sort_kahn(n, [(u, v) for u in adj for v, _ in adj[u]])
    
    if not topo_order:
        return None, None  # Graph has cycle
    
    dist = [-float('inf')] * n
    pred = [-1] * n
    
    # Set distance to all vertices to negative infinity
    # Start from vertices with no incoming edges
    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0
        
        for neighbor, weight in adj[node]:
            if dist[node] + weight > dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                pred[neighbor] = node
    
    return dist, pred

def count_paths_dag(n, edges, start, end):
    """
    Count number of paths from start to end in DAG
    
    Returns:
        number of paths from start to end
    """
    if isinstance(edges, list):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
    else:
        adj = edges
    
    topo_order = topological_sort_kahn(n, [(u, v) for u in adj for v in adj[u]])
    
    if not topo_order:
        return 0  # Graph has cycle
    
    dp = [0] * n
    dp[start] = 1
    
    # Process vertices in topological order
    start_idx = topo_order.index(start)
    for i in range(start_idx, len(topo_order)):
        node = topo_order[i]
        for neighbor in adj[node]:
            dp[neighbor] += dp[node]
    
    return dp[end]

# Test functions
def test_topological_sort():
    """Test topological sorting algorithms"""
    print("Testing Topological Sort:")
    
    # Create test DAG
    n = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    
    print(f"Edges: {edges}")
    
    # Test DFS-based topological sort
    topo_dfs = topological_sort_dfs(n, edges)
    print(f"DFS Topological Order: {topo_dfs}")
    
    # Test Kahn's algorithm
    topo_kahn = topological_sort_kahn(n, edges)
    print(f"Kahn's Topological Order: {topo_kahn}")
    
    # Test lexicographically smallest
    topo_lex = lexicographically_smallest_topological_order(n, edges)
    print(f"Lexicographically Smallest: {topo_lex}")
    
    # Test cycle detection
    print(f"Has cycle: {has_cycle_directed(n, edges)}")

def test_cycle_detection():
    """Test cycle detection in directed graph"""
    print("\nTesting Cycle Detection:")
    
    # Graph with cycle
    n = 4
    edges_with_cycle = [(0, 1), (1, 2), (2, 3), (3, 1)]
    
    print(f"Edges with cycle: {edges_with_cycle}")
    print(f"Has cycle: {has_cycle_directed(n, edges_with_cycle)}")
    
    cycle = find_cycle_directed(n, edges_with_cycle)
    print(f"Cycle found: {cycle}")

def test_dag_algorithms():
    """Test DAG-specific algorithms"""
    print("\nTesting DAG Algorithms:")
    
    n = 6
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (1, 4)]
    
    # Test longest path
    dist, pred = longest_path_dag(n, edges)
    print(f"Longest distances: {dist}")
    
    # Test path counting
    paths = count_paths_dag(n, edges, 0, 4)
    print(f"Number of paths from 0 to 4: {paths}")

if __name__ == "__main__":
    test_topological_sort()
    test_cycle_detection()
    test_dag_algorithms()
