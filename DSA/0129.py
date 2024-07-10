# DSA Problem 129

'''
Problem Statement:
You are given a list of integers representing the heights of a row of buildings. You can see a building if there is no taller or equal height building directly in front of it. Calculate the number of buildings you can see from the left side. For example, if the list of building heights is [3, 7, 8, 3, 6], you can see the buildings with heights 3, 7, and 8 from the left, as the subsequent buildings are not taller or equal in height. Thus, the answer is 3.

Write a function `count_visible_buildings` that takes a list of non-negative integers representing building heights and returns the number of buildings visible from the left.

Example:
- count_visible_buildings([3, 7, 8, 3, 6]) should return 3.
- count_visible_buildings([1, 4, 2, 0, 5, 6, 3]) should return 4.
- count_visible_buildings([0, 1, 2, 3, 4, 5]) should return 6.
'''

Solution:
```python
def count_visible_buildings(building_heights):
    """
    Counts the number of buildings visible from the left side.
    """
    if not building_heights:
        return 0

    visible_count = 1  # The first building is always visible
    current_max_height = building_heights[0]

    for height in building_heights[1:]:
        if height > current_max_height:
            visible_count += 1
            current_max_height = height

    return visible_count

# Check function with provided data points
print(count_visible_buildings([3, 7, 8, 3, 6]))  # Expected output: 3
print(count_visible_buildings([1, 4, 2, 0, 5, 6, 3]))  # Expected output: 4
print(count_visible_buildings([0, 1, 2, 3, 4, 5]))  # Expected output: 6
```

This problem focuses on iterating through a list while keeping track of the tallest building seen so far, ensuring an efficient solution with a time complexity of O(n), where n is the number of buildings.