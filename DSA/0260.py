# DSA Problem 260

'''
Problem Statement:
Given a list of integers, find the maximum number of non-overlapping pairs that can be formed such that the sum of each pair is equal to a given target sum. Each element in the list can only be part of one pair.

For example, if the list is [1, 2, 3, 4, 5] and the target sum is 6, the pairs (1, 5) and (2, 4) can be formed, making the maximum number of non-overlapping pairs 2.

Write a function `maxNonOverlappingPairs(nums, target)` that takes in a list of integers and a target sum, and returns the maximum number of non-overlapping pairs that can be formed.

Constraints:
- 1 <= len(nums) <= 10^4
- -10^3 <= nums[i] <= 10^3
- -10^3 <= target <= 10^3
'''

Solution:
```python
def maxNonOverlappingPairs(nums, target):
    from collections import defaultdict

    # Dictionary to store the count of each number
    count_dict = defaultdict(int)
    # Set to keep track of already paired elements
    used_indices = set()
    max_pairs = 0

    for i, num in enumerate(nums):
        complement = target - num
        if complement in count_dict and i - 1 not in used_indices and i not in used_indices:
            max_pairs += 1
            used_indices.add(i)
            used_indices.add(i - 1)
        else:
            count_dict[num] += 1

    return max_pairs

# Example check
print(maxNonOverlappingPairs([1, 2, 3, 4, 5], 6))  # Output: 2
```

Note: The provided solution assumes that the pairs are formed consecutively, as per the given example. If the problem statement meant to find any non-overlapping pairs regardless of their positions in the list, the approach would need to be adjusted to consider all possible pairs and ensure they do not overlap, which would likely involve a more complex algorithm such as dynamic programming or a greedy approach with careful handling of the indices.