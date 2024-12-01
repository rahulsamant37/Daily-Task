# DSA Problem for 2024-12-02

Here is a novel DSA problem with a Python solution for 2024-12-02:

**Problem Statement:**

**Maximum Sum of Non-Overlapping Subarrays**

Given an array of integers `arr` and an integer `k`, find the maximum sum of `k` non-overlapping subarrays in `arr`. A subarray is considered non-overlapping if it does not share any elements with any other subarray.

**Example:**

Input: `arr = [3, 2, 1, 4, 5, 2, 3, 1, 4], k = 3`
Output: `18` (maximum sum of non-overlapping subarrays is `4 + 5 + 9 = 18`)

**Optimal Solution:**
```python
def max_sum_non_overlapping_subarrays(arr, k):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            max_sum = float('-inf')
            for m in range(j - 1, i):
                max_sum = max(max_sum, dp[m][j - 1] + prefix_sum[i] - prefix_sum[m])
            dp[i][j] = max_sum

    return dp[n][k]
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n^2 \* k), where `n` is the length of the input array `arr`. This is because we have three nested loops:

1. The outer loop iterates `n` times, where `n` is the length of the input array.
2. The middle loop iterates at most `k` times, where `k` is the number of non-overlapping subarrays to find.
3. The inner loop iterates at most `n` times, where `n` is the length of the input array.

The total time complexity is thus O(n^2 \* k).

**Space Complexity Analysis:**

The space complexity of the solution is O(n \* k), where `n` is the length of the input array and `k` is the number of non-overlapping subarrays to find. This is because we need to store a 2D array `dp` of size (n + 1) x (k + 1) to store the dynamic programming table.

Overall, the solution has a time complexity of O(n^2 \* k) and a space complexity of O(n \* k).