# Python Question: Largest Sum Contiguous Subarray with Kadane's Algorithm
'''
Given an array of integers `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Solution
def largest_subarray_sum(nums):
    """
    Finds the largest sum of a contiguous subarray using Kadane's Algorithm.

    Args:
        nums: A list of integers.

    Returns:
        The largest sum of a contiguous subarray.
    """
    max_so_far = float('-inf')  # Initialize max_so_far to negative infinity to handle arrays with all negative numbers
    current_max = 0  # Initialize current_max to 0

    for i in range(len(nums)):
        current_max += nums[i] # Add the current element to the current_max

        if current_max > max_so_far: # If current_max is greater than max_so_far, update max_so_far
            max_so_far = current_max

        if current_max < 0: # If current_max becomes negative, reset it to 0 because a negative sum will always reduce the sum of subsequent subarrays.
            current_max = 0

    return max_so_far # Return the largest sum found
    

# Test cases
def test_largest_subarray_sum():
    """
    Tests the largest_subarray_sum function with several test cases.
    """
    assert largest_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert largest_subarray_sum([1]) == 1
    assert largest_subarray_sum([5, 4, -1, 7, 8]) == 23
    assert largest_subarray_sum([-1, -2, -3, -4]) == -1
    assert largest_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert largest_subarray_sum([0]) == 0
    assert largest_subarray_sum([-1, 0, -2]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_subarray_sum()