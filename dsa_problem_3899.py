# DSA Problem generated on 2024-01-01

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a list of integers, write a function to find the maximum sum of a subarray that contains at most K distinct elements. For example, if the input list is `[1, 2, 3, 2, 4, 3, 5, 4]` and `K = 2`, the function should return `10`, which is the sum of the subarray `[2, 3, 2, 3]`.

**Solution Code:**
```
def max_sum_k_distinct(nums, K):
    if not nums or K == 0:
        return 0

    num_freq = {}
    window_start = 0
    max_sum = 0
    curr_sum = 0
    distinct_count = 0

    for window_end in range(len(nums)):
        right_num = nums[window_end]
        if right_num not in num_freq:
            distinct_count += 1
        num_freq[right_num] = num_freq.get(right_num, 0) + 1

        curr_sum += right_num

        while distinct_count > K:
            left_num = nums[window_start]
            num_freq[left_num] -= 1
            if num_freq[left_num] == 0:
                distinct_count -= 1
            curr_sum -= left_num
            window_start += 1

        max_sum = max(max_sum, curr_sum)

    return max_sum
```
**Time Complexity Analysis:**

The time complexity of this solution is O(N), where N is the length of the input list. Here's a breakdown of the time complexity:

* The outer loop iterates over the input list, which takes O(N) time.
* The inner while loop iterates at most N times, since we slide the window from left to right.
* The operations inside the loops, such as updating the frequency dictionary and calculating the current sum, take O(1) time.

Therefore, the overall time complexity is O(N).

**Space Complexity Analysis:**

The space complexity of this solution is O(K), where K is the maximum number of distinct elements allowed in the subarray. This is because we use a dictionary to store the frequency of each element in the window, which at most has K elements.

I hope this problem and solution are helpful!