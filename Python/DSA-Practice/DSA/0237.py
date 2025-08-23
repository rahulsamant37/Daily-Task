# DSA Problem 237

'''
Problem Statement:
Given a list of integers `nums`, you are to find the total number of unique pairs (i, j) where `nums[i]` is divisible by `nums[j]` and `i < j`. The pairs should be unique, meaning if there are multiple occurrences of the same pair, it should only be counted once. For example, if nums = [2, 4, 8, 4] then (2, 4) should only be counted once even though there are two 4s in the list.

Write a function `count_divisible_pairs(nums)` that returns the total number of such unique divisible pairs in the list.

Example:
- count_divisible_pairs([2, 4, 8, 4]) should return 4, because there are 4 unique pairs where one number is divisible by another: (2, 4), (2, 8), (4, 8), (2, 4) again (but counted only once).
'''

Solution:
```python
def count_divisible_pairs(nums):
    from collections import defaultdict

    nums.sort()  # Sort the list to ensure i < j for pairs (nums[i], nums[j])
    pair_count = 0
    seen_pairs = defaultdict(set)  # To track seen pairs and avoid counting duplicates

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] % nums[i] == 0 and nums[i] not in seen_pairs[nums[j]]:
                pair_count += 1
                seen_pairs[nums[j]].add(nums[i])  # Mark this pair as seen

    return pair_count

# Example check
print(count_divisible_pairs([2, 4, 8, 4]))  # Expected output: 4
```

Note: This solution takes into account that the pairs should be unique. By sorting the list first, we ensure that every comparison `nums[j] % nums[i]` where `i < j` is only made once, effectively avoiding counting the same pair twice. The use of a `defaultdict` with sets (`seen_pairs`) helps in tracking which pairs have already been counted, especially in the case where the list might contain duplicate values.