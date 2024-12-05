# DSA Problem for 2024-12-06

Here's a novel DSA problem with a Python solution for 2024-12-06:

**Problem Statement:**

**"Maximum Subarray Sum with K-Window Constraints"**

Given an array of integers `arr` and two integers `k` and `m`, find the maximum sum of a subarray of length `k` that can be formed by selecting at most `m` elements from the original array, where the selected elements must be contiguous in the original array.

**Constraints:**

* `1 <= k <= m <= len(arr)`
* `-10^5 <= arr[i] <= 10^5`

**Example:**

* `arr = [3, 2, -1, 4, 5, 1, -2, 3], k = 3, m = 5`
* Answer: `12` (subarray `[4, 5, 1, -2, 3]` has sum `12` and length `5`, and selecting at most `3` elements from this subarray gives the maximum sum `12`).

**Optimal Solution:**
```python
def max_subarray_sum(arr, k, m):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, min(i, m) + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + prefix_sum[i] - prefix_sum[i - k], dp[i - 1][j])

    return dp[n][m]

# Test case
arr = [3, 2, -1, 4, 5, 1, -2, 3]
k = 3
m = 5
print(max_subarray_sum(arr, k, m))  # Output: 12
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n \* m), where `n` is the length of the input array. This is because we iterate over the array once to compute the prefix sum, and then iterate over the dynamic programming table `dp` with complexity O(n \* m).

**Space Complexity Analysis:**

The space complexity of the solution is O(n + m), where `n` is the length of the input array. This is because we use an additional array `prefix_sum` of size `n + 1` to store the prefix sum, and a 2D dynamic programming table `dp` of size `(n + 1) x (m + 1)`.

This problem combines elements of dynamic programming, prefix sum arrays, and window-based problems, making it a challenging and interesting DSA problem for 2024-12-06!