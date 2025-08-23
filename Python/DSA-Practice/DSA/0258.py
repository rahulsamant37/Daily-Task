# DSA Problem 258

'''
Problem Statement:
You are given a list of positive integers representing the heights of a series of buildings in a city skyline. A building is considered a "prominent building" if it is taller than all the buildings to its right and shorter than all the buildings to its left. Your task is to count the number of prominent buildings in the skyline.

For example, given the list of building heights [3, 7, 8, 4], the buildings with heights 8 and 3 are considered prominent. 8 is prominent because it is taller than the building to its right and there are no buildings to its left. 3 is prominent because it is shorter than the building to its right and there are no buildings to its left.

Write a function `count_prominent_buildings` that takes a list of integers as input and returns the number of prominent buildings in the skyline.

Note:
- The list will not be empty.
- The list can contain up to 10^5 elements.
'''

Solution:
```python
def count_prominent_buildings(building_heights):
    n = len(building_heights)
    max_right = [0] * n
    max_right[n-1] = building_heights[n-1]
    
    # Fill the max_right array such that max_right[i] contains the max value from index i to n-1
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], building_heights[i])
    
    prominent_count = 0
    max_left = 0
    
    # Count prominent buildings
    for i in range(n-1):
        if building_heights[i] > max_left and building_heights[i] > max_right[i+1]:
            prominent_count += 1
        max_left = max(max_left, building_heights[i])
    
    return prominent_count

# Test the function
print(count_prominent_buildings([3, 7, 8, 4]))  # Output: 2
print(count_prominent_buildings([4, 2, 3, 1]))  # Output: 1
```

This problem and solution illustrate an algorithmic approach to count "prominent buildings" in a city skyline, with a focus on optimal performance, especially important given the potential size of the input list.