# DSA Problem 45

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. You need to find the maximum length of a contiguous subarray that sums to `k`. If there is no such subarray, return 0.

For example, given nums = [1, -1, 5, -2, 3], k = 3, the subarray [1, -1, 5] sums to 5, which is not equal to `k`, but the subarray [5, -2] sums to 3, which matches `k`. The length of this subarray is 2, so the function should return 2.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- -10^5 <= k <= 10^5
'''

Solution:
```python
def max_subarray_length(nums, k):
    max_length = 0
    sum_index_map = {0: -1}  # Initialize with 0 to handle cases where the sum from the start is k
    sum_so_far = 0
    
    for i, num in enumerate(nums):
        sum_so_far += num
        if sum_so_far - k in sum_index_map:
            max_length = max(max_length, i - sum_index_map[sum_so_far - k])
        if sum_so_far not in sum_index_map:
            sum_index_map[sum_so_far] = i  # Store only the first occurrence to ensure the maximum length
    
    return max_length

# Example check
print(max_subarray_length([1, -1, 5, -2, 3], 3))  # Expected output: 2
```

Explanation:
This solution uses a hashmap (`sum_index_map`) to store the cumulative sum up to the current index. If at any point the difference between the current cumulative sum and `k` was found in the map, it means we've found a subarray that sums to `k`. The length of this subarray is calculated, and if it's longer than the previously recorded maximum length, it replaces the maximum length. This approach ensures that we find the longest subarray with a sum equal to `k`.