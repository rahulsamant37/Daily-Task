# DSA Problem 220

'''
Problem Statement:
You are given a list of integers representing the heights of a row of walls. Your task is to find the maximum area of water that can be trapped between two walls. The width between two walls is the difference in their indices.

For example, given the list [1,8,6,2,5,4,8,3,7], the maximum amount of water that can be trapped is 49 units (between the walls of heights 8 and 7).

Write a function `max_water_trapped` that takes a list of integers and returns the maximum amount of water that can be trapped.

Constraints:
- 2 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^6

Example:
Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum water can be trapped between the walls at index 1 and 8 (heights 8 and 7).
'''

Solution:
def max_water_trapped(heights):
    max_area = 0
    left, right = 0, len(heights) - 1
    
    while left < right:
        # Calculate the area of water trapped between the walls
        height = min(heights[left], heights[right])
        width = right - left
        area = height * width
        
        # Update max_area if the current area is larger
        max_area = max(max_area, area)
        
        # Move the pointer that points to the shorter wall inward
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example check
print(max_water_trapped([1,8,6,2,5,4,8,3,7]))  # Expected output: 49

This solution uses the two-pointer technique to efficiently find the maximum area of water that can be trapped. The time complexity is O(n), where n is the length of the input list, and the space complexity is O(1).