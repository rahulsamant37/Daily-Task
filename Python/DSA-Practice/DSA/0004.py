# DSA Problem 4

'''
Problem Statement:
You are given a list of integers `nums`. Write a function `find_unique_pairs` that returns the number of unique pairs (i, j) where `i < j` and the difference between `nums[i]` and `nums[j]` is exactly 1. Consider the list to be 0-indexed.

For example, given the list [1, 2, 3, 4], the unique pairs that satisfy the condition are (0, 1), (1, 2), and (2, 3), since the difference between the elements of these pairs is exactly 1.
'''

Solution:
```python
from collections import defaultdict

def find_unique_pairs(nums):
    """
    Returns the number of unique pairs (i, j) where i < j and the difference between nums[i] and nums[j] is exactly 1.
    """
    count = 0
    num_counts = defaultdict(int)
    
    for num in nums:
        # Check for pairs where nums[j] = num + 1
        count += num_counts[num + 1]
        # Check for pairs where nums[j] = num - 1
        count += num_counts[num - 1]
        # Increment the occurrence of the current number
        num_counts[num] += 1
    
    return count

# Example check function
def check_solution():
    assert find_unique_pairs([1, 2, 3, 4]) == 3, "Test case 1 failed"
    assert find_unique_pairs([1, 1, 3, 4, 5, 6, 7, 8, 9]) == 5, "Test case 2 failed"
    assert find_unique_pairs([10, 11, 11, 11, 12]) == 6, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This solution leverages a `defaultdict` to count occurrences of each number and then iterates through the list to find and count the pairs that satisfy the given condition.