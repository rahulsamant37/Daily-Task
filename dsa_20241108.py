# DSA Problem for 2024-11-08

Here is a novel DSA problem with a Python solution for 2024-11-08:

**Problem Statement:**

You are given a list of intervals, where each interval is represented as a tuple of two integers, start and end, denoting the start and end points of the interval respectively. You need to find the maximum number of non-overlapping intervals that can be selected from the given list such that the sum of their lengths is maximum.

**Example:**

Input: `[(1, 3), (2, 4), (5, 7), (6, 8), (9, 10)]`

Output: `3`

Explanation: The maximum number of non-overlapping intervals that can be selected is 3, which are `(1, 3)`, `(5, 7)`, and `(9, 10)`. The sum of their lengths is 6, which is the maximum possible.

**Optimal Solution:**

Here is a Python solution using dynamic programming:
```python
def max_non_overlapping_intervals(intervals):
    # Sort the intervals by their end points
    intervals.sort(key=lambda x: x[1])

    # Initialize dynamic programming table
    dp = [0] * len(intervals)
    dp[0] = intervals[0][1] - intervals[0][0]

    for i in range(1, len(intervals)):
        # Find the maximum sum of non-overlapping intervals ending at i
        max_sum = 0
        for j in range(i):
            if intervals[i][0] >= intervals[j][1]:
                max_sum = max(max_sum, dp[j] + intervals[i][1] - intervals[i][0])
        dp[i] = max(max_sum, dp[i-1])

    return dp[-1]

# Example usage
intervals = [(1, 3), (2, 4), (5, 7), (6, 8), (9, 10)]
print(max_non_overlapping_intervals(intervals))  # Output: 6
```
**Time/Space Complexity Analysis:**

* Time complexity: O(n^2), where n is the number of intervals. This is because we have a nested loop that iterates over all intervals.
* Space complexity: O(n), where n is the number of intervals. We need to store the dynamic programming table of size n.

Note: The time complexity can be improved to O(n log n) using a more efficient algorithm, but the above solution is a simple and intuitive one.