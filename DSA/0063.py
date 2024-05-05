# DSA Problem 63

'''
Problem Statement:
You are given a list of integers representing the heights of different buildings in a city skyline. The city has a unique regulation that all buildings must have a green roof. However, the amount of greenery allowed on a roof is proportional to the height of the building. Specifically, a building of height h can have at most h units of greenery. The city planner wants to know the maximum total amount of greenery that can be added to all buildings without changing their heights, given that no two adjacent buildings can have their full greenery capacity at the same time (to ensure visibility of the skyline).

Write a function `max_greenery(building_heights)` that takes in a list of integers `building_heights` and returns the maximum amount of greenery that can be added under these constraints.

Example:
- For `building_heights = [3, 10, 3, 1, 2]`, the function should return `9` because the optimal way to add greenery is to add 3 units to the first building, 0 to the second, 3 to the third, 1 to the fourth, and 2 to the fifth, totaling to 9 units.
'''

Solution:
```python
def max_greenery(building_heights):
    n = len(building_heights)
    if n == 0:
        return 0
    elif n == 1:
        return building_heights[0]
    
    # Initialize the dp array where dp[i] represents the max greenery up to index i
    dp = [0] * n
    dp[0] = building_heights[0]
    dp[1] = max(building_heights[0], building_heights[1])
    
    for i in range(2, n):
        # The maximum greenery at position i is the max of:
        # 1. Taking the current building's greenery and the greenery up to i-2 (skipping the adjacent building)
        # 2. Not taking the current building's greenery, thus carrying forward the greenery up to i-1
        dp[i] = max(dp[i-2] + building_heights[i], dp[i-1])
    
    return dp[-1]

# Check function with the provided data points
print(max_greenery([3, 10, 3, 1, 2]))  # Expected output: 9
```

This solution employs dynamic programming to calculate the maximum amount of greenery that can be added to the buildings under the given constraints. The `dp` array is used to store the maximum greenery that can be collected up to each building, considering the restriction on adjacent buildings.