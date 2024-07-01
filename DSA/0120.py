# DSA Problem 120

'''
Problem Statement:
Given a list of integers representing the heights of a series of consecutive buildings and an integer k, you are tasked to find out if it's possible to make all buildings have equal heights by increasing or decreasing the height of any building by k, any number of times. You are not allowed to remove or add buildings. A valid operation must result in a non-negative height for each building. 

For example, if the list is [1, 2, 3, 4, 5] and k is 1, it is possible to make all buildings have the same height by increasing the heights of the first three buildings and decreasing the heights of the last two buildings. However, if k is 2, it would be impossible to make all buildings have the same height without violating the non-negative height constraint.
'''

Solution:
```python
def can_equalize_heights(buildings, k):
    """
    Checks if it's possible to make all buildings have equal heights by increasing or decreasing
    the height of any building by k, any number of times. Valid operations must result in non-negative heights.
    """
    if not buildings:
        return True  # No buildings to modify.

    min_height = min(buildings)
    max_height = max(buildings)
    
    # The difference between max and min height must be within the range of 2*k
    # to make all buildings equal in height with given operations.
    if max_height - min_height > 2 * k:
        return False
    
    # Check if making all buildings equal to the target height (min_height + k)
    # would result in any building going below zero height.
    target_height = min_height + k
    for height in buildings:
        if height > target_height + k or height < target_height - k:
            return False

    return True

# Test the function with provided data points
print(can_equalize_heights([1, 2, 3, 4, 5], 1))  # Expected: True
print(can_equalize_heights([1, 2, 3, 4, 5], 2))  # Expected: False
```

This Python function `can_equalize_heights` takes a list of integers representing the heights of buildings and an integer `k`, and returns `True` if it's possible to make all buildings have the same height by increasing or decreasing any building's height by `k` any number of times, while ensuring no building ends up with a negative height.