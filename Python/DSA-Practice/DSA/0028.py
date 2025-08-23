# DSA Problem 28

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings in a city skyline. Your task is to find the maximum area of a rectangle that can be formed by any number of consecutive buildings. The width of each building is considered as 1 unit.

For example, if the heights of the buildings are given as [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10 units, formed by the buildings with heights [5, 6].

Write a function `maxRectangleArea` that takes a list of integers as input and returns the maximum area of a rectangle that can be formed.

Constraints:
- The list of heights will contain between 1 and 10^5 elements.
- Each element in the list will be an integer between 1 and 10^4.
'''

Solution:
def maxRectangleArea(heights):
    stack = []
    max_area = 0
    p = 0

    while p < len(heights):
        if not stack or heights[stack[-1]] <= heights[p]:
            stack.append(p)
            p += 1
        else:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((p - stack[-1] - 1) if stack else p))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((p - stack[-1] - 1) if stack else p))
        max_area = max(max_area, area)

    return max_area

# Example check
print(maxRectangleArea([2, 1, 5, 6, 2, 3]))  # Expected output: 10
'''
This solution utilizes a stack to keep track of buildings that form potential rectangles. It iterates through the list of building heights, calculating the maximum area whenever a smaller building is encountered (indicating the end of a potential rectangle). This ensures that all possible rectangle areas are considered, and the maximum is returned at the end. The time complexity of this solution is O(n), where n is the number of buildings.