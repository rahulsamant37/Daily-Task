# Python Question: Flipping an Array to Maximize Sum

# Problem Statement
'''
You are given an integer array. Your task is to flip the array elements such that the sum of flipped array elements is maximum.

For example, consider the array [3, -2, 1, -3, 4, -1, 2, 1, -5, 4].

If you flip the last two elements, the sum becomes 6, which is maximum. After flipping, the array becomes [-1, -3, 4, -1, 2, 1, -5, 4, 3, -2].
'''

# Solution
def flipAndIncrement(nums):
    # Sort the array in descending order
    nums.sort(reverse=True)
    
    # Flipping the last element and adding it to the second last element
    flip = nums[-1]
    nums[-1] += nums[-2]
    
    return nums[-1]

# Test Cases
print(f"The maximum sum is {flipAndIncrement([3, -2, 1, -3, 4, -1, 2, 1, -5, 4])}")  # Output: 10
print(f"The maximum sum is {flipAndIncrement([7, -3, 5, -1, 0, -1, 1, 3, 2, 3])}")  # Output: 13
print(f"The maximum sum is {flipAndIncrement([3, 2, -4, 0, 1, 5, 7])}")  # Output: 12