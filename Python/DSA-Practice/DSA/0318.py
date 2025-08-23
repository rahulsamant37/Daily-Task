# DSA Problem 318

'''
Problem Statement:
Given a list of positive integers and a non-negative integer k, write a function that returns the maximum sum of a subsequence of the list such that the sum of the subsequence does not exceed k. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, if the input list is [3, 1, 4, 2] and k is 6, the function should return 6 because the subsequence [3, 1, 2] sums up to 6, which is the closest possible sum to k without exceeding it.

Constraints:
- The length of the list will be between 1 and 100.
- Each element of the list will be between 1 and 100.
- k will be between 0 and the sum of all elements in the list.
'''

Solution:
def max_sum_subsequence(nums, k):
    """
    Finds the maximum sum of a subsequence of nums that does not exceed k.
    """
    n = len(nums)
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j]
            if nums[i-1] <= j:
                dp[i][j] = max(dp[i][j], dp[i-1][j-nums[i-1]] + nums[i-1])
    
    return dp[n][k]

# Example check (This is not part of the solution code, just for verification)
if __name__ == "__main__":
    nums = [3, 1, 4, 2]
    k = 6
    print(max_sum_subsequence(nums, k))  # Expected output: 6
'''
This problem is a variation of the classic 0/1 Knapsack problem, where the objective is to maximize the total value of items in the knapsack without exceeding the weight capacity. Here, we are trying to maximize the sum of a subsequence without exceeding a given limit k. The solution uses dynamic programming to efficiently compute the desired result.
'''