# DSA Problem 334

'''
Problem Statement:
You are given a list of integers representing the heights of consecutive buildings. You need to calculate the maximum amount of water that can be trapped between the buildings after a rain. The width of each building is 1 unit.

For example, given the heights [3, 0, 2, 0, 4], the water trapped can be visualized as follows:

  #
  ##
## WW#
####W#
######

Where 'W' represents water. So the total units of water trapped are 7 units.

Write a function `max_trapped_water` that takes a list of non-negative integers and returns an integer representing the total units of water trapped.
'''

Solution:
def max_trapped_water(heights):
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

# Explanation:
# This solution works by maintaining two pointers at both ends of the list, moving inward. 
# It also keeps track of the maximum height observed from both sides. The water trapped at 
# any point is determined by the minimum of the maximum heights observed from both sides 
# minus the height of the current building. The time complexity is O(n) and space complexity 
# is O(1).