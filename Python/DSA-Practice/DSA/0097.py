# DSA Problem 97

'''
Problem Statement:
You are given a list of integers representing the heights of different buildings in a city skyline. The city has a peculiar rule: the cost to maintain a building is equal to the number of buildings that are at least as tall as it. For example, if there are 3 buildings that are taller or equal in height to a particular building, the maintenance cost for that building is 3.

Given a list of building heights, calculate the total maintenance cost for all buildings.

Example:
Input: [2, 5, 5, 1, 2]
Output: 7
Explanation: The tallest building (height 5) has a maintenance cost of 2 (itself and the other building of height 5). The buildings of height 2 each have a cost of 4 (both buildings of height 2, both buildings of height 5, and the building of height 1). The building of height 1 has a maintenance cost of 5 (all buildings are taller or equal in height to it). Thus, the total maintenance cost is 2 + 4 + 4 + 5 = 15.
'''

Solution:
```python
def total_maintenance_cost(heights):
    cost = 0
    n = len(heights)
    for i in range(n):
        current_cost = 0
        for j in range(n):
            if heights[j] >= heights[i]:
                current_cost += 1
        cost += current_cost
    return cost

# Example usage:
print(total_maintenance_cost([2, 5, 5, 1, 2]))  # Output: 15
```

This solution iterates through each building and counts the number of buildings that are at least as tall for each one, summing these counts to find the total maintenance cost.