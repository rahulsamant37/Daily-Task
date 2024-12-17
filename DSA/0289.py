# DSA Problem 289

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the number of unique pairs (i, j) where `i < j` and the difference between `nums[i]` and `nums[j]` is exactly `k`.

For example, if `nums = [1, 5, 3, 4, 2]` and `k = 2`, the pairs with a difference of 2 are (1, 3) and (3, 5). Note that (4, 2) is not considered because i should be less than j.

Your task is to write a function `count_pairs_with_diff(nums, k)` that returns the total number of such unique pairs.
'''

Solution:
```python
def count_pairs_with_diff(nums, k):
    from collections import defaultdict

    num_count = defaultdict(int)
    pair_count = 0

    for num in nums:
        # Check for pairs with the current number as the higher number
        pair_count += num_count[num - k]
        # Check for pairs with the current number as the lower number
        pair_count += num_count[num + k]

        # Record the occurrence of the current number
        num_count[num] += 1

    return pair_count

# Example check function
def check_solution():
    assert count_pairs_with_diff([1, 5, 3, 4, 2], 2) == 3, "Test case 1 failed"
    assert count_pairs_with_diff([1, 2, 3, 4, 5], 1) == 4, "Test case 2 failed"
    assert count_pairs_with_diff([1, 3], 3) == 0, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This solution uses a dictionary to keep track of the occurrence of each number in the list and calculates the number of pairs by checking if the complement (number ± k) exists for each number encountered.