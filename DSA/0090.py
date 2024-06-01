# DSA Problem 90

'''
Problem Statement:
You are given a list of integers representing the heights of a row of buildings. You need to calculate the maximum amount of water that can be trapped after raining. The width of each building's base is considered to be 1 unit.

For example, given the list of building heights [3, 0, 2, 0, 4], the function should return the amount of water that would be trapped. In this case, the total trapped water would be 7 units. The trapped water can be visualized as follows:

```
          X
    X     X X
X   X X   X X
X X X X X X X
3 0 2 0 4
```

Here, 'X' represents water.
'''

Solution:
def trap_water(heights):
    """
    Calculates the maximum amount of water that can be trapped given a list of building heights.
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
building_heights = [3, 0, 2, 0, 4]
print(f"Trapped Water: {trap_water(building_heights)}")  # Expected output: 7
'''
This solution implements an efficient two-pointer approach to calculate the trapped water by maintaining the maximum heights on the left and right sides as the pointers move towards each other. This ensures that the solution runs in O(n) time complexity, where n is the number of buildings.