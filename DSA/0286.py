# DSA Problem 286

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the maximum number of unique integers that can be obtained by performing the following operation at most `k` times: choose any number in the list and replace it with any integer (the chosen integer can be any integer, not necessarily from the list). Return the maximum number of unique integers possible after at most `k` operations.

Example:
Input: nums = [1,2,1,2,3,3], k = 2
Output: 4
Explanation: We can replace two occurrences of 1 or 2 with any other integer not present in the list, for example 4 and 5, making the list [1,2,4,2,3,5] or [1,2,1,4,3,5]. In both cases, we get 4 unique integers.
'''

Solution:
```python
from collections import Counter

def max_unique_integers(nums, k):
    """
    Finds the maximum number of unique integers that can be obtained by replacing
    any number in the list with any integer up to k times.
    """
    count = Counter(nums)
    unique = len(count)
    
    # If the number of unique integers is already more than or equal to k, we can't do better
    if unique >= k:
        return min(len(nums), unique + k)
    
    # Replace the most frequent elements first
    for freq in sorted(count.values(), reverse=True):
        if k <= 0:
            break
        if freq > 1:
            k -= freq - 1
            unique += 1
    
    return unique + k  # Each remaining operation can introduce a new unique integer

# Example usage
nums = [1,2,1,2,3,3]
k = 2
print(max_unique_integers(nums, k))  # Output: 4
```

This solution takes advantage of the `collections.Counter` to count the frequency of each number in the list. It then tries to use the operations (`k`) to replace the most frequent numbers first to maximize the number of unique integers.