# DSA Problem 77

'''
Problem Statement:
A "bouncy" number is a positive integer whose digits neither increase nor decrease. For example, 123 is not bouncy (it's strictly increasing), 321 is not bouncy (it's strictly decreasing), but 155349 is bouncy. Write a function `bouncy_ratio` that takes an integer `n` and returns the least positive integer `m` such that exactly `n` percent of the numbers less than or equal to `m` are bouncy. 

Note:
- Assume `n` is between 1 and 99, inclusive.
- The percentage is rounded to the nearest integer.
'''

Solution:
```python
def bouncy_ratio(n):
    def is_bouncy(num):
        num_str = str(num)
        increasing = decreasing = True
        for i in range(len(num_str) - 1):
            if num_str[i] > num_str[i + 1]:
                increasing = False
            if num_str[i] < num_str[i + 1]:
                decreasing = False
        return not increasing and not decreasing

    total = bouncy = 0
    m = 99  # Start from 99 as numbers below are not likely to be bouncy
    while True:
        m += 1
        total += 1
        if is_bouncy(m):
            bouncy += 1
        if round(bouncy / total * 100) == n:
            return m

# Test the function with a couple of data points
print(bouncy_ratio(50))  # Example output for 50%
print(bouncy_ratio(90))  # Example output for 90%
```

This code snippet defines a function `bouncy_ratio` that computes the least integer `m` such that `n` percent of the numbers less than or equal to `m` are bouncy. It includes a helper function `is_bouncy` to determine if a given number is bouncy. The function iterates upwards from 99 (since all numbers up to 99 are either strictly increasing or decreasing) and calculates the ratio until it matches the target `n` percentage.