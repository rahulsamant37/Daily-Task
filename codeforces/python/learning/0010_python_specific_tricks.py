"""
Python-Specific Competitive Programming Tricks
==============================================

Advanced Python tricks and optimizations specifically for competitive programming.
"""

import sys
import gc
import itertools
from functools import lru_cache, reduce
from collections import defaultdict, Counter, deque
import bisect
import heapq

def python_cp_setup():
    """
    Essential Python setup for competitive programming
    """
    
    def setup_fast_io():
        """
        Setup fast I/O and disable garbage collection
        """
        # Fast input
        input = sys.stdin.readline
        
        # Disable garbage collection for performance
        gc.disable()
        
        # Increase recursion limit if needed
        sys.setrecursionlimit(10**6)
        
        return input
    
    def template_setup():
        """
        Complete CP template setup
        """
        import sys
        from collections import defaultdict, deque, Counter
        from functools import lru_cache
        import heapq
        import bisect
        import math
        
        # Fast I/O
        input = sys.stdin.readline
        gc.disable()
        
        # Common constants
        MOD = 10**9 + 7
        INF = float('inf')
        
        return input, MOD, INF
    
    return setup_fast_io, template_setup

def advanced_builtin_tricks():
    """
    Advanced tricks using Python built-ins
    """
    
    # Using any() and all() for complex conditions
    def efficient_condition_checking():
        arr = [1, 2, 3, 4, 5]
        
        # Check if any element is even
        has_even = any(x % 2 == 0 for x in arr)
        
        # Check if all elements are positive
        all_positive = all(x > 0 for x in arr)
        
        # Check if array is sorted
        is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
        
        return has_even, all_positive, is_sorted
    
    # Using enumerate smartly
    def enumerate_tricks():
        arr = ['a', 'b', 'c', 'd']
        
        # Get index of specific element
        indices = [i for i, x in enumerate(arr) if x == 'b']
        
        # Enumerate with custom start
        for i, val in enumerate(arr, 1):  # Start from 1
            pass
        
        # Enumerate multiple lists
        arr2 = [1, 2, 3, 4]
        for i, (char, num) in enumerate(zip(arr, arr2)):
            pass
        
        return indices
    
    # Using zip and zip(*) (transpose)
    def zip_tricks():
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        # Transpose matrix
        transposed = list(zip(*matrix))
        
        # Pair adjacent elements
        arr = [1, 2, 3, 4, 5]
        pairs = list(zip(arr, arr[1:]))
        
        # Multiple list operations
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        list3 = [7, 8, 9]
        combined = list(zip(list1, list2, list3))
        
        return transposed, pairs, combined
    
    # Using map and filter efficiently
    def map_filter_tricks():
        # Parse multiple integers
        line = "1 2 3 4 5"
        numbers = list(map(int, line.split()))
        
        # Apply function to multiple lists
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        sums = list(map(sum, zip(arr1, arr2)))
        
        # Filter with condition
        evens = list(filter(lambda x: x % 2 == 0, range(10)))
        
        return numbers, sums, evens
    
    return efficient_condition_checking, enumerate_tricks, zip_tricks, map_filter_tricks

def itertools_power_tricks():
    """
    Advanced itertools usage for competitive programming
    """
    
    # Combinations and permutations
    def combinatorial_operations():
        arr = [1, 2, 3, 4]
        
        # All combinations of size r
        from itertools import combinations, permutations, combinations_with_replacement
        
        combos_2 = list(combinations(arr, 2))
        perms_2 = list(permutations(arr, 2))
        combo_with_rep = list(combinations_with_replacement(arr, 2))
        
        return combos_2, perms_2, combo_with_rep
    
    # Grouping and chunking
    def grouping_operations():
        from itertools import groupby, islice, chain
        
        # Group consecutive elements
        data = [1, 1, 2, 2, 2, 3, 1, 1]
        grouped = [(k, len(list(g))) for k, g in groupby(data)]
        
        # Take chunks of data
        def chunked(iterable, n):
            iterator = iter(iterable)
            while chunk := list(islice(iterator, n)):
                yield chunk
        
        chunks = list(chunked(range(10), 3))
        
        # Flatten nested lists
        nested = [[1, 2], [3, 4], [5, 6]]
        flattened = list(chain.from_iterable(nested))
        
        return grouped, chunks, flattened
    
    # Infinite iterators
    def infinite_iterators():
        from itertools import count, cycle, repeat, islice
        
        # Infinite counter
        counter = count(1, 2)  # 1, 3, 5, 7, ...
        first_5_odds = list(islice(counter, 5))
        
        # Cycle through values
        colors = cycle(['red', 'green', 'blue'])
        first_10_colors = list(islice(colors, 10))
        
        # Repeat value
        zeros = list(repeat(0, 5))
        
        return first_5_odds, first_10_colors, zeros
    
    # Product for nested loops
    def product_operations():
        from itertools import product
        
        # Cartesian product
        coords = list(product(range(3), range(3)))
        
        # Multiple ranges
        three_d = list(product(range(2), range(2), range(2)))
        
        # Repeat with self
        binary_strings = [''.join(p) for p in product('01', repeat=3)]
        
        return coords, three_d, binary_strings
    
    return combinatorial_operations, grouping_operations, infinite_iterators, product_operations

def functional_programming_tricks():
    """
    Functional programming patterns useful in CP
    """
    
    # Using reduce for complex operations
    def reduce_operations():
        from functools import reduce
        import operator
        
        arr = [1, 2, 3, 4, 5]
        
        # Product of all elements
        product = reduce(operator.mul, arr, 1)
        
        # GCD of all elements
        import math
        gcd_all = reduce(math.gcd, arr)
        
        # Find maximum using reduce
        maximum = reduce(max, arr)
        
        # Custom operation
        def custom_op(a, b):
            return a * 10 + b
        
        combined = reduce(custom_op, arr)  # 12345
        
        return product, gcd_all, maximum, combined
    
    # Using partial for optimization
    def partial_optimization():
        from functools import partial
        
        # Pre-configure frequently used functions
        def power_mod(base, exp, mod):
            return pow(base, exp, mod)
        
        MOD = 10**9 + 7
        power_mod_fixed = partial(power_mod, mod=MOD)
        
        result = power_mod_fixed(2, 10)  # pow(2, 10, MOD)
        
        return result
    
    # Memoization with lru_cache
    def memoization_patterns():
        @lru_cache(maxsize=None)
        def fibonacci(n):
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)
        
        @lru_cache(maxsize=None)
        def count_paths(x, y, target_x, target_y):
            if x == target_x and y == target_y:
                return 1
            if x > target_x or y > target_y:
                return 0
            return count_paths(x+1, y, target_x, target_y) + count_paths(x, y+1, target_x, target_y)
        
        fib_10 = fibonacci(10)
        paths = count_paths(0, 0, 2, 2)
        
        return fib_10, paths
    
    return reduce_operations, partial_optimization, memoization_patterns

def string_and_parsing_tricks():
    """
    Advanced string manipulation and parsing tricks
    """
    
    # String formatting and manipulation
    def string_tricks():
        # Fast string building
        parts = ['hello', 'world', 'python']
        result = ''.join(parts)
        
        # String multiplication
        separator = '-' * 20
        
        # Character operations
        def char_to_index(c):
            return ord(c) - ord('a')  # For lowercase letters
        
        def index_to_char(i):
            return chr(i + ord('a'))
        
        # String slicing tricks
        s = "abcdefgh"
        reversed_string = s[::-1]
        every_second = s[::2]
        middle_part = s[2:-2]
        
        return result, separator, char_to_index('c'), reversed_string
    
    # Parsing complex input
    def parsing_tricks():
        # Multiple test cases
        def parse_multiple_testcases():
            # Example input parsing
            input_lines = [
                "3",
                "5 1 2 3 4 5",
                "3 apple banana cherry",
                "2 10 20"
            ]
            
            t = int(input_lines[0])
            results = []
            
            for i in range(1, t + 1):
                parts = input_lines[i].split()
                n = int(parts[0])
                data = parts[1:n+1]
                
                # Convert to appropriate type
                if data[0].isdigit() or data[0].lstrip('-').isdigit():
                    data = list(map(int, data))
                
                results.append((n, data))
            
            return results
        
        # Parse coordinates
        def parse_coordinates(line):
            # "1,2 3,4 5,6"
            pairs = line.split()
            coords = []
            for pair in pairs:
                x, y = map(int, pair.split(','))
                coords.append((x, y))
            return coords
        
        return parse_multiple_testcases(), parse_coordinates("1,2 3,4 5,6")
    
    return string_tricks, parsing_tricks

def mathematical_shortcuts():
    """
    Mathematical shortcuts and optimizations
    """
    
    # Fast mathematical operations
    def math_tricks():
        import math
        
        # Fast operations
        def fast_operations(a, b):
            # Fast power of 2 check
            is_power_2 = a > 0 and (a & (a - 1)) == 0
            
            # Fast multiplication/division by powers of 2
            multiply_by_4 = a << 2
            divide_by_8 = a >> 3
            
            # Fast modulo by power of 2
            mod_by_16 = a & 15  # Same as a % 16
            
            # Sign without branching
            sign = (a > 0) - (a < 0)
            
            return is_power_2, multiply_by_4, divide_by_8, mod_by_16, sign
        
        # Number theory functions
        def number_theory():
            # Fast GCD
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a
            
            # Fast LCM
            def lcm(a, b):
                return a * b // gcd(a, b)
            
            # Fast prime check
            def is_prime(n):
                if n < 2:
                    return False
                if n == 2:
                    return True
                if n % 2 == 0:
                    return False
                
                for i in range(3, int(n**0.5) + 1, 2):
                    if n % i == 0:
                        return False
                return True
            
            return gcd(48, 18), lcm(12, 8), is_prime(17)
        
        return fast_operations(12, 5), number_theory()
    
    # Bit manipulation shortcuts
    def bit_tricks():
        # Count set bits
        def popcount(n):
            return bin(n).count('1')
        
        # Get all subsets of a number
        def all_subsets(mask):
            submask = mask
            subsets = []
            while True:
                subsets.append(submask)
                if submask == 0:
                    break
                submask = (submask - 1) & mask
            return subsets
        
        # Next permutation in lexicographic order
        def next_permutation_bits(n):
            # Find rightmost set bit followed by unset bit
            c = n
            c0 = 0  # Count trailing zeros
            c1 = 0  # Count ones to right of trailing zeros
            
            while ((c & 1) == 0) and c != 0:
                c0 += 1
                c >>= 1
            
            while (c & 1) == 1:
                c1 += 1
                c >>= 1
            
            if c0 + c1 == 31 or c0 + c1 == 0:
                return -1
            
            p = c0 + c1  # Position of rightmost non-trailing zero
            n |= (1 << p)  # Flip rightmost non-trailing zero
            n &= ~((1 << p) - 1)  # Clear all bits to right of p
            n |= (1 << (c1 - 1)) - 1  # Insert (c1-1) ones on right
            
            return n
        
        return popcount(15), all_subsets(5)
    
    return math_tricks, bit_tricks

def performance_optimization_tricks():
    """
    Python-specific performance optimizations
    """
    
    # Local variable optimization
    def local_variable_tricks():
        # Cache frequently used functions/methods
        def optimized_loop(arr):
            append = arr.append  # Cache method
            len_func = len      # Cache builtin
            
            result = []
            append_result = result.append
            
            for i in range(len_func(arr)):
                append_result(arr[i] * 2)
            
            return result
        
        return optimized_loop([1, 2, 3, 4, 5])
    
    # Memory optimization
    def memory_tricks():
        # Use generators for large sequences
        def large_sequence_generator(n):
            return (i * i for i in range(n))
        
        # Use __slots__ for classes
        class OptimizedPoint:
            __slots__ = ['x', 'y']
            
            def __init__(self, x, y):
                self.x = x
                self.y = y
        
        # Use array for numeric data
        from array import array
        
        int_array = array('i', range(1000))  # More memory efficient than list
        
        return large_sequence_generator, OptimizedPoint, int_array
    
    # Input/Output optimization
    def io_optimization():
        # Batch input reading
        def read_all_input():
            import sys
            data = sys.stdin.read().split()
            iterator = iter(data)
            
            n = int(next(iterator))
            numbers = [int(next(iterator)) for _ in range(n)]
            
            return n, numbers
        
        # Batch output writing
        def write_batch_output(results):
            import sys
            sys.stdout.write('\n'.join(map(str, results)) + '\n')
        
        return read_all_input, write_batch_output
    
    return local_variable_tricks, memory_tricks, io_optimization

def cp_templates_and_patterns():
    """
    Common templates and patterns for competitive programming
    """
    
    # Complete CP template
    def complete_template():
        template = '''
import sys
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

def solve():
    # Your solution here
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Process and return result
    return sum(arr)

def main():
    t = int(input())
    for _ in range(t):
        result = solve()
        print(result)

if __name__ == "__main__":
    main()
'''
        return template
    
    # Common patterns
    def common_patterns():
        patterns = {
            'sliding_window_maximum': '''
from collections import deque

def sliding_window_max(arr, k):
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
''',
            'binary_search_template': '''
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
    
    return -1  # Not found
''',
            'dfs_template': '''
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited
'''
        }
        return patterns
    
    return complete_template, common_patterns

if __name__ == "__main__":
    print("Python-Specific CP Tricks")
    
    # Test setup
    setup_func, template_func = python_cp_setup()
    input_func, MOD, INF = template_func()
    print(f"Setup complete. MOD: {MOD}, INF: {INF}")
    
    # Test builtin tricks
    cond_check, enum_tricks, zip_tricks, map_filter = advanced_builtin_tricks()
    has_even, all_pos, is_sorted = cond_check()
    print(f"Condition checks: has_even={has_even}, all_positive={all_pos}, is_sorted={is_sorted}")
    
    # Test itertools
    combo_ops, group_ops, inf_ops, prod_ops = itertools_power_tricks()
    combos, perms, combo_rep = combo_ops()
    print(f"Combinations of [1,2,3,4] size 2: {combos}")
    
    # Test functional programming
    reduce_ops, partial_ops, memo_ops = functional_programming_tricks()
    product, gcd_all, maximum, combined = reduce_ops()
    print(f"Reduce operations: product={product}, gcd_all={gcd_all}, combined={combined}")
    
    # Test string tricks
    str_tricks, parse_tricks = string_and_parsing_tricks()
    result, sep, char_idx, reversed_str = str_tricks()
    print(f"String tricks: result='{result}', char_index={char_idx}")
    
    # Test math shortcuts
    math_funcs, bit_funcs = mathematical_shortcuts()
    fast_ops, nt_results = math_funcs()
    print(f"Number theory results: {nt_results}")
    
    # Test performance optimization
    local_vars, memory_opt, io_opt = performance_optimization_tricks()
    optimized_result = local_vars()
    print(f"Optimized loop result: {optimized_result}")
    
    # Show templates
    template_func, pattern_func = cp_templates_and_patterns()
    patterns = pattern_func()
    print(f"Available patterns: {list(patterns.keys())}")
    
    print("\nPython CP tricks demonstrated successfully!")
