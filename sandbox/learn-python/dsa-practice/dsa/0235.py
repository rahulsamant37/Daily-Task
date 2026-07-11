# DSA Problem 235

'''
Problem Statement:
Arun has a list of positive integers representing the heights of a series of buildings. He wants to find the total number of ways he can choose three buildings such that the middle building's height is strictly greater than the heights of the first and third buildings. For example, if the heights are [4, 2, 5, 1], one valid set of buildings would be (4, 5, 1). Help Arun by writing a function that takes a list of positive integers as input and returns the total number of such ways.

Note: The buildings are considered in the order they appear in the list.
'''

Solution:
```python
def count_building_sets(heights):
    """
    Counts the number of ways to choose three buildings such that the middle building's height
    is strictly greater than the heights of the first and third buildings.
    """
    n = len(heights)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if heights[j] > heights[i]:
                for k in range(j+1, n):
                    if heights[k] < heights[j]:
                        count += 1
    return count

# Example check function
def check_solution():
    assert count_building_sets([2, 4, 3, 1]) == 3, "Test case 1 failed"
    assert count_building_sets([2, 1, 3]) == 0, "Test case 2 failed"
    assert count_building_sets([4, 2, 5, 1]) == 1, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This Python function, `count_building_sets`, efficiently calculates the total number of valid sets of buildings based on the given criteria. The `check_solution` function is used to verify the correctness of the solution with predefined data points.