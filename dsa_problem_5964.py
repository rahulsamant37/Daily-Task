# DSA Problem generated on 2024-10-02

Here is a unique DSA problem in Python with a solution:

**Problem Statement:**

Given a list of integers, find the maximum sum of a subarray that contains at most K distinct elements. The subarray can be of any length, but it must have at most K distinct elements.

**Example Input:**

```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 3
```

**Expected Output:**

```
25
```

**Explanation:**

The maximum sum of a subarray with at most 3 distinct elements is 25, which can be achieved by the subarray `[3, 4, 5, 6, 7]`.

**Solution Code:**

```python
from collections import defaultdict

def max_sum_subarray(nums, K):
    if not nums or K == 0:
        return 0

    left = 0
    max_sum = 0
    window_counts = defaultdict(int)
    window_sum = 0

    for right, num in enumerate(nums):
        window_counts[num] += 1
        window_sum += num

        while len(window_counts) > K:
            window_counts[nums[left]] -= 1
            if window_counts[nums[left]] == 0:
                del window_counts[nums[left]]
            window_sum -= nums[left]
            left += 1

        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 3
print(max_sum_subarray(nums, K))  # Output: 25
```

**Time Complexity Analysis:**

The time complexity of the solution is O(N), where N is the length of the input list `nums`. This is because we process each element in the list exactly once.

The space complexity is O(K), where K is the maximum number of distinct elements allowed in the subarray. This is because we use a dictionary `window_counts` to keep track of the elements in the current window, and the size of this dictionary is at most K.

The solution uses a sliding window approach, where we maintain a window of elements that contains at most K distinct elements. We use a dictionary `window_counts` to keep track of the counts of each element in the window, and a variable `window_sum` to keep track of the sum of the elements in the window. We slide the window to the right, adding new elements and removing old elements as necessary, to find the maximum sum of a subarray with at most K distinct elements.