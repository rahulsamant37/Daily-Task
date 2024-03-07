# Python Question: Fibonacci Series till a given number
'''
Given a positive number n, write a function to generate the Fibonacci series up to n.

Example:
Input: n = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

# Solution
def fibonacci(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# Test Cases
def test_fibonacci():
    assert fibonacci(0) == [0], "Fibonacci(0) should return [0]"
    assert fibonacci(1) == [1], "Fibonacci(1) should return [1]"
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5], \
        "Fibonacci(5) should return [0, 1, 1, 2, 3, 5]"
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], \
        "Fibonacci(10) should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"

# Driver Code
if __name__ == '__main__':
    test_fibonacci()