# DSA Problem 229

'''
Problem Statement:
You are given a list of integers representing the heights of consecutive buildings. You need to calculate the total amount of water that can be trapped between the buildings after a heavy rain. The width of each building is considered to be 1 unit.

For example, given the list of building heights [3, 0, 2, 0, 4], the function should return 7, as 7 units of water can be trapped between the buildings.

Write a function `calculate_trapped_water` that takes a list of integers as input and returns the total amount of water that can be trapped.
'''

Solution:
def calculate_trapped_water(heights):
    if not heights:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])

    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - heights[i]

    return trapped_water

# Test the function
building_heights = [3, 0, 2, 0, 4]
print(f"Water trapped: {calculate_trapped_water(building_heights)}")  # Output: Water trapped: 7

This solution calculates the maximum height to the left and right of every building and then computes the trapped water by finding the minimum of the max heights and subtracting the building height at each position.