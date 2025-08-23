# DSA Problem 302

'''
Problem Statement:
A sequence of positive integers is called a "jumping sequence" if for every pair of consecutive integers (a, b) in the sequence, b is greater than a and b is exactly a+2 or a+3. Given a positive integer n, find the total number of unique jumping sequences that start with 1 and have a length of n. Since the answer can be very large, return it modulo 10^9 + 7.

For example, if n = 4, two possible jumping sequences are [1, 3, 5, 7] and [1, 4, 6, 9].
'''

Solution:
```python
def countJumpingSequences(n: int) -> int:
    MOD = 10**9 + 7
    
    # dp[i] stores the count of jumping sequences of length i
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty sequence
    
    for i in range(1, n + 1):
        for j in range(i - 2, i - 3, -1):
            if j >= 0:
                dp[i] = (dp[i] + dp[j]) % MOD
    
    return dp[n] % MOD

# Example usage:
print(countJumpingSequences(4))  # Replace with actual expected output based on problem statement
```

This solution uses dynamic programming to efficiently calculate the number of unique jumping sequences. The `dp` array is used to store the count of sequences for each length, where `dp[i]` represents the number of sequences of length `i`. The loop iterates over possible previous sequence lengths that could logically lead up to the current length, updating the count accordingly. The result for `n` is returned modulo 10^9 + 7 to prevent overflow and meet the problem's requirements.