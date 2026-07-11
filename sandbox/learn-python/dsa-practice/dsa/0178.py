# DSA Problem 178

'''
Problem Statement:
Given a list of integers, find the length of the longest subarray where the absolute difference between any two elements is less than or equal to 1. For example, in the array [4, 6, 5, 3, 3, 1], the longest such subarray would be [3, 3] or [4, 5], both of length 2.

Write a function `longest_subarray_with_diff_one(nums)` that takes a list of integers `nums` and returns the length of the longest subarray meeting the criteria.

Constraints:
- 1 <= len(nums) <= 10^5
- 0 <= nums[i] <= 10^4
'''

Solution:
```python
from collections import defaultdict

def longest_subarray_with_diff_one(nums):
    num_counts = defaultdict(int)
    max_length = 0
    
    for num in nums:
        # Count the number of occurrences of the number and the number + 1
        current_length = num_counts[num] + num_counts[num + 1]
        max_length = max(max_length, current_length)
        
        # Increment the count for the current number
        num_counts[num] += 1
    
    return max_length

# Example check function
def check_solution():
    assert longest_subarray_with_diff_one([4, 6, 5, 3, 3, 1]) == 2
    assert longest_subarray_with_diff_one([1, 3, 2, 3, 1, 3]) == 3
    assert longest_subarray_with_diff_one([10]) == 1
    print("All tests passed!")

check_solution()
```

Note: This solution assumes the problem is asking for the longest subarray with elements differing by at most 1, ignoring the order of elements. The solution provided uses a sliding approach with a hash map to keep track of numbers and their counts, achieving an efficient solution with O(n) time complexity.