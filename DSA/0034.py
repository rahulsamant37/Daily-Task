# DSA Problem 34

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the number of unique pairs (i, j) in the list such that `nums[i] - nums[j] = k`, where `0 <= i, j < len(nums)` and `i != j`. Note that the pairs (i, j) and (j, i) are considered the same, so if `nums[i] - nums[j] = k`, you should not count both pairs.

For example, if nums = [2, 4, 1, 3, 5] and k = 2, the pairs are (1, 0), (2, 0), and (3, 2), so the answer would be 3.
'''

Solution:
```python
from collections import Counter

def find_unique_pairs(nums, k):
    if k < 0:
        return 0  # As the difference cannot be negative
    
    num_counts = Counter(nums)
    count = 0
    
    for num in num_counts:
        if num + k in num_counts:
            count += num_counts[num] * num_counts[num + k]
    
    return count

# Example usage
nums = [2, 4, 1, 3, 5]
k = 2
print(find_unique_pairs(nums, k))  # Output: 3
```

This solution leverages a `Counter` from the `collections` module to count occurrences of each number in the list. It then iterates through each unique number in the list, checking if there's another number in the list that when subtracted by the current number equals `k`. If such a pair is found, it increments the count by the product of the occurrences of both numbers, ensuring that all unique pairs are counted.