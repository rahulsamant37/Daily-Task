# Python Question: Fibonacci Series without Recursion
'''
The Fibonacci sequence is a series of numbers where each number in the sequence is the sum of the two preceding numbers, typically starting from 0 and 1. Write a Python function to generate the first n numbers of the Fibonacci series without using recursion.

Example:
Input: n = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''

def fibonacci_iterative(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def main():
    n = int(input("Enter the number of terms: "))
    print("The Fibonacci series of", n, "terms are:", fibonacci_iterative(n))

if __name__ == "__main__":
    main()