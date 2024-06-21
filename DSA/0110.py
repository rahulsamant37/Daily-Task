# DSA Problem 110

'''
Problem Statement:
You are given a list of positive integers representing the heights of different towers. Your task is to find the maximum area of a rectangle that can be formed by these towers. The area of a rectangle is computed as the height of the tower (which will be the height of the rectangle) multiplied by the width (number of consecutive towers of at least that height).

For example, if the list of tower heights is [2, 1, 5, 6, 2, 3], the maximum rectangle area that can be formed is 10 (using the towers of heights 5 and 6, with a width of 2).

Write a function `max_rectangle_area` that takes a list of positive integers as input and returns the maximum area of a rectangle that can be formed.

Example:
- Input: [2, 1, 5, 6, 2, 3]
- Output: 10
'''

Solution:
```python
def max_rectangle_area(heights):
    stack = []
    max_area = 0
    # Add a zero to the end to ensure remaining bars are processed
    heights.append(0)
    
    for i, h in enumerate(heights):
        # Process bars that are taller than the current one
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

# Test the function
print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected output: 10
```

This Python solution uses a stack to keep track of the indices of the towers as it iterates through the list of heights. It calculates the area of rectangles that can be formed by each tower acting as the shortest tower (height) and updates the maximum area accordingly.