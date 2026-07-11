# DSA Problem 193

'''
Problem Statement:
You are given an integer array `nums` and an integer `k`. You can perform the following operation on the array any number of times: choose any element and decrease it by `k`. Your task is to determine the minimum number of operations required to make all elements of the array equal. If it is not possible to make all elements equal, return -1.

For example, if `nums = [4, 1, 6]` and `k = 2`, you can perform the following operations:
1. Decrease 4 to 2 (nums becomes [2, 1, 6]).
2. Decrease 6 to 2 (nums becomes [2, 1, 2]).
3. Decrease 2 to 0 (nums becomes [0, 1, 0]).
4. Decrease 1 to 0 (nums becomes [0, 0, 0]).

Thus, the minimum number of operations to make all elements equal is 4.
'''

Solution:
```python
def min_operations(nums, k):
    """
    Calculate the minimum number of operations required to make all elements of the array equal.
    """
    if len(set(nums)) == 1:
        # If all elements are already equal, no operations are needed.
        return 0
    
    # Find the minimum and maximum values in the array
    min_val, max_val = min(nums), max(nums)
    
    # Check if it is possible to make all elements equal
    if (max_val - min_val) % k != 0:
        return -1
    
    # Calculate the number of operations needed for each element to reach the target value
    target = (max_val - min_val) // k
    operations = sum((num - min_val) // k for num in nums)
    
    return operations

# Example check function
def check_solution():
    assert min_operations([4, 1, 6], 2) == 4, "Test case 1 failed"
    assert min_operations([2, 2, 2], 3) == 0, "Test case 2 failed"
    assert min_operations([3, 9, 6], 2) == -1, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This solution first checks if all elements are already equal, in which case no operations are needed. It then determines the minimum and maximum values in the list to check if it's possible to make all values equal by repeatedly subtracting `k`. If the difference between the maximum and minimum values is not divisible by `k`, it's impossible to make all elements equal, and the function returns `-1`. Otherwise, it calculates the total number of operations required to make all elements equal by adjusting each number to the maximum value that can be reached by subtracting multiples of `k`.