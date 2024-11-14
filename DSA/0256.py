# DSA Problem 256

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. Your task is to find the number of unique pairs of integers `(a, b)` in `nums` such that `a + b` is divisible by `k`. Note that the order of integers in the pair does not matter, i.e., `(a, b)` is considered the same as `(b, a)`.

For example, if `nums = [1, 2, 2, 3, 4]` and `k = 3`, the pairs that satisfy the condition are `(1, 2)`, `(1, 2)`, `(1, 2)`, and `(1, 2)`, making the total count 4.

Write a function `count_divisible_pairs(nums, k)` that returns the count of such pairs.
'''

Solution:
```python
from collections import defaultdict

def count_divisible_pairs(nums, k):
    remainder_counts = defaultdict(int)
    for num in nums:
        remainder_counts[num % k] += 1
    
    count = 0
    for i in range(k // 2 + 1):
        if i == 0 or (k % 2 == 0 and i == k // 2):
            count += remainder_counts[i] * (remainder_counts[i] - 1) // 2
        else:
            count += remainder_counts[i] * remainder_counts[k - i]
    
    return count

# Example check (This is not part of the solution, just for verification)
print(count_divisible_pairs([1, 2, 2, 3, 4], 3))  # Expected output: 4
```

In this solution, we first count the occurrences of each remainder when each number in the list is divided by `k`. Using this information, we calculate the number of valid pairs that satisfy the problem's condition.