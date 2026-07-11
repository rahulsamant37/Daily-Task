# Python Question: Largest Sum Contiguous Subarray (Kadane's Algorithm)
'''
Given an array of integers `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
'''

# Solution
def solution(nums):
    """
    Finds the largest sum of a contiguous subarray in the given array.

    Args:
        nums: A list of integers.

    Returns:
        The largest sum of a contiguous subarray.
    """
    # Initialize max_so_far to the smallest possible integer value.  This ensures that if all numbers in the array are negative, we still find the largest negative number.
    max_so_far = float('-inf')
    # Initialize current_max to 0.  This variable tracks the sum of the current subarray.
    current_max = 0

    # Iterate through the array
    for i in range(len(nums)):
        # Add the current element to the current_max
        current_max += nums[i]

        # If current_max is greater than max_so_far, update max_so_far
        if current_max > max_so_far:
            max_so_far = current_max

        # If current_max becomes negative, reset it to 0.  This is because a negative current_max will only decrease the sum of any subsequent subarray.
        if current_max < 0:
            current_max = 0

    # Return the maximum sum found
    return max_so_far

# Test cases
def test_solution():
    assert solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution([1]) == 1
    assert solution([5, 4, -1, 7, 8]) == 23
    assert solution([-1, -2, -3, -4]) == -1
    assert solution([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert solution([]) == float('-inf')
    assert solution([-1, 0, -2]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()