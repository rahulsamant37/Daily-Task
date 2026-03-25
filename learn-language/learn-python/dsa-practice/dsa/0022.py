# DSA Problem 22

'''
Problem Statement:
You are given a list of integers representing the heights of buildings in a straight line. Your task is to calculate the total amount of rainwater that can be trapped between the buildings after a rainstorm. Each building has a width of 1 unit.

For example, given the list of building heights [3, 0, 2, 0, 4], the function should calculate the total amount of rainwater that can be trapped.

Note:
- The input list will have at least 2 buildings.
- All building heights will be non-negative integers.
'''

Solution:
def trap_rainwater(heights):
    """
    Calculates the total amount of rainwater that can be trapped between buildings.
    """
    if not heights:
        return 0

    water_trapped = 0
    left_max = [0] * len(heights)
    right_max = [0] * len(heights)
    
    left_max[0] = heights[0]
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i-1], heights[i])

    right_max[-1] = heights[-1]
    for i in range(len(heights)-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    for i in range(1, len(heights) - 1):
        water_trapped += max(0, min(left_max[i], right_max[i]) - heights[i])

    return water_trapped

# Example usage
building_heights = [3, 0, 2, 0, 4]
print(trap_rainwater(building_heights))  # Output: 7

# Explanation:
# - Between the first and third buildings, 3 units of water can be trapped.
# - Between the third and fifth buildings, 4 units of water can be trapped.
# - Total trapped water: 3 + 4 = 7 units.
'''