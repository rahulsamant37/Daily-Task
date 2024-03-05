# DSA Problem 2

'''
Problem Statement:
You are given a list of integers `nums` and a positive integer `k`. You need to find the number of unique pairs (i, j) in the list such that the absolute difference between `nums[i]` and `nums[j]` is exactly `k`. Note that (i, j) and (j, i) are considered the same pair, so they should only be counted once.

For example, if `nums = [1, 5, 3, 4, 2]` and `k = 2`, the valid pairs are (1, 3), (2, 4), and (3, 5), making the total count 3.

Write a function `count_pairs_with_diff_k(nums, k)` that returns the total number of such unique pairs.
'''

Solution:
```python
def count_pairs_with_diff_k(nums, k):
    from collections import Counter
    
    # Count the frequency of each number in nums
    num_counts = Counter(nums)
    count = 0
    
    # For each unique number in the list, check if there is another number
    # that, when subtracted from it, gives a difference of k
    for num in num_counts:
        if num + k in num_counts:
            count += num_counts[num] * num_counts[num + k]
    
    return count

# Example check function
def check_solution():
    assert count_pairs_with_diff_k([1, 5, 3, 4, 2], 2) == 3
    assert count_pairs_with_diff_k([1, 2, 2, 1], 1) == 4
    assert count_pairs_with_diff_k([1, 3], 3) == 0
    print("All test cases passed.")

check_solution()
```

This Python code defines a function that efficiently counts the number of unique pairs in a list `nums` that have a difference of `k`, using a hash map (`Counter`) to track the frequency of each number. This allows the function to iteratively check for the presence of a complement number that would form a valid pair with the current number, leading to an optimal solution.