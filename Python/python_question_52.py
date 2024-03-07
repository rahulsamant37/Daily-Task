# Python Question: Fibonacci Sequence Problem
'''
You are given a problem where you need to find the nth number in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. For example, the first few numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, and so on.

Example:
Input: n = 10
Output: 55
'''

def fibonacci(n):
    # Base cases
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Enter the value of n: "))
    print("The", n, "th number in the Fibonacci sequence is", fibonacci(n))

if __name__ == "__main__":
    main()