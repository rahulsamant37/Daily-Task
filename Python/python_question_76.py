# Python Question: Find the largest number that can be divided by each of the numbers from 2 to 10 without any remainder
'''
Problem statement: Given a list of numbers, find the largest number that can be divided without any remainder by each number in the list.

Example:
Input: {2, 3, 4, 5, 6, 7, 8, 9, 10}
Output: 60 (The largest number that can be divided by 2, 3, 4, 5, 6, 7, 8, 9, and 10 without any remainder)
'''

def findLargestCommonDivisor(nums):
    # Find the maximum and minimum numbers from the given list
    maxNum = max(nums)
    minNum = min(nums)
    
    # Iterate through the list and find the common divisors of the maximum number
    for num in nums:
        while num > 0:
            if (maxNum % num == 0 and minNum % num == 0):
                return num
            num //= 2
    
    return -1

# Test cases
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The largest number that can be divided without any remainder is", findLargestCommonDivisor(numbers))