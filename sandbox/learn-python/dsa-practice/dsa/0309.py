# DSA Problem 309

'''
Problem Statement:
You are given a list of positive integers representing the heights of buildings in a city skyline. Your task is to find the maximum area of a rectangle that can be formed by a contiguous sequence of buildings, where the width of the rectangle is the number of buildings and the height is the minimum height among the selected buildings.

For example, if the list of building heights is [2, 1, 5, 6, 2, 3], the maximum rectangle area is 10, which is formed by the buildings with heights 5, 6, and 2.

Write a function `max_rectangle_area` that takes in a list of positive integers and returns the maximum rectangle area as an integer.
'''

Solution:
def max_rectangle_area(heights):
    stack = []
    max_area = 0
    p = 0
    while p < len(heights):
        if not stack or heights[stack[-1]] <= heights[p]:
            stack.append(p)
            p += 1
        else:
            top = stack.pop()
            # Calculate the width of the rectangle
            width = (p - stack[-1] - 1) if stack else p
            max_area = max(max_area, heights[top] * width)
    
    while stack:
        top = stack.pop()
        width = (p - stack[-1] - 1) if stack else p
        max_area = max(max_area, heights[top] * width)
    
    return max_area

# Test the function
heights = [2, 1, 5, 6, 2, 3]
print(max_rectangle_area(heights))  # Expected output: 10

This solution uses a stack-based approach to efficiently compute the maximum rectangle area. It iterates through the list of heights, maintaining a stack to keep track of the indices of the buildings that form potential rectangles with increasing heights. When a shorter building is encountered, it calculates the area for the previously taller buildings that can no longer form a rectangle with the current building and updates the maximum area if necessary.