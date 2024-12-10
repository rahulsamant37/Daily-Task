# DSA Problem for 2024-12-11

Here is a novel DSA problem with a Python solution for 2024-12-11:

**Problem Statement:**

**"Maximum Subarray Sum with K Reversals"**

Given an array of integers `arr` and an integer `k`, find the maximum sum of a subarray that can be obtained by reversing at most `k` segments of the array.

A segment reversal means swapping the elements of a contiguous subarray in reverse order. For example, if `arr = [1, 2, 3, 4, 5]` and `k = 2`, one possible reversal is `[1, 2, 5, 4, 3]`.

**Optimal Solution:**
```python
def max_subarray_sum_with_k_reversals(arr, k):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            max_sum = float('-inf')
            for segment_end in range(i):
                segment_sum = prefix_sum[i] - prefix_sum[segment_end]
                if segment_end > 0:
                    segment_sum += dp[segment_end - 1][j - 1]
                max_sum = max(max_sum, segment_sum)
            dp[i][j] = max_sum

    return dp[n][k]
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n^2 \* k), where `n` is the length of the input array and `k` is the number of reversals allowed.

The outer loop iterates `n` times, and the inner loop iterates `min(i, k)` times. The innermost loop iterates `i` times, which is bounded by `n`. Therefore, the total time complexity is O(n^2 \* k).

**Space Complexity Analysis:**

The space complexity of this solution is O(n \* k), where `n` is the length of the input array and `k` is the number of reversals allowed.

We use a 2D array `dp` of size `(n + 1) x (k + 1)` to store the maximum subarray sum for each subproblem. Therefore, the space complexity is O(n \* k).

**Note:**

This problem is a variation of the classic "Maximum Subarray Sum" problem, but with the added twist of allowing `k` reversals. The solution uses dynamic programming to build up a table of maximum subarray sums for each subproblem, and then iterates over the table to find the maximum sum achievable with `k` reversals.