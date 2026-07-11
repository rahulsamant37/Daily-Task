# DSA Problem 168

'''
Problem Statement:
A group of friends decide to play a game where each person picks a number. The game's goal is to find the friend who has picked the number which is the absolute difference between the highest and the lowest numbers picked by the group. If multiple friends have picked this number, return the count of such friends. If no one has picked this number, return 0.

For example, if the numbers picked are [3, 7, 1, 9, 5], the absolute difference between the highest and lowest is 8 (9 - 1). Since no one picked 8, the function should return 0. If the numbers are [2, 4, 6, 2], the difference is 4 (6 - 2), and two people picked 4, so the function should return 2.
'''

Solution:
```python
def count_friends_with_difference(numbers):
    if not numbers:
        return 0
    
    min_num = min(numbers)
    max_num = max(numbers)
    difference = max_num - min_num
    
    return numbers.count(difference)

# Example check function
def check_solution():
    assert count_friends_with_difference([3, 7, 1, 9, 5]) == 0, "Example 1 failed"
    assert count_friends_with_difference([2, 4, 6, 2]) == 2, "Example 2 failed"
    assert count_friends_with_difference([1, 1, 1, 1]) == 4, "Example 3 failed"
    assert count_friends_with_difference([10]) == 0, "Example 4 failed"
    print("All examples passed!")

check_solution()
```

This code defines a function `count_friends_with_difference` that takes a list of integers as input and returns the count of friends who picked the number equivalent to the absolute difference between the highest and lowest numbers picked by the group. It also includes a check function to verify the correctness of the solution with given data points.