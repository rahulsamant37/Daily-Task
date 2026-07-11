# DSA Problem 6

'''
Problem Statement:
A "jumping number" is defined as a number where all adjacent digits differ by exactly 1. For example, 123 and 321 are jumping numbers, but 124 and 359 are not. Given a positive integer `n`, write a function `countJumpingNumbers(n)` that returns the count of all jumping numbers less than or equal to `n`.

Example:
If n = 35, the function should return 15, as the jumping numbers less than or equal to 35 are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32.
'''

Solution:
```python
def countJumpingNumbers(n):
    if n < 10:
        return n + 1

    def dfs(num, last_digit):
        if num > n:
            return 0
        count = 1
        if last_digit > 0:
            count += dfs(num * 10 + (last_digit - 1), last_digit - 1)
        if last_digit < 9:
            count += dfs(num * 10 + (last_digit + 1), last_digit + 1)
        return count

    total_count = 10  # All single-digit numbers are jumping numbers
    for i in range(1, 10):
        total_count += dfs(i, i)
    
    return total_count

# Example check function
def check_solution():
    print(countJumpingNumbers(35))  # Expected output: 15

check_solution()
```

Note: This solution uses a depth-first search (DFS) approach to generate and count all jumping numbers up to `n`. The function `dfs` recursively builds jumping numbers starting from each digit 1-9 and counts them if they are less than or equal to `n`. The base case for the recursion is when the number exceeds `n`. The total count also includes all single-digit numbers (0-9) as all of them are considered jumping numbers.