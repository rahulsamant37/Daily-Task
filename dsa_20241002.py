# DSA Problem for 2024-10-02

Here's a novel DSA problem with a Python solution for 2024-10-02:

**Problem Statement:**

**Maximum Subarray Sum with Dynamic Constraints**

Given an array of integers `arr` of length `n` and a set of dynamic constraints `constraints`, find the maximum subarray sum that satisfies all the constraints. The constraints are defined as follows:

* Each constraint is a tuple `(start, end, min_sum, max_sum)`, where `start` and `end` are indices in the array, and `min_sum` and `max_sum` are the minimum and maximum allowed sums for the subarray from `start` to `end`.
* The subarray sum must be within the range `[min_sum, max_sum]` for each constraint.
* The maximum subarray sum is the maximum sum of any subarray that satisfies all the constraints.

**Example:**

```
arr = [1, 2, 3, 4, 5, 6]
constraints = [(0, 3, 5, 10), (1, 4, 7, 12), (2, 5, 10, 15)]
```

**Optimal Solution:**

Here's a Python solution using dynamic programming and Kadane's algorithm:
```python
def max_subarray_sum_with_constraints(arr, constraints):
    n = len(arr)
    dp = [[float('-inf')] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = arr[i]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = max(dp[i][j-1] + arr[j], arr[j])

    max_sum = float('-inf')
    for constraint in constraints:
        start, end, min_sum, max_sum_constraint = constraint
        curr_sum = 0
        for k in range(start, end + 1):
            curr_sum = max(curr_sum + arr[k], arr[k])
            if curr_sum >= min_sum and curr_sum <= max_sum_constraint:
                max_sum = max(max_sum, curr_sum)

    return max_sum
```

**Time/Space Complexity Analysis:**

* Time complexity: O(n^2 + m), where `n` is the length of the array and `m` is the number of constraints. The time complexity is dominated by the dynamic programming step, which has a quadratic time complexity.
* Space complexity: O(n^2), where `n` is the length of the array. The space complexity is dominated by the dynamic programming table, which has a quadratic space complexity.

Note that the time complexity can be improved by using a more efficient algorithm for finding the maximum subarray sum, such as the Kadane's algorithm with a time complexity of O(n). However, the space complexity remains the same.