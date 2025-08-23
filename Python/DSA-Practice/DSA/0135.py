# DSA Problem 135

'''
Problem Statement:
A sequence of integers is called a zigzag sequence if each element is either strictly greater than both of its neighbors or strictly less than both of its neighbors. Given a list of integers `nums`, determine the length of the longest zigzag subsequence that can be found within the list. A subsequence is derived from the original list by deleting some or no elements without changing the order of the remaining elements.

For example, in the list [1, 7, 4, 9, 2, 5], one of the longest zigzag subsequences is [1, 7, 4, 9, 2], which has a length of 5.

Write a function `longest_zigzag_subsequence(nums)` that takes a list of integers and returns the length of the longest zigzag subsequence.
'''

Solution:
```python
def longest_zigzag_subsequence(nums):
    if len(nums) < 2:
        return len(nums)
    
    up = [0] * len(nums)
    down = [0] * len(nums)
    
    up[0], down[0] = 1, 1
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and down[j] + 1 > up[i]:
                up[i] = down[j] + 1
            if nums[i] < nums[j] and up[j] + 1 > down[i]:
                down[i] = up[j] + 1
    
    return max(max(up), max(down))

# Example check (This part is not part of the solution code, just for verification)
nums_example = [1, 7, 4, 9, 2, 5]
print(longest_zigzag_subsequence(nums_example))  # Output should be 5
```

This Python solution uses dynamic programming to track the longest zigzag subsequences ending with each element in the given list, distinguishing between those that end with an 'up' move and those that end with a 'down' move.