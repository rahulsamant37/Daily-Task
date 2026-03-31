"""
Memory Optimizations and Garbage Collection
==========================================

Optimize memory usage and manage garbage collection for competitive programming.
"""

import gc
import sys
from array import array

def garbage_collection_optimization():
    """
    Manage garbage collection for performance
    """
    
    # Disable garbage collection during computation-heavy tasks
    def disable_gc_during_computation():
        gc.disable()
        
        # Your computation here
        result = sum(i*i for i in range(100000))
        
        # Re-enable if needed (usually not necessary in CP)
        # gc.enable()
        
        return result
    
    # Manual garbage collection at strategic points
    def manual_gc_control():
        # Do memory-intensive work
        large_data = [list(range(1000)) for _ in range(1000)]
        
        # Force garbage collection
        gc.collect()
        
        # Continue with computation
        result = sum(sum(row) for row in large_data)
        return result
    
    return disable_gc_during_computation, manual_gc_control

def memory_efficient_data_structures():
    """
    Use memory-efficient alternatives to standard data structures
    """
    
    # Use array instead of list for numeric data
    def use_array_vs_list():
        # Regular list (more memory overhead)
        regular_list = [i for i in range(10000)]
        
        # Array (less memory, faster for numeric operations)
        int_array = array('i', range(10000))  # 'i' for signed int
        
        # Different array types
        byte_array = array('b', range(-128, 128))  # signed char
        unsigned_int_array = array('I', range(10000))  # unsigned int
        
        return {
            'list_size': sys.getsizeof(regular_list),
            'array_size': sys.getsizeof(int_array),
            'memory_saved': sys.getsizeof(regular_list) - sys.getsizeof(int_array)
        }
    
    # Use bytearray for mutable byte sequences
    def use_bytearray():
        # For binary data or when you need mutable bytes
        data = bytearray(b"hello world")
        data[0] = ord('H')  # Modify in place
        
        # Efficient for building binary strings
        builder = bytearray()
        for i in range(256):
            builder.append(i)
        
        return data, builder
    
    # Use __slots__ in classes to reduce memory
    class RegularClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class SlottedClass:
        __slots__ = ['x', 'y']  # Reduces memory overhead
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    return use_array_vs_list, use_bytearray, RegularClass, SlottedClass

def generator_for_memory_efficiency():
    """
    Use generators to avoid storing large sequences in memory
    """
    
    # BAD: Store entire sequence in memory
    def memory_intensive_approach(n):
        squares = [i*i for i in range(n)]  # Stores all values
        total = sum(squares)
        return total
    
    # GOOD: Use generator (constant memory)
    def memory_efficient_approach(n):
        squares = (i*i for i in range(n))  # Generator expression
        total = sum(squares)
        return total
    
    # Generator function for complex logic
    def fibonacci_generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    # Generator for reading large files
    def read_large_file_efficiently(filename):
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    
    return memory_efficient_approach, fibonacci_generator

def itertools_for_memory_efficiency():
    """
    Use itertools for memory-efficient iterations
    """
    
    import itertools
    
    # Infinite sequences without memory overhead
    def itertools_examples():
        # Infinite counter
        counter = itertools.count(1, 2)  # 1, 3, 5, 7, ...
        first_10_odds = list(itertools.islice(counter, 10))
        
        # Cycle through a sequence
        colors = itertools.cycle(['red', 'green', 'blue'])
        first_10_colors = list(itertools.islice(colors, 10))
        
        # Chain multiple iterables
        chained = itertools.chain(range(3), range(5, 8))
        chained_list = list(chained)
        
        # Combinations without storing all at once
        from itertools import combinations
        
        # For large datasets, don't convert to list immediately
        def process_combinations(items, r):
            for combo in combinations(items, r):
                # Process each combination individually
                yield sum(combo)
        
        return {
            'first_10_odds': first_10_odds,
            'first_10_colors': first_10_colors,
            'chained': chained_list
        }
    
    return itertools_examples

def string_memory_optimization():
    """
    Memory-efficient string operations
    """
    
    # Use string interning for repeated strings
    def string_interning_example():
        # Python automatically interns some strings
        a = "hello"
        b = "hello"
        same_object = a is b  # Often True for string literals
        
        # Manual interning for dynamic strings
        def intern_dynamic_string(s):
            return sys.intern(s)
        
        return same_object
    
    # Use join instead of concatenation for memory efficiency
    def memory_efficient_string_building(words):
        # BAD: Creates many intermediate strings
        # result = ""
        # for word in words:
        #     result += word
        
        # GOOD: Single allocation
        result = "".join(words)
        return result
    
    # Use format strings efficiently
    def efficient_formatting():
        # f-strings are generally most efficient
        name = "Alice"
        age = 30
        
        # Efficient
        result1 = f"Hello, {name}! You are {age} years old."
        
        # Also efficient for simple cases
        result2 = "Hello, {}! You are {} years old.".format(name, age)
        
        # Less efficient for many concatenations
        result3 = "Hello, " + name + "! You are " + str(age) + " years old."
        
        return result1, result2, result3
    
    return string_interning_example, memory_efficient_string_building

def memory_profiling_techniques():
    """
    Techniques to monitor and profile memory usage
    """
    
    # Check memory usage of objects
    def check_memory_usage():
        import sys
        
        # Size of different data structures
        empty_list = []
        small_list = [1, 2, 3]
        large_list = list(range(10000))
        
        empty_dict = {}
        small_dict = {i: i*i for i in range(10)}
        
        memory_info = {
            'empty_list': sys.getsizeof(empty_list),
            'small_list': sys.getsizeof(small_list),
            'large_list': sys.getsizeof(large_list),
            'empty_dict': sys.getsizeof(empty_dict),
            'small_dict': sys.getsizeof(small_dict)
        }
        
        return memory_info
    
    # Track memory during execution
    def memory_tracking_example():
        import gc
        
        # Get current memory statistics
        stats_before = gc.get_stats()
        
        # Create some objects
        data = [list(range(1000)) for _ in range(100)]
        
        # Force garbage collection
        collected = gc.collect()
        
        stats_after = gc.get_stats()
        
        return {
            'collected_objects': collected,
            'stats_before': len(stats_before),
            'stats_after': len(stats_after)
        }
    
    return check_memory_usage, memory_tracking_example

def memory_optimization_tips():
    """
    Key memory optimization strategies
    """
    tips = [
        "1. Disable garbage collection during intensive computations",
        "2. Use array.array() instead of lists for numeric data",
        "3. Use __slots__ in classes to reduce memory overhead",
        "4. Prefer generators over lists for large sequences",
        "5. Use itertools for memory-efficient iterations",
        "6. Use bytearray for mutable byte sequences",
        "7. Use string interning for repeated strings",
        "8. Prefer ''.join() over += for string concatenation",
        "9. Use tuples instead of lists when immutability is acceptable",
        "10. Delete large objects explicitly with 'del' when done",
        "11. Use sys.getsizeof() to check object memory usage",
        "12. Consider using numpy arrays for large numeric datasets (if allowed)"
    ]
    return tips

def practical_memory_optimization():
    """
    Practical example combining multiple optimization techniques
    """
    
    def optimized_large_computation(n):
        # Disable GC during computation
        gc.disable()
        
        # Use generator instead of list
        def square_generator(limit):
            for i in range(limit):
                yield i * i
        
        # Use array for storing results if needed
        results = array('L', [])  # unsigned long array
        
        # Process in chunks to avoid memory buildup
        chunk_size = 10000
        total = 0
        
        for i in range(0, n, chunk_size):
            chunk_end = min(i + chunk_size, n)
            chunk_sum = sum(x for x in square_generator(chunk_end - i))
            total += chunk_sum
        
        # Re-enable GC if needed (optional in CP)
        # gc.enable()
        
        return total
    
    return optimized_large_computation

if __name__ == "__main__":
    print("Memory Optimization Techniques")
    
    # Test array vs list memory usage
    array_func, _, _, _ = memory_efficient_data_structures()
    memory_comparison = array_func()
    print(f"Memory comparison: {memory_comparison}")
    
    # Test memory usage checking
    check_mem, _ = memory_profiling_techniques()
    memory_info = check_mem()
    print(f"Memory usage info: {memory_info}")
    
    # Test itertools
    itertools_func = itertools_for_memory_efficiency()
    itertools_results = itertools_func()
    print(f"Itertools results: {itertools_results}")
    
    # Show optimization tips
    tips = memory_optimization_tips()
    print("\nMemory Optimization Tips:")
    for tip in tips:
        print(tip)
    
    # Test optimized computation
    optimized_comp = practical_memory_optimization()
    result = optimized_comp(1000)
    print(f"\nOptimized computation result: {result}")
    
    print(f"\nGarbage collection disabled: {not gc.isenabled()}")
