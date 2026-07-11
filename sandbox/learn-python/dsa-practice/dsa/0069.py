# DSA Problem 69

'''
Problem Statement:
You are given a list of positive integers. Your task is to find the maximum difference between two elements in the list such that the larger element appears after the smaller one in the list. If no such pair exists, return 0.

For example, given the list [2, 3, 10, 6, 4, 8, 1], the function should return 8 because the maximum difference is between 10 and 2.

Constraints:
- The length of the list is between 1 and 10^5.
- Each element in the list is between 1 and 10^6.
'''

Solution:
```python
def max_diff(lst):
    """
    Finds the maximum difference between two elements in the list such that
    the larger element appears after the smaller one in the list.
    """
    if not lst or len(lst) < 2:
        return 0
    
    min_element = lst[0]
    max_diff = 0
    
    for i in range(1, len(lst)):
        # Update the maximum difference if the current element minus the min_element
        # is greater than the current max_diff.
        if lst[i] - min_element > max_diff:
            max_diff = lst[i] - min_element
        
        # Update the minimum element if the current element is smaller than min_element.
        if lst[i] < min_element:
            min_element = lst[i]
    
    return max_diff

# Check function to verify the correctness of the solution
def check():
    assert max_diff([2, 3, 10, 6, 4, 8, 1]) == 8
    assert max_diff([7, 9, 5, 6, 3, 2]) == 2
    assert max_diff([1, 2, 90, 10, 110]) == 109
    assert max_diff([10, 8, 7, 6, 4]) == 0
    assert max_diff([1]) == 0
    print("All test cases passed successfully.")

check()
```

This code snippet defines a function `max_diff` that implements the logic to find the maximum difference between two elements in the list as described in the problem statement. The `check` function is used to validate the solution against several test cases.