# DSA Problem 58

'''
Problem Statement:
You are given a list of integers representing the heights of walls of buildings. Each building's width is 1 unit. You need to calculate the total amount of rainwater trapped between the buildings after a rain. For example, given the heights [0,1,0,2,1,0,1,3,2,1,2,1], the function should return the total amount of water trapped, which is 6 units in this case.
'''

Solution:
def trap(height):
    if not height:
        return 0

    water_trapped = 0
    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                water_trapped += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water_trapped += max_right - height[right]
            right -= 1

    return water_trapped

# Test the function with a sample input
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected output: 6

# Explanation: The solution uses a two-pointer approach to calculate the trapped water. It iterates from both ends of the list, moving the pointer that points to a shorter wall. At each step, it calculates the water trapped at that position based on the maximum heights seen so far from both ends. This ensures that the water trapped is calculated efficiently with a time complexity of O(n).