# Python Question: Fibonacci Series using Recursion
'''
A series of numbers where each number is the sum of the two preceding ones,
generally starting from 0 and 1. For example, the first ten numbers in the series are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Input: Start the series from 0 and 1.
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Input: Start the series from 1 and -1.
Output: [-1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci_series(size):
    series = []
    a, b = 0, 1
    while len(series) < size:
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    size = 10
    print("Fibonacci Series:")
    print(generate_fibonacci_series(size))