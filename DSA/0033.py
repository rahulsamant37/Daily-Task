# DSA Problem 33

'''
Problem Statement:
You are given a list of integers representing the heights of a series of buildings. You need to calculate how many buildings you can see from both the left and the right side. When viewing the buildings from either side, taller buildings block the view of shorter buildings behind them. 

For example, if the buildings' heights are [3, 7, 8, 3, 6, 1], you can see 3 buildings from the left (3, 7, 8) and 2 from the right (6, 1). Thus, the total number of unique buildings visible from both sides is 5.

Write a function `count_visible_buildings(heights)` that takes a list of integers and returns the total number of unique buildings visible from both the left and the right.

Constraints:
- 1 <= len(heights) <= 10^5
- 1 <= heights[i] <= 10^9
'''

Solution:
def count_visible_buildings(heights):
    """
    Counts the number of unique buildings visible from both the left and the right.
    """
    left_max = 0
    right_max = 0
    visible_from_left = set()
    visible_from_right = set()
    
    # Check from left
    for i in range(len(heights)):
        if heights[i] > left_max:
            visible_from_left.add(i)
            left_max = heights[i]
    
    # Check from right
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > right_max:
            visible_from_right.add(i)
            right_max = heights[i]
    
    # Union of both sets will give us the total unique buildings visible
    total_visible = visible_from_left.union(visible_from_right)
    return len(total_visible)

# Example check
print(count_visible_buildings([3, 7, 8, 3, 6, 1]))  # Output: 5
'''
This problem involves iterating over a list while keeping track of the maximum values seen so far from both directions, then using sets to ensure uniqueness of the buildings visible from each side. The solution efficiently counts the number of buildings visible when viewed from both the left and right, ensuring no building is double-counted if it's visible from both sides.