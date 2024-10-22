# DSA Problem generated on 2024-10-23

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a list of integers, find the maximum sum of a subarray that contains at most `k` distinct elements. The subarray can be of any length, but it must contain at most `k` distinct elements.

**Example:**

Input: `nums = [1, 2, 3, 2, 1, 4, 5, 6, 7], k = 3`

Output: `17` (maximum sum of a subarray with at most 3 distinct elements is `[3, 2, 1, 4, 5, 6, 7]` which sums up to 17)

**Solution Code:**
```python
from collections import defaultdict

def max_sum_k_distinct(nums, k):
    if k == 0 or not nums:
        return 0

    max_sum = 0
    window_start = 0
    freq_map = defaultdict(int)
    window_sum = 0

    for window_end in range(len(nums)):
        freq_map[nums[window_end]] += 1
        window_sum += nums[window_end]

        while len(freq_map) > k:
            freq_map[nums[window_start]] -= 1
            if freq_map[nums[window_start]] == 0:
                del freq_map[nums[window_start]]
            window_sum -= nums[window_start]
            window_start += 1

        max_sum = max(max_sum, window_sum)

    return max_sum
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input list `nums`.

Here's a breakdown of the time complexity:

* We iterate through the input list once, which takes O(n) time.
* Inside the loop, we perform the following operations:
	+ Updating the frequency map takes O(1) time.
	+ Checking if the frequency map has more than `k` distinct elements takes O(1) time.
	+ If we need to shrink the window, we iterate through the frequency map to remove an element, which takes O(k) time in the worst case.
	+ Updating the window sum takes O(1) time.
* The while loop inside the main loop runs at most `n` times, since we increment `window_start` in each iteration.
* The maximum sum is updated in O(1) time.

Since the while loop runs at most `n` times, the overall time complexity is O(n). The space complexity is O(k), since we need to store the frequency map which can have at most `k` elements.