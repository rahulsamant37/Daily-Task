# DSA Problem 121

'''
Problem Statement:
Given a list of integers `nums`, write a function `find_max_product` that returns the maximum product that can be achieved by multiplying any three distinct numbers from the list. Assume that the list contains at least three numbers and can include both positive and negative numbers.

Example:
For the list `nums = [1, 2, 3, 4]`, the function should return `24` because the maximum product is achieved by multiplying `2 * 3 * 4`.
For the list `nums = [-1, -2, -3, -4]`, the function should return `-6` because the maximum product of three numbers in this case is `-1 * -2 * -3`.
'''

Solution:
```python
def find_max_product(nums):
    """
    Finds the maximum product of any three distinct numbers in the list nums.
    """
    nums.sort()
    # The maximum product can be either (a) the product of the three largest numbers
    # or (b) the product of the two smallest numbers (which could be negative) and the largest number.
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Check function to verify the correctness of the solution
def check_solution():
    assert find_max_product([1, 2, 3, 4]) == 24, "Test case 1 failed"
    assert find_max_product([-1, -2, -3, -4]) == -6, "Test case 2 failed"
    assert find_max_product([-1, -2, 1, 2, 3]) == 6, "Test case 3 failed"
    assert find_max_product([1, 10, 2, 6, 5, 3]) == 300, "Test case 4 failed"
    assert find_max_product([-100, -98, 1, 2, 3, 4]) == 39200, "Test case 5 failed"
    print("All test cases passed!")

check_solution()
```

This problem and solution focus on sorting and considering both negative and positive numbers to find the maximum product, which is a common algorithmic challenge in programming interviews and competitions.