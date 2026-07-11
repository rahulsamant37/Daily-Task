# DSA Problem 48

'''
Problem Statement:
You are given a list of integers representing the heights of bars in a histogram where the width of each bar is 1. Write a function to find the area of the largest rectangle that can be formed within the histogram.

For example, if the heights of the bars are [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10 units.

Constraints:
- 1 <= len(heights) <= 10^5
- 1 <= heights[i] <= 10^4
'''

Solution:
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    p = 0
    while p < len(heights):
        if (not stack) or (heights[stack[-1]] <= heights[p]):
            stack.append(p)
            p += 1
        else:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * ((p - stack[-1] - 1) if stack else p))
            max_area = max(max_area, area)
    
    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] * ((p - stack[-1] - 1) if stack else p))
        max_area = max(max_area, area)
    
    return max_area

# Example usage
heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))  # Output: 10

This solution works by using a stack to keep track of the bars that form the potential largest rectangle. It iterates through the list of heights, calculating the area of rectangles that can be formed with each bar as the shortest bar. The time complexity of this solution is O(n), where n is the number of bars in the histogram.