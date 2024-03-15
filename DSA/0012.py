# DSA Problem 12

'''
Problem Statement:
You are given a list of integers and a positive integer k. Your task is to find the maximum sum of any contiguous subarray of size exactly k. If the list is empty or the value of k is greater than the length of the list, return 0.

For example, if the list is [1, 4, 2, 10, 23, 3, 1, 0, 20] and k = 4, the subarray with the maximum sum is [10, 23, 3, 1] with a sum of 37.

Constraints:
- The length of the list will be in the range [1, 10^5].
- The elements of the list will be in the range [-1000, 1000].
- k will be in the range [1, 10^5].
'''

Solution:
```python
def max_sum_subarray(nums, k):
    """
    Finds the maximum sum of any contiguous subarray of size exactly k.
    """
    if not nums or k <= 0 or k > len(nums):
        return 0

    max_sum = float('-inf')
    window_sum = 0
    window_start = 0

    for window_end in range(len(nums)):
        window_sum += nums[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return max_sum if max_sum != float('-inf') else 0

# Example check
print(max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))  # Output should be 37
```

This solution utilizes a sliding window approach to efficiently find the maximum sum of any contiguous subarray of size k. The time complexity is O(n), where n is the number of elements in the input list, as each element is processed at most twice.