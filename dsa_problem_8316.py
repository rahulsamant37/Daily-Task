# DSA Problem generated on 2024-12-24

Here's a unique DSA problem in Python:

**Problem Statement:**

You are given a list of pairs of integers, where each pair represents a range of integers. The task is to find the total count of unique integers that are present in at least one of the given ranges.

For example, if the input is `[(1, 3), (2, 4), (5, 7), (6, 8)]`, the output should be `7` because the unique integers that are present in at least one of the given ranges are `[1, 2, 3, 4, 5, 6, 7]`.

**Solution Code:**
```
def count_unique_integers(ranges):
    seen = set()
    for start, end in ranges:
        for i in range(start, end + 1):
            seen.add(i)
    return len(seen)

# Test the function
ranges = [(1, 3), (2, 4), (5, 7), (6, 8)]
print(count_unique_integers(ranges))  # Output: 7
```
**Time Complexity Analysis:**

The time complexity of this solution is O(N \* M), where N is the number of ranges and M is the maximum range size.

Here's a breakdown of the time complexity:

* The outer loop iterates N times, where N is the number of ranges.
* The inner loop iterates M times, where M is the maximum range size.
* The `add` operation on the `set` takes constant time, O(1).
* The total time complexity is O(N \* M) because we are iterating over each range and each integer in the range.

Note that the time complexity can be improved to O(N log M) using a more efficient data structure, such as a `set` of intervals, but the above solution is simple and easy to understand.