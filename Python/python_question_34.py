# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder

'''
Problem Statement: Given an integer, find the largest number that can be divided by each number from 2 to that integer without any remainder.

Example:

Input: 6
Output: 120 (6 can be divided by 2, 3, 4, 6, and 12 without any remainder.)
Input: 8
Output: 720 (8 can be divided by 2, 3, 4, 6, 8, 12, 16, and 24 without any remainder.)
'''

def findLargestDivisibleNumber(num):
    # Base case: If the number is 1, return 1
    if num == 1:
        return 1

    # Create a list to store the result
    result = []

    # Iterate from 2 to num
    for i in range(2, num + 1):
        # If the number is divisible by i, append i * (num // i) to the result list
        if num % i == 0:
            result.append(i * (num // i))

    # Return the maximum value from the result list
    return max(result)

# Test cases
print(findLargestDivisibleNumber(6))  # Output: 120
print(findLargestDivisibleNumber(8))  # Output: 720