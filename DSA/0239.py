# DSA Problem 239

'''
Problem Statement:
Given a list of integers representing the heights of walls, you need to find the maximum amount of water that can be trapped after raining. The width of each wall is considered to be 1 unit. For example, if the heights of walls are [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], the maximum amount of water trapped would be 6 units.

Write a function `max_trapped_water` that takes a list of non-negative integers representing the heights and returns an integer representing the maximum amount of water that can be trapped.
'''

Solution:
def max_trapped_water(heights):
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    max_water = 0
    left_max, right_max = heights[left], heights[right]

    while left < right:
        if heights[left] < heights[right]:
            left += 1
            left_max = max(left_max, heights[left])
            max_water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            max_water += right_max - heights[right]

    return max_water

# Example check
print(max_trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Expected output: 6
'''
This problem and solution exemplify an efficient approach (O(n)) to solve the classic "Trapping Rain Water" problem using the two-pointer technique.
'''