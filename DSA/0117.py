# DSA Problem 117

'''
Problem Statement:
You are given a list of positive integers `nums` and an integer `k`. Your task is to find the number of unique pairs (i, j) where `i < j` and the absolute difference between `nums[i]` and `nums[j]` is exactly `k`. For example, if `nums = [1, 5, 3, 4, 2]` and `k = 2`, the valid pairs are (1, 3), (2, 4), and (3, 5), where the indices are 1-based.

Write a function `count_pairs_with_diff_k(nums, k)` that returns the number of such unique pairs.
'''

Solution:
def count_pairs_with_diff_k(nums, k):
    """
    Returns the number of unique pairs (i, j) where i < j and the absolute
    difference between nums[i] and nums[j] is exactly k.
    """
    num_count = {}
    count = 0
    for num in nums:
        # Check for pairs where the current number is the larger number in the pair
        if num - k in num_count:
            count += num_count[num - k]
        # Check for pairs where the current number is the smaller number in the pair
        if num + k in num_count:
            count += num_count[num + k]
        # Update the count of the current number
        num_count[num] = num_count.get(num, 0) + 1
    return count

# Example check function
def check_solution():
    assert count_pairs_with_diff_k([1, 5, 3, 4, 2], 2) == 3, "Example 1 failed"
    assert count_pairs_with_diff_k([1, 2, 3, 4, 5], 1) == 4, "Example 2 failed"
    assert count_pairs_with_diff_k([1, 3], 3) == 0, "Example 3 failed"
    print("All examples passed!")

check_solution()
'''

The example check function `check_solution()` is provided to verify the correctness of the `count_pairs_with_diff_k` function using some predefined test cases.