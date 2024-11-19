# DSA Problem 261

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings from left to right. A building is considered a "skyline building" if no other building is taller than it when viewed from the left, and there are no taller buildings to its right up to the end of the list. Write a function `count_skyline_buildings` that takes in a list of integers and returns the number of skyline buildings.

For example:
- In the list [3, 7, 8, 4], buildings with heights 7 and 8 are skyline buildings.
- In the list [3, 7, 5, 4], the building with height 7 is the only skyline building.
'''

Solution:
```python
def count_skyline_buildings(building_heights):
    if not building_heights:
        return 0
    
    # Initialize the count of skyline buildings and the maximum height seen so far from the left
    skyline_count = 0
    left_max = building_heights[0]
    
    # Initialize a list to store the maximum heights from the right
    right_maxes = [0] * len(building_heights)
    right_maxes[-1] = building_heights[-1]
    
    # Fill the right_maxes array with the highest building to the right of each position
    for i in range(len(building_heights) - 2, -1, -1):
        right_maxes[i] = max(right_maxes[i + 1], building_heights[i + 1])
    
    # Determine if a building is a skyline building
    for i in range(len(building_heights)):
        if building_heights[i] > left_max and (i == len(building_heights) - 1 or building_heights[i] > right_maxes[i]):
            skyline_count += 1
        left_max = max(left_max, building_heights[i])
    
    return skyline_count
```

This solution correctly identifies and counts skyline buildings based on the given definition. It first calculates the maximum building heights to the right of each building, then iterates through the buildings to check if they are taller than all buildings to their left and right, counting those that are.