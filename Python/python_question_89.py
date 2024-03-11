# Python Question: Fibonacci Series till a given number
'''
Find the Fibonacci series till a given number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

Example:
Input: 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

# Solution
def fibonacci_series(n: int) -> list:
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# Test cases
def test_fibonacci_series():
    assert fibonacci_series(0) == []
    assert fibonacci_series(1) == [1]
    assert fibonacci_series(5) == [0, 1, 1, 2, 3, 5]
    assert fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Main
if __name__ == "__main__":
    test_fibonacci_series()