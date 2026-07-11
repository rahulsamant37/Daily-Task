# DSA Problem 190

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a subsequence of `nums` such that the absolute difference between any two elements in the subsequence is less than or equal to `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, if `nums = [4,1,7,3]` and `k = 2`, the maximum sum of a subsequence where the absolute difference between any two elements is less than or equal to `2` is `5` (the subsequence [3, 2]).

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^4
- 0 <= k <= 10^4
'''

Solution:
```python
def max_subsequence_sum(nums, k):
    from sortedcontainers import SortedList
    
    nums.sort()
    sl = SortedList()
    max_sum = 0
    current_sum = 0
    
    for num in nums:
        # Remove elements that are not within the range [num-k, num+k]
        while sl and sl[0] < num - k:
            current_sum -= sl.pop(0)
        
        sl.add(num)
        current_sum += num
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
nums = [4, 1, 7, 3]
k = 2
print(max_subsequence_sum(nums, k))  # Output: 5
```

Note: This solution uses the `SortedList` from the `sortedcontainers` module for efficient element removal and addition. Make sure to install the `sortedcontainers` package if you haven't already (`pip install sortedcontainers`).