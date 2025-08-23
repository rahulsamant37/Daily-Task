# DSA Problem 277

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings in a straight line. Your task is to find the maximum rectangular area that can be formed between two buildings, such that the shorter building's height determines the height of the rectangle. The width of the rectangle is the distance between the two buildings. Return the maximum possible area.

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The maximum area is formed by a height of 2 (the shorter building) and a width of 5 (distance between the first and the fifth building).

Constraints:
- 2 <= len(heights) <= 10^5
- 1 <= heights[i] <= 10^4
'''

Solution:
def max_rectangle_area(heights):
    max_area = 0
    stack = []
    # Add a 0 to the end to ensure all buildings are processed
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, width * height)
        stack.append(i)
    return max_area

# Example usage
heights = [2,1,5,6,2,3]
print(max_rectangle_area(heights))  # Output: 10
'''

This problem is a variation of the "Largest Rectangle in Histogram" problem and can be solved using a stack to keep track of the buildings that are currently being considered for forming the maximum area. The logic involves iterating through the list of building heights and using a stack to determine the width and height of potential maximum rectangular areas.