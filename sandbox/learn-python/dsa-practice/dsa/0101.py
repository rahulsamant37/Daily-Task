# DSA Problem 101

'''
Problem Statement:
A "happy string" is defined as a string consisting only of the letters 'a', 'b', and 'c', where no two consecutive characters are the same. Given a positive integer `n`, how many unique "happy strings" of length `n` can be generated? Since the number can be very large, return your answer modulo `10^9 + 7`.

For example, if `n = 3`, some of the happy strings would be "abc", "bac", and "bca", but "aab" would not be a happy string because it has two consecutive 'a's.
'''

Solution:
```python
def count_happy_strings(n: int) -> int:
    MOD = 10**9 + 7
    
    # Initialize a list to hold the count of strings ending in 'a', 'b', and 'c' respectively.
    # Initially, with a string of length 1, there is exactly one string ending in 'a', 'b', and 'c'.
    count = [1, 1, 1]
    
    # For each additional character in the string (from length 2 to n),
    # we update the counts of strings ending in 'a', 'b', and 'c'.
    for _ in range(2, n + 1):
        # The number of strings of length i ending in 'a' is the sum of the strings of length i-1 ending in 'b' and 'c'.
        # Similarly, for 'b' and 'c'.
        new_count = [
            (count[1] + count[2]) % MOD,  # Ending in 'a'
            (count[0] + count[2]) % MOD,  # Ending in 'b'
            (count[0] + count[1]) % MOD,  # Ending in 'c'
        ]
        count = new_count
    
    # The total number of happy strings of length n is the sum of strings ending in 'a', 'b', and 'c'.
    return sum(count) % MOD

# Example usage:
print(count_happy_strings(3))  # Output: 12
```

This code calculates the number of unique "happy strings" of a given length `n` by dynamic programming, keeping track of the count of strings that end with each of the allowed characters ('a', 'b', or 'c') and making sure no two consecutive characters are the same.