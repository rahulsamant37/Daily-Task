# DSA Problem 80

'''
Problem Statement:
Given a list of integers, find the length of the longest sublist where the sum of its elements is divisible by a given integer `k`. If no such sublist exists, return 0.

For example, if given the list [3, 1, 2, 4] and k = 3, the longest sublist with a sum divisible by 3 is [1, 2] or [3], so the function should return 2.
'''

Solution:
```python
def longest_sublist_divisible(nums, k):
    """
    Finds the length of the longest sublist where the sum of its elements is divisible by k.
    """
    # Dictionary to store the earliest occurrence of remainder when sum modulo k
    remainder_map = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        remainder = current_sum % k
        
        if remainder < 0:
            remainder += k
        
        if remainder in remainder_map:
            # Check if the current sublist length is the maximum found so far
            max_length = max(max_length, i - remainder_map[remainder])
        else:
            # Store the first occurrence of this remainder
            remainder_map[remainder] = i
    
    return max_length

# Example check function
def check_solution():
    assert longest_sublist_divisible([3, 1, 2, 4], 3) == 2, "Test case 1 failed"
    assert longest_sublist_divisible([22, 44, 66, 88], 7) == 4, "Test case 2 failed"
    assert longest_sublist_divisible([1, 2, 3], 5) == 0, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This solution uses a hashmap (`remainder_map`) to keep track of the earliest occurrence of each remainder when the cumulative sum is divided by `k`. By doing this, it can efficiently find the longest sublist where the sum of its elements is divisible by `k`.