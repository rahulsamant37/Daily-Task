# DSA Problem 104

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings. Your task is to find the maximum volume of water that can be trapped between buildings after a rain. The width of each building is considered to be 1 unit. Note that the water trapped between two buildings is determined by the height of the shorter building.

For example, given the list of building heights as [3, 0, 2, 0, 4], the maximum volume of water that can be trapped is 7 units.
'''

Solution:
def trap_water(building_heights):
    n = len(building_heights)
    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = building_heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], building_heights[i])
    
    right_max[n-1] = building_heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], building_heights[i])
    
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - building_heights[i]
    
    return trapped_water

# Test the solution
building_heights = [3, 0, 2, 0, 4]
print(f"Maximum water trapped: {trap_water(building_heights)}")