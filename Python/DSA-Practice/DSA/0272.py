# DSA Problem 272

'''
Problem Statement:
Given a list of integers `nums`, you are to return the smallest positive integer that is missing from the list. The solution should be efficient and avoid sorting the list.

For example:
- If nums = [1,2,0], the missing smallest positive integer is 3.
- If nums = [3,4,-1,1], the missing smallest positive integer is 2.
- If nums = [7,8,9,11,12], the missing smallest positive integer is 1.
'''

Solution:
def find_missing_positive(nums):
    n = len(nums)
    
    # Place each number in its corresponding index, i.e., 1 at index 0, 2 at index 1, etc.
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Find the first index i where nums[i] is not i + 1, which means i + 1 is missing.
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all numbers from 1 to n are present, then the missing number is n + 1.
    return n + 1

# Test the function with provided data points
print(find_missing_positive([1, 2, 0]))  # Expected output: 3
print(find_missing_positive([3, 4, -1, 1]))  # Expected output: 2
print(find_missing_positive([7, 8, 9, 11, 12]))  # Expected output: 1
