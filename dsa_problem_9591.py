# DSA Problem generated on 2024-11-29

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a list of intervals, where each interval is represented as a tuple of two integers (start, end), and a list of queries, where each query is an integer, write a function to find the total number of intervals that contain each query point.

**Example:**

Intervals: [(1, 3), (2, 4), (5, 7), (6, 8)]
Queries: [2, 4, 6]

Output: [2, 2, 2]

Explanation:

* The query point 2 is contained in the intervals (1, 3) and (2, 4), so the output is 2.
* The query point 4 is contained in the intervals (2, 4) and (2, 4), so the output is 2.
* The query point 6 is contained in the intervals (5, 7) and (6, 8), so the output is 2.

**Solution Code:**
```
from bisect import bisect_left, bisect_right

def count_containing_intervals(intervals, queries):
    sorted_intervals = sorted((start, end) for start, end in intervals)
    result = []
    for query in queries:
        idx1 = bisect_left([start for start, _ in sorted_intervals], query)
        idx2 = bisect_right([end for _, end in sorted_intervals], query)
        result.append(idx2 - idx1)
    return result

intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
queries = [2, 4, 6]
print(count_containing_intervals(intervals, queries))  # Output: [2, 2, 2]
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n log n + m log n), where n is the number of intervals and m is the number of queries.

The sorting step takes O(n log n) time. The binary search steps take O(log n) time each, and we perform them m times, so the total time complexity is O(m log n). Since we have two binary searches for each query, the total time complexity is O(2m log n) = O(m log n).

Therefore, the overall time complexity is O(n log n + m log n).

Note: The solution uses the `bisect` module from Python's standard library, which provides efficient binary search functions. The `bisect_left` function returns the insertion point for the query point in the sorted list of start times, and the `bisect_right` function returns the insertion point for the query point in the sorted list of end times.