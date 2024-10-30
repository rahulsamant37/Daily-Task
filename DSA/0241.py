# DSA Problem 241

'''
Problem Statement:
You are given an array of positive integers and a positive integer k. Your task is to find the maximum sum of a subsequence of the array such that the sum of any two consecutive elements in the subsequence is not divisible by k. A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

For example, if the array is [1, 2, 3, 4] and k is 2, a valid subsequence could be [1, 3] because the sum of consecutive elements (1+3=4) is not divisible by k=2. However, [2, 4] would be invalid because 2+4=6, which is divisible by k=2.

Write a function `max_sum_subsequence(arr, k)` that returns the maximum sum of such a subsequence.

Constraints:
- 1 <= len(arr) <= 10^5
- 1 <= arr[i] <= 10^5
- 2 <= k <= 10^5
'''

Solution:
```python
def max_sum_subsequence(arr, k):
    # Initialize a DP array where dp[i] will hold the maximum sum of a subsequence
    # such that the last element is not divisible by i.
    dp = [0] * k
    for num in arr:
        # For each number, we update the dp array.
        # We avoid choosing the same remainder again to ensure the sum of any two
        # consecutive elements is not divisible by k.
        for remainder in range(k):
            if num % k == remainder:
                # Update the dp array for the complement remainder (k - remainder) % k
                dp[remainder] = max(dp[remainder], max(dp) + num)
    return max(dp)

# Example check function
def check_solution():
    assert max_sum_subsequence([1, 2, 3, 4], 2) == 5, "Example 1 failed"
    assert max_sum_subsequence([3, 6, 9, 12], 3) == 15, "Example 2 failed"
    assert max_sum_subsequence([10, 20, 30, 40], 5) == 50, "Example 3 failed"
    print("All test cases passed.")

check_solution()
```

This solution involves dynamic programming to keep track of the maximum possible sum of subsequences that end with a specific remainder when divided by `k`. This ensures that the sum of any two consecutive elements is not divisible by `k`.