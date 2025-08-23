# DSA Problem 176

'''
Problem Statement:
You are given a list of positive integers `nums` and an integer `k`. A pair of indices `(i, j)` is considered beautiful if `nums[i] + nums[j]` is divisible by `k` and `i < j`. Your task is to return the total number of beautiful pairs in the given list.

For example, given `nums = [2, 5, 1, 3]` and `k = 3`, the beautiful pairs are (0, 1) and (2, 3) because `(2+5) % 3 == 0` and `(1+3) % 3 == 0`.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^5
'''

Solution:
```python
from collections import defaultdict

def count_beautiful_pairs(nums, k):
    """
    Counts the number of beautiful pairs in the list nums.
    A pair (i, j) is beautiful if (nums[i] + nums[j]) % k == 0 and i < j.
    """
    remainder_counts = defaultdict(int)
    beautiful_pairs = 0
    
    for num in nums:
        remainder = num % k
        complement = (-remainder) % k  # Find the complement to form a multiple of k
        beautiful_pairs += remainder_counts[complement]
        remainder_counts[remainder] += 1
    
    return beautiful_pairs

# Example usage
nums = [2, 5, 1, 3]
k = 3
print(count_beautiful_pairs(nums, k))  # Output: 2
```

This solution efficiently counts the number of beautiful pairs by using the remainder when divided by `k` to track possible complements which can form a sum divisible by `k`. It utilizes a dictionary to keep track of the counts of remainders seen so far, and for each number, it calculates how many of its complements have been seen, adding this count to the total number of beautiful pairs.