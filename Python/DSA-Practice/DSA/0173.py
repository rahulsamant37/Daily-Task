# DSA Problem 173

'''
Problem Statement:
You are given a list of integers representing the heights of a series of walls. Your task is to determine the maximum area of a rectangle that can be formed with the walls such that the rectangle's sides are parallel to the walls. The area is calculated as the product of the height (minimum height of the two walls forming the rectangle) and the width (distance between the two walls).

For example, if the list of heights is [2, 1, 5, 6, 2, 3], the maximum area of the rectangle would be 10, formed by the height of 2 and the width of 5 (from index 2 to index 5).

Write a function `max_rectangle_area(heights)` that takes in a list of positive integers representing the heights of the walls and returns the maximum area of the rectangle that can be formed.

Constraints:
- 2 <= len(heights) <= 10^5
- 1 <= heights[i] <= 10^4
'''

Solution:
```python
def max_rectangle_area(heights):
    stack = []
    max_area = 0
    # Add a zero to the end to ensure all heights are processed
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

# Example check
print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected output: 10
```

This solution uses a stack to maintain a list of heights in increasing order. When a shorter height is encountered, it calculates the area of the rectangle that can be formed with the top of the stack as the height and updates the maximum area if the calculated area is larger.