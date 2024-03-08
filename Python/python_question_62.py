# Python Question: Find the largest number that can be divided by each of the numbers from 2 to 10 without any remainder
'''
Given an integer, find the largest number that can be divided by each of the numbers from 2 to the given number (inclusive) without any remainder.

For example,

Input: 5
Output: 120 (as 5 is divisible by 2, 3, 4, 5, and 6)

Input: 8
Output: 720 (as 8 is divisible by 2, 3, 4, 5, 6, 7, 8, and 9)
'''

def solution(n: int) -> int:
    # Initialize the result
    result = 1
    
    # Iterate from 2 to n
    for i in range(2, n+1):
        # If i divides n without remainder, multiply result
        if n % i == 0:
            result *= i
    
    return result

# Test cases
print(solution(5))  # Output: 120
print(solution(8))  # Output: 720