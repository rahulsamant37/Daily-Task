# DSA Problem generated on 2024-09-23

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a list of intervals, where each interval is represented as a list of two integers [start, end], write a function to merge overlapping intervals. For example, if the input is [[1, 3], [2, 6], [8, 10], [15, 18]], the output should be [[1, 6], [8, 10], [15, 18]].

**Solution Code:**

```
def merge_intervals(intervals):
    # Sort the intervals based on the start value
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current_interval in intervals[1:]:
        last_merged_interval = merged_intervals[-1]

        # Check if the current interval overlaps with the last merged interval
        if current_interval[0] <= last_merged_interval[1]:
            # Merge the current interval with the last merged interval
            merged_intervals[-1] = [last_merged_interval[0], max(last_merged_interval[1], current_interval[1])]
        else:
            # Add the current interval to the list of merged intervals
            merged_intervals.append(current_interval)

    return merged_intervals

# Test the function
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
```

**Time Complexity Analysis:**

The time complexity of the merge_intervals function is O(n log n), where n is the number of intervals. This is because we first sort the intervals, which takes O(n log n) time. Then, we iterate over the sorted intervals, which takes O(n) time. Therefore, the overall time complexity is O(n log n).

The space complexity is O(n), as we need to store the merged intervals in a list. In the worst case, the number of merged intervals can be equal to the number of input intervals.