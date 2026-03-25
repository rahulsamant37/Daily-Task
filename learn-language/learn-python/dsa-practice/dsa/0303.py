# DSA Problem 303

'''
Problem Statement:
Given a list of integers `nums`, and an integer `k`, write a function `find_kth_unique` that returns the kth unique (non-duplicate) integer from the list when sorted. If there are fewer than k unique integers in the list, return -1.

For example, if the input list is [7, 3, 3, 9, 2, 2, 7] and k = 2, the unique numbers are [7, 3, 9, 2]. When sorted, they become [2, 3, 7, 9]. The second unique number here is 3.

Constraints:
- 1 <= len(nums) <= 10^5
- 0 <= nums[i] <= 10^5
- 1 <= k <= len(nums)
'''

Solution:
```python
def find_kth_unique(nums, k):
    from collections import Counter
    
    # Count the occurrences of each number
    num_counts = Counter(nums)
    
    # Filter the numbers that occur exactly once and sort them
    unique_nums = sorted([num for num, count in num_counts.items() if count == 1])
    
    # Check if k is within the bounds of unique numbers
    if k <= 0 or k > len(unique_nums):
        return -1
    else:
        return unique_nums[k-1]

# Example check function
def check_solution():
    assert find_kth_unique([7, 3, 3, 9, 2, 2, 7], 2) == 3, "Test case 1 failed"
    assert find_kth_unique([1, 2, 2, 3, 4], 3) == 4, "Test case 2 failed"
    assert find_kth_unique([1, 1, 1, 1], 1) == -1, "Test case 3 failed"
    print("All test cases passed")

check_solution()
```

This code snippet defines a function `find_kth_unique` that takes a list of integers and an integer `k` as inputs and returns the kth unique integer from the list, following the problem statement. It uses the `collections.Counter` class to count occurrences of each integer, filters out the unique ones, sorts them, and then selects the kth element. If `k` is out of bounds for the list of unique elements, it returns -1. The `check_solution` function provides a few test cases to validate the solution.