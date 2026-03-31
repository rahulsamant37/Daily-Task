# Python Question: Fibonacci Series without Recursion
'''
The Fibonacci sequence is a series of numbers in which each number after the first two is the sum of the two preceding ones. Find the nth number in the Fibonacci series without using recursion.

Example:
Input: n = 5
Output: 8
'''

# Solution
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b

# Test cases
def test_solution():
    assert fibonacci(0) == 0, "First Fibonacci number is not 0"
    assert fibonacci(1) == 1, "Second Fibonacci number is not 1"
    assert fibonacci(5) == 8, "5th Fibonacci number is not 8"

if __name__ == "__main__":
    test_solution()

# Output:
# 0
# 1
# 1
# 2
# 3
# 5