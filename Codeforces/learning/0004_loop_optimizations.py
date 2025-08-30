"""
Loop and Iteration Optimizations
===============================

Optimize loops for maximum performance in competitive programming.
Avoid common bottlenecks and use Python's strengths.
"""

import sys

def avoid_attribute_lookups_in_loops():
    """
    Cache method references to avoid repeated attribute lookups
    """
    
    # BAD: Repeated attribute lookup in loop
    def slow_list_building(n):
        result = []
        for i in range(n):
            result.append(i * i)  # 'append' lookup every iteration
        return result
    
    # GOOD: Cache the method reference
    def fast_list_building(n):
        result = []
        append = result.append  # Cache the method
        for i in range(n):
            append(i * i)  # Direct function call
        return result
    
    # Even better: Use list comprehension (C-optimized)
    def fastest_list_building(n):
        return [i * i for i in range(n)]
    
    return fast_list_building, fastest_list_building

def range_vs_xrange_and_enumerate():
    """
    Efficient iteration patterns
    """
    
    # Use range (it's already optimized in Python 3)
    def efficient_range_usage(n):
        total = 0
        for i in range(n):
            total += i
        return total
    
    # Avoid enumerate in hot loops - track manually
    def manual_indexing(arr):
        result = []
        for i in range(len(arr)):
            result.append(arr[i] * i)
        return result
    
    # Sometimes enumerate is cleaner (use when performance isn't critical)
    def with_enumerate(arr):
        return [val * i for i, val in enumerate(arr)]
    
    return efficient_range_usage, manual_indexing

def list_comprehensions_vs_loops():
    """
    List comprehensions are often faster than manual loops
    """
    
    # Manual loop
    def manual_loop(n):
        result = []
        for i in range(n):
            if i % 2 == 0:
                result.append(i * 2)
        return result
    
    # List comprehension (faster)
    def list_comp(n):
        return [i * 2 for i in range(n) if i % 2 == 0]
    
    # Generator expression for memory efficiency
    def generator_exp(n):
        return (i * 2 for i in range(n) if i % 2 == 0)
    
    # Map and filter for functional approach
    def map_filter(n):
        return list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, range(n))))
    
    return list_comp, generator_exp

def nested_loop_optimizations():
    """
    Optimize nested loops and avoid unnecessary operations
    """
    
    # BAD: Redundant calculations in inner loop
    def slow_nested(matrix):
        n, m = len(matrix), len(matrix[0])
        result = 0
        for i in range(n):
            for j in range(m):
                result += matrix[i][j] * (i + j)
        return result
    
    # GOOD: Precompute what you can
    def fast_nested(matrix):
        n, m = len(matrix), len(matrix[0])
        result = 0
        for i in range(n):
            row = matrix[i]  # Cache row reference
            for j in range(m):
                result += row[j] * (i + j)
        return result
    
    # Even better: Flatten when possible
    def flattened_approach(matrix):
        result = 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                result += val * (i + j)
        return result
    
    return fast_nested, flattened_approach

def loop_unrolling_and_batching():
    """
    Sometimes manual loop unrolling helps
    """
    
    # Process multiple elements at once
    def batch_processing(arr):
        result = 0
        n = len(arr)
        
        # Process 4 elements at a time
        for i in range(0, n - 3, 4):
            result += arr[i] + arr[i+1] + arr[i+2] + arr[i+3]
        
        # Handle remaining elements
        for i in range(n - (n % 4), n):
            result += arr[i]
        
        return result
    
    # Or use sum() which is C-optimized
    def optimized_sum(arr):
        return sum(arr)
    
    return batch_processing, optimized_sum

def avoid_function_calls_in_loops():
    """
    Minimize function call overhead in hot loops
    """
    
    # BAD: Function call in loop
    def slow_with_function_calls(arr):
        def square(x):
            return x * x
        
        result = []
        for x in arr:
            result.append(square(x))  # Function call overhead
        return result
    
    # GOOD: Inline the operation
    def fast_inline(arr):
        result = []
        for x in arr:
            result.append(x * x)  # Direct operation
        return result
    
    # Best: Use list comprehension or map
    def fastest_builtin(arr):
        return [x * x for x in arr]
    
    return fast_inline, fastest_builtin

def memory_efficient_iterations():
    """
    Use generators and iterators for memory efficiency
    """
    
    # Generator for large sequences
    def number_generator(n):
        for i in range(n):
            yield i * i
    
    # Iterator for processing large files
    def process_large_input():
        input_iter = iter(sys.stdin.readline, '')
        for line in input_iter:
            yield line.strip()
    
    # Use itertools for complex iterations
    import itertools
    
    def itertools_examples():
        # Infinite counter
        counter = itertools.count(1, 2)  # 1, 3, 5, 7, ...
        
        # Combinations and permutations
        from itertools import combinations, permutations
        
        arr = [1, 2, 3, 4]
        combs = list(combinations(arr, 2))
        perms = list(permutations(arr, 2))
        
        return combs, perms
    
    return number_generator, itertools_examples

def loop_optimization_checklist():
    """
    Checklist for optimizing loops
    """
    checklist = [
        "1. Cache method references (append = list.append)",
        "2. Use list comprehensions when possible",
        "3. Avoid enumerate in hot loops - track index manually",
        "4. Precompute values outside loops",
        "5. Use range() instead of creating lists",
        "6. Cache repeated calculations",
        "7. Use built-in functions (sum, min, max, any, all)",
        "8. Consider generators for memory efficiency",
        "9. Minimize function calls in loops",
        "10. Use itertools for complex iterations",
        "11. Flatten nested structures when possible",
        "12. Batch process when applicable"
    ]
    return checklist

def timing_comparison_example():
    """
    Example showing performance differences
    """
    import time
    
    n = 100000
    
    # Method 1: Manual loop with append
    start = time.time()
    result1 = []
    for i in range(n):
        result1.append(i * 2)
    time1 = time.time() - start
    
    # Method 2: Cached append
    start = time.time()
    result2 = []
    append = result2.append
    for i in range(n):
        append(i * 2)
    time2 = time.time() - start
    
    # Method 3: List comprehension
    start = time.time()
    result3 = [i * 2 for i in range(n)]
    time3 = time.time() - start
    
    return {
        'manual_loop': time1,
        'cached_append': time2,
        'list_comprehension': time3,
        'speedup_cached': time1 / time2 if time2 > 0 else float('inf'),
        'speedup_listcomp': time1 / time3 if time3 > 0 else float('inf')
    }

if __name__ == "__main__":
    print("Loop Optimization Techniques")
    
    # Show checklist
    checklist = loop_optimization_checklist()
    print("Optimization Checklist:")
    for item in checklist:
        print(item)
    
    print("\n" + "="*50)
    
    # Demonstrate optimizations
    fast_build, fastest_build = avoid_attribute_lookups_in_loops()
    result1 = fast_build(1000)
    result2 = fastest_build(1000)
    print(f"Fast build first 10: {result1[:10]}")
    print(f"Fastest build first 10: {result2[:10]}")
    
    # Show itertools examples
    _, itertools_func = memory_efficient_iterations()
    combs, perms = itertools_func()
    print(f"Combinations: {combs[:5]}")
    print(f"Permutations: {perms[:5]}")
    
    # Timing comparison (uncomment to run)
    # timing_results = timing_comparison_example()
    # print(f"Timing results: {timing_results}")
