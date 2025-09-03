
# 🐍 Python STL-Equivalent Guide for Competitive Programming

> *Complete reference guide for Python's built-in data structures and algorithm---

## 📊 Graph Utilities

### 🌐 Graph Representations

```python
from collections import defaultdict, deque
import heapq

# Adjacency List
graph = defaultdict(list)
graph[u].append(v)  # Add edge u -> v

# Weighted Graph
weighted_graph = defaultdict(list)
weighted_graph[u].append((v, weight))

# Adjacency Matrix
n = 100  # number of vertices
adj_matrix = [[0] * n for _ ---

## 📝 Code Templates

### 🎯 Complete CP Template

```python
#!/usr/bin/env python3
import sys
from collections import *
from itertools import *
from heapq import *
import math
import bisect
from functools import lru_cache

# Fast I/O
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# Constants
MOD = 10**9 + 7
INF = float('inf')

# Utility functions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    # Your solution here
    pass

# Main execution
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        solve()
```

### 🔧 Common Code Snippets

```python
# Reading different input formats
n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))
s = input().strip()

# 2D array/matrix input
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Or one-liner
matrix = [list(map(int, input().split())) for _ in range(n)]

# Coordinate compression
def compress(arr):
    sorted_unique = sorted(set(arr))
    return {v: i for i, v in enumerate(sorted_unique)}

# Binary search on answer
def binary_search_answer(left, right, check_function):
    while left < right:
        mid = (left + right) // 2
        if check_function(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Modular arithmetic
def mod_add(a, b, mod=MOD):
    return (a + b) % mod

def mod_mul(a, b, mod=MOD):
    return (a * b) % mod

def mod_pow(base, exp, mod=MOD):
    return pow(base, exp, mod)

def mod_inv(a, mod=MOD):
    return pow(a, mod-2, mod)  # When mod is prime
```

---

## 🎯 Quick Reference

### ⚡ Time Complexity Cheat Sheet

| Operation                 | List      | Set       | Dict      | Deque     | Heap      |
| ------------------------- | --------- | --------- | --------- | --------- | --------- |
| Access by index          | O(1)      | N/A       | N/A       | O(1)      | N/A       |
| Search                    | O(n)      | O(1) avg  | O(1) avg  | O(n)      | O(n)      |
| Insertion (end)           | O(1) amor | O(1) avg  | O(1) avg  | O(1)      | O(log n)  |
| Insertion (beginning)     | O(n)      | O(1) avg  | O(1) avg  | O(1)      | N/A       |
| Deletion                  | O(n)      | O(1) avg  | O(1) avg  | O(1)      | O(log n)  |
| Min/Max                   | O(n)      | O(n)      | O(n)      | O(n)      | O(1)      |

### 🔄 Common Algorithm Complexities

| Algorithm                 | Time Complexity | Space Complexity | Use Case                    |
| ------------------------- | --------------- | ---------------- | --------------------------- |
| Linear Search             | O(n)            | O(1)            | Unsorted data               |
| Binary Search             | O(log n)        | O(1)            | Sorted data                 |
| Merge Sort                | O(n log n)      | O(n)            | Stable sorting              |
| Quick Sort                | O(n log n) avg  | O(log n)        | In-place sorting            |
| BFS                       | O(V + E)        | O(V)            | Shortest path (unweighted)  |
| DFS                       | O(V + E)        | O(V)            | Graph traversal             |
| Dijkstra                  | O(E log V)      | O(V)            | Shortest path (weighted)    |
| Union-Find                | O(α(n))         | O(n)            | Connected components        |

### 🎨 Python Tricks Summary

```python
# Useful one-liners
max_element = max(arr)
min_element = min(arr)
sum_elements = sum(arr)
sorted_arr = sorted(arr)
reversed_arr = arr[::-1]

# Multiple assignment
a, b = b, a  # Swap
x, y, z = 1, 2, 3  # Multiple assignment

# List comprehensions
squares = [x*x for x in range(10)]
evens = [x for x in arr if x % 2 == 0]
matrix_transpose = list(zip(*matrix))

# String operations
digits = ''.join(filter(str.isdigit, string))
letters = ''.join(filter(str.isalpha, string))

# Dictionary tricks
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1

# Or better
from collections import Counter
freq = Counter(string)

# Set operations
intersection = set1 & set2
union = set1 | set2
difference = set1 - set2
```

---

## 🏆 Contest-Specific Tips

### 🎪 Codeforces
- Use PyPy3 for better performance
- Watch out for integer overflow (rare in Python)
- Read problem constraints carefully
- Practice implementation speed

### 🎭 AtCoder
- Often requires mathematical insight
- Japanese contest style problems
- Good for learning advanced algorithms
- Strong mathematical foundation needed

### 🌟 General CP Advice
1. **Read the problem twice** before coding
2. **Think about edge cases** early
3. **Use meaningful variable names** for debugging
4. **Test with sample inputs** before submission
5. **Consider time/space complexity** before implementing

---

## 📚 Further Learning Resources

### 📖 Books
- **"Competitive Programming 4"** by Steven Halim
- **"Guide to Competitive Programming"** by Antti Laaksonen
- **"Algorithm Design Manual"** by Steven Skiena

### 🌐 Online Platforms
- **Codeforces**: [codeforces.com](https://codeforces.com)
- **AtCoder**: [atcoder.jp](https://atcoder.jp)
- **LeetCode**: [leetcode.com](https://leetcode.com)
- **HackerRank**: [hackerrank.com](https://hackerrank.com)

### 📺 YouTube Channels
- **Errichto**: Advanced CP concepts
- **William Lin**: Contest solutions
- **SecondThread**: Algorithm explanations

---

*Made with ❤️ for competitive programmers. Happy coding! 🚀*

---

**Last Updated**: September 2025  
**Python Version**: 3.8+  
**Tested on**: Codeforces, AtCoder, LeetCodee(n)]
adj_matrix[u][v] = 1  # or weight
```

### 🔍 Graph Algorithms

```python
# BFS Template
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        # Process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS Template
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Dijkstra's Algorithm
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

# Union-Find (Disjoint Set Union)
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
```e Python equivalent of C++ STL*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![CP](https://img.shields.io/badge/Competitive-Programming-orange.svg)](https://codeforces.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents
- [🏗️ Data Structures](#-data-structures)
- [🔄 Algorithms](#-algorithms)
- [🧮 Math & Number Theory](#-math--number-theory)
- [📊 Graph Utilities](#-graph-utilities)
- [⚡ Performance Tips](#-performance-tips)
- [🔧 Advanced Techniques](#-advanced-techniques)
- [📝 Code Templates](#-code-templates)
- [🎯 Quick Reference](#-quick-reference)

---

## 🏗️ Data Structures

### 📦 Core Containers (Python vs C++ STL)

| C++ STL          | Python Equivalent             | Time Complexity | Notes                                                                            |
| ---------------- | ----------------------------- | --------------- | -------------------------------------------------------------------------------- |
| `vector<T>`      | `list`                        | O(1) append     | Dynamic arrays, very versatile. Use for stacks too.                            |
| `set<T>`         | `set`                         | O(log n) avg    | Ordered set, maintains sorted order.                                           |
| `unordered_set<T>`| `set`                        | O(1) avg        | Python sets are hash-based by default.                                         |
| `map<K,V>`       | `dict`                        | O(log n) → O(1) | Key-value store. Python dicts maintain insertion order (3.7+).                |
| `unordered_map<K,V>`| `dict`                     | O(1) avg        | Hash-based dictionary with average O(1) operations.                           |
| `stack<T>`       | `list` or `collections.deque` | O(1)           | Use `list.append()` and `list.pop()` for stack operations.                    |
| `queue<T>`       | `collections.deque`           | O(1)           | Double-ended queue with O(1) append/pop from both ends.                       |
| `priority_queue<T>`| `heapq`                     | O(log n)        | Min-heap by default. For max-heap, push negative values.                      |
| `deque<T>`       | `collections.deque`           | O(1)           | Fast O(1) insertions/removals from both ends.                                 |

### 📊 Advanced Containers

| Container                | Use Case                      | Example                                    |
| ------------------------ | ----------------------------- | ------------------------------------------ |
| `collections.Counter`    | Frequency counting            | `Counter(['a','b','a']) → {'a':2, 'b':1}` |
| `collections.defaultdict`| Auto-initialize missing keys | `defaultdict(list)` for adjacency lists   |
| `collections.OrderedDict`| Maintain insertion order     | LRU cache implementation                   |
| `collections.ChainMap`   | Multiple dict lookup          | Merging configurations                     |
| `collections.namedtuple` | Lightweight objects           | `Point = namedtuple('Point', ['x', 'y'])`  |

---

## 🔄 Algorithms

### 🔍 Search & Sort Operations

| Functionality             | Python Equivalent                                  | Time Complexity | Example Usage                           |
| ------------------------- | -------------------------------------------------- | --------------- | --------------------------------------- |
| Sorting                   | `sorted()`, `list.sort()`                          | O(n log n)     | `sorted(arr, key=lambda x: x[1])`      |
| Binary Search             | `bisect.bisect_left()`, `bisect.bisect_right()`    | O(log n)       | `bisect_left(arr, target)`              |
| Lower Bound               | `bisect.bisect_left()`                             | O(log n)       | First position ≥ target                |
| Upper Bound               | `bisect.bisect_right()`                            | O(log n)       | First position > target                |
| Custom Sorting            | `sorted(arr, key=...)`                             | O(n log n)     | `sorted(points, key=lambda p: p[0])`   |

### 🔄 Iteration & Generation

| Functionality             | Python Equivalent                                  | Use Case                                   |
| ------------------------- | -------------------------------------------------- | ------------------------------------------ |
| Permutations              | `itertools.permutations(arr, r)`                  | All permutations of r elements            |
| Combinations              | `itertools.combinations(arr, r)`                  | All combinations of r elements            |
| Combinations w/ Replacement| `itertools.combinations_with_replacement(arr, r)` | Combinations allowing repetition          |
| Cartesian Product        | `itertools.product(arr1, arr2)`                   | All pairs between two arrays              |
| Accumulate / Prefix Sums  | `itertools.accumulate(arr)`                       | Running totals: `[1,2,3] → [1,3,6]`      |
| Group By                  | `itertools.groupby(sorted_arr)`                   | Group consecutive equal elements          |
| Cycle                     | `itertools.cycle(arr)`                            | Infinite repetition of sequence           |
| Count                     | `itertools.count(start, step)`                    | Infinite arithmetic sequence              |

---

## 🧮 Math & Number Theory

### 🔢 Basic Math Functions

| Function                  | Python Implementation                              | Use Case                                   |
| ------------------------- | -------------------------------------------------- | ------------------------------------------ |
| GCD                      | `math.gcd(a, b)`                                  | Greatest Common Divisor                    |
| LCM                      | `math.lcm(a, b)` (Python 3.9+)                   | Least Common Multiple                      |
| Power with Modulo        | `pow(base, exp, mod)`                             | Fast modular exponentiation               |
| Modular Inverse          | `pow(a, -1, mod)` (Python 3.8+)                  | Multiplicative inverse                     |
| Integer Square Root      | `math.isqrt(n)` (Python 3.8+)                    | Floor of square root                       |
| Product of Elements      | `math.prod(iterable)` (Python 3.8+)              | Product of all elements                    |
| Combinations             | `math.comb(n, k)` (Python 3.8+)                  | nCk combinatorics                          |
| Permutations             | `math.perm(n, k)` (Python 3.8+)                  | nPk permutations                           |

### 📐 Advanced Math

```python
import math
from fractions import Fraction
from decimal import Decimal, getcontext

# High precision arithmetic
getcontext().prec = 50  # Set precision for Decimal
pi_precise = Decimal('3.141592653589793238462643383279502884197')

# Exact fractions
frac = Fraction(1, 3) + Fraction(2, 3)  # Result: Fraction(1, 1)

# Euclidean distance
distance = math.hypot(x2-x1, y2-y1)
# or for multiple dimensions
distance = math.dist([x1, y1], [x2, y2])
```

### 📊 Number Theory Utilities

```python
# Sieve of Eratosthenes
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

# Fast prime check
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

# Extended GCD
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
```

✅ Graphs and Other Utilities

- `collections.defaultdict(list)` — for adjacency lists
- `heapq` — for Dijkstra, A*, Prim’s, etc.
- `queue.Queue or deque` — for BFS
- `set` — for visited nodes / fast lookups

---

## ⚡ Performance Tips

### 🚀 Fast I/O Operations

```python
import sys

# Fast input reading
input = sys.stdin.readline

# Read single integers
n = int(input())

# Read multiple integers
a, b, c = map(int, input().split())

# Read array of integers
arr = list(map(int, input().split()))

# Read 2D grid
grid = []
for _ in range(n):
    grid.append(list(input().strip()))

# Alternative grid reading
grid = [list(input().strip()) for _ in range(n)]

# Fast output (when needed)
print(*result, sep='\n')  # Print each element on new line
```

### ⚙️ Performance Optimizations

```python
# Increase recursion limit
import sys
sys.setrecursionlimit(10**6)

# Use PyPy for better performance
# Run with: pypy3 solution.py

# Efficient string operations
result = []
for item in items:
    result.append(str(item))
output = ''.join(result)  # Better than concatenation

# Use local variables in loops
def solve():
    local_append = result.append  # Cache method lookup
    for item in large_list:
        local_append(process(item))
```

### 🎯 Python-Specific Optimizations

```python
# Use enumerate instead of range(len())
for i, value in enumerate(arr):
    # Better than: for i in range(len(arr)): value = arr[i]

# Use zip for parallel iteration
for a, b in zip(list1, list2):
    # Better than: for i in range(len(list1)): a, b = list1[i], list2[i]

# Use any() and all() for boolean checks
if any(x > 0 for x in arr):  # Check if any positive
if all(x > 0 for x in arr):  # Check if all positive

# Efficient counting
from collections import Counter
count = Counter(arr)  # Better than manual counting

# Use bisect for sorted insertions
import bisect
bisect.insort(sorted_list, new_item)
```

✅ Summary
Python’s standard library is very CP-friendly, and while it's not called "STL", you have a rich toolkit at your disposal:
**Core Modules to Know:**
- `collections`
- `itertools`
- `heapq`
- `bisect`
- `math`

Yes — beyond the basics of Python’s "STL-equivalent" features, there are **more advanced tools, techniques, and modules** you should be aware of, especially for high-level or edge-case-heavy competitive programming. Let’s go beyond the usual and unlock some **lesser-known yet powerful features** that many competitive programmers miss.

---

## 🔍 Extended Toolkit for Competitive Programming in Python

---

### 1. **`collections` (Advanced Usage)**

* **`OrderedDict`**
  Maintains insertion order (though since Python 3.7+, `dict` does this too).

* **`ChainMap`**
  Useful for merging multiple dictionaries:

  ```python
  from collections import ChainMap
  merged = ChainMap(dict1, dict2)
  ```

* **`namedtuple`**
  A lightweight object for better readable tuple-like structures.

  ```python
  from collections import namedtuple
  Point = namedtuple('Point', ['x', 'y'])
  p = Point(1, 2)
  ```

---

### 2. **`functools`**

* **`lru_cache`**
  Built-in memoization decorator — fantastic for DP with recursion.

  ```python
  from functools import lru_cache

  @lru_cache(None)
  def fib(n):
      if n < 2: return n
      return fib(n-1) + fib(n-2)
  ```

* **`cmp_to_key`**
  For custom complex sorting using a comparator function (like C++'s `sort` with a comparator).

---

### 3. **`itertools` (Advanced Patterns)**

* **`product`, `permutations`, `combinations`, `combinations_with_replacement`**

* **`groupby()`**
  Similar to SQL GROUP BY. Requires sorted input.

  ```python
  from itertools import groupby
  data = sorted(['a', 'a', 'b', 'b', 'b', 'c'])
  for key, group in groupby(data):
      print(key, list(group))
  ```

* **`cycle()`, `count()`, `repeat()`** — infinite iterators

---

### 4. **`bisect` (Deep Dive)**

Used for binary search in sorted lists:

* `bisect_left(a, x)` → first position where `x` could be inserted.
* `bisect_right(a, x)` → position after last occurrence of `x`.

Also works for finding:

* Upper/lower bounds
* Position in prefix sums
* Coordinate compression

---

### 5. **`heapq` Tricks**

Python’s `heapq` is **min-heap only**. But for **max-heap**, do:

```python
import heapq
max_heap = []
heapq.heappush(max_heap, -val)  # push negative
max_val = -heapq.heappop(max_heap)
```

Also:

* `heapify()` — convert a list into a heap in O(n)
* Supports heap-based multi-source Dijkstra, Prim’s algorithm

---

### 6. **`array` Module**

Useful for space-efficient storage of large numeric arrays:

```python
from array import array
a = array('i', [1, 2, 3])  # 'i' is typecode for integers
```

Not often used in CP unless strict memory is required.

---

### 7. **`math` (Advanced)**

* `math.isqrt(n)` — integer square root (Python 3.8+)
* `math.prod(iterable)` — product of elements (Python 3.8+)
* `math.comb(n, k)` and `math.perm(n, k)` — combinatorics (Python 3.8+)
* `math.dist()` — Euclidean distance
* `math.hypot(x, y)` — √(x² + y²) (Euclidean norm)

---

### 8. **`decimal` and `fractions`**

Use when:

* High-precision arithmetic is needed.
* Floating-point inaccuracies can cause WA.

```python
from decimal import Decimal
from fractions import Fraction
```

---

### 9. **Big Integer Arithmetic**

* Python supports **arbitrary-precision integers** by default:

  ```python
  a = 10**1000  # perfectly valid
  ```

---

### 10. **Useful CP Snippets / Idioms**

* **Fast Input:**

  ```python
  import sys
  input = sys.stdin.readline
  ```

* **Read space-separated integers:**

  ```python
  a, b = map(int, input().split())
  arr = list(map(int, input().split()))
  ```

* **Grid input:**

  ```python
  grid = [list(input().strip()) for _ in range(n)]
  ```

* **Modular inverse:**

  ```python
  pow(a, -1, mod)  # Since Python 3.8
  ```

---

## 🧠 Pro CP Tips

* **Use `PyPy` for better performance**, especially for heavy loops or recursion.

* Know how to **override recursion limit** safely:

  ```python
  import sys
  sys.setrecursionlimit(10**6)
  ```

* Build templates: input handling, graph boilerplate, common functions like GCD, DFS, BFS, etc.

---

## 📚 Optional External Libraries (if allowed)

Usually not allowed in most contests like Codeforces or AtCoder, but helpful in hackathons or custom contests:

* **NumPy**: fast numerical computations.
* **SymPy**: symbolic math (like solving equations).
* **NetworkX**: graph algorithms (but slow for CP).

---

## ⚡ Final Words

Python is a **powerful CP language** if you:

* Master the standard library (like the above).
* Write clean, optimized code.
* Avoid Python’s few performance traps (nested loops, slow I/O, excessive object creation).

---