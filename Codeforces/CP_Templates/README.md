# Python Competitive Programming Templates

This directory contains Python implementations of all the C++ competitive programming templates, converted with the same approach and functionality.

## Directory Structure

### Template Stuff
- `Template.py` - Main competitive programming template with utilities
- `Int_128.py` - Large number handling (Python's built-in arbitrary precision integers)

### Number Theory
- `MillerRabinDeterministic.py` - Deterministic primality testing

### Range Queries
- `Segment_tree.py` - Segment tree with point updates and range queries
- `Lazy_SGT.py` - Lazy propagation segment tree for range updates
- `Sparse_Table.py` - Sparse table for idempotent and general range queries
- `Mo_algo.py` - Mo's algorithm for offline query processing

### Common Techniques
- `Fibonacci in LogN.py` - Matrix exponentiation for Fibonacci and linear recurrences
- `Distinct in Range Queries.py` - Count distinct elements in range queries

### Graph Algorithms
- `Dijkstra.py` - Single source shortest path algorithm
- `UnionFind.py` - Disjoint Set Union with optimizations
- `BellmanFord.py` - Single source shortest path with negative edge detection
- `FloydWarshall.py` - All pairs shortest path algorithm
- `Topological_sorting.py` - Topological ordering of directed acyclic graphs

### String Algorithms
- `String_Hashing.py` - Polynomial rolling hash for string matching
- `Prefix_Function.py` - KMP algorithm and prefix function applications
- `Trie.py` - Trie data structure for string operations

### Tree Algorithms
- `LCA_tree.py` - Lowest Common Ancestor with Binary Lifting

## Key Features

### Python-Specific Optimizations
- Uses Python's built-in arbitrary precision integers (no need for special 128-bit handling)
- Leverages Python data structures like `defaultdict`, `deque`, `heapq`
- Includes comprehensive error handling and edge cases
- Provides multiple implementation variants for different use cases

### Template Structure
Each template includes:
- Main algorithm implementation
- Helper functions and utilities
- Multiple variants for different problem types
- Comprehensive test functions
- Example usage and applications

### Competitive Programming Ready
- Fast I/O setup with `sys.stdin.readline`
- Common constants and utility functions
- Modular arithmetic functions
- Debug functionality for local testing

## Usage Examples

### Basic Template
```python
from Template import *

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Your solution here

if __name__ == "__main__":
    solve()
```

### Segment Tree
```python
from Segment_tree import SegmentTree, Node, Update

arr = [1, 3, 5, 7, 9]
st = SegmentTree(arr)

# Range query
result = st.make_query(1, 3)
print(result.val)

# Point update
st.make_update(2, 10)
```

### Graph Algorithms
```python
from Dijkstra import dijkstra
from UnionFind import UnionFind

# Dijkstra
graph = {0: [(1, 4), (2, 2)], 1: [(3, 5)], 2: [(3, 1)]}
distances, parents = dijkstra(graph, 0, 4)

# Union Find
uf = UnionFind(5)
uf.union(0, 1)
uf.union(2, 3)
print(uf.connected(0, 1))  # True
print(uf.num_components())  # 3
```

### String Algorithms
```python
from String_Hashing import StringHashing
from Trie import Trie

# String Hashing
hasher = StringHashing("abcabc")
print(hasher.compare_substrings(0, 2, 3, 5))  # True

# Trie
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))  # True
print(trie.get_words_with_prefix("ap"))  # ['apple', 'app']
```

## Performance Notes

- All algorithms maintain the same time complexity as C++ versions
- Python's built-in data structures are utilized for optimal performance
- Memory usage is optimized with appropriate data structure choices
- Includes both recursive and iterative implementations where applicable

## Testing

Each template includes comprehensive test functions to verify correctness:
```python
python Template.py  # Run template tests
python Segment_tree.py  # Test segment tree
python Dijkstra.py  # Test Dijkstra algorithm
```

## Additional Features

### Advanced Data Structures
- Binary Indexed Trees (Fenwick Trees)
- Heavy-Light Decomposition
- Persistent Union Find
- Binary Tries for XOR operations

### Algorithm Variants
- Multiple shortest path algorithms
- Different string matching approaches
- Various tree traversal and query methods
- Optimized implementations for specific constraints

### Utility Functions
- Graph building from edge lists
- Path reconstruction
- Coordinate compression
- Matrix operations for recurrence relations

This collection provides a complete toolkit for competitive programming in Python, maintaining the efficiency and approach of the original C++ templates while leveraging Python's strengths.
