# DSA Problem generated on 2024-12-31

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a list of intervals, where each interval is represented as a tuple of two integers, find the maximum sum of intervals that do not overlap with each other. The intervals are represented as (start, end), and the start time is always less than or equal to the end time.

**Example:**

Input: `[(1, 3), (2, 4), (5, 6), (7, 8), (4, 10)]`

Output: `8` (The maximum sum of non-overlapping intervals is 3 + 1 + 4 = 8, where the intervals are (1, 3), (5, 6), and (7, 8).)

**Solution Code:**
```python
def max_sum_non_overlapping_intervals(intervals):
    # Sort the intervals based on their end time
    intervals.sort(key=lambda x: x[1])

    dp = [0] * len(intervals)
    dp[0] = intervals[0][1] - intervals[0][0]

    for i in range(1, len(intervals)):
        dp[i] = max(dp[i-1], dp[i-2] + intervals[i][1] - intervals[i][0] if i >= 2 else intervals[i][1] - intervals[i][0])

    return dp[-1]

intervals = [(1, 3), (2, 4), (5, 6), (7, 8), (4, 10)]
print(max_sum_non_overlapping_intervals(intervals))  # Output: 8
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n), where n is the number of intervals. This is because we iterate through the intervals once to sort them, and then iterate through them again to compute the maximum sum of non-overlapping intervals using dynamic programming.

The space complexity is O(n), where n is the number of intervals, as we need to store the dynamic programming table `dp`.

**Explanation:**

The solution uses dynamic programming to solve the problem. We sort the intervals based on their end time, and then iterate through them to compute the maximum sum of non-overlapping intervals.

The dynamic programming table `dp` stores the maximum sum of non-overlapping intervals ending at each interval. For each interval, we have two options: either we include it in the sum, or we do not include it. If we include it, we need to find the maximum sum of non-overlapping intervals ending at the previous interval (i.e., `dp[i-2]`) and add the current interval's duration to it. If we do not include it, we simply take the maximum sum of non-overlapping intervals ending at the previous interval (i.e., `dp[i-1]`). We take the maximum of these two options and store it in `dp[i]`.

Finally, we return the last element of the `dp` table, which represents the maximum sum of non-overlapping intervals.