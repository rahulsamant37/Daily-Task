# DSA Problem 210

'''
Problem Statement:
You are given a list of integers representing the heights of a series of towers. Your task is to find the maximum area of water that can be contained between two towers. The width of each tower is 1 unit, and the distance between any two consecutive towers is also 1 unit. You need to return the maximum amount of water that can be contained.

Example:
For towers with heights [1, 8, 6, 2, 5, 4, 8, 3, 7], the maximum amount of water that can be contained is 49 units.
'''

Solution:
def max_water_container(tower_heights):
    """
    Finds the maximum amount of water that can be contained between two towers.
    """
    left, right = 0, len(tower_heights) - 1
    max_area = 0
    
    while left < right:
        height = min(tower_heights[left], tower_heights[right])
        width = right - left
        max_area = max(max_area, height * width)
        
        if tower_heights[left] < tower_heights[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

# Test the function with provided data points
assert max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Test case 1 failed"
assert max_water_container([1, 1]) == 1, "Test case 2 failed"
assert max_water_container([4, 3, 2, 1, 4]) == 16, "Test case 3 failed"
assert max_water_container([1, 2, 1]) == 2, "Test case 4 failed"

# Print the results of the test cases
print("All test cases passed!")