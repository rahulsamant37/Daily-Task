# DSA Problem for 2024-10-07

Here is a novel DSA problem with a Python solution for 2024-10-07:

**Problem Statement:**

"Maximum Sum of Non-Overlapping Subarrays"

Given an array of integers `arr` of length `n`, find the maximum sum of `k` non-overlapping subarrays. A subarray is non-overlapping if it does not share any elements with any other subarray. The sum of a subarray is the sum of its elements.

**Example:**

Input: `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3`

Output: `30` (The maximum sum of 3 non-overlapping subarrays is 30, which can be achieved by taking the subarrays [1, 2, 3], [5, 6], and [8, 9])

**Optimal Solution:**

Here is the Python solution:
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

The time complexity of this solution is O(n^2 \* k), where `n` is the length of the input array and `k` is the number of non-overlapping subarrays.

The outer loop iterates `n` times, and the inner loop iterates `min(i, k)` times. The innermost loop iterates `i` times. Therefore, the total time complexity is O(n \* (n + k)) = O(n^2 \* k).

**Space Complexity Analysis:**

The space complexity of this solution is O(n \* k), where `n` is the length of the input array and `k` is the number of non-overlapping subarrays.

We use a 2D array `dp` of size (n + 1) x (k + 1) to store the dynamic programming table, and a 1D array `prefix_sum` of size (n + 1) to store the prefix sums of the input array. Therefore, the total space complexity is O(n \* k).

Note: The problem can be optimized to have a time complexity of O(n \* k) by using a more efficient dynamic programming approach, but the above solution is a simpler and more intuitive approach.