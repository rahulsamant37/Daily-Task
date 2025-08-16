# Python Question: Largest Sum Contiguous Subarray
'''
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
'''

# Solution
def largest_sum_contiguous_subarray(nums):
    """
    Finds the largest sum of a contiguous subarray in a given array.

    Args:
        nums: A list of integers.

    Returns:
        The largest sum of a contiguous subarray.
    """
    # Kadane's Algorithm
    # Initialize max_so_far to negative infinity to handle cases where all numbers are negative.
    max_so_far = float('-inf')
    current_max = 0

    # Iterate through the array
    for i in range(len(nums)):
        # Update current_max by adding the current element
        current_max += nums[i]

        # If current_max is greater than max_so_far, update max_so_far
        if current_max > max_so_far:
            max_so_far = current_max

        # If current_max becomes negative, reset it to 0 because a negative sum will only decrease the overall sum of the subarray.
        if current_max < 0:
            current_max = 0

    # Return the maximum sum found
    return max_so_far

# Test cases
def test_largest_sum_contiguous_subarray():
    """
    Tests the largest_sum_contiguous_subarray function with several test cases.
    """
    assert largest_sum_contiguous_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert largest_sum_contiguous_subarray([1, 2, 3, 4, 5]) == 15
    assert largest_sum_contiguous_subarray([-1, -2, -3, -4, -5]) == -1
    assert largest_sum_contiguous_subarray([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert largest_sum_contiguous_subarray([5, 4, -1, 7, 8]) == 23
    assert largest_sum_contiguous_subarray([-10]) == -10
    assert largest_sum_contiguous_subarray([10]) == 10
    assert largest_sum_contiguous_subarray([2, -1, 2, 3, 4, -5]) == 10
    assert largest_sum_contiguous_subarray([8, -19, 5, -4, 20]) == 21
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_sum_contiguous_subarray()