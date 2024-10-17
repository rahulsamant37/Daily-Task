# DSA Problem generated on 2024-10-18

Here is a unique DSA problem in Python:

**Problem Statement:**

You are given a list of intervals, where each interval is represented as a tuple of two integers, start and end, representing the start and end points of the interval respectively. The intervals may overlap with each other. You need to find the maximum number of intervals that can be selected such that no two intervals overlap with each other.

For example, if the input is `[(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]`, the output should be `3`, because we can select the intervals `(1, 3)`, `(3, 5)`, and `(5, 7)`.

**Solution Code:**
```
def max_non_overlapping_intervals(intervals):
    # Sort the intervals by their end points
    intervals.sort(key=lambda x: x[1])

    # Initialize the count of non-overlapping intervals
    count = 1

    # Initialize the end point of the last selected interval
    last_end = intervals[0][1]

    # Iterate through the sorted intervals
    for interval in intervals[1:]:
        # If the current interval does not overlap with the last selected interval
        if interval[0] >= last_end:
            # Increment the count of non-overlapping intervals
            count += 1
            # Update the end point of the last selected interval
            last_end = interval[1]

    return count
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n log n), where n is the number of intervals.

Here's the breakdown:

* Sorting the intervals takes O(n log n) time using the built-in `sort` method.
* The iteration through the sorted intervals takes O(n) time.
* The comparison and updating of the `last_end` variable takes constant time, O(1).

Since the sorting step dominates the time complexity, the overall time complexity is O(n log n).

Note that this problem is a variation of the "Activity Selection Problem", which is a classic problem in computer science and operations research.