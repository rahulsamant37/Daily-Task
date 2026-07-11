# DSA Problem 56

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings. You need to calculate the total amount of water that can be trapped after a rain. The width of each building is considered to be 1 unit. The water trapped between the buildings depends on the height of the buildings on both sides. The water cannot be trapped if the building is at the edge of the list. 

For example, if the heights of the buildings are [3, 0, 2, 0, 4], the total amount of trapped water would be 7 units.
'''

Solution:
```python
def calculate_trapped_water(heights):
    """
    Calculate the total amount of water that can be trapped after a rain.
    
    :param heights: List of positive integers representing the heights of the buildings.
    :return: Total amount of trapped water.
    """
    if not heights:
        return 0

    left_max = [0] * len(heights)
    right_max = [0] * len(heights)
    water_trapped = 0

    # Fill left_max array with the max height from the left side
    left_max[0] = heights[0]
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i-1], heights[i])

    # Fill right_max array with the max height from the right side
    right_max[-1] = heights[-1]
    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    # Calculate the water that can be trapped
    for i in range(len(heights)):
        water_trapped += min(left_max[i], right_max[i]) - heights[i]

    return water_trapped

# Example usage
heights = [3, 0, 2, 0, 4]
print(calculate_trapped_water(heights))  # Output should be 7
```

This solution calculates the maximum height to the left and right of every building, which helps in determining how much water can be trapped above each building. The total trapped water is the sum of water trapped above all the buildings.