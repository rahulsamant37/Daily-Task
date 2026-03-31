"""
Advanced Data Structures for Competitive Programming
===================================================

Implement efficient data structures commonly used in competitive programming.
"""

import heapq
from collections import defaultdict, deque

class SegmentTree:
    """
    Segment Tree for range queries and updates
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2*node+1, start, mid, idx, val)
            else:
                self.update(2*node+2, mid+1, end, idx, val)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self.query(2*node+1, start, mid, l, r)
        right_sum = self.query(2*node+2, mid+1, end, l, r)
        return left_sum + right_sum
    
    def update_point(self, idx, val):
        self.update(0, 0, self.n-1, idx, val)
    
    def range_sum(self, l, r):
        return self.query(0, 0, self.n-1, l, r)

class FenwickTree:
    """
    Binary Indexed Tree (Fenwick Tree) for prefix sum queries
    """
    
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)
        return result
    
    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

class UnionFind:
    """
    Disjoint Set Union (Union-Find) with path compression and union by rank
    """
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        self.size[px] += self.size[py]
        
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def component_size(self, x):
        return self.size[self.find(x)]

class Trie:
    """
    Trie (Prefix Tree) for string operations
    """
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # Count of words passing through this node
    
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
            node.count += 1
        node.is_end = True
    
    def search(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def count_words_with_prefix(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

class LRUCache:
    """
    LRU Cache implementation using doubly linked list and hash map
    """
    
    class Node:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Create dummy head and tail
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # Move to head (most recently used)
            self._remove_node(node)
            self._add_to_head(node)
            return node.val
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used
                tail_node = self.tail.prev
                self._remove_node(tail_node)
                del self.cache[tail_node.key]
            
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

class SparseTable:
    """
    Sparse Table for range minimum/maximum queries
    """
    
    def __init__(self, arr, operation=min):
        self.op = operation
        self.n = len(arr)
        self.k = self.n.bit_length()
        self.st = [[0] * self.k for _ in range(self.n)]
        
        # Initialize first column
        for i in range(self.n):
            self.st[i][0] = arr[i]
        
        # Build sparse table
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[i][j] = self.op(self.st[i][j-1], 
                                       self.st[i + (1 << (j-1))][j-1])
                i += 1
            j += 1
    
    def query(self, l, r):
        # Query range [l, r] inclusive
        length = r - l + 1
        k = length.bit_length() - 1
        return self.op(self.st[l][k], self.st[r - (1 << k) + 1][k])

class MonotonicDeque:
    """
    Monotonic deque for sliding window maximum/minimum
    """
    
    def __init__(self, maximize=True):
        self.dq = deque()
        self.maximize = maximize
    
    def push(self, val, idx):
        # Remove elements that can't be optimal
        if self.maximize:
            while self.dq and self.dq[-1][0] <= val:
                self.dq.pop()
        else:
            while self.dq and self.dq[-1][0] >= val:
                self.dq.pop()
        
        self.dq.append((val, idx))
    
    def get_optimal(self, left_bound):
        # Remove elements outside window
        while self.dq and self.dq[0][1] < left_bound:
            self.dq.popleft()
        
        return self.dq[0][0] if self.dq else None

def sliding_window_maximum(arr, k):
    """
    Find maximum in each sliding window of size k
    """
    result = []
    dq = MonotonicDeque(maximize=True)
    
    for i in range(len(arr)):
        dq.push(arr[i], i)
        
        if i >= k - 1:
            max_val = dq.get_optimal(i - k + 1)
            result.append(max_val)
    
    return result

class Graph:
    """
    Graph representation with common algorithms
    """
    
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))
    
    def bfs(self, start):
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor, _ in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = [False] * self.n
        
        visited[start] = True
        result = [start]
        
        for neighbor, _ in self.adj[start]:
            if not visited[neighbor]:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
    def dijkstra(self, start):
        dist = [float('inf')] * self.n
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, weight in self.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        return dist

def data_structure_usage_examples():
    """
    Examples of using the implemented data structures
    """
    
    # Segment Tree example
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    range_sum = seg_tree.range_sum(1, 4)  # Sum from index 1 to 4
    
    # Fenwick Tree example
    bit = FenwickTree(6)
    for i, val in enumerate(arr, 1):
        bit.update(i, val)
    prefix_sum = bit.query(4)  # Sum of first 4 elements
    
    # Union-Find example
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    connected = uf.connected(0, 1)
    
    # Trie example
    trie = Trie()
    words = ["apple", "app", "application", "apply"]
    for word in words:
        trie.insert(word)
    has_app = trie.search("app")
    prefix_count = trie.count_words_with_prefix("app")
    
    # Sliding window maximum
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    max_windows = sliding_window_maximum(arr, 3)
    
    return {
        'segment_tree_sum': range_sum,
        'fenwick_tree_sum': prefix_sum,
        'union_find_connected': connected,
        'trie_has_app': has_app,
        'trie_prefix_count': prefix_count,
        'sliding_window_max': max_windows
    }

if __name__ == "__main__":
    print("Advanced Data Structures for CP")
    
    # Test all data structures
    results = data_structure_usage_examples()
    
    print("Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
    
    # Test sparse table
    arr = [4, 2, 3, 7, 1, 5]
    st = SparseTable(arr, min)
    range_min = st.query(1, 4)  # Minimum in range [1, 4]
    print(f"Range minimum [1,4]: {range_min}")
    
    # Test graph algorithms
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    
    bfs_result = g.bfs(0)
    dfs_result = g.dfs(0)
    
    print(f"BFS from 0: {bfs_result}")
    print(f"DFS from 0: {dfs_result}")
    
    print("\nData structures implemented successfully!")
