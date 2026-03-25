# DSA Problem 35

'''
Problem Statement:
You are given a list of integers representing the heights of various towers. Your task is to find the maximum area of a rectangle that can be formed by a contiguous segment of these towers. The width of each tower is 1 unit.

For example, given a list of tower heights [2, 1, 5, 6, 2, 3], the maximum area of a rectangle that can be formed is 10 (formed by the segment [5, 6], with a width of 2 and a height of 5).

Write a function `max_rectangle_area` that takes a list of integers as input and returns the maximum area of a rectangle that can be formed.
'''

Solution:
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

# Test the function
heights = [2, 1, 5, 6, 2, 3]
print(max_rectangle_area(heights))  # Expected output: 10

This Python solution uses a stack to keep track of the indices of the towers. It iterates through the list of heights, calculating the maximum area of the rectangle that can be formed with each tower as the shortest tower. The stack helps in maintaining the indices of the towers in increasing order of their heights. When a shorter tower is encountered, the area for the previously encountered taller towers is calculated and the maximum area is updated.