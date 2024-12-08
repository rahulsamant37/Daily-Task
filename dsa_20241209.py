# DSA Problem for 2024-12-09

Here is a novel DSA problem with a Python solution for 2024-12-09:

**Problem Statement:**

**"Maximum Subarray Sum with Threshold"**

Given an array of integers `arr` and an integer `threshold`, find the maximum sum of a subarray that does not exceed the `threshold` value. If no such subarray exists, return `-1`.

For example, if `arr = [3, 1, 2, 5, 4, 3]` and `threshold = 8`, the maximum subarray sum that does not exceed the threshold is `7` (from the subarray `[3, 2, 2]`).

**Optimal Solution:**
```
def max_subarray_sum_threshold(arr, threshold):
    max_sum = -1
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > threshold and left <= right:
            window_sum -= arr[left]
            left += 1

        if window_sum <= threshold:
            max_sum = max(max_sum, window_sum)

    return max_sum
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input array `arr`. This is because we are iterating through the array once using a sliding window approach.

**Space Complexity Analysis:**

The space complexity of this solution is O(1), which means the space required does not change with the size of the input array `arr`, so it is constant. We are only using a few extra variables to store the maximum sum, window sum, and the left pointer of the sliding window.

**Explanation:**

The solution uses a sliding window approach to find the maximum subarray sum that does not exceed the threshold. We maintain a window sum that is the sum of the elements in the current window. We iterate through the array, adding elements to the window sum. If the window sum exceeds the threshold, we start reducing the window sum by removing elements from the left of the window until the window sum is within the threshold. We keep track of the maximum sum that is within the threshold and return it at the end.