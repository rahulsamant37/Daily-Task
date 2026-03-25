"""
Fast Input/Output for Competitive Programming
============================================

The first and most critical optimization for Python CP.
Regular input() is slow - use sys.stdin.readline instead.
"""

import sys

def fast_input_setup():
    """
    Setup fast input/output for competitive programming
    """
    # Fast input - avoids overhead of input()
    input = sys.stdin.readline
    
    # Example usage
    n = int(input())
    arr = list(map(int, input().split()))
    
    return input

def fast_output_batch():
    """
    Batch output instead of printing in loops
    """
    results = []
    
    # Collect results instead of printing immediately
    for i in range(100):
        results.append(str(i * i))
    
    # Print all at once - much faster
    sys.stdout.write("\n".join(results) + "\n")

def fast_input_multiple_testcases():
    """
    Efficient way to handle multiple test cases
    """
    input = sys.stdin.readline
    
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Process and store result
        result = sum(arr)
        results.append(str(result))
    
    # Output all results at once
    sys.stdout.write("\n".join(results) + "\n")

def bulk_input_reading():
    """
    For problems with large input, read everything at once
    """
    data = sys.stdin.read().split()
    it = iter(data)
    
    n = int(next(it))
    m = int(next(it))
    
    # Read matrix efficiently
    matrix = []
    for i in range(n):
        row = [int(next(it)) for _ in range(m)]
        matrix.append(row)
    
    return matrix

# Template for fast I/O
def competitive_template():
    """
    Standard template for competitive programming
    """
    import sys
    input = sys.stdin.readline
    
    # Your solution here
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Process
    result = sum(arr)
    
    # Fast output
    print(result)

if __name__ == "__main__":
    # Demonstrate different I/O methods
    print("Fast I/O techniques for CP")
    fast_output_batch()
