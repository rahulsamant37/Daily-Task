# DSA Problem 161

'''
Problem Statement:
You are given a list of integers representing the heights of various towers. Your task is to find the maximum rectangular area formed by these towers. Each tower has a width of 1 unit. You need to return the area of the largest rectangle that can be formed.

Example:
Input: [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: The largest rectangle has a height of 5 and a width of 2, thus the area is 10.
'''

Solution:
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    index = 0
    while index < len(heights):
        if not stack or (heights[stack[-1]] <= heights[index]):
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

# Test the function
print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Expected output: 10

# Explanation of the function:
# This function uses a stack to keep track of the towers that are part of the current largest rectangle.
# It iterates through each tower, calculating the area whenever a taller tower is found, and updates the maximum area found.
# After iterating through all the towers, it processes any remaining towers in the stack to calculate the area.
# The function returns the maximum area found.

# The solution is optimal with a time complexity of O(n) due to the single pass through the list and each element being pushed or popped from the stack at most once.