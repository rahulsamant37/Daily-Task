# 🐍 Python STL Guide for Competitive Programming

> *Simple and practical reference for Python's built-in data structures and algorithms*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![CP](https://img.shields.io/badge/Competitive-Programming-orange.svg)](https://codeforces.com/)

---

## 📋 Table of Contents
- [📦 Data Structures](#-data-structures)
- [🔍 Algorithms](#-algorithms)
- [🧮 Math Functions](#-math-functions)
- [📊 Graph Basics](#-graph-basics)
- [⚡ Performance Tips](#-performance-tips)
- [📝 Templates](#-templates)

---

## 📦 Data Structures

### Basic Containers

| C++ STL | Python | Usage Example |
|---------|--------|---------------|
| `vector` | `list` | `arr = [1, 2, 3]` |
| `set` | `set` | `s = {1, 2, 3}` |
| `map` | `dict` | `d = {'a': 1, 'b': 2}` |
| `stack` | `list` | `stack.append(x)`, `stack.pop()` |
| `queue` | `deque` | `from collections import deque` |
| `priority_queue` | `heapq` | `import heapq` |

### Useful Collections

```python
from collections import defaultdict, Counter, deque

# Auto-initialize dict
graph = defaultdict(list)
graph[1].append(2)  # No KeyError

# Count frequencies
count = Counter([1, 2, 2, 3])  # {2: 2, 1: 1, 3: 1}

# Double-ended queue
q = deque([1, 2, 3])
q.appendleft(0)  # [0, 1, 2, 3]
q.pop()          # [0, 1, 2]
```

---

## 🔍 Algorithms

### Sorting & Searching

```python
# Sorting
arr = [3, 1, 4, 1, 5]
sorted_arr = sorted(arr)           # [1, 1, 3, 4, 5]
arr.sort()                         # In-place sort
arr.sort(key=lambda x: -x)         # Descending order

# Binary Search
import bisect
arr = [1, 3, 5, 7, 9]
pos = bisect.bisect_left(arr, 5)   # Position to insert 5
```

### Itertools (Combinations & Permutations)

```python
from itertools import permutations, combinations, product

arr = [1, 2, 3]
perms = list(permutations(arr, 2))      # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
combs = list(combinations(arr, 2))      # [(1,2), (1,3), (2,3)]
cart = list(product([1,2], [3,4]))     # [(1,3), (1,4), (2,3), (2,4)]
```

---

## 🧮 Math Functions

### Basic Math

```python
import math

# Common functions
math.gcd(12, 8)        # 4
math.sqrt(16)          # 4.0
math.floor(3.7)        # 3
math.ceil(3.2)         # 4

# Power with modulo
pow(2, 10, 1000)       # 24 (2^10 % 1000)

# Python 3.8+ features
math.isqrt(16)         # 4 (integer square root)
math.comb(5, 2)        # 10 (5 choose 2)
```

### Number Theory

```python
# Check if prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Generate primes (Sieve)
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]
```

---

## 📊 Graph Basics

### Graph Representation

```python
from collections import defaultdict, deque

# Adjacency List
graph = defaultdict(list)
graph[1] = [2, 3]
graph[2] = [4]

# Weighted Graph
weighted_graph = defaultdict(list)
weighted_graph[1] = [(2, 5), (3, 10)]  # (neighbor, weight)
```

### BFS & DFS

```python
# BFS Template
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node)  # Process node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS Template
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)  # Process node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

---

## ⚡ Performance Tips

### Fast Input/Output

```python
import sys

# Fast input
input = sys.stdin.readline

# Read integers
n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))

# Increase recursion limit
sys.setrecursionlimit(10**6)
```

### Python Tricks

```python
# Useful one-liners
a, b = b, a              # Swap variables
arr[::-1]                # Reverse array
max(arr), min(arr)       # Max and min
sum(arr)                 # Sum of elements

# List comprehensions
squares = [x*x for x in range(10)]
evens = [x for x in arr if x % 2 == 0]

# Use enumerate and zip
for i, val in enumerate(arr):        # Better than range(len(arr))
    print(f"{i}: {val}")

for a, b in zip(arr1, arr2):         # Parallel iteration
    print(a, b)
```

---

## 📝 Templates

### Basic CP Template

```python
import sys
from collections import defaultdict, deque, Counter
import heapq
import math

# Fast I/O
input = sys.stdin.readline

def solve():
    # Read input
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Your solution here
    result = 0
    
    # Output
    print(result)

# Main
if __name__ == "__main__":
    t = int(input())  # Test cases
    for _ in range(t):
        solve()
```

### Common Patterns

```python
# Reading 2D grid
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(input().strip())
    grid.append(row)

# Frequency counting
from collections import Counter
freq = Counter(string)
most_common = freq.most_common(1)[0]

# Coordinate compression
def compress(arr):
    unique = sorted(set(arr))
    return {v: i for i, v in enumerate(unique)}

# Binary search on answer
def can_achieve(target):
    # Check if target is achievable
    return True  # or False

left, right = 0, 10**9
while left < right:
    mid = (left + right) // 2
    if can_achieve(mid):
        right = mid
    else:
        left = mid + 1
answer = left
```

---

## 🎯 Quick Reference

### Time Complexities

| Operation | List | Set | Dict | Deque |
|-----------|------|-----|------|-------|
| Access | O(1) | - | O(1) | O(1) |
| Search | O(n) | O(1) | O(1) | O(n) |
| Insert | O(1) | O(1) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) | O(1) |

### Contest Tips

**Codeforces:**
- Use PyPy3 for better performance
- Watch time limits carefully
- Read all test cases first

**General:**
- Test with sample inputs
- Handle edge cases (n=0, n=1)
- Use meaningful variable names
- Comment your approach

---

## 📚 Resources

### Practice Platforms
- [Codeforces](https://codeforces.com) - Regular contests
- [AtCoder](https://atcoder.jp) - Math-heavy problems
- [LeetCode](https://leetcode.com) - Interview prep

### Learning
- **CP Handbook** by Antti Laaksonen
- **Competitive Programming 4** by Steven Halim
- **Errichto** YouTube channel

---

*Made with ❤️ for competitive programmers. Happy coding! 🚀*

---

**Last Updated:** September 2025  
**Python Version:** 3.8+  
**Tested on:** Codeforces, AtCoder, LeetCode
