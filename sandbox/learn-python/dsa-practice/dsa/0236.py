# DSA Problem 236

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the number of unique pairs (i, j) in the list such that the absolute difference between `nums[i]` and `nums[j]` is exactly `k`. Note that the pairs (i, j) and (j, i) are considered the same, and `i` should not be equal to `j`.

For example, if `nums = [1, 5, 3, 4, 2]` and `k = 2`, the unique pairs with a difference of 2 are (1, 3), (3, 5), and (2, 4), so the answer would be 3.
'''

Solution:
```python
def count_pairs_with_difference(nums, k):
    num_set = set(nums)
    count = 0
    for num in num_set:
        if num + k in num_set:
            count += 1
    return count

# Example usage
nums = [1, 5, 3, 4, 2]
k = 2
print(count_pairs_with_difference(nums, k))  # Output: 3
```

This solution utilizes a set to ensure that each number is only considered once, which helps to efficiently find pairs with the required difference.