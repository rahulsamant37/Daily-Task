# DSA Problem 292

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings in a straight line. Your task is to calculate the maximum amount of water that can be trapped between the buildings after a heavy rain. The width of each building is considered to be 1 unit. 

For example, given the list of building heights as [3, 0, 2, 0, 4], the maximum amount of water that can be trapped is 7 units. The water trapped between the buildings is visualized as follows:

  #
##w#
#ww#
####

Where '#' represents the building, and 'w' represents the water trapped.

Write a function `max_trapped_water` that takes a list of integers as input and returns the maximum amount of water that can be trapped.
'''

Solution:
def max_trapped_water(heights):
    """
    Calculate the maximum amount of water that can be trapped between buildings.
    """
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    max_left, max_right = 0, 0
    trapped_water = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= max_left:
                max_left = heights[left]
            else:
                trapped_water += max_left - heights[left]
            left += 1
        else:
            if heights[right] >= max_right:
                max_right = heights[right]
            else:
                trapped_water += max_right - heights[right]
            right -= 1

    return trapped_water

# Example check
print(max_trapped_water([3, 0, 2, 0, 4]))  # Expected output: 7
'''
This problem revolves around the idea of calculating the trapped rainwater, which is a classic problem in algorithmic challenges. The solution uses a two-pointer technique to efficiently calculate the trapped water, making it optimal in terms of time complexity, specifically O(N), where N is the number of buildings. This approach ensures that the solution is both efficient and easy to understand.
'''