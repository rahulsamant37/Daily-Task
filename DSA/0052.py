# DSA Problem 52

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings in a city skyline. Your task is to determine the maximum area of a rectangle that can be formed by any number of consecutive buildings. The width of each building is considered to be 1 unit.

For example, if the heights of the buildings are [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10 square units (formed by the buildings with heights 5, 6, 2).

Write a function `max_rectangle_area` that takes a list of integers as input and returns the maximum area of a rectangle that can be formed.

Constraints:
- The list can contain between 1 and 10^5 buildings.
- The height of each building is between 1 and 10^4.
'''

Solution:
```python
def max_rectangle_area(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

# Example test case
print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected output: 10
```

The solution uses a stack to keep track of buildings that are not yet part of the largest rectangle. The algorithm iterates over each building, and for each building, it calculates the area of the rectangle that can be formed with the current building as the shortest building. This is done by popping buildings from the stack until a shorter or equal building is found, calculating the area, and updating the maximum area if necessary.