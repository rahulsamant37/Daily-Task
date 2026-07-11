# DSA Problem 177

'''
Problem Statement:
A sequence of integers is called harmonic if the difference between any two consecutive numbers is the same. Given a list of integers, count the number of ways to choose three distinct indices (i, j, k) such that i < j < k and the numbers at these indices form a harmonic sequence. Note that the difference must be the same for the pairs (arr[j] - arr[i]) and (arr[k] - arr[j]).

For example, in the list [5, 10, 15, 20], the triplet (10, 15, 20) forms a harmonic sequence because the difference between consecutive numbers is 5.

Write a function `count_harmonic_triplets(arr)` that takes a list of integers as input and returns the number of harmonic triplets.
'''

Solution:
```python
from collections import defaultdict

def count_harmonic_triplets(arr):
    n = len(arr)
    count = 0
    # Dictionary to store the number of times a difference has occurred up to index j
    diff_count = defaultdict(lambda: defaultdict(int))
    
    for j in range(n):
        for i in range(j):
            diff = arr[j] - arr[i]
            count += diff_count[i][diff]
            diff_count[j][diff] += 1
            
    return count

# Example usage:
arr = [5, 10, 15, 20]
print(count_harmonic_triplets(arr))  # Output should be 1
```

This Python solution uses dynamic programming with a dictionary to keep track of the differences between numbers, counting how many harmonic triplets can be formed as it iterates through the list.