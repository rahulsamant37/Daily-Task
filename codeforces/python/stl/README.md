# 🐍 Python STL Guide for Competitive Programming

> *Progressive learning path from beginner to expert level*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![CP](https://img.shields.io/badge/Competitive-Programming-orange.svg)](https://codeforces.com/)

---

## 📋 Table of Contents
- [� Beginner Level](#-beginner-level)
- [� Intermediate Level](#-intermediate-level)
- [🟠 Advanced Level](#-advanced-level)
- [� Expert Level](#-expert-level)
- [🎯 Quick Reference](#-quick-reference)

---

## � Beginner Level
*Essential concepts for getting started in competitive programming*

### 🧱 Basic Data Structures

| C++ STL | Python | Usage | Complexity |
|---------|--------|-------|------------|
| `vector` | `list` | `arr = [1, 2, 3]` | O(1) append |
| `set` | `set` | `s = {1, 2, 3}` | O(1) avg lookup |
| `map` | `dict` | `d = {'a': 1, 'b': 2}` | O(1) avg lookup |

### 📥 Basic Input/Output

```python
# Simple I/O
n = int(input())                    # Read single integer
a, b = map(int, input().split())    # Read two integers
arr = list(map(int, input().split())) # Read array

# Output
print(result)
print(*arr)  # Print array elements separated by space
```

### 🔧 Essential Operations

```python
# Array operations
arr = [3, 1, 4, 1, 5]
arr.sort()                    # Sort in place: [1, 1, 3, 4, 5]
sorted_arr = sorted(arr)      # Create new sorted array
arr.reverse()                 # Reverse in place
reversed_arr = arr[::-1]      # Create new reversed array

# Basic math
max_val = max(arr)
min_val = min(arr)
total = sum(arr)
length = len(arr)
```

### 📚 Simple String Operations

```python
s = "Hello World"
s.upper()           # "HELLO WORLD"
s.lower()           # "hello world"
s.split()           # ["Hello", "World"]
"".join(arr)        # Join array elements
s[0]                # First character
s[-1]               # Last character
s[1:4]              # Substring
```

---

## 🟡 Intermediate Level
*Building stronger foundations for contest problems*

### 📊 Advanced Collections

```python
from collections import defaultdict, Counter, deque

# Auto-initializing dictionary
graph = defaultdict(list)
freq = defaultdict(int)
graph[1].append(2)  # No KeyError
freq['a'] += 1      # No KeyError

# Count frequencies efficiently
count = Counter([1, 2, 2, 3])        # {2: 2, 1: 1, 3: 1}
most_common = count.most_common(2)   # [(2, 2), (1, 1)]

# Double-ended queue (deque)
q = deque([1, 2, 3])
q.appendleft(0)     # [0, 1, 2, 3]
q.append(4)         # [0, 1, 2, 3, 4]
q.popleft()         # [1, 2, 3, 4]
q.pop()             # [1, 2, 3]
```

### 🔍 Searching & Sorting

```python
import bisect

# Binary search on sorted array
arr = [1, 3, 5, 7, 9, 11]
pos = bisect.bisect_left(arr, 5)    # Position of 5 or where to insert
right_pos = bisect.bisect_right(arr, 5)  # Position after 5

# Custom sorting
students = [("Alice", 85), ("Bob", 90), ("Charlie", 85)]
students.sort(key=lambda x: (-x[1], x[0]))  # Sort by grade desc, then name asc

# Sort with multiple criteria
arr.sort(key=lambda x: (x[0], -x[1]))  # First asc, second desc
```

### 🧮 Essential Math

```python
import math

# Basic math functions
math.gcd(12, 8)         # Greatest Common Divisor: 4
math.sqrt(16)           # Square root: 4.0
math.floor(3.7)         # Floor: 3
math.ceil(3.2)          # Ceiling: 4

# Power with modulo (very important!)
pow(2, 10, 1000)        # (2^10) % 1000 = 24

# Check if number is prime
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True
```

### ⚡ Performance Basics

```python
import sys

# Fast input (essential for large inputs)
input = sys.stdin.readline

# List comprehensions (faster than loops)
squares = [x*x for x in range(10)]
evens = [x for x in arr if x % 2 == 0]

# Useful built-ins
all([True, True, False])    # False - all elements true?
any([False, False, True])   # True - any element true?
```

---

## � Advanced Level
*Complex algorithms and data structures for challenging problems*

### 🌲 Graph Algorithms

```python
from collections import defaultdict, deque
import heapq

# Graph representation
graph = defaultdict(list)
weighted_graph = defaultdict(list)

# BFS (Breadth-First Search)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    distance = {start: 0}
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[node] + 1
    return distance

# DFS (Depth-First Search)
def dfs(graph, node, visited=None, path=None):
    if visited is None: visited = set()
    if path is None: path = []
    
    visited.add(node)
    path.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    return path

# Dijkstra's Algorithm (shortest path)
def dijkstra(graph, start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > distances[node]:
            continue
            
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
```

### 🔄 Advanced Itertools

```python
from itertools import permutations, combinations, product, groupby

# Generate combinations and permutations
arr = [1, 2, 3]
perms = list(permutations(arr, 2))              # All 2-element permutations
combs = list(combinations(arr, 2))              # All 2-element combinations
cart_prod = list(product([1,2], ['a','b']))    # Cartesian product

# Group consecutive elements
data = [1, 1, 2, 2, 2, 3, 1, 1]
for key, group in groupby(data):
    print(f"{key}: {len(list(group))}")  # Group consecutive same elements
```

### 🏗️ Advanced Data Structures

```python
import heapq

# Min-Heap operations
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
min_val = heapq.heappop(heap)  # Gets 1

# Max-Heap (use negative values)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
max_val = -heapq.heappop(max_heap)  # Gets 5

# Convert list to heap
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)  # O(n) operation
```

### 🧮 Advanced Number Theory

```python
# Sieve of Eratosthenes (generate all primes up to n)
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
                
    return [i for i in range(2, n + 1) if is_prime[i]]

# Extended GCD
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Fast modular exponentiation
def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result
```

---

## � Expert Level
*Advanced techniques for competitive programming mastery*

### 🧠 Dynamic Programming Optimization

```python
from functools import lru_cache

# Memoization with decorator
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

# Custom memoization
def dp_solve():
    memo = {}
    def solve(state):
        if state in memo:
            return memo[state]
        # Base cases and recursive logic here
        result = some_computation()
        memo[state] = result
        return result
    return solve

# 2D DP pattern
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### 🌟 Advanced Patterns

```python
# Binary search on answer
def binary_search_answer():
    def can_achieve(target):
        # Check if target is achievable
        return True  # Implementation depends on problem
    
    left, right = 0, 10**9
    while left < right:
        mid = (left + right) // 2
        if can_achieve(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Coordinate compression
def compress_coordinates(coords):
    unique_coords = sorted(set(coords))
    coord_map = {coord: i for i, coord in enumerate(unique_coords)}
    return [coord_map[coord] for coord in coords]

# Sliding window maximum
from collections import deque
def sliding_window_maximum(arr, k):
    dq = deque()
    result = []
    
    for i in range(len(arr)):
        # Remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result
```

### 🔧 Union-Find (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
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
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### 🎲 Advanced Techniques

```python
# Segment Tree (Range queries)
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node, start, mid)
            self.build(arr, 2*node+1, mid+1, end)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self.query(2*node, start, mid, l, r)
        right_sum = self.query(2*node+1, mid+1, end, l, r)
        return left_sum + right_sum

# Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
```

---

## 🎯 Quick Reference

### 📊 Complexity Cheat Sheet

| Data Structure | Access | Search | Insert | Delete |
|----------------|--------|--------|--------|--------|
| **List**       | O(1)   | O(n)   | O(1)*  | O(n)   |
| **Set**        | -      | O(1)   | O(1)   | O(1)   |
| **Dict**       | O(1)   | O(1)   | O(1)   | O(1)   |
| **Deque**      | O(1)   | O(n)   | O(1)   | O(1)   |
| **Heap**       | -      | O(n)   | O(log n)| O(log n)|

*O(1) amortized for append

### 🎯 Skill Level Progression

| Level | Focus Areas | Contest Rating |
|-------|-------------|----------------|
| **🟢 Beginner** | Basic I/O, Arrays, Strings, Simple Math | 0-1000 |
| **🟡 Intermediate** | Collections, Binary Search, Graph Traversal | 1000-1400 |
| **🟠 Advanced** | DP, Advanced Graphs, Number Theory | 1400-1800 |
| **🔴 Expert** | Complex DS, Optimization, Advanced Algorithms | 1800+ |

### 📝 Quick Templates

```python
# 🟢 Beginner Template
n = int(input())
arr = list(map(int, input().split()))
result = sum(arr)
print(result)

# 🟡 Intermediate Template
from collections import defaultdict, Counter
import bisect

def solve():
    n = int(input())
    # Your logic here
    return result

# 🟠 Advanced Template
import sys
from collections import defaultdict, deque
import heapq
from functools import lru_cache

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 🔴 Expert Template
class AdvancedDS:
    def __init__(self):
        # Complex data structure implementation
        pass
```

---

## 📚 Learning Resources

### 🎯 Practice by Level

**🟢 Beginner (800-1000):**
- [Codeforces A problems](https://codeforces.com/problemset?tags=800-1000)
- Focus: Basic implementation, arrays, strings

**🟡 Intermediate (1000-1400):**
- [Codeforces B problems](https://codeforces.com/problemset?tags=1000-1400)
- Focus: Binary search, greedy, basic graphs

**🟠 Advanced (1400-1800):**
- [Codeforces C problems](https://codeforces.com/problemset?tags=1400-1800)
- Focus: DP, advanced graphs, number theory

**🔴 Expert (1800+):**
- [Codeforces D+ problems](https://codeforces.com/problemset?tags=1800)
- Focus: Complex algorithms, optimization

### � Recommended Books
- **"Competitive Programming 4"** by Steven Halim
- **"Guide to Competitive Programming"** by Antti Laaksonen
- **"Elements of Programming Interviews"** by Aziz, Lee, Prakash

### 🌐 Practice Platforms
- **[Codeforces](https://codeforces.com)** - Regular contests, strong community
- **[AtCoder](https://atcoder.jp)** - High-quality problems, math focus
- **[LeetCode](https://leetcode.com)** - Interview preparation
- **[HackerRank](https://hackerrank.com)** - Skill-based tracks

### 📺 YouTube Channels
- **Errichto** - Advanced algorithms and contest solutions
- **William Lin** - Contest participation and problem solving
- **SecondThread** - Algorithm explanations
- **Gennady Korotkevich (tourist)** - Contest streams

---

## 🏆 Contest Strategy by Level

### 🟢 Beginner Strategy
1. **Read carefully** - Understand the problem completely
2. **Start simple** - Implement the most straightforward solution
3. **Test manually** - Verify with sample inputs
4. **Time management** - Aim to solve A and B problems

### 🟡 Intermediate Strategy
1. **Pattern recognition** - Identify common problem types
2. **Optimize early** - Think about time complexity
3. **Use libraries** - Leverage collections and bisect
4. **Target rating** - Consistently solve A, B, and attempt C

### 🟠 Advanced Strategy
1. **Algorithm selection** - Choose the right approach quickly
2. **Implementation speed** - Code efficiently and accurately
3. **Edge cases** - Consider boundary conditions
4. **Multiple approaches** - Have backup solutions ready

### 🔴 Expert Strategy
1. **Problem decomposition** - Break complex problems into parts
2. **Advanced techniques** - Apply sophisticated algorithms
3. **Optimization** - Fine-tune for time and space constraints
4. **Innovation** - Develop novel approaches when needed

---

*Made with ❤️ for competitive programmers. Happy coding! 🚀*

---

**Last Updated:** September 2025  
**Python Version:** 3.8+  
**Tested on:** Codeforces, AtCoder, LeetCode
