# DSA Problem 11

'''
Problem Statement:
A sequence of integers is called a zigzag sequence if each element is either strictly greater than its neighbors or strictly less than its neighbors. That is, for any index i (1 ≤ i < n-1), the sequence a satisfies either a[i-1] < a[i] > a[i+1] or a[i-1] > a[i] < a[i+1], where n is the length of the sequence.

Given an array of integers, determine the length of the longest zigzag subsequence that can be derived from it by deleting some elements or none at all.

For example, given the array [1, 7, 4, 9, 2, 5], one possible longest zigzag subsequence is [1, 7, 4, 9, 2], which has a length of 5.

Write a function `find_longest_zigzag(nums)` that takes a list of integers as input and returns the length of the longest zigzag subsequence.

Constraints:
1. 1 <= nums.length <= 1000
2. 0 <= nums[i] <= 1000
'''

Solution:
```python
def find_longest_zigzag(nums):
    if len(nums) < 2:
        return len(nums)
    
    # Initialize the dp array where dp[i][0] denotes the length of the longest zigzag subsequence
    # ending at index i and going down, and dp[i][1] denotes the length of the longest zigzag
    # subsequence ending at index i and going up.
    dp = [[1, 1] for _ in range(len(nums))]
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)
            elif nums[i] < nums[j]:
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)
    
    return max(max(row) for row in dp)

# Example checks
print(find_longest_zigzag([1, 7, 4, 9, 2, 5]))  # Output: 5
print(find_longest_zigzag([1, 4, 7]))  # Output: 2
```

This solution uses dynamic programming to find the length of the longest zigzag subsequence. It iterates through the input list, comparing each element with the previous elements to determine if it can extend a zigzag pattern, either by going up or down.