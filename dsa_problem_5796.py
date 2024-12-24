# DSA Problem generated on 2024-12-25

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a list of integers, find the maximum sum of a subarray that contains at most `k` distinct elements. For example, if the input list is `[1, 2, 3, 4, 5, 6]` and `k = 2`, the maximum sum of a subarray with at most 2 distinct elements is `9` (subarray `[2, 3, 4]`).

**Solution Code:**
```
def max_sum_k_distinct(nums, k):
    if not nums or k == 0:
        return 0

    num_freq = {}
    window_start = 0
    max_sum = 0
    curr_sum = 0

    for window_end in range(len(nums)):
        right_num = nums[window_end]
        if right_num not in num_freq:
            num_freq[right_num] = 0
        num_freq[right_num] += 1

        curr_sum += right_num

        while len(num_freq) > k:
            left_num = nums[window_start]
            num_freq[left_num] -= 1
            if num_freq[left_num] == 0:
                del num_freq[left_num]
            curr_sum -= left_num
            window_start += 1

        max_sum = max(max_sum, curr_sum)

    return max_sum
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input list `nums`. Here's a breakdown of the time complexity:

* The outer loop iterates over the input list, which takes O(n) time.
* The inner while loop runs at most O(n) times, since we slide the window to the right and update the frequency dictionary.
* The dictionary operations (insertion, deletion, and lookup) take O(1) time on average.
* The update of `curr_sum` and `max_sum` takes O(1) time.

Since the inner while loop is bounded by the outer loop, the overall time complexity is O(n). The space complexity is O(k), since we store at most k elements in the frequency dictionary.

**Example Usage:**

```
nums = [1, 2, 3, 4, 5, 6]
k = 2
print(max_sum_k_distinct(nums, k))  # Output: 9
```
This solution uses a sliding window approach to find the maximum sum of a subarray with at most k distinct elements. It maintains a frequency dictionary to keep track of the elements in the current window, and updates the maximum sum accordingly.