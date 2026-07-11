# DSA Problem 341

'''
Problem Statement:
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

For example, for the input sequence [1,17,5,10,13,15,10,5,16,8], the longest wiggle subsequence is [1,17,10,13,10,16,8], and the length is 7.
'''

Solution:
```python
def wiggleMaxLength(nums):
    if not nums:
        return 0

    up = down = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1

    return max(up, down)

# Example usage:
print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))  # Output: 7
```

This solution works as follows:
1. It iterates through the list of numbers, maintaining two counters: `up` and `down`.
2. `up` keeps track of the length of the longest wiggle subsequence that ends with an upward move.
3. `down` keeps track of the length of the longest wiggle subsequence that ends with a downward move.
4. For each number in the list, if the number is greater than the previous one, it means the last move was an upward move, so we update `up` to be `down + 1`.
5. If the number is less than the previous one, we update `down` to be `up + 1`.
6. The maximum of `up` and `down` is the length of the longest wiggle subsequence.