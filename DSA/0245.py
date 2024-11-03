# DSA Problem 245

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the number of unique pairs `(nums[i], nums[j])` such that the absolute difference between `nums[i]` and `nums[j]` is exactly `k`. Note that `(nums[i], nums[j])` and `(nums[j], nums[i])` are considered the same pair, and `i` must not equal `j`.

For example, if nums = [1, 5, 3, 4, 2] and k = 2, the pairs are (1, 3) and (3, 5), so the function should return 2.
'''

Solution:
```python
def count_k_diff_pairs(nums, k):
    from collections import Counter
    
    # Count the occurrences of each number
    num_counts = Counter(nums)
    count = 0
    
    # For each unique number, check if there's a number that is exactly 'k' away from it
    for num in num_counts:
        if num + k in num_counts:
            count += num_counts[num] * num_counts[num + k]
    
    return count

# Example check function
def check_solution():
    assert count_k_diff_pairs([1, 5, 3, 4, 2], 2) == 3, "Test case 1 failed"
    assert count_k_diff_pairs([1, 2, 3, 4, 5], 1) == 4, "Test case 2 failed"
    assert count_k_diff_pairs([1, 3], 3) == 0, "Test case 3 failed"
    assert count_k_diff_pairs([6, 3, 5, 7, 2, 3, 3, 8, 2, 4], 2) == 5, "Test case 4 failed"
    print("All test cases passed!")

check_solution()
```

This Python code snippet defines a function `count_k_diff_pairs` that solves the problem as described. A check function `check_solution` is also provided to verify the correctness of the solution with several test cases.