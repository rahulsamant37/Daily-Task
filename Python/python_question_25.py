# Python Question: Fibonacci Series without Recursion
'''
Given a positive number n, print the first n numbers of the Fibonacci series.

Example:
Input: n = 5
Output:
1 1 2 3 5
'''

# Solution
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        temp = a
        a = b
        b = temp + b
    return [a] + list(map(str, b-(1<<n)//2))

# Test cases
def test_solution():
    print(fibonacci_iterative(5))  # Output: [1, 1, 2, 3, 5]
    print(fibonacci_iterative(10))  # Output: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

if __name__ == "__main__":
    test_solution()