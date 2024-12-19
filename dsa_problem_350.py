# DSA Problem generated on 2024-12-20

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a list of integers, find the maximum sum of a subarray that contains exactly k distinct elements. The subarray can be of any length, but it must contain exactly k distinct elements.

**Example:**

Input: `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3`

Output: `21` (The maximum sum of a subarray with exactly 3 distinct elements is 21, which is the sum of the subarray `[3, 4, 5, 6, 7, 8, 9]`)

**Solution Code:**
```python
def max_sum_subarray_with_k_distinct(arr, k):
    if k == 0:
        return 0
    
    max_sum = float('-inf')
    window_start = 0
    window_end = 0
    window_sum = 0
    distinct_count = 0
    freq_map = {}
    
    while window_end < len(arr):
        right_num = arr[window_end]
        if right_num not in freq_map:
            freq_map[right_num] = 0
            distinct_count += 1
        
        freq_map[right_num] += 1
        window_sum += right_num
        
        while distinct_count > k:
            left_num = arr[window_start]
            freq_map[left_num] -= 1
            if freq_map[left_num] == 0:
                del freq_map[left_num]
                distinct_count -= 1
            window_sum -= left_num
            window_start += 1
        
        max_sum = max(max_sum, window_sum)
        window_end += 1
    
    return max_sum
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input array. Here's a breakdown of the steps:

1. The outer loop iterates over the entire array, so that's O(n).
2. Inside the outer loop, we iterate over the window of elements, but the window size is bounded by the number of distinct elements (k), so that's O(k) in the worst case.
3. We use a frequency map to keep track of the distinct elements in the window, which takes O(1) time for each insertion/deletion.
4. We update the window sum and max sum in O(1) time.

Since k is a constant, the overall time complexity is O(n).

Note that this problem is a variation of the sliding window problem, and the use of a frequency map helps us efficiently keep track of the distinct elements in the window.