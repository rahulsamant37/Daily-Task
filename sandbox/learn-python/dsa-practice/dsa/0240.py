# DSA Problem 240

'''
Problem Statement:
A "bouncy" number is defined as a positive integer whose digits neither increase nor decrease from left to right. For example, 1244133 is bouncy because it does not satisfy the property of being monotonically increasing (123) or decreasing (432). Write a function `count_bouncy_numbers` that takes an integer `n` and returns the number of bouncy numbers in the range [1, n]. Note that the numbers 123 and 321 are not bouncy, but 1244133 is.

Example:
- count_bouncy_numbers(50) should return 0, as there are no bouncy numbers between 1 and 50.
- count_bouncy_numbers(217) should return 1, as 134 is the first bouncy number in the range [1, 217].
'''

Solution:
```python
def count_bouncy_numbers(n):
    def is_bouncy(num):
        num_str = str(num)
        increasing = decreasing = True
        for i in range(len(num_str) - 1):
            if num_str[i] > num_str[i + 1]:
                increasing = False
            if num_str[i] < num_str[i + 1]:
                decreasing = False
        return not (increasing or decreasing)
    
    bouncy_count = 0
    for number in range(1, n + 1):
        if is_bouncy(number):
            bouncy_count += 1
    return bouncy_count

# Check function to verify the solution with provided data points
def check_solution():
    assert count_bouncy_numbers(50) == 0, "Test case 1 failed"
    assert count_bouncy_numbers(217) == 1, "Test case 2 failed"
    print("All test cases passed!")

check_solution()
```

This code defines a function `count_bouncy_numbers` which counts how many bouncy numbers are within a given range. It includes a helper function `is_bouncy` that determines if a single number is bouncy according to the definition provided.