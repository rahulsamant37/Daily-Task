# DSA Problem 71

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the maximum sum of a non-empty subsequence of `nums` such that for every pair of consecutive integers in the subsequence, their difference is at most `k`. A subsequence is formed by deleting some or no elements without changing the order of the remaining elements.

For example, if nums = [1, 4, 2, 6, 7] and k = 2, a valid subsequence could be [1, 2, 6] because the differences between consecutive elements are 1 and 4, which are both less than or equal to 2.
'''

Solution:
```python
from collections import deque

def max_subsequence_sum(nums, k):
    """
    Finds the maximum sum of a non-empty subsequence of nums such that the difference between
    every pair of consecutive integers in the subsequence is at most k.
    """
    nums.sort()  # Sorting to ensure that subsequences are easier to find
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = nums[0]
    queue = deque([0])  # To maintain indices of useful values in dp[]

    for i in range(1, len(nums)):
        # Remove elements from the front of the queue that do not satisfy the condition
        while queue and nums[i] - nums[queue[0]] > k:
            queue.popleft()
        
        # Calculate dp[i] and update max_sum
        dp[i] = nums[i] + (dp[queue[0]] if queue else 0)
        max_sum = max(max_sum, dp[i])
        
        # Maintain queue in decreasing order of dp values
        while queue and dp[i] >= dp[queue[-1]]:
            queue.pop()
        queue.append(i)
    
    return max_sum

# Check function to verify the solution with provided data points
def check_solution():
    assert max_subsequence_sum([10, 5, 9, 100], 5) == 24, "Test case 1 failed"
    assert max_subsequence_sum([-6, -1, 5, 2, -4], 2) == 0, "Test case 2 failed"
    assert max_subsequence_sum([4, 2, 1], 2) == 6, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This solution uses dynamic programming to keep track of the maximum sum possible up to each index, ensuring that the difference between elements in the subsequence does not exceed `k`. It utilizes a queue to maintain the indices of elements that are currently useful for the calculation, thus optimizing the computation of the maximum sum for subsequences.