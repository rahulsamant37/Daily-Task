# DSA Problem 55

'''
Problem Statement:
You are given a list of integers representing the heights of buildings in a city. The city has a unique rule: if the height of a building is greater than the average height of all the buildings, it must be painted red; otherwise, it is painted blue. Your task is to implement a function `paint_buildings` that takes a list of building heights and returns a list of strings, where each string represents the color of the corresponding building ('red' or 'blue').

Example:
For the input [10, 5, 8, 20], the average height is 10.75, so the output should be ['blue', 'blue', 'blue', 'red'] since only the last building is taller than the average.
'''

Solution:
def paint_buildings(building_heights):
    """
    Paints buildings based on their height relative to the average height of all buildings.
    
    :param building_heights: List of integers representing the heights of buildings.
    :return: List of strings representing the color of each building ('red' or 'blue').
    """
    average_height = sum(building_heights) / len(building_heights)
    return ['red' if height > average_height else 'blue' for height in building_heights]

# Check function to verify the correctness of the solution
def check_solution():
    assert paint_buildings([10, 5, 8, 20]) == ['blue', 'blue', 'blue', 'red'], "Test case 1 failed"
    assert paint_buildings([5, 5, 5, 5]) == ['blue', 'blue', 'blue', 'blue'], "Test case 2 failed"
    assert paint_buildings([1, 2, 3, 4, 100]) == ['blue', 'blue', 'blue', 'blue', 'red'], "Test case 3 failed"
    print("All test cases passed!")

check_solution()