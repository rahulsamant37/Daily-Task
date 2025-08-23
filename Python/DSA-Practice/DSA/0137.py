# DSA Problem 137

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings. Your task is to find the maximum area of a rectangle that can be formed by concatenating any number of consecutive buildings. The rectangle's width will be the number of buildings included, and its height will be the height of the shortest building in the selected range. For example, if the buildings' heights are [2, 1, 5, 6, 2, 3], the maximum rectangle area you can form is 10, using buildings with heights 5, 6, 2.

Write a function `max_rectangle_area` that takes a list of integers as input and returns the maximum area of the rectangle that can be formed as described above.

Example:
- max_rectangle_area([2, 1, 5, 6, 2, 3]) should return 10.
- max_rectangle_area([1, 2, 3, 4, 5]) should return 9.
- max_rectangle_area([5, 4, 3, 2, 1]) should return 9.
'''

Solution:
```python
def max_rectangle_area(heights):
    """
    Finds the maximum area of a rectangle formed by consecutive buildings.
    """
    heights.append(0)  # Add a zero height to ensure the stack is cleared
    stack = [-1]  # Initialize stack with -1 as the starting index
    max_area = 0
    
    for i, h in enumerate(heights):
        while heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

# Test cases
print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected output: 10
print(max_rectangle_area([1, 2, 3, 4, 5]))    # Expected output: 9
print(max_rectangle_area([5, 4, 3, 2, 1]))    # Expected output: 9
```

This solution uses a stack to keep track of the indices of the buildings' heights. It iterates through each building, and if the current building's height is lower than the height of the building at the top of the stack, it calculates the area of the rectangle that can be formed with the height of the building at the top of the stack and the width determined by the current index and the index at the top of the stack. This ensures that the area is calculated for all possible rectangles, and the maximum area is stored and returned.