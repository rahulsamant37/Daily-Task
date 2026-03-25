# DSA Problem 26

'''
Problem Statement:
You are given a list of positive integers representing the heights of walls. Your task is to calculate how much rainwater can be trapped between the walls after a rain. The width of each wall is considered to be 1 unit. For example, given the heights [2, 1, 2], the amount of water trapped is 1 unit.

Write a function `trap` that takes in a list of integers and returns the total amount of trapped rainwater.

Example:
- Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
- Output: 6 units of water trapped
'''

Solution:
def trap(height):
    if not height:
        return 0

    water_trapped = 0
    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                water_trapped += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water_trapped += max_right - height[right]
            right -= 1

    return water_trapped

# Test the function
walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"Water trapped: {trap(walls)} units")