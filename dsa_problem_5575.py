# DSA Problem generated on 2024-10-15

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a list of integers, find the maximum sum of a contiguous subarray such that the subarray contains at most K distinct elements. For example, if the input list is `[1, 2, 3, 4, 5, 6]` and `K = 3`, the maximum sum of a contiguous subarray with at most 3 distinct elements is `15` (subarray `[3, 4, 5, 6]`).

**Solution Code:**
```python
def max_sum_subarray_with_k_distinct(arr, k):
    if k == 0 or not arr:
        return 0

    max_sum = float('-inf')
    window_start = 0
    window_end = 0
    distinct_elements = {}
    window_sum = 0

    while window_end < len(arr):
        if arr[window_end] not in distinct_elements:
            distinct_elements[arr[window_end]] = 1
        else:
            distinct_elements[arr[window_end]] += 1

        window_sum += arr[window_end]

        while len(distinct_elements) > k:
            distinct_elements[arr[window_start]] -= 1
            if distinct_elements[arr[window_start]] == 0:
                del distinct_elements[arr[window_start]]
            window_sum -= arr[window_start]
            window_start += 1

        max_sum = max(max_sum, window_sum)
        window_end += 1

    return max_sum
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input list. Here's why:

* We iterate through the input list once, using a single loop that runs from `window_start` to `window_end`.
* Within the loop, we perform the following operations:
	+ Check if an element is in the `distinct_elements` dictionary (O(1) amortized time complexity).
	+ Increment the count of an element in the `distinct_elements` dictionary (O(1) amortized time complexity).
	+ Update the `window_sum` variable (O(1) time complexity).
	+ Check if the number of distinct elements exceeds `k` and slide the window to the right (O(1) amortized time complexity).

Since we only iterate through the input list once and perform constant-time operations within the loop, the overall time complexity is O(n).

**Example Usage:**
```python
arr = [1, 2, 3, 4, 5, 6]
k = 3
print(max_sum_subarray_with_k_distinct(arr, k))  # Output: 15
```
Note that this problem is a variation of the classic "Sliding Window" problem, and the solution uses a similar approach to the "Maximum Sum Subarray" problem. However, the added twist of limiting the number of distinct elements within the subarray requires a more careful implementation of the sliding window approach.