# DSA Problem 75

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings in a straight line. A "skyline view" is defined as the number of buildings you can see when looking from the left side of the row. A building blocks the view of all buildings that are shorter and to its right. Calculate the number of buildings visible from the left.

For example, if the buildings are of heights [3, 1, 4, 5, 2], you can see 3 buildings from the left. The buildings with heights 3, 4, and 5 are visible because they are not blocked by any taller or equally tall buildings to their left.

Write a function `visible_buildings` that takes a list of integers representing the heights of the buildings and returns the number of buildings visible from the left.

Constraints:
- 1 <= len(buildings) <= 10^4
- All heights are positive integers less than 10^5.
'''

Solution:
def visible_buildings(buildings):
    """
    Calculates the number of buildings visible from the left side.
    """
    if not buildings:
        return 0
    
    visible = 1  # At least the first building is always visible
    max_height = buildings[0]
    
    for height in buildings[1:]:
        if height > max_height:
            visible += 1
            max_height = height
            
    return visible

# Example check function
def check_solution():
    assert visible_buildings([3, 1, 4, 5, 2]) == 3, "Test case 1 failed"
    assert visible_buildings([1, 2, 3, 4, 5]) == 5, "Test case 2 failed"
    assert visible_buildings([5, 4, 3, 2, 1]) == 1, "Test case 3 failed"
    assert visible_buildings([1, 1, 1, 1, 1]) == 1, "Test case 4 failed"
    assert visible_buildings([10, 20, 30, 5, 25]) == 3, "Test case 5 failed"
    print("All test cases passed!")

check_solution()
'''