# DSA Problem 172

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings in a city skyline. Your task is to find the maximum number of buildings that can be seen from the left side of the skyline. A building is considered visible if there are no taller buildings to its left. 

For example, if the list of building heights is [3, 1, 5, 2, 6], the buildings that can be seen from the left are 3, 5, and 6. Therefore, the output should be 3.

Write a function `visible_buildings` that takes a list of integers and returns the number of buildings that can be seen from the left.

Constraints:
- The list will contain between 1 and 1000 elements.
- Each element will be an integer between 1 and 1000.
'''

Solution:
def visible_buildings(heights):
    """
    Returns the number of buildings visible from the left side of the skyline.
    """
    visible = 0
    current_max_height = 0
    for height in heights:
        if height > current_max_height:
            visible += 1
            current_max_height = height
    return visible

# Example check
print(visible_buildings([3, 1, 5, 2, 6]))  # Expected output: 3
print(visible_buildings([4, 2, 3]))  # Expected output: 2
print(visible_buildings([1, 2, 3, 4, 5]))  # Expected output: 5
print(visible_buildings([7, 6, 5, 4, 3, 2, 1]))  # Expected output: 1
```