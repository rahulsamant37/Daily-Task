# DSA Problem 291

'''
Problem Statement:
A "bouncy" number is defined as a positive integer that is neither increasing nor decreasing. For example, 123 is not bouncy (it's increasing), 321 is not bouncy (it's decreasing), but 155349 is bouncy. Write a function `count_bouncy_numbers(ratio)` that takes a ratio as input (a float between 0 and 1) and returns the smallest positive integer n such that the proportion of bouncy numbers up to n (including n) is exactly the given ratio. 

Note:
- An increasing number has each digit greater than or equal to the previous digit.
- A decreasing number has each digit less than or equal to the previous digit.
- The ratio is the proportion of bouncy numbers among all numbers from 1 to n.
'''

Solution:
```python
def is_bouncy(num):
    increasing = decreasing = False
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if num_str[i] < num_str[i + 1]:
            increasing = True
        elif num_str[i] > num_str[i + 1]:
            decreasing = True
        if increasing and decreasing:
            return True
    return False

def count_bouncy_numbers(ratio):
    bouncy_count = 0
    total_count = 99  # Starting from 100, as numbers < 100 are not bouncy
    n = 100  # Start checking from 100

    while True:
        if is_bouncy(n):
            bouncy_count += 1
        if bouncy_count / total_count >= ratio:
            return n
        n += 1
        total_count += 1

# Function to check the correctness of the solution
def check_solution():
    print(count_bouncy_numbers(0.50))  # Example check for 50% ratio
    print(count_bouncy_numbers(0.90))  # Example check for 90% ratio

check_solution()
```

This code defines a function `count_bouncy_numbers` to find the smallest integer n where the proportion of bouncy numbers up to n matches the given ratio. It uses a helper function `is_bouncy` to determine if a number is bouncy. The solution iterates over integers starting from 100, counting bouncy numbers until the desired ratio is reached.