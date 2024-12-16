# DSA Problem for 2024-12-17

Here is a novel DSA problem with a Python solution for 2024-12-17:

**Problem Statement:**

**"Maximum Subarray Sum with Alternating Signs"**

Given an array of integers `arr` of length `n`, find the maximum sum of a subarray that has alternating signs (i.e., the signs of the elements alternate between positive and negative). If no such subarray exists, return 0.

For example, if `arr = [3, -2, 4, -1, 5, -3]`, the maximum sum of a subarray with alternating signs is `3 - 2 + 4 - 1 + 5 - 3 = 6`.

**Optimal Solution:**

Here is a Python solution using dynamic programming:
```python
def max_alternating_sum(arr):
    n = len(arr)
    dp_pos = [0] * n  # dp_pos[i] stores the max sum of subarray ending at i with last element positive
    dp_neg = [0] * n  # dp_neg[i] stores the max sum of subarray ending at i with last element negative
    dp_pos[0] = arr[0]
    dp_neg[0] = 0
    for i in range(1, n):
        dp_pos[i] = max(dp_pos[i-1], dp_neg[i-1] + arr[i]) if arr[i] > 0 else 0
        dp_neg[i] = max(dp_neg[i-1], dp_pos[i-1] - arr[i]) if arr[i] < 0 else 0
    return max(max(dp_pos), max(dp_neg))
```
**Time and Space Complexity Analysis:**

* Time complexity: O(n), where n is the length of the input array. We iterate through the array once, and each iteration takes constant time.
* Space complexity: O(n), where n is the length of the input array. We use two arrays of length n to store the dynamic programming tables `dp_pos` and `dp_neg`.

The solution works by maintaining two dynamic programming tables `dp_pos` and `dp_neg`, where `dp_pos[i]` stores the maximum sum of a subarray ending at index `i` with the last element being positive, and `dp_neg[i]` stores the maximum sum of a subarray ending at index `i` with the last element being negative.

We iterate through the array, and for each element, we update the `dp_pos` and `dp_neg` tables based on the sign of the current element and the previous elements. Finally, we return the maximum value between the maximum sum in `dp_pos` and `dp_neg`.

This solution has a linear time complexity and space complexity, making it efficient for large input arrays.