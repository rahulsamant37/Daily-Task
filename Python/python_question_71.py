# Python Question: Finding the smallest number in an array that is divisible by a given number (n)
'''
Given an array of integers and a number n, find the smallest number in the array that is divisible by n.

For example,

Input: nums = [10, 20, 30, 40, 50] and n = 20
Output: 30 (Since 30 is the smallest number divisible by 20)

Input: nums = [5, 10, 15, 20, 25] and n = 5
Output: 5 (Since 5 is the smallest number divisible by 5)
'''

def findSmallestDivisibleNumber(nums, n):
    # Find the minimum element in the array
    min_elem = min(nums)

    # Iterate through the array to find the first number which is divisible by n
    for elem in nums:
        if elem % n == 0:
            if elem < min_elem:
                min_elem = elem
    
    return min_elem

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    n = 20
    result = findSmallestDivisibleNumber(nums, n)
    print(result)  # Output: 30