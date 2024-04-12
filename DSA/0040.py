# DSA Problem 40

'''
Problem Statement:
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a list of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example:
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
'''

Solution:
def wiggleMaxLength(nums):
    n = len(nums)
    if n < 2:
        return n
    
    up = [1] * n
    down = [1] * n
    
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            up[i] = down[i-1] + 1
            down[i] = down[i-1]
        elif nums[i] < nums[i-1]:
            down[i] = up[i-1] + 1
            up[i] = up[i-1]
        else:
            down[i] = down[i-1]
            up[i] = up[i-1]
    
    return max(up[-1], down[-1])

# Test the function
nums = [1,7,4,9,2,5]
print(wiggleMaxLength(nums))  # Output: 6

The solution uses dynamic programming to keep track of the longest wiggle subsequence that ends with an up or down difference. The space complexity can be optimized to O(1) by using only two variables instead of arrays for `up` and `down`.