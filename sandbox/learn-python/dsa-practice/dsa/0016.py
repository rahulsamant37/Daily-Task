# DSA Problem 16

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings. Your task is to find the maximum area of a rectangle formed by consecutive buildings. The width of each building is considered to be 1 unit.

For example, if the input list is [2, 1, 5, 6, 2, 3], the maximum rectangle area would be formed by the buildings with heights 5, 6, and 5 (or 2, 5, 6, 2), giving an area of 10 units.

Write a function `max_rectangle_area` that takes a list of integers and returns the maximum possible rectangle area.

Constraints:
- 1 <= len(building_heights) <= 10^5
- 1 <= building_heights[i] <= 10^4
'''

Solution:
def max_rectangle_area(building_heights):
    stack = []
    max_area = 0
    index = 0
    while index < len(building_heights):
        if not stack or building_heights[stack[-1]] <= building_heights[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = (building_heights[top] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
    
    while stack:
        top = stack.pop()
        area = (building_heights[top] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    
    return max_area

# Example check (You can remove or comment this part before submitting your solution)
print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected output: 10
print(max_rectangle_area([2, 4]))  # Expected output: 4
