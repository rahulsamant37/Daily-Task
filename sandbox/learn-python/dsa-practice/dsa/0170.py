# DSA Problem 170

'''
Problem Statement:
You are given a list of integers representing the heights of a series of walls. You need to calculate how much rainwater can be trapped between the walls after a rain. The width of each wall is considered to be 1 unit. The input list will have at least two walls.

For example, given the heights [3, 0, 2, 0, 4], the function should return the total amount of rainwater that can be trapped.

Note:
- The trapped water between walls is determined by the height of the shorter wall.
- If there is a higher wall on both sides, water can be trapped above the current wall up to the height of the shorter of the two higher walls.
'''

Solution:
def trap(heights):
    if not heights:
        return 0

    water_trapped = 0
    left_max = [0] * len(heights)
    right_max = [0] * len(heights)

    # Fill left_max array
    left_max[0] = heights[0]
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i-1], heights[i])

    # Fill right_max array
    right_max[-1] = heights[-1]
    for i in range(len(heights)-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    # Calculate the trapped water using the min of left_max and right_max
    # and subtracting the height of the wall at that position
    for i in range(len(heights)):
        water_trapped += min(left_max[i], right_max[i]) - heights[i]

    return water_trapped

# Example check (This part is not part of the solution, just for verification)
print(trap([3, 0, 2, 0, 4]))  # Expected output: 7
'''
This solution calculates the maximum height to the left and right of every wall. Then, for each wall, it calculates how much water can be trapped above it. The total trapped water is the sum of all such individual trapped water amounts.