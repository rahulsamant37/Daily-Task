# DSA Problem 21

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings. Your task is to calculate the total area of the shadow cast by these buildings when the sun is at a 45-degree angle. The shadow of each building extends to the next smaller building on its right, or to the end of the list if there is no smaller building.

For example, if the buildings' heights are [3, 1, 2, 4], the shadows would be cast as follows:
- The building of height 3 casts a shadow to the building of height 2.
- The building of height 1 casts a shadow to the end (since it's the smallest).
- The building of height 2 casts a shadow to the end.
- The building of height 4 casts a shadow to the end.

The shadow area for each building is the difference in height between the building and the next smaller building on its right, multiplied by the distance (number of buildings) to that next smaller building. If there's no smaller building, the shadow area is the height of the building multiplied by the distance to the end of the list.

Write a function `total_shadow_area` that takes a list of building heights and returns the total shadow area cast by all buildings.

Example:
- total_shadow_area([3, 1, 2, 4]) should return 8 (3*1 + 1*3 + 2*2 + 4*1).
- total_shadow_area([4, 6, 2, 8]) should return 16 (4*2 + 6*1 + 2*1 + 8*1).
'''

Solution:
```python
def total_shadow_area(heights):
    total_area = 0
    stack = []
    
    for i, height in enumerate(heights + [0]):
        distance = 0
        while stack and stack[-1][0] > height:
            h, d = stack.pop()
            distance += d
            total_area += (h - height) * distance
        stack.append((height, distance + 1))
    
    return total_area

# Check function with provided data points
print(total_shadow_area([3, 1, 2, 4]))  # Expected output: 8
print(total_shadow_area([4, 6, 2, 8]))  # Expected output: 16
```

This solution uses a stack to keep track of buildings and their distances. It iterates through each building's height, calculating the total shadow area cast by the current building based on the height difference and the distance to the next smaller building. The stack ensures that each building is considered only once, making the solution efficient.