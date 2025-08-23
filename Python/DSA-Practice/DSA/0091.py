# DSA Problem 91

'''
Problem Statement:
Given a list of integers, find the length of the longest subsequence where each element in the subsequence is a prime number and the difference between consecutive prime numbers is the same. For example, for the list [5, 7, 10, 11, 13, 17], the longest subsequence with the same difference between consecutive primes is [7, 11, 13] with a difference of 4. Write a function `longest_prime_arithmetic_sequence` that takes a list of integers and returns the length of the longest subsequence that satisfies the conditions.

Note: Assume the list contains at least one prime number.
'''

Solution:
```python
from itertools import combinations
from sympy import isprime

def longest_prime_arithmetic_sequence(nums):
    # Filter out non-prime numbers
    primes = [num for num in nums if isprime(num)]
    primes.sort()  # Sort the primes for easier combination generation
    longest_seq = 0

    # Generate all possible subsequences of primes
    for r in range(2, len(primes) + 1):
        for combo in combinations(primes, r):
            if is_arithmetic_sequence(combo):
                longest_seq = max(longest_seq, len(combo))

    return longest_seq

def is_arithmetic_sequence(seq):
    if len(seq) < 2:
        return False
    common_diff = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if seq[i] - seq[i-1] != common_diff:
            return False
    return True

# Example check
print(longest_prime_arithmetic_sequence([5, 7, 10, 11, 13, 17]))  # Output: 3
```

Explanation:
- The function `longest_prime_arithmetic_sequence` first filters out and sorts the prime numbers from the input list.
- It then generates all possible subsequences of these prime numbers and checks if they form an arithmetic sequence.
- The helper function `is_arithmetic_sequence` checks if the difference between consecutive elements in a sequence is the same.
- The function returns the length of the longest subsequence that meets the criteria.