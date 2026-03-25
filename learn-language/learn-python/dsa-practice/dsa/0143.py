# DSA Problem 143

'''
Problem Statement:
Given a list of integers, find the length of the longest subarray where the absolute difference between any two elements is less than or equal to 1.

For example, given the list [4, 6, 5, 3, 3, 1], the longest subarray meeting the criteria is [3, 3], and the function should return 2.
'''

Solution:
```python
def longest_subarray(nums):
    from collections import defaultdict
    
    count = defaultdict(int)
    max_length = 0
    
    for num in nums:
        # Consider subarray ending at num and num+1
        max_length = max(max_length, count[num] + count[num + 1])
        count[num] += 1
    
    return max_length

# Test the function
nums = [4, 6, 5, 3, 3, 1]
print(longest_subarray(nums))  # Expected output: 2
```

Note: This solution assumes that the input list contains only integers. It uses a dictionary to count occurrences of each number in the input list and calculates the maximum length of a subarray where the absolute difference between any two elements is less than or equal to 1.