# DSA Problem 319

'''
Problem Statement:
Given a list of integers representing the heights of a series of buildings, imagine you are painting a skyline from left to right. Each building has a width of 1 and the height is given by the value at each index. When you reach a building that is taller than the previously tallest building, you "paint" the skyline. How many times will you "paint" the skyline as you traverse the list from left to right?

For example, given the list [3, 4, 2, 5, 6], you would paint the skyline 4 times: at the 1st (3), 2nd (4), 4th (5), and 5th (6) building.
'''

Solution:
def paint_skylines(building_heights):
    """
    Counts how many times a skyline is painted as you traverse the list of building heights from left to right.
    :param building_heights: List[int] - A list of integers representing the heights of buildings.
    :return: int - The number of times the skyline is painted.
    """
    if not building_heights:
        return 0

    max_height = building_heights[0]
    paint_count = 1  # First building always counts as a new skyline

    for height in building_heights[1:]:
        if height > max_height:
            max_height = height
            paint_count += 1

    return paint_count

# Example check
print(paint_skylines([3, 4, 2, 5, 6]))  # Expected output: 4
print(paint_skylines([1, 2, 3, 4, 5, 6]))  # Expected output: 6
print(paint_skylines([6, 5, 4, 3, 2, 1]))  # Expected output: 1
print(paint_skylines([]))  # Expected output: 0
print(paint_skylines([10]))  # Expected output: 1
'''

This problem checks the understanding of iterating over a list and maintaining a running maximum, while also counting occurrences of a specific condition being met. The solution is straightforward and can be adapted to various levels of difficulty by changing the problem's constraints or the nature of the input data.