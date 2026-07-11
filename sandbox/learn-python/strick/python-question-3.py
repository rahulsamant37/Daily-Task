# Python Question: Fibonacci Series up to a Given Number
'''
Problem: Given a positive number n, print the Fibonacci series up to n. A Fibonacci series is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

Example:
Input: n = 5
Output:
0 1 1 2 3
'''

# Solution
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Test Cases
def test_fibonacci():
    assert fibonacci(1) == [0], "For n=1, the output should be [0]"
    assert fibonacci(5) == [0, 1, 1, 2, 3], "For n=5, the output should be [0, 1, 1, 2, 3]"
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "For n=10, the output should be [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"

# Main Program
if __name__ == "__main__":
    test_fibonacci()