# DSA Problem 38

'''
Problem Statement:
You are given a list of integers representing the heights of buildings in a city skyline. A city has a unique characteristic where the buildings are arranged in such a way that the skyline is symmetrical. However, due to recent construction, the skyline is no longer perfectly symmetrical. Your task is to find the minimum number of buildings that need to be resized (either increased or decreased in height) to make the skyline symmetrical again. You can resize any building to any height.

For example, if the skyline is represented by the array [1, 2, 3, 4, 3, 2, 2], you could resize the last building to make the skyline symmetrical: [1, 2, 3, 4, 3, 2, 1]. The goal is to find the minimum number of such resizing operations needed.
'''

Solution:
```python
def min_building_resizes(skyline):
    """
    Finds the minimum number of buildings that need to be resized to make the skyline symmetrical.
    """
    resizes = 0
    left, right = 0, len(skyline) - 1
    
    while left < right:
        if skyline[left] != skyline[right]:
            resizes += 1
        left += 1
        right -= 1
    
    return resizes

# Check function to verify the solution with provided data points
def check_solution():
    assert min_building_resizes([1, 2, 3, 4, 3, 2, 2]) == 1, "Test case 1 failed"
    assert min_building_resizes([5, 3, 3, 4, 2, 2, 1]) == 3, "Test case 2 failed"
    assert min_building_resizes([1, 2, 3, 3, 2, 1]) == 0, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This Python code snippet defines a function `min_building_resizes` that calculates the minimum number of buildings that need to be resized to make the skyline symmetrical. The function iterates over the array from both ends towards the center, counting the number of positions where the buildings do not match, which indicates a required resize. The `check_solution` function verifies the correctness of the solution using predefined test cases.