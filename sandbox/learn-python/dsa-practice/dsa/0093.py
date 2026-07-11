# DSA Problem 93

'''
Problem Statement:
Arun has a collection of unique postcards, each with a serial number from 1 to N. He decides to give some of these postcards to his friends. However, Arun is very particular about the serial numbers he gives away. He only gives away postcards if the serial number is a prime number. Given an integer N, your task is to find out how many postcards Arun will give away. Note: 1 is not considered a prime number.

For example, if N is 10, the prime numbers between 1 and 10 are 2, 3, 5, and 7. Hence, Arun will give away 4 postcards.
'''

Solution:
```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_postcards(N):
    """Count how many prime numbered postcards Arun will give away."""
    count = 0
    for num in range(2, N + 1):
        if is_prime(num):
            count += 1
    return count

# Example usage
N = 10
print(count_prime_postcards(N))  # Output: 4
```

This Python code defines a function `count_prime_postcards(N)` which takes an integer N as input and returns the count of prime numbered postcards Arun will give away, using a helper function `is_prime(n)` to check the primality of each number in the range from 2 to N.