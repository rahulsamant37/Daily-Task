# Python Question: Fibonacci Series until a given number
'''
Find the Fibonacci series until a given number. The Fibonacci series starts with 0 or 1 and each subsequent number is the sum of the two preceding ones, generating a sequence of numbers.

Example:
Input: 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

def solution():
    # Initialize the first two numbers in the series
    a, b = 0, 1

    # Generate the Fibonacci series until the number is reached
    while a < n:
        print(a)
        a, b = b, a + b

def test_solution(n):
    solution()
    print("Generate the Fibonacci series until", n)

if __name__ == "__main__":
    test_solution(10)