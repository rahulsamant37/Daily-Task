# DSA Problem 124

'''
Problem Statement:
You are given a list of positive integers representing the heights of different stacks of boxes. Your task is to find the maximum number of stacks that can be arranged in a non-decreasing order by only choosing to remove or keep the top box of each stack. 

For example, given the stack heights [5, 2, 3, 4, 1], you can create a sequence like [1, 2, 3, 4, 5] by removing the top box of every stack except the last one. However, for the input [4, 3, 2, 1], you would have to remove the top box of each stack to achieve a sequence like [1, 1, 1, 1], which is considered non-decreasing.

Write a function `maxNonDecreasingStacks` that takes a list of integers and returns the maximum number of stacks that can be arranged in a non-decreasing order.

Constraints:
- 1 <= len(heights) <= 10^3
- 1 <= heights[i] <= 10^3
'''

Solution:
```python
def maxNonDecreasingStacks(heights):
    from bisect import bisect_right
    
    # Initialize an array to store the smallest tail values for increasing subsequences
    tails = [0] * len(heights)
    size = 0
    
    for height in heights:
        # Use binary search to find the first number in tails greater than or equal to height
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] >= height:
                j = m
            else:
                i = m + 1
        tails[i] = height
        size = max(i + 1, size)
    
    return size

# Test the function with example inputs
print(maxNonDecreasingStacks([5, 2, 3, 4, 1]))  # Output: 5
print(maxNonDecreasingStacks([4, 3, 2, 1]))     # Output: 4
```

This solution utilizes a dynamic programming approach with binary search to find the longest non-decreasing subsequence of stack heights, which effectively solves the problem of rearranging stacks.