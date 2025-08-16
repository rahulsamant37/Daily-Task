# Python Question: Fibonacci Series till a given number
'''
Define a function that takes a positive integer as input and returns a list containing the Fibonacci series till that number.

For example, if the input is 10, the expected output is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].
'''

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def test_solution():
    assert fibonacci(0) == [0], 'Fibonacci(0) should return [0]'
    assert fibonacci(1) == [1], 'Fibonacci(1) should return [1]'
    assert fibonacci(5) == [0, 1, 1, 2, 3], 'Fibonacci(5) should return [0, 1, 1, 2, 3]'
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Fibonacci(10) should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'

if __name__ == "__main__":
    test_solution()