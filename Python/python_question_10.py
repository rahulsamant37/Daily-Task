# Python Question: Fibonacci Series until a given number
'''
Write a program to generate the Fibonacci series until a given number. The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting from 0 and 1.

Example:
Input: 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

def solution():
    # Initialize the first two numbers of the Fibonacci series
    a, b = 0, 1
    
    # Loop until the number of terms exceeds the given limit
    while a < n:
        # Append the sum of a and b to the result list
        result.append(a)
        # Update a and b for the next number in the series
        a, b = b, a + b
    
    return result

def test_solution():
    n = 10  # Change this value to test for different numbers of terms
    result = solution()
    print("Fibonacci Series up to", n, "terms:", result)

if __name__ == "__main__":
    test_solution()