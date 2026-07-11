# DSA Problem 324

'''
Problem Statement:
You are given a list of integers representing the heights of various buildings in a city skyline. Your task is to calculate the total area of the silhouette formed by these buildings when viewed from the side. Assume each building has a width of 1 and is placed next to each other without any gaps. For example, a list [2, 1, 3] would form a silhouette that has an area of 6 square units (2*1 + 1*1 + 3*1).

Write a Python function `calculate_silhouette_area` that takes a list of non-negative integers as input and returns the total area of the silhouette formed by the buildings.

Example:
- calculate_silhouette_area([2, 1, 3]) should return 6.
- calculate_silhouette_area([4, 2, 0, 3, 2, 5]) should return 22.
'''

Solution:
```python
def calculate_silhouette_area(buildings):
    """
    Calculate the total area of the silhouette formed by a list of buildings.
    
    :param buildings: List of non-negative integers representing the heights of the buildings.
    :return: The total area of the silhouette formed by the buildings.
    """
    return sum(buildings)

# Test the function with provided data points
print(calculate_silhouette_area([2, 1, 3]))  # Expected output: 6
print(calculate_silhouette_area([4, 2, 0, 3, 2, 5]))  # Expected output: 22
```

This code defines a function that calculates the total silhouette area as described, using a straightforward approach by summing up the heights of the buildings.