# DSA Problem 350

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings viewed from a street level. You need to find the maximum rectangular area possible from the histogram formed by these buildings. The width of each building is considered to be 1 unit.

For example, if the heights of the buildings are given as [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10 units.

Write a function `max_rectangle_area` that takes a list of integers as input and returns the maximum area of the rectangle that can be formed.

Note:
- The list will contain at least one element and at most 10^5 elements.
- Each element in the list will be a positive integer not exceeding 10^4.
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
            top = stack.pop()
            area = (heights[top] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
    
    while stack:
        top = stack.pop()
        area = (heights[top] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

# Example usage:
# print(max_rectangle_area([2, 1, 5, 6, 2, 3]))  # Output: 10

'''
This solution uses a stack to keep track of the indices of the histogram's heights. It iterates through the list of heights, using the stack to calculate the maximum area of a rectangle that can be formed at each step. The stack ensures that the areas are calculated efficiently by maintaining the indices of the heights in non-decreasing order. This allows the algorithm to run in O(n) time complexity, making it suitable for large inputs.
'''