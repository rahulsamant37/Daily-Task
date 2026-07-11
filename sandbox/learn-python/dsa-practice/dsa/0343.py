# DSA Problem 343

'''
Problem Statement:
You are given a list of positive integers `nums` and a positive integer `k`. You need to find the number of unique pairs (i, j) in the list such that `nums[i] + nums[j]` is divisible by `k`. Note that (i, j) and (j, i) are considered the same pair and should be counted only once.

For example, if `nums = [1, 3, 2, 5, 4]` and `k = 3`, the valid pairs are (1, 2), (1, 5), (2, 4), and (3, 4) since the sums of these pairs are 3, 6, 6, and 7 respectively, and all of these sums are divisible by `k`.

Write a function `count_divisible_pairs(nums, k)` that returns the total number of such unique pairs.

Constraints:
- 1 <= len(nums) <= 10^4
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^5
'''

Solution:
```python
from collections import defaultdict

def count_divisible_pairs(nums, k):
    # Create a dictionary to store the frequency of remainders
    remainder_counts = defaultdict(int)
    for num in nums:
        remainder_counts[num % k] += 1
    
    count = 0
    # Handle the special cases for 0 and k/2 remainders
    count += remainder_counts[0] * (remainder_counts[0] - 1) // 2
    if k % 2 == 0:
        half = k // 2
        count += remainder_counts[half] * (remainder_counts[half] - 1) // 2
    
    # Handle the general cases for other remainders
    for i in range(1, (k + 1) // 2):
        count += remainder_counts[i] * remainder_counts[k - i]
    
    return count

# Example check (this is not part of the solution code):
# nums = [1, 3, 2, 5, 4]
# k = 3
# print(count_divisible_pairs(nums, k))  # Expected output: 4
```

This Python function `count_divisible_pairs` efficiently counts the number of unique pairs in the list `nums` whose sum is divisible by `k`. It leverages the properties of modular arithmetic to reduce the problem complexity.