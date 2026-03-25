# DSA Problem 163

'''
Problem Statement:
You are given a list of integers `nums` and a positive integer `k`. Your task is to find the number of unique pairs of indices (i, j) such that:
1. i < j
2. nums[i] + nums[j] is divisible by k

For example, if nums = [1, 2, 3, 4] and k = 3, the valid pairs are (1, 2) and (2, 4) since 1+2=3 and 2+4=6, both of which are divisible by k=3. Note that pairs are considered unique based on their indices, not their values.

Write a function `count_divisible_pairs(nums, k)` that returns the number of such pairs.
'''

Solution:
```python
def count_divisible_pairs(nums, k):
    from collections import defaultdict

    # Dictionary to hold the frequency of remainders when elements of nums are divided by k
    remainder_counts = defaultdict(int)
    count = 0

    for num in nums:
        # Calculate the remainder of num when divided by k
        remainder = num % k
        # Calculate the complement remainder which when added to remainder makes a number divisible by k
        complement = (k - remainder) % k

        # Add the count of numbers that have the complement remainder to the count of pairs
        count += remainder_counts[complement]

        # Increment the count of the current remainder
        remainder_counts[remainder] += 1

    return count

# Example check function
def check_solution():
    assert count_divisible_pairs([1, 2, 3, 4], 3) == 2
    assert count_divisible_pairs([4, 5, 1, 2], 4) == 2
    assert count_divisible_pairs([1, 2, 3, 4, 5], 5) == 4
    print("All test cases passed.")

check_solution()
```

This solution uses the concept of remainders and their complements to find pairs efficiently. The time complexity of this solution is O(n), where n is the length of the input list `nums`.