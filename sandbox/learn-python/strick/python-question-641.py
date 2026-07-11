# Python Question: Largest Sum Contiguous Subarray (Kadane's Algorithm)
'''
Given an array of integers `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Solution
def largest_subarray_sum(nums):
    '''
    This function implements Kadane's Algorithm to find the largest sum of a contiguous subarray.

    The algorithm works by iterating through the array and maintaining two variables:
    - max_so_far:  The maximum sum found so far.
    - current_max: The maximum sum ending at the current position.

    At each element, we decide whether to include the current element in the current subarray or start a new subarray from the current element.
    If the current_max becomes negative, we reset it to 0, effectively starting a new subarray.
    '''
    max_so_far = nums[0]  # Initialize the maximum sum so far with the first element
    current_max = nums[0]  # Initialize the current maximum sum with the first element

    for i in range(1, len(nums)):
        # Update current_max: either extend the previous subarray or start a new one from the current element
        current_max = max(nums[i], current_max + nums[i])

        # Update max_so_far if the current maximum is greater
        max_so_far = max(max_so_far, current_max)

    return max_so_far

# Test cases
def test_largest_subarray_sum():
    assert largest_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert largest_subarray_sum([1]) == 1
    assert largest_subarray_sum([5, 4, -1, 7, 8]) == 23
    assert largest_subarray_sum([-1, -2, -3, -4]) == -1
    assert largest_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert largest_subarray_sum([0, 0, 0, 0]) == 0
    assert largest_subarray_sum([-1, 0, -2]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_subarray_sum()