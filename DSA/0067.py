# DSA Problem 67

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings. Your task is to find the largest rectangular area possible in the histogram formed by these buildings. The width of each building is 1 unit. For example, if the heights are [2, 1, 5, 6, 2, 3], the largest rectangular area is 10 units (formed by the buildings with heights 5, 6, and 2).

Write a function `max_rectangle_area` that takes a list of integers and returns the area of the largest rectangle that can be formed.

Example:
- `max_rectangle_area([2, 1, 5, 6, 2, 3])` should return `10`.
- `max_rectangle_area([2, 4])` should return `4`.
'''

Solution:
```python
def max_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0
    while index < len(heights):
        if not stack or heights[stack[-1]] <= heights[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = (heights[top] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        area = (heights[top] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

# Test the function
print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Should return 10
print(max_rectangle_area([2, 4]))  # Should return 4
```

This Python solution uses a stack to keep track of the buildings (represented by their indices) that form the largest rectangle. It iterates through the heights, calculating the area for each building as if it were the shortest in the rectangle, and updates the maximum area found so far.