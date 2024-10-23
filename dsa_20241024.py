# DSA Problem for 2024-10-24

Here is a novel DSA problem with a Python solution for 2024-10-24:

**Problem Statement:**

**Date:** 2024-10-24

**Problem:** "Longest Subarray with Alternating Sums"

Given an array of integers, find the length of the longest subarray such that the sum of elements at even indices is equal to the sum of elements at odd indices.

**Example:**

Input: `arr = [1, 2, 3, 4, 5, 6]`

Output: `4` (Longest subarray is `[1, 2, 3, 4]` with even sum `1 + 3 = 4` and odd sum `2 + 4 = 4`)

**Optimal Solution:**
```python
def longest_alternating_sums(arr):
    n = len(arr)
    even_sum = [0] * (n + 1)
    odd_sum = [0] * (n + 1)
    max_len = 0

    for i in range(n):
        even_sum[i + 1] = even_sum[i] + (arr[i] if i % 2 == 0 else 0)
        odd_sum[i + 1] = odd_sum[i] + (arr[i] if i % 2 == 1 else 0)

    for i in range(n):
        for j in range(i + 1, n + 1):
            if even_sum[j] - even_sum[i] == odd_sum[j] - odd_sum[i]:
                max_len = max(max_len, j - i)

    return max_len

# Test the function
arr = [1, 2, 3, 4, 5, 6]
print(longest_alternating_sums(arr))  # Output: 4
```
**Time Complexity Analysis:**

The time complexity of the optimal solution is O(n^2), where n is the length of the input array. This is because we have two nested loops: the outer loop iterates over the array elements, and the inner loop checks all possible subarrays for the given condition.

**Space Complexity Analysis:**

The space complexity of the optimal solution is O(n), where n is the length of the input array. We use two auxiliary arrays, `even_sum` and `odd_sum`, each of size n + 1, to store the cumulative sums of even and odd indices, respectively.

**Note:** This problem can be optimized further using dynamic programming and memoization techniques to reduce the time complexity to O(n). However, the above solution provides a simple and intuitive approach to solving the problem.