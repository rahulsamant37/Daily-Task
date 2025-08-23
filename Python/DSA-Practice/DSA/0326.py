# DSA Problem 326

'''
Problem Statement:
You are given a list of integers and a positive integer k. Your task is to find the k-th largest unique number in the list. If there are less than k unique numbers, return -1.

For example, if the list is [4, 2, 2, 3, 3, 1] and k = 2, the unique numbers are [4, 2, 3, 1], and the 2nd largest unique number is 3.

Assume:
- The list will have between 1 and 1000 integers.
- Each integer in the list will be between -1000 and 1000.
- k is a positive integer.
'''

Solution:
```python
def find_kth_largest_unique(nums, k):
    """
    Finds the k-th largest unique number in the list.
    
    :param nums: List[int] -- a list of integers
    :param k: int -- the k-th position to find
    :return: int -- the k-th largest unique number or -1 if not found
    """
    unique_nums = list(set(nums))  # Remove duplicates
    unique_nums.sort(reverse=True)  # Sort in descending order
    
    if len(unique_nums) < k:
        return -1
    else:
        return unique_nums[k-1]

# Example check (This part is not part of the solution, just for checking)
print(find_kth_largest_unique([4, 2, 2, 3, 3, 1], 2))  # Output: 3
print(find_kth_largest_unique([1, 2, 3, 4, 5], 6))     # Output: -1
```

This solution involves first removing duplicates by converting the list to a set and back to a list. It then sorts the list in descending order and checks if the position k-1 exists in the list. If it does, it returns the k-th largest unique number; otherwise, it returns -1.