# DSA Problem 202

'''
Problem Statement:
Given a list of integers, you need to find all unique triplets in the list which gives the sum of zero.

For example, given array nums = [-1, 0, 1, 2, -1, -4], the function should return the unique triplets that sum up to zero:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Note:
- The solution set must not contain duplicate triplets.
- You can assume that the input array will have at least 3 integers and will not exceed 1000 integers.
'''

Solution:
def three_sum(nums):
    nums.sort()
    result = []
    length = len(nums)
    
    for i in range(length-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, length-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return result

# Example check
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
# Expected output: [[-1, -1, 2], [-1, 0, 1]]
'''
This solution first sorts the array to make it easier to avoid duplicates and use a two-pointer technique to find the triplets. The time complexity is O(n^2) due to the need to iterate through all possible pairs after fixing one number. The space complexity is O(n) for the output list.
'''