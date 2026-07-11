# Python Question: Largest Sum Contiguous Subarray
'''
Given an array of integers `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
'''

# Solution
def largest_sum_subarray(nums):
    """
    Finds the largest sum contiguous subarray in a given array.

    Args:
        nums: A list of integers.

    Returns:
        The largest sum of any contiguous subarray in nums.
    """
    # Kadane's Algorithm:
    # Initialize max_so_far to negative infinity to handle cases where all numbers are negative.
    max_so_far = float('-inf')
    # Initialize current_max to 0. This will track the sum of the current contiguous subarray.
    current_max = 0

    # Iterate through the array.
    for num in nums:
        # Update current_max by adding the current element.
        current_max += num

        # If current_max is greater than max_so_far, update max_so_far.
        if current_max > max_so_far:
            max_so_far = current_max

        # If current_max becomes negative, reset it to 0. This is because a negative current_max
        # will only decrease the sum of any subsequent subarray.
        if current_max < 0:
            current_max = 0

    # Return the maximum sum found.
    return max_so_far

# Test cases
def test_largest_sum_subarray():
    assert largest_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert largest_sum_subarray([1]) == 1
    assert largest_sum_subarray([5,4,-1,7,8]) == 23
    assert largest_sum_subarray([-1,-2,-3,-4]) == -1
    assert largest_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert largest_sum_subarray([0, 0, 0, 0]) == 0
    assert largest_sum_subarray([-1]) == -1
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_sum_subarray()