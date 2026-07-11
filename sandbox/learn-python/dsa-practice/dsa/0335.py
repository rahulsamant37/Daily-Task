# DSA Problem 335

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. Your task is to find the maximum number of unique pairs of numbers in the list whose sum is divisible by `k`. A number can be part of only one pair. Return the maximum number of such pairs.

Example:
For the input nums = [1, 2, 3, 4, 5, 6] and k = 3, the function should return 3, as we can form 3 pairs: (1, 2), (3, 6), and (4, 5), each sum of which is divisible by 3.
'''

Solution:
```python
from collections import Counter

def max_divisible_pairs(nums, k):
    remainders = Counter([n % k for n in nums])
    count = min(remainders[0] // 2, remainders[0])  # Pairs with remainder 0
    
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += min(remainders[i], remainders[k - i])
        else:
            count += remainders[i] // 2  # Self-complementary pairs
            
    return count

# Test the function
nums = [1, 2, 3, 4, 5, 6]
k = 3
print(max_divisible_pairs(nums, k))  # Output should be 3
```

This Python solution efficiently counts the number of pairs whose sum is divisible by `k` using the remainder when divided by `k` and leveraging the `Counter` class to keep track of remainders.