# DSA Problem 275

'''
Problem Statement:
Alice has a list of positive integers, `nums`. She wants to know the minimum number of operations required to make all the elements in the list equal. In one operation, she can increment or decrement any element by 1. However, there is a twist: Alice can only perform operations on elements that are at even indices. The elements at odd indices cannot be changed. Help Alice find the minimum number of operations needed.

For example, given the list [1, 3, 2, 4, 5], Alice can only modify the elements at indices 0, 2, and 4 (1, 2, and 5 respectively). The optimal solution would be to make all elements equal to 2 (modifying 1 to 2 and 5 to 2), thus the minimum number of operations is 3.

Constraints:
- 1 <= len(nums) <= 1000
- 1 <= nums[i] <= 10^6
'''

Solution:
```python
def min_operations(nums):
    """
    Calculate the minimum number of operations needed to make all elements at even indices equal.
    """
    even_indices_values = [nums[i] for i in range(0, len(nums), 2)]
    even_indices_values.sort()
    target_value = even_indices_values[len(even_indices_values) // 2]
    operations = sum(abs(num - target_value) for num in even_indices_values)
    return operations

# Example check function
def check_solution():
    assert min_operations([1, 3, 2, 4, 5]) == 3
    assert min_operations([4, 1, 1, 2, 3]) == 4
    assert min_operations([10, 1, 10, 1, 10]) == 0
    print("All test cases passed.")

check_solution()
```
This solution calculates the minimum number of operations by focusing only on the elements at even indices, sorting them to find the median (which minimizes the sum of absolute deviations), and then summing up the absolute differences between each even-indexed element and this median.