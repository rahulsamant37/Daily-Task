# Python Question: Fibonacci Series till a Given Number
'''
Problem statement: Write a function that generates Fibonacci series till a given number.

Example:
Input: n = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''

# Solution
def fibonacci(n):
    a, b = 0, 1
    res = []
    while a < n:
        res.append(a)
        a, b = b, a + b
    return res

# Test cases
def test_solution():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

if __name__ == "__main__":
    test_solution()