"""
Graph Algorithms and Optimizations
=================================

Efficient graph algorithms and optimizations for competitive programming.
"""

import heapq
from collections import defaultdict, deque
import sys

def graph_representations():
    """
    Different ways to represent graphs and their trade-offs
    """
    
    # Adjacency List (most common in CP)
    class AdjacencyList:
        def __init__(self, n, directed=False):
            self.n = n
            self.directed = directed
            self.adj = [[] for _ in range(n)]
        
        def add_edge(self, u, v, weight=1):
            self.adj[u].append((v, weight))
            if not self.directed:
                self.adj[v].append((u, weight))
        
        def get_neighbors(self, u):
            return self.adj[u]
    
    # Adjacency Matrix (for dense graphs)
    class AdjacencyMatrix:
        def __init__(self, n, directed=False):
            self.n = n
            self.directed = directed
            self.adj = [[0] * n for _ in range(n)]
        
        def add_edge(self, u, v, weight=1):
            self.adj[u][v] = weight
            if not self.directed:
                self.adj[v][u] = weight
        
        def has_edge(self, u, v):
            return self.adj[u][v] != 0
    
    # Edge List (for algorithms like Kruskal's)
    class EdgeList:
        def __init__(self, n):
            self.n = n
            self.edges = []
        
        def add_edge(self, u, v, weight=1):
            self.edges.append((weight, u, v))
        
        def sort_edges(self):
            self.edges.sort()
    
    return AdjacencyList, AdjacencyMatrix, EdgeList

def bfs_variations():
    """
    BFS variations and optimizations
    """
    
    # Standard BFS
    def bfs_standard(graph, start):
        visited = [False] * graph.n
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor, _ in graph.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    # BFS with distance tracking
    def bfs_distance(graph, start):
        distance = [-1] * graph.n
        queue = deque([start])
        distance[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbor, _ in graph.adj[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        
        return distance
    
    # Multi-source BFS
    def bfs_multi_source(graph, sources):
        distance = [-1] * graph.n
        queue = deque()
        
        # Initialize all sources
        for source in sources:
            distance[source] = 0
            queue.append(source)
        
        while queue:
            node = queue.popleft()
            
            for neighbor, _ in graph.adj[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        
        return distance
    
    # 0-1 BFS (for graphs with edges of weight 0 or 1)
    def bfs_01(graph, start):
        distance = [float('inf')] * graph.n
        deque_bfs = deque([start])
        distance[start] = 0
        
        while deque_bfs:
            node = deque_bfs.popleft()
            
            for neighbor, weight in graph.adj[node]:
                new_dist = distance[node] + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    
                    if weight == 0:
                        deque_bfs.appendleft(neighbor)  # Add to front
                    else:
                        deque_bfs.append(neighbor)      # Add to back
        
        return distance
    
    return bfs_standard, bfs_distance, bfs_multi_source, bfs_01

def dfs_variations():
    """
    DFS variations and applications
    """
    
    # Iterative DFS (avoids recursion limit)
    def dfs_iterative(graph, start):
        visited = [False] * graph.n
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                result.append(node)
                
                # Add neighbors in reverse order for correct traversal
                for neighbor, _ in reversed(graph.adj[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        return result
    
    # DFS with timestamps (for topological sort, cycle detection)
    def dfs_timestamps(graph):
        n = graph.n
        visited = [False] * n
        start_time = [0] * n
        end_time = [0] * n
        time = [0]  # Use list for mutable reference
        
        def dfs(node):
            visited[node] = True
            time[0] += 1
            start_time[node] = time[0]
            
            for neighbor, _ in graph.adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            
            time[0] += 1
            end_time[node] = time[0]
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return start_time, end_time
    
    # Topological Sort using DFS
    def topological_sort_dfs(graph):
        visited = [False] * graph.n
        stack = []
        
        def dfs(node):
            visited[node] = True
            for neighbor, _ in graph.adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)
        
        for i in range(graph.n):
            if not visited[i]:
                dfs(i)
        
        return stack[::-1]  # Reverse to get topological order
    
    # Cycle detection in directed graph
    def has_cycle_directed(graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * graph.n
        
        def dfs(node):
            if color[node] == GRAY:
                return True  # Back edge found, cycle exists
            if color[node] == BLACK:
                return False
            
            color[node] = GRAY
            for neighbor, _ in graph.adj[node]:
                if dfs(neighbor):
                    return True
            color[node] = BLACK
            return False
        
        for i in range(graph.n):
            if color[i] == WHITE:
                if dfs(i):
                    return True
        return False
    
    return dfs_iterative, dfs_timestamps, topological_sort_dfs, has_cycle_directed

def shortest_path_algorithms():
    """
    Various shortest path algorithms
    """
    
    # Dijkstra's algorithm
    def dijkstra(graph, start):
        dist = [float('inf')] * graph.n
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, weight in graph.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        return dist
    
    # Bellman-Ford algorithm (handles negative weights)
    def bellman_ford(graph, start):
        dist = [float('inf')] * graph.n
        dist[start] = 0
        
        # Relax edges V-1 times
        for _ in range(graph.n - 1):
            for u in range(graph.n):
                if dist[u] != float('inf'):
                    for v, weight in graph.adj[u]:
                        dist[v] = min(dist[v], dist[u] + weight)
        
        # Check for negative cycles
        for u in range(graph.n):
            for v, weight in graph.adj[u]:
                if dist[u] + weight < dist[v]:
                    return None  # Negative cycle detected
        
        return dist
    
    # Floyd-Warshall (all pairs shortest path)
    def floyd_warshall(adj_matrix):
        n = len(adj_matrix)
        dist = [row[:] for row in adj_matrix]  # Copy matrix
        
        # Initialize distances
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                elif dist[i][j] == 0:
                    dist[i][j] = float('inf')
        
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        return dist
    
    return dijkstra, bellman_ford, floyd_warshall

def minimum_spanning_tree():
    """
    MST algorithms - Kruskal's and Prim's
    """
    
    # Union-Find for Kruskal's
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            
            return True
    
    # Kruskal's algorithm
    def kruskal_mst(edge_list):
        edge_list.sort_edges()
        uf = UnionFind(edge_list.n)
        mst_edges = []
        mst_weight = 0
        
        for weight, u, v in edge_list.edges:
            if uf.union(u, v):
                mst_edges.append((u, v, weight))
                mst_weight += weight
                
                if len(mst_edges) == edge_list.n - 1:
                    break
        
        return mst_edges, mst_weight
    
    # Prim's algorithm
    def prim_mst(graph, start=0):
        visited = [False] * graph.n
        min_heap = [(0, start, -1)]  # (weight, node, parent)
        mst_edges = []
        mst_weight = 0
        
        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
            
            if visited[u]:
                continue
            
            visited[u] = True
            if parent != -1:
                mst_edges.append((parent, u, weight))
                mst_weight += weight
            
            for v, w in graph.adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v, u))
        
        return mst_edges, mst_weight
    
    return kruskal_mst, prim_mst

def strongly_connected_components():
    """
    Tarjan's and Kosaraju's algorithms for SCCs
    """
    
    # Kosaraju's algorithm
    def kosaraju_scc(graph):
        # Step 1: Get finish times using DFS
        visited = [False] * graph.n
        finish_order = []
        
        def dfs1(node):
            visited[node] = True
            for neighbor, _ in graph.adj[node]:
                if not visited[neighbor]:
                    dfs1(neighbor)
            finish_order.append(node)
        
        for i in range(graph.n):
            if not visited[i]:
                dfs1(i)
        
        # Step 2: Create transpose graph
        transpose = [[] for _ in range(graph.n)]
        for u in range(graph.n):
            for v, _ in graph.adj[u]:
                transpose[v].append((u, 1))
        
        # Step 3: DFS on transpose in reverse finish order
        visited = [False] * graph.n
        scc_id = [-1] * graph.n
        scc_count = 0
        
        def dfs2(node, scc_id_val):
            visited[node] = True
            scc_id[node] = scc_id_val
            for neighbor, _ in transpose[node]:
                if not visited[neighbor]:
                    dfs2(neighbor, scc_id_val)
        
        for node in reversed(finish_order):
            if not visited[node]:
                dfs2(node, scc_count)
                scc_count += 1
        
        return scc_id, scc_count
    
    # Tarjan's algorithm (single DFS)
    def tarjan_scc(graph):
        index_counter = [0]
        stack = []
        lowlinks = [0] * graph.n
        index = [0] * graph.n
        on_stack = [False] * graph.n
        index_set = [False] * graph.n
        sccs = []
        
        def strongconnect(node):
            index[node] = index_counter[0]
            lowlinks[node] = index_counter[0]
            index_counter[0] += 1
            index_set[node] = True
            stack.append(node)
            on_stack[node] = True
            
            for neighbor, _ in graph.adj[node]:
                if not index_set[neighbor]:
                    strongconnect(neighbor)
                    lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
                elif on_stack[neighbor]:
                    lowlinks[node] = min(lowlinks[node], index[neighbor])
            
            if lowlinks[node] == index[node]:
                component = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    component.append(w)
                    if w == node:
                        break
                sccs.append(component)
        
        for node in range(graph.n):
            if not index_set[node]:
                strongconnect(node)
        
        return sccs
    
    return kosaraju_scc, tarjan_scc

def graph_optimization_tips():
    """
    Key optimization tips for graph algorithms
    """
    tips = [
        "1. Use adjacency lists for sparse graphs, matrices for dense graphs",
        "2. Use iterative DFS to avoid recursion limits",
        "3. Use deque for BFS, not list (O(1) popleft vs O(n))",
        "4. Use 0-1 BFS for graphs with edges of weight 0 or 1",
        "5. Use multi-source BFS for problems with multiple starting points",
        "6. Cache frequently accessed data (like graph size)",
        "7. Use early termination when possible",
        "8. For shortest paths: Dijkstra for non-negative, Bellman-Ford for negative",
        "9. Use bitmasking for state compression in graph DP",
        "10. Precompute reverse graphs when needed (like in Kosaraju's)",
        "11. Use Union-Find for connectivity queries",
        "12. Consider binary lifting for LCA queries in trees"
    ]
    return tips

def graph_examples():
    """
    Test various graph algorithms
    """
    
    # Create adjacency list graph
    AdjList, _, EdgeList = graph_representations()
    
    # Test graph
    graph = AdjList(6, directed=True)
    edges = [(0, 1, 2), (0, 2, 4), (1, 3, 1), (2, 3, 3), (3, 4, 2), (4, 5, 1)]
    
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    
    # Test BFS
    bfs_std, bfs_dist, _, _ = bfs_variations()
    bfs_result = bfs_std(graph, 0)
    distances = bfs_dist(graph, 0)
    
    # Test shortest paths
    dijkstra_func, _, _ = shortest_path_algorithms()
    shortest_paths = dijkstra_func(graph, 0)
    
    # Test topological sort
    _, _, topo_sort, _ = dfs_variations()
    topo_order = topo_sort(graph)
    
    return {
        'bfs_traversal': bfs_result,
        'bfs_distances': distances,
        'shortest_paths': shortest_paths,
        'topological_order': topo_order
    }

if __name__ == "__main__":
    print("Graph Algorithms and Optimizations")
    
    # Test algorithms
    results = graph_examples()
    
    print("Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
    
    # Test MST
    AdjList, _, EdgeList = graph_representations()
    
    # Create undirected graph for MST
    undirected_graph = AdjList(4, directed=False)
    edge_list = EdgeList(4)
    
    mst_edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 4), (0, 2, 5)]
    
    for u, v, w in mst_edges:
        undirected_graph.add_edge(u, v, w)
        edge_list.add_edge(u, v, w)
    
    # Test Kruskal's MST
    kruskal, prim = minimum_spanning_tree()
    mst_edges_k, mst_weight_k = kruskal(edge_list)
    mst_edges_p, mst_weight_p = prim(undirected_graph)
    
    print(f"\nKruskal MST edges: {mst_edges_k}, weight: {mst_weight_k}")
    print(f"Prim MST edges: {mst_edges_p}, weight: {mst_weight_p}")
    
    # Show optimization tips
    tips = graph_optimization_tips()
    print("\nGraph Optimization Tips:")
    for tip in tips:
        print(tip)
    
    print("\nGraph algorithms demonstrated successfully!")
