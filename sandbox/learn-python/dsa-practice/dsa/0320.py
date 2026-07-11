# DSA Problem 320

'''
Problem Statement:
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a list of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (possibly zero, or all) from the original list, leaving the remaining elements in their original order.

Example:
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
'''

Solution:
def wiggleMaxLength(nums):
    if len(nums) < 2:
        return len(nums)
    
    up = down = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    return max(up, down)

# Example check
print(wiggleMaxLength([1,7,4,9,2,5]))  # Output: 6

# Explanation of the solution:
# We keep two counters, `up` and `down`, to record the maximum length of wiggle subsequence that ends with an up or down movement respectively.
# Iterate through the list once, and for each element, if it's greater than the previous one, the new `up` counter will be `down + 1`, and similarly for the `down` counter.
# The final result is the larger of the two counters, as the longest wiggle sequence can end with either an up or down movement.