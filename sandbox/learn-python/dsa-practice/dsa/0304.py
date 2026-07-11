# DSA Problem 304

'''
Problem Statement:
You are given a list of integers representing the heights of consecutive buildings. You are allowed to increase the height of any building by 1 unit exactly once. Find the maximum possible height difference between any two buildings after performing this operation optimally.

For example, if the input list is [1, 5, 3, 9], you can increase the height of the building with height 1 to 2, making the maximum height difference 9 - 2 = 7.

Write a function `max_height_difference` that takes a list of integers and returns the maximum height difference possible after the operation.
'''

Solution:
```python
def max_height_difference(buildings):
    """
    Calculates the maximum height difference between any two buildings after
    increasing the height of any one building by 1 unit.
    """
    min_height = min(buildings)
    max_height = max(buildings)
    # If all buildings have the same height, the difference is 0 or 1 (if there's more than one building).
    if min_height == max_height:
        return 1 if len(buildings) > 1 else 0
    
    # The maximum possible difference after increasing any one building by 1
    max_diff = max_height - min_height
    # If the minimum height is the only occurrence of its value, adding 1 to it will change the min_height
    if buildings.count(min_height) == 1:
        max_diff = max(max_diff, max_height - (min_height + 1))
    
    return max_diff

# Example check function
def check_solution():
    assert max_height_difference([1, 3, 6]) == 5
    assert max_height_difference([1, 10, 9, 2]) == 9
    assert max_height_difference([5, 5, 5, 5]) == 1
    assert max_height_difference([2]) == 0
    print("All tests passed.")

check_solution()
```

This code defines a function that calculates the maximum possible difference in heights between any two buildings after increasing any single building's height by one unit. It includes a check function with some test cases to verify the correctness of the solution.