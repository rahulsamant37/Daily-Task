# Python Question: Find the largest number that can be divided by each number from 2 to n without any remainder

# Problem Statement
"""
Write a function that takes an integer n and returns the largest number that can be divided by each number from 2 to n without any remainder.

For example,

Input: n = 5
Output: 120 (120 is the largest number that can be divided by 1, 2, 3, 4, and 5 without any remainder)

Input: n = 10
Output: 4410 (4410 is the largest number that can be divided by 1, 2, 3, ..., 10 without any remainder)
"""

# Solution
def find_largest_divisible_by(n):
    # Base case: when n == 2, the largest number is n itself
    if n == 2:
        return n
    
    # Find the largest number without considering odd numbers
    largest_without_odds = 1
    for i in range(2, n+1):
        if i * largest_without_odds % 2 == 0:
            largest_without_odds *= i
    
    # Find the largest number considering all numbers (including odd numbers)
    largest_with_odds = 1
    for i in range(2, n+1):
        if i % 2 == 0:  # Odd number
            largest_with_odds *= i
        else:  # Even number
            largest_with_odds *= (i * n) // 2  # Multiply even numbers and divide by 2
    
    return largest_with_odds

if __name__ == "__main__":
    n = 10  # Change this value to test for different values of n
    print("The largest number that can be divided by 1, 2, ...,", n, "is", find_largest_divisible_by(n))