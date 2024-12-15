# DSA Problem generated on 2024-12-16

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a list of integers, find the maximum sum of a subarray that contains exactly k distinct elements. The subarray can be of any length, but it must contain exactly k distinct elements.

**Example:**

Input: `nums = [1, 2, 3, 2, 1, 4, 3, 5, 6, 7, 8], k = 3`

Output: `15` (The subarray `[3, 2, 1, 4, 5]` contains exactly 3 distinct elements and has a sum of 15, which is the maximum possible sum.)

**Solution Code:**
```python
from collections import defaultdict

def max_sum_k_distinct(nums, k):
    window_counts = defaultdict(int)
    max_sum = 0
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_counts[nums[right]] += 1
        window_sum += nums[right]

        while len(window_counts) > k:
            window_counts[nums[left]] -= 1
            if window_counts[nums[left]] == 0:
                del window_counts[nums[left]]
            window_sum -= nums[left]
            left += 1

        if len(window_counts) == k:
            max_sum = max(max_sum, window_sum)

    return max_sum
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input list `nums`. Here's why:

* We iterate through the list `nums` once, using a single loop that runs from 0 to n-1. This loop has a time complexity of O(n).
* Within the loop, we perform a constant amount of work for each element, which includes updating the `window_counts` dictionary and the `window_sum` variable. This work has a time complexity of O(1) per element.
* The `while` loop inside the main loop has a time complexity of O(k), where k is the number of distinct elements in the window. However, since k is a constant input parameter, this loop has a time complexity of O(1) amortized over the entire algorithm.
* The space complexity of this solution is O(k) as well, since we store at most k elements in the `window_counts` dictionary.

Note that the time complexity of this solution is linear in the length of the input list, making it efficient for large inputs.