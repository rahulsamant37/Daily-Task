# DSA Problem 112

'''
Problem Statement:
You are given a list of integers representing the heights of different bars in a histogram. Each bar has a width of 1. Your task is to find the area of the largest rectangle that can be formed within the histogram.

For example, given the list of heights [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10 units. The rectangle is formed by the bars with heights 5 and 6.

Write a function `largest_rectangle_area` that takes a list of integers as input and returns the area of the largest rectangle that can be formed.

Constraints:
- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^5
'''

Solution:
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    p = 0
    while p < len(heights):
        if not stack or heights[stack[-1]] <= heights[p]:
            stack.append(p)
            p += 1
        else:
            top = stack.pop()
            area = (heights[top] * ((p - stack[-1] - 1) if stack else p))
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        area = (heights[top] * ((p - stack[-1] - 1) if stack else p))
        max_area = max(max_area, area)
    return max_area

# Test the function
heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_area(heights))  # Output should be 10
'''
This problem involves using a stack to keep track of the bars that can potentially form the largest rectangle. The algorithm traverses the list of heights once, making it efficient even for large inputs.
'''