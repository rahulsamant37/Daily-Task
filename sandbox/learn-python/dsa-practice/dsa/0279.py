# DSA Problem 279

'''
Problem Statement:
A sequence of positive integers `nums` is given. You can perform the following operation any number of times:
- Pick any two distinct indices `i` and `j` in the sequence, and if `nums[i]` and `nums[j]` share the same highest prime factor, you can swap `nums[i]` and `nums[j]`.

After performing any number of these operations, find the lexicographically largest sequence that can be obtained. Return the modified sequence.

Note:
- The highest prime factor of a number is the largest prime number that divides the number.
- If two numbers have the same highest prime factor, they can be freely swapped.
- The sequence is lexicographically larger if, at the first position where the sequences differ, the sequence has a larger number.
'''

Solution:
```python
from typing import List
from math import sqrt
from collections import defaultdict

def highest_prime_factor(n: int) -> int:
    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n >>= 1
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n // i
    if n > 2:
        max_prime = n
    return max_prime

def lexicographically_largest_sequence(nums: List[int]) -> List[int]:
    highest_prime_factors = [highest_prime_factor(num) for num in nums]
    groups = defaultdict(list)
    
    for i, prime in enumerate(highest_prime_factors):
        groups[prime].append(nums[i])
    
    for group in groups.values():
        group.sort(reverse=True)
    
    result = []
    for prime in highest_prime_factors:
        num = groups[prime].pop()
        result.append(num)
    
    return result

# Example check (you can modify the input list to test different cases)
print(lexicographically_largest_sequence([8, 12, 6, 24, 18]))
```

This Python solution addresses the problem by first calculating the highest prime factor for each number in the sequence. Then, it groups numbers with the same highest prime factor together. By sorting each group in reverse order, it ensures that when numbers are placed back into their original positions, the sequence is lexicographically as large as possible under the given constraints.