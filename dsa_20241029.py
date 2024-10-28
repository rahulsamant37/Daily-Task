# DSA Problem for 2024-10-29

Here is a novel DSA problem with a Python solution for 2024-10-29:

**Problem Statement:**

"Maximum Subarray Sum with K Reversals"

Given an array of integers `arr` and an integer `k`, find the maximum sum of a subarray that can be obtained by reversing at most `k` subarrays within the original array.

For example, if `arr = [3, -2, 1, -4, 2, 3]` and `k = 2`, one possible solution is to reverse the subarrays `[3, -2]` and `[-4, 2]` to get the maximum sum of `11` (`[3, 2, 1, 2, 3, 3]`).

**Optimal Solution:**

Here is a Python solution using dynamic programming:
```python
def max_subarray_sum_with_k_reversals(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1], dp[i - 2][j - 1] + sum(arr[i - 2:i]))

    return dp[n][k]
```
**Time/Space Complexity Analysis:**

Time complexity: O(nk)
The solution iterates over the array `arr` and the number of reversals `k`, resulting in a time complexity of O(nk).

Space complexity: O(nk)
The solution uses a 2D array `dp` of size (n + 1) x (k + 1) to store the maximum sum of subarrays with at most `j` reversals up to index `i`. This results in a space complexity of O(nk).

Note: This problem is an extension of the classic "Maximum Subarray Sum" problem, and the solution uses a similar dynamic programming approach with an additional dimension to account for the number of reversals.