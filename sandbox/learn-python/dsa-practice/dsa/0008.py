# DSA Problem 8

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of adjacent buildings. You need to calculate the maximum rectangular area possible amongst all subarrays of the building heights. This area can be seen as the largest plot of flat land you could find between the buildings if you were to look at the skyline from the side.

For example, if the heights are [2, 1, 5, 6, 2, 3], the largest rectangle formed would have an area of 10, which can be achieved by considering the subarray [5, 6].

Write a function `max_rectangle_area` that takes a list of positive integers and returns the maximum rectangular area that can be formed.

Constraints:
- 1 <= len(heights) <= 10^5
- 1 <= heights[i] <= 10^4
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
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

# Example check (You can comment this part if it's a submission to a coding challenge)
print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected output: 10
```

This solution uses a stack to keep track of the buildings that form the largest rectangle area in a linear pass through the list, making it efficient for large lists as per the constraints.