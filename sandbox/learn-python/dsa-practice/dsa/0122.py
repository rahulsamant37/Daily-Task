# DSA Problem 122

'''
Problem Statement:
You are given a list of integers representing the heights of different towers in a city. The city has a very peculiar rule for constructing towers: no tower can be taller than the sum of the heights of the two towers immediately before it. Given a non-empty list of positive integers representing the heights of the first two towers, your task is to determine the maximum possible height of the tallest tower that can be built following the city's rules. The list will always contain at least two elements.

For example, if the input list is [1, 2], the maximum possible height of the tallest tower is 3, as the third tower can be 1 + 2 = 3. However, the fourth tower cannot exceed 2 + 3 = 5.

Write a function `max_tower_height` that takes a list of integers and returns the maximum possible height of the tallest tower that can be built.
'''

Solution:
```python
def max_tower_height(tower_heights):
    """
    Calculate the maximum possible height of the tallest tower that can be built.
    
    :param tower_heights: List[int] - A list of integers representing the heights of the first two towers.
    :return: int - The maximum possible height of the tallest tower.
    """
    a, b = tower_heights  # Initialize the first two towers
    max_height = max(a, b)  # Start with the maximum height of the first two towers
    
    # Loop to calculate the height of each subsequent tower
    while True:
        next_height = a + b
        if next_height < a or next_height < b:  # Check for overflow or exceeding conditions
            break
        max_height = max(max_height, next_height)
        a, b = b, next_height  # Update the heights for the next iteration
    
    return max_height

# Check function to verify the correctness of the solution
def check():
    assert max_tower_height([1, 2]) == 3
    assert max_tower_height([5, 8]) == 13
    assert max_tower_height([2, 2]) == 4
    assert max_tower_height([10, 1]) == 11
    assert max_tower_height([3, 5]) == 8
    print("All test cases passed successfully.")

check()
```

This solution defines a function `max_tower_height` that calculates the maximum possible height of the tallest tower that can be built based on the peculiar rule of the city. It iterates to calculate the height of each subsequent tower until it cannot be calculated anymore due to exceeding conditions, and returns the maximum height found. The `check` function is used to verify the correctness of the solution with given test cases.