# Python Competitive Programming Optimization Guide

This directory contains a comprehensive collection of Python optimization techniques and algorithms specifically designed for competitive programming. Each file focuses on one specific topic with practical examples and optimizations.

## 📁 File Structure

### Core Optimizations

**0001_fast_input_output.py** - Input/Output Optimization
- Fast input using `sys.stdin.readline`
- Batch output techniques
- Multiple test case handling
- Bulk input reading strategies

**0002_optimized_data_structures.py** - Data Structure Choices
- Set vs List for membership testing
- Deque vs List for queue operations
- Heap operations with `heapq`
- Binary search with `bisect`
- Counter and defaultdict usage

**0003_math_and_bit_tricks.py** - Mathematical Optimizations
- Fast power operations and modular arithmetic
- Bit manipulation techniques
- Number theory functions (GCD, LCM, primes)
- Combinatorics with modular arithmetic
- Optimization tips for mathematical operations

**0004_loop_optimizations.py** - Loop and Iteration Optimizations
- Avoiding attribute lookups in loops
- List comprehensions vs manual loops
- Nested loop optimizations
- Memory-efficient iterations with generators
- Performance comparison examples

**0005_string_optimizations.py** - String Operations
- Efficient string concatenation with `join()`
- String searching and pattern matching
- String hashing and rolling hash
- Common string algorithms (KMP, LCS)
- String manipulation best practices

**0006_memory_optimizations.py** - Memory Management
- Garbage collection control
- Memory-efficient data structures (`array`, `bytearray`)
- Generator usage for memory efficiency
- String interning and memory profiling
- Practical memory optimization examples

### Advanced Algorithms

**0007_advanced_data_structures.py** - Advanced Data Structures
- Segment Tree for range queries
- Fenwick Tree (Binary Indexed Tree)
- Union-Find (Disjoint Set Union)
- Trie (Prefix Tree)
- LRU Cache implementation
- Sparse Table for RMQ
- Monotonic Deque for sliding window problems

**0008_dynamic_programming_optimizations.py** - DP Optimizations
- Memoization vs Tabulation comparison
- Space-optimized DP (1D arrays)
- Advanced DP patterns (Digit DP, Bitmask DP)
- State compression techniques
- DP optimization strategies

**0009_graph_algorithms.py** - Graph Algorithms
- Efficient graph representations
- BFS variations (multi-source, 0-1 BFS)
- DFS applications (topological sort, cycle detection)
- Shortest path algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall)
- Minimum Spanning Tree (Kruskal's, Prim's)
- Strongly Connected Components (Tarjan's, Kosaraju's)

**0010_python_specific_tricks.py** - Python-Specific Optimizations
- Advanced built-in function usage
- Itertools power techniques
- Functional programming patterns
- Performance optimization tricks
- Complete CP templates and common patterns

## 🚀 Quick Start Guide

### Essential Setup for CP

```python
import sys
import gc
from collections import defaultdict, deque, Counter
from functools import lru_cache
import heapq
import bisect
import math

# Fast I/O setup
input = sys.stdin.readline
gc.disable()

# Constants
MOD = 10**9 + 7
INF = float('inf')
```

### Performance Hierarchy (Fastest to Slowest)

1. **Built-in functions** - `sum()`, `min()`, `max()`, `sorted()`
2. **List comprehensions** - `[x*2 for x in arr]`
3. **Generator expressions** - `(x*2 for x in arr)`
4. **Map/filter** - `list(map(lambda x: x*2, arr))`
5. **Manual loops with cached methods** - `append = list.append`
6. **Regular manual loops** - `for i in range(len(arr))`

### Memory Efficiency Tips

- Use `array.array()` instead of lists for numeric data
- Use generators for large sequences
- Use `__slots__` in classes
- Disable garbage collection during intensive computations
- Use `collections.deque` for queue operations

### Common CP Patterns

#### Fast Input/Output
```python
# Fast input
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# Batch output
results = []
for i in range(n):
    results.append(str(process(arr[i])))
print('\n'.join(results))
```

#### Binary Search Template
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#### Graph BFS Template
```python
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
```

## 🎯 Problem-Specific Optimizations

### For Array Problems
- Use prefix sums for range queries
- Use two pointers for sorted arrays
- Use monotonic stack/deque for next greater/smaller element

### For String Problems
- Use rolling hash for substring comparison
- Use KMP for pattern matching
- Use Trie for prefix operations

### For Graph Problems
- Use adjacency lists for sparse graphs
- Use BFS for shortest path in unweighted graphs
- Use Union-Find for connectivity queries

### For Mathematical Problems
- Use modular arithmetic to prevent overflow
- Precompute factorials and powers
- Use sieve for prime-related problems

## 📊 Time Complexity Guidelines

### Safe for Python in CP:
- **n ≤ 10^6**: O(n) or O(n log n) algorithms
- **n ≤ 10^5**: O(n log n) algorithms
- **n ≤ 10^4**: O(n²) algorithms (with optimizations)
- **n ≤ 10^3**: O(n³) algorithms

### Risky but possible:
- **n ≤ 2×10^6**: O(n) algorithms with heavy optimizations
- **n ≤ 5×10^5**: O(n log n) with fast I/O and optimizations

## 🔧 Debugging and Testing

### Performance Testing
```python
import time

def time_function(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")
    return result
```

### Memory Usage Checking
```python
import sys

def check_memory(obj):
    return sys.getsizeof(obj)
```

## 📚 Additional Resources

### When to Use Each Data Structure:
- **List**: Random access, append operations
- **Set**: Membership testing, unique elements
- **Dict**: Key-value mapping, counting
- **Deque**: Queue/stack operations at both ends
- **Heap**: Priority queue operations
- **Bisect**: Binary search on sorted data

### Python vs C++ in CP:
- **Python advantages**: Easier implementation, rich built-ins, dynamic typing
- **Python disadvantages**: Slower execution, larger memory usage
- **Best for**: Problems with complex logic, string manipulation, mathematical computations

## 🎖️ Best Practices Summary

1. **Always** use fast I/O setup for competitive programming
2. **Profile** your code to identify bottlenecks
3. **Choose** the right data structure for the problem
4. **Optimize** the most critical parts first
5. **Practice** with time constraints to build muscle memory
6. **Know** when to switch to C++ for very tight time limits

---

*This guide covers the essential optimizations needed to use Python effectively in competitive programming. Each file contains detailed implementations and examples that can be directly used or adapted for contest problems.*
