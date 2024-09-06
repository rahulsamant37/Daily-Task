# DSA Problem 187

'''
Problem Statement:
You are given a list of positive integers. Your task is to find the smallest positive integer that is a multiple of 4 and is not present in the list. The list can contain up to 1000 integers, and each integer in the list does not exceed 10000. 

For example, if the input list is [4, 8, 12, 16], the first few multiples of 4 not in this list would be 20, 24, 28, etc. Hence, the answer would be 20.
'''

Solution:
```python
def find_missing_multiple(nums):
    """
    Finds the smallest positive integer that is a multiple of 4 and not present in the given list.
    """
    # Convert the list to a set for O(1) lookups
    num_set = set(nums)
    
    # Start with the smallest multiple of 4
    multiple_of_4 = 4
    
    # Keep increasing by 4 until we find a multiple not in the set
    while multiple_of_4 in num_set:
        multiple_of_4 += 4
    
    return multiple_of_4

# Example check function
def check_solution():
    assert find_missing_multiple([4, 8, 12, 16]) == 20
    assert find_missing_multiple([1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]) == 4
    assert find_missing_multiple([4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 44
    print("All checks passed.")

check_solution()
```

This problem involves understanding basic arithmetic properties and set operations in Python, making it a good practice problem for intermediate Python learners.