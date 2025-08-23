# DSA Problem 138

'''
Problem Statement:
Given a list of positive integers `nums`, and an integer `k`, find the maximum number of unique pairs (i, j) in the list such that the absolute difference between the elements at indices i and j is exactly `k`. Each pair (i, j) should satisfy i < j. Note that the same number can be used in multiple pairs as long as the pairs are unique.

For example, given the list [1, 3, 1, 5, 4] and k = 2, the function should return 2, as there are two pairs that satisfy the condition: (1, 3) and (3, 5).
'''

Solution:
```python
from collections import defaultdict

def find_pairs(nums, k):
    if k < 0:
        return 0
    num_counts = defaultdict(int)
    for num in nums:
        num_counts[num] += 1

    count = 0
    for num in num_counts:
        if k == 0:
            if num_counts[num] > 1:
                count += num_counts[num] // 2
        else:
            if num + k in num_counts:
                count += min(num_counts[num], num_counts[num + k])
    return count

# Example check function
def check_solution():
    assert find_pairs([1, 3, 1, 5, 4], 2) == 2
    assert find_pairs([1, 2, 3, 4, 5], 1) == 4
    assert find_pairs([1, 3, 1, 5, 4], 0) == 1
    assert find_pairs([1, 1, 1, 1], 0) == 2
    print("All test cases passed.")

check_solution()
```

Note: The solution provided above is a Python function that calculates the maximum number of unique pairs in the list `nums` such that the absolute difference between the elements of a pair is exactly `k`. The `check_solution` function is used to validate the correctness of the `find_pairs` function with predefined test cases.