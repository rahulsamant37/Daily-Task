"""
Optimized Data Structures for Competitive Programming
====================================================

Python's built-in data structures are C-optimized and faster than manual implementations.
Choose the right data structure for O(1) operations.
"""

import heapq
from collections import deque, defaultdict, Counter
import bisect

def set_vs_list_membership():
    """
    Demonstrate why sets are faster for membership testing
    """
    # BAD: O(n) membership test
    large_list = list(range(10000))
    
    def slow_check(x):
        return x in large_list  # O(n) operation
    
    # GOOD: O(1) average membership test
    large_set = set(range(10000))
    
    def fast_check(x):
        return x in large_set  # O(1) average operation
    
    return fast_check, slow_check

def deque_vs_list_operations():
    """
    Deque for O(1) operations at both ends
    """
    # BAD: list.pop(0) is O(n)
    def slow_queue_ops():
        queue = [1, 2, 3, 4, 5]
        while queue:
            item = queue.pop(0)  # O(n) operation!
            print(item)
    
    # GOOD: deque.popleft() is O(1)
    def fast_queue_ops():
        queue = deque([1, 2, 3, 4, 5])
        while queue:
            item = queue.popleft()  # O(1) operation
            print(item)
    
    return fast_queue_ops

def heap_operations():
    """
    Using heapq for priority queue operations
    """
    # Min heap (default)
    min_heap = []
    heapq.heappush(min_heap, 5)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 3)
    
    smallest = heapq.heappop(min_heap)  # Gets 1
    
    # Max heap (negate values)
    max_heap = []
    values = [5, 1, 3, 9, 2]
    for val in values:
        heapq.heappush(max_heap, -val)
    
    largest = -heapq.heappop(max_heap)  # Gets 9
    
    # Heap from list
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    heapq.heapify(arr)  # O(n) operation
    
    return smallest, largest

def binary_search_with_bisect():
    """
    Use bisect for fast binary search operations
    """
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    # Find insertion point
    pos = bisect.bisect_left(sorted_arr, 6)  # Returns 3
    
    # Insert and maintain sorted order
    bisect.insort(sorted_arr, 6)
    
    # Find if element exists
    def binary_search(arr, x):
        pos = bisect.bisect_left(arr, x)
        return pos < len(arr) and arr[pos] == x
    
    return pos, sorted_arr

def counter_for_frequency():
    """
    Counter for frequency counting operations
    """
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    
    # Count frequencies
    freq = Counter(arr)
    
    # Most common elements
    most_common = freq.most_common(2)  # [(4, 4), (3, 3)]
    
    # Update counts
    freq.update([1, 1, 2])
    
    return freq, most_common

def defaultdict_usage():
    """
    defaultdict to avoid KeyError and initialize values
    """
    # For adjacency lists
    graph = defaultdict(list)
    graph[1].append(2)
    graph[1].append(3)
    
    # For counting
    count = defaultdict(int)
    for char in "hello":
        count[char] += 1
    
    # For grouping
    groups = defaultdict(list)
    words = ["cat", "dog", "rat", "log"]
    for word in words:
        groups[len(word)].append(word)
    
    return dict(graph), dict(count), dict(groups)

def optimized_data_structure_choices():
    """
    Summary of when to use which data structure
    """
    choices = {
        "Fast membership testing": "set() - O(1) average",
        "Queue operations": "deque() - O(1) at both ends",
        "Priority queue": "heapq - O(log n) push/pop",
        "Binary search": "bisect - O(log n) search",
        "Frequency counting": "Counter() - optimized counting",
        "Default values": "defaultdict() - avoid KeyError",
        "Ordered data": "list with bisect for insertion",
        "Range queries": "Consider segment tree/fenwick tree"
    }
    
    return choices

if __name__ == "__main__":
    print("Optimized Data Structures for CP")
    
    # Demonstrate heap operations
    smallest, largest = heap_operations()
    print(f"Smallest: {smallest}, Largest: {largest}")
    
    # Demonstrate binary search
    pos, arr = binary_search_with_bisect()
    print(f"Position: {pos}, Array: {arr}")
    
    # Demonstrate Counter
    freq, common = counter_for_frequency()
    print(f"Frequencies: {freq}")
    print(f"Most common: {common}")
    
    # Show choices
    choices = optimized_data_structure_choices()
    for use_case, recommendation in choices.items():
        print(f"{use_case}: {recommendation}")
