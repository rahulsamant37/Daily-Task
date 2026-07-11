# DSA Problem 134

'''
Problem Statement:
Given a list of integers, find the length of the longest subsequence such that the absolute difference between any two consecutive elements in the subsequence is at most 1. A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: [1,2,2,3]
Output: 4
Explanation: The longest subsequence satisfying the condition is [1,2,2,3] or [1,2,2,2].

Example 2:
Input: [1,3,5,7]
Output: 1
Explanation: Any subsequence of length greater than 1 will not satisfy the condition.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
'''

Solution:
def longest_subsequence(nums):
    dp = {}
    for num in nums:
        if num in dp:
            dp[num] += 1
        else:
            dp[num] = 1
        if num - 1 in dp:
            dp[num] = max(dp[num], dp[num - 1] + 1)
        if num + 1 in dp:
            dp[num] = max(dp[num], dp[num + 1] + 1)
    return max(dp.values())

# Test the function
print(longest_subsequence([1,2,2,3]))  # Output: 4
print(longest_subsequence([1,3,5,7]))  # Output: 1
print(longest_subsequence([4,5,6,7,8,5,6,7,8,9]))  # Output: 10