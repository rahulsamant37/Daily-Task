# DSA Problem 147

'''
Problem Statement:
You are given a list of integers and an integer k. Your task is to find out if there are two distinct indices i and j in the list such that the absolute difference between nums[i] and nums[j] is at most k and the absolute difference between i and j is at most 5. 

For example, given nums = [2, 3, 6, 8, 4, 7] and k = 2, the function should return True because the absolute difference between nums[2] (6) and nums[4] (4) is 2, which is within the given limit, and the index difference is 2, which is also within the limit of 5.

Write a function that takes in the list of numbers and the integer k, and returns True if such a pair exists, otherwise False.
'''

Solution:
```python
def check_nearby_elements(nums, k):
    """
    This function checks if there exist two distinct indices i and j such that
    the absolute difference between nums[i] and nums[j] <= k and the absolute
    difference between i and j <= 5.
    """
    num_dict = {}
    for i, num in enumerate(nums):
        if i > 5:
            del num_dict[nums[i-6]]
        for key in num_dict.keys():
            if abs(key - num) <= k:
                return True
        num_dict[num] = i
    return False

# Example check function
def check_solution():
    test_cases = [([2, 3, 6, 8, 4, 7], 2, True),
                  ([1, 5, 9, 1, 5, 9], 3, False),
                  ([10, 15, 20, 25], 6, False)]
    
    for nums, k, expected in test_cases:
        assert check_nearby_elements(nums, k) == expected, f"Failed on input {nums} with k={k}"
    print("All test cases passed.")

check_solution()
```

This solution uses a dictionary to keep track of the last 5 elements and their indices, constantly checking the condition against the current element. If the condition is met, it returns True; otherwise, it continues until the end of the list, then returns False.