# DSA Problem 208

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings in a straight line. Your task is to find the maximum volume of water that can be trapped between buildings after a rain. The volume of water trapped between two buildings is determined by the shorter building's height and the distance between them. However, water can only be trapped between two buildings if there's a taller building on either side that can 'contain' the water.

For example, given the building heights [3, 0, 2, 0, 4], the maximum volume of water trapped would be 7 units (3 units between the first and third buildings, and 4 units between the third and fifth buildings).

Write a function `max_water_trapped` that takes a list of positive integers as input and returns the maximum volume of water that can be trapped.
'''

Solution:
def max_water_trapped(heights):
    if not heights or len(heights) < 3:
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

    total_water = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level > heights[i]:
            total_water += water_level - heights[i]

    return total_water

# Test the function
heights = [3, 0, 2, 0, 4]
print(max_water_trapped(heights))  # Output should be 7
'''
This problem is a variation of the classic "trapping rain water" problem and is designed to test the understanding of array manipulation and two-pointer (or in this case, two-array) techniques in Python. The solution calculates the maximum height to the left and right of every building, and then calculates the water level that can be trapped at each building based on the minimum of these two heights, subtracting the actual height of the building.
'''