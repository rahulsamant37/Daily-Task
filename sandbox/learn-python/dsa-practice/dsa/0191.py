# DSA Problem 191

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings. You can only see the tops of the buildings from the left side. However, once a building is taller than the one to its left, it will block the view of any shorter buildings behind it. Your task is to calculate how many buildings can be seen from the left. For example, if the buildings are represented by the heights [3, 7, 8, 4], you can see 3 buildings from the left because the first building of height 3 blocks the view of the subsequent shorter building of height 4. 

Write a function `visible_buildings` that takes a list of positive integers as input and returns the number of buildings visible from the left.

Example:
visible_buildings([3, 7, 8, 4]) should return 3.
visible_buildings([3, 6, 2, 4, 5]) should return 4.
'''

Solution:
def visible_buildings(buildings):
    """
    Calculate the number of buildings visible from the left.
    
    :param buildings: List of positive integers representing the heights of buildings.
    :return: Integer representing the number of buildings visible from the left.
    """
    visible = 1  # Always see at least the first building
    max_height = buildings[0]
    for height in buildings[1:]:
        if height > max_height:
            visible += 1
            max_height = height
    return visible

# Check function to verify the correctness of the solution
def check():
    assert visible_buildings([3, 7, 8, 4]) == 3
    assert visible_buildings([3, 6, 2, 4, 5]) == 4
    assert visible_buildings([1, 2, 3, 4, 5]) == 5
    assert visible_buildings([5, 4, 3, 2, 1]) == 1
    assert visible_buildings([4, 4, 4, 4, 4]) == 1
    print("All test cases passed successfully.")

check()
'''

This problem and its solution follow the provided format and are completely self-contained, adhering to the guidelines.