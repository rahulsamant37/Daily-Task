# DSA Problem for 2024-11-12

Here's a novel DSA problem with a Python solution for 2024-11-12:

**Problem Statement:**

You are given a list of integers representing the heights of buildings in a city. A strong wind is approaching the city, and the government wants to identify the buildings that will be most affected by the wind. A building is considered affected if it is shorter than both its adjacent buildings. Your task is to write a function that takes the list of building heights as input and returns the indices of the affected buildings.

For example, if the input list is `[3, 1, 2, 4, 3, 2, 1]`, the affected buildings are at indices `1`, `2`, and `5`.

**Optimal Solution:**
```
def affected_buildings(heights):
    n = len(heights)
    affected = [False] * n
    for i in range(1, n-1):
        if heights[i] < heights[i-1] and heights[i] < heights[i+1]:
            affected[i] = True
    return [i for i, affected in enumerate(affected) if affected]
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n), where n is the length of the input list. This is because we iterate over the list once to identify the affected buildings.

**Space Complexity Analysis:**

The space complexity of the solution is O(n), where n is the length of the input list. This is because we need to store a boolean array of size n to keep track of the affected buildings.

**Explanation:**

The solution uses a simple iterative approach to identify the affected buildings. We iterate over the list, starting from the second building (index 1) and ending at the second-to-last building (index n-2). For each building, we check if it is shorter than both its adjacent buildings. If it is, we mark it as affected. Finally, we return a list of indices of the affected buildings using a list comprehension.

Note that we don't need to consider the first and last buildings separately, as they can't be affected by the wind since they don't have adjacent buildings on both sides.