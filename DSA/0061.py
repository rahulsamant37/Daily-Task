# DSA Problem 61

'''
Problem Statement:
You are given a list of integers representing the heights of different buildings in a straight line. You need to find out how many buildings can see the sunset. A building can see the sunset if there is no taller building to its right. For instance, if the heights are [4, 2, 3, 1], then the buildings with heights 4 and 3 can see the sunset.

Write a function `count_visible_buildings` that takes a list of positive integers representing the heights of buildings and returns the number of buildings that can see the sunset.

Example:
- count_visible_buildings([4, 2, 3, 1]) should return 2.
- count_visible_buildings([1, 2, 3, 4]) should return 4.
'''

Solution:
```python
def count_visible_buildings(buildings):
    """
    Counts how many buildings can see the sunset given their heights.
    
    :param buildings: List of integers representing the heights of buildings.
    :return: Integer count of buildings that can see the sunset.
    """
    visible_count = 0
    max_height = 0
    for height in reversed(buildings):
        if height > max_height:
            visible_count += 1
            max_height = height
    return visible_count

# Check function to verify the correctness of the solution
def check_solution():
    assert count_visible_buildings([4, 2, 3, 1]) == 2, "Test case 1 failed"
    assert count_visible_buildings([1, 2, 3, 4]) == 4, "Test case 2 failed"
    assert count_visible_buildings([4, 5, 3, 2, 1]) == 3, "Test case 3 failed"
    assert count_visible_buildings([10, 6, 8, 9, 11]) == 4, "Test case 4 failed"
    print("All test cases passed.")

check_solution()
```

This code snippet defines a function `count_visible_buildings` which calculates the number of buildings that can see the sunset based on their heights. It includes a check function with provided data points to verify the correctness of the generated function.