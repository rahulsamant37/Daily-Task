# DSA Problem 333

'''
Problem Statement:
A sequence of integers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) alternate between positive and negative.

Given a list of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (possibly zero, or all) from the original list, leaving the remaining elements in their original order.

Example:
Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
'''

Solution:
def wiggleMaxLength(nums):
    if not nums:
        return 0

    up = [0] * len(nums)
    down = [0] * len(nums)
    up[0], down[0] = 1, 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            down[i] = down[i - 1]
            up[i] = up[i - 1]

    return max(up[-1], down[-1])

# Test the function with the provided example
print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))  # Expected output: 7

# Explanation: The function initializes two arrays, 'up' and 'down', to keep track of the maximum length of wiggle sequences ending with a positive or negative difference, respectively. It iterates through the list, updating the arrays based on whether the current number increases or decreases with respect to the previous number. The result is the maximum value in either array.
'''