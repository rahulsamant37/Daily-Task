# DSA Problem for 2024-11-01

Here is a novel DSA problem for 2024-11-01:

**Problem Statement:**

You are given a list of intervals, where each interval is represented as a tuple of two integers, `start` and `end`, denoting the start and end points of the interval, respectively. The intervals may overlap with each other. Your task is to find the maximum number of non-overlapping intervals that can be selected from the given list.

For example, if the input is `[(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]`, the output should be `3`, because the non-overlapping intervals `(1, 3)`, `(3, 5)`, and `(5, 7)` can be selected.

**Optimal Solution:**
```
def max_non_overlapping_intervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # sort by end point

    count = 1
    end = intervals[0][1]

    for interval in intervals[1:]:
        if interval[0] >= end:
            count += 1
            end = interval[1]

    return count
```
**Time/Space Complexity Analysis:**

* Time complexity: O(n log n), where n is the number of intervals. This is because we sort the intervals, which takes O(n log n) time.
* Space complexity: O(1), because we only use a small amount of extra memory to store the `count` and `end` variables.

The idea behind the solution is to sort the intervals by their end points, and then iterate through the sorted list to find the maximum number of non-overlapping intervals. We keep track of the end point of the last selected interval, and only consider intervals that start after the last end point.

This problem is a variation of the classic "activity selection problem", which is a well-known problem in algorithms and computer science.