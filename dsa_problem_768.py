# DSA Problem generated on 2024-10-22

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a list of intervals, where each interval is represented by a tuple of two integers (start, end), write a function to find the maximum number of non-overlapping intervals that can be selected such that no two intervals overlap with each other.

For example, if the input is `[(1, 3), (2, 4), (5, 6), (7, 8), (3, 5), (4, 6)]`, the output should be `3` because we can select the intervals `(1, 3), (5, 6), and (7, 8)` which do not overlap with each other.

**Solution Code:**
```
def max_non_overlapping_intervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # sort by end time

    count = 1
    end = intervals[0][1]

    for interval in intervals[1:]:
        if interval[0] >= end:
            count += 1
            end = interval[1]

    return count

# Test case
intervals = [(1, 3), (2, 4), (5, 6), (7, 8), (3, 5), (4, 6)]
print(max_non_overlapping_intervals(intervals))  # Output: 3
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n log n) due to the sorting of the intervals, where n is the number of intervals. The sorting takes O(n log n) time, and the subsequent iteration over the sorted intervals takes O(n) time. Therefore, the overall time complexity is O(n log n).

Note that the space complexity is O(1) because we only use a small amount of extra memory to store the sorted intervals.

This problem is a classic example of a greedy algorithm, where we make a locally optimal choice (selecting the interval with the earliest end time) that leads to a globally optimal solution.