# Python Question:  Largest Sum Contiguous Subarray with Kadane's Algorithm
'''
Given an array of integers `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

For example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Solution
def largest_contiguous_subarray_sum(nums):
    '''
    Implements Kadane's Algorithm to find the largest sum of a contiguous subarray.

    Kadane's Algorithm works by iterating through the array and maintaining two variables:
    - max_so_far: The maximum sum found so far.
    - current_max: The maximum sum ending at the current position.

    For each element in the array:
    1. Update current_max by adding the current element to it.
    2. If current_max becomes negative, reset it to 0 (because a negative sum will always reduce the sum of a subsequent subarray).
    3. Update max_so_far with the maximum of max_so_far and current_max.

    Finally, return max_so_far.
    '''
    max_so_far = float('-inf')  # Initialize max_so_far to negative infinity to handle arrays with all negative numbers.
    current_max = 0  # Initialize current_max to 0

    for i in range(len(nums)):
        current_max += nums[i]  # Add the current element to the current_max

        if current_max > max_so_far:
            max_so_far = current_max  # Update max_so_far if current_max is greater

        if current_max < 0:
            current_max = 0  # Reset current_max to 0 if it becomes negative

    return max_so_far  # Return the largest sum found

# Test cases
def test_solution():
    assert largest_contiguous_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert largest_contiguous_subarray_sum([1,2,3,4,5]) == 15
    assert largest_contiguous_subarray_sum([-1,-2,-3,-4,-5]) == -1
    assert largest_contiguous_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert largest_contiguous_subarray_sum([5,4,-1,7,8]) == 23
    assert largest_contiguous_subarray_sum([8, -19, 5, -4, 20]) == 21
    assert largest_contiguous_subarray_sum([1]) == 1
    assert largest_contiguous_subarray_sum([-1]) == -1
    assert largest_contiguous_subarray_sum([0]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()