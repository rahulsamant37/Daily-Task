# Python Question: Fibonacci Series using Dynamic Programming
'''
Discuss the application of dynamic programming in solving the Fibonacci series problem efficiently. The Fibonacci series is a sequence of numbers where each number after the first two (0 and 1) is the sum of the two preceding ones. Write a function that generates the first n numbers of the Fibonacci series.

Example:
Input: n = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
''''

# Solution
def fibonacci(n):
    '''This function generates the first n numbers of the Fibonacci series.'''
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result

def test_fibonacci():
    assert fibonacci(0) == [], 'Input should be an empty list when n is 0'
    assert fibonacci(1) == [1], '1 is the first number of the Fibonacci series when n is 1'
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5], 'Input 5 should return the first 5 numbers of the Fibonacci series'
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Input 10 should return the first 10 numbers of the Fibonacci series'

# Test the solution
test_fibonacci()

# Usage: fibonacci(5) will return [0, 1, 1, 2, 3, 5]