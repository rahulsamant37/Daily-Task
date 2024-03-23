# DSA Problem 20

'''
Problem Statement:
You are given a list of positive integers representing the heights of walls. Your task is to find the maximum area of a rectangle that can be formed by any two walls and the ground. The width of the rectangle is the distance between the two walls, and the height of the rectangle is the shorter wall between the two. Return the maximum area possible.

For example, if the heights of the walls are given as [1,8,6,2,5,4,8,3,7], the maximum area of the rectangle that can be formed is 49, which is formed by the walls with heights 8 and 7, with a distance of 7 units between them.

Constraints:
- The list of wall heights will contain between 2 and 10^5 elements.
- Each wall height will be between 1 and 2^31 - 1.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is formed by the walls of height 8 and 7, which are 7 units apart.
'''

Solution:
def max_area(wall_heights):
    """
    Finds the maximum area of a rectangle that can be formed by any two walls and the ground.
    """
    left, right = 0, len(wall_heights) - 1
    max_area = 0
    while left < right:
        height = min(wall_heights[left], wall_heights[right])
        width = right - left
        max_area = max(max_area, height * width)
        if wall_heights[left] < wall_heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example check (Uncomment to test)
# print(max_area([1,8,6,2,5,4,8,3,7]))  # Expected output: 49

This problem is a variant of the "Container With Most Water" problem and follows the two-pointer technique for an optimal solution.