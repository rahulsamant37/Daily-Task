# DSA Problem for 2024-10-10

Here is a novel DSA problem with a Python solution for 2024-10-10:

**Problem Statement:**

**"Maximum Subarray Sum with K Reversals"**

Given an array of integers `arr` and an integer `k`, find the maximum sum of a subarray that can be obtained by reversing at most `k` subarrays within the original array.

**Constraints:**

* `1 <= arr.length <= 10^5`
* `-10^9 <= arr[i] <= 10^9`
* `0 <= k <= arr.length`

**Example:**

Input: `arr = [3, -2, 5, -1, 2, 4, -3], k = 2`
Output: `14`

Explanation: One possible solution is to reverse the subarrays `[3, -2]` and `[-1, 2]`, resulting in the maximum sum of `14 (= 5 + 4 + 3 + 2)`.

**Optimal Solution:**
```python
def max_subarray_sum_with_k_reversals(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + arr[i - 1])

    for j in range(1, k + 1):
        for i in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1], dp[i - 1][j - 1] - arr[i - 1])

    return dp[n][k]
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n \* k), where `n` is the length of the input array and `k` is the maximum number of reversals allowed. This is because we have a nested loop structure with two loops, each iterating `n` times, and an inner loop iterating `k` times.

**Space Complexity Analysis:**

The space complexity of the solution is O(n \* k), as we need to store the dynamic programming table `dp` with dimensions `(n + 1) x (k + 1)`.

**Note:**

This problem is an extension of the classic "Maximum Subarray Sum" problem, with the added twist of allowing at most `k` reversals. The solution uses dynamic programming to store the maximum sum of subarrays with at most `j` reversals ending at each index `i`.