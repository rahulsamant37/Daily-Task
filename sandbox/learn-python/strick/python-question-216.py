# Python Question: Max Consecutive Sum in a Circular Array
'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), find the maximum possible sum of a non-empty subarray.
A subarray may only include each element of the original array at most once.

Example:
Input: nums = [1,-2,3,-2]
Output: 4
Explanation: Subarray [3,-2,1] has maximum sum 4.

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 10.

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
'''

# Solution
def solution():
    def max_subarray_sum(nums):
        """
        Helper function to find the maximum subarray sum in a normal (non-circular) array.
        Uses Kadane's Algorithm.
        """
        max_so_far = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)

        return max_so_far

    def min_subarray_sum(nums):
        """
        Helper function to find the minimum subarray sum in a normal array.
        Uses Kadane's Algorithm, but finds the minimum.
        """
        min_so_far = nums[0]
        current_min = nums[0]

        for i in range(1, len(nums)):
            current_min = min(nums[i], current_min + nums[i])
            min_so_far = min(min_so_far, current_min)

        return min_so_far

    def max_circular_subarray_sum(nums):
        """
        Finds the maximum subarray sum in a circular array.
        Handles the case where all elements are negative.
        """
        max_kadane = max_subarray_sum(nums)  # Max sum in a normal subarray

        arr_sum = sum(nums)
        min_kadane = min_subarray_sum(nums) # Min sum in a normal subarray

        max_wrap = arr_sum - min_kadane  # Max sum with wrap around

        # If all elements are negative, max_wrap will be 0.  In this case, we want to return the largest negative number
        # which is already handled by max_kadane.
        if max_kadane > 0:
            return max(max_kadane, max_wrap)
        else:
            return max_kadane  # Return the largest negative number (or 0 if all nums are 0).

    return max_circular_subarray_sum

# Test cases
def test_solution():
    def assert_equal(actual, expected, message=""):
        if actual != expected:
            print(f"Assertion failed: {message}")
            print(f"  Actual: {actual}")
            print(f"  Expected: {expected}")

    nums1 = [1,-2,3,-2]
    assert_equal(solution()(nums1), 4, "Test Case 1 Failed")

    nums2 = [5,-3,5]
    assert_equal(solution()(nums2), 10, "Test Case 2 Failed")

    nums3 = [-3,-2,-3]
    assert_equal(solution()(nums3), -2, "Test Case 3 Failed")

    nums4 = [-2, -3, -1]
    assert_equal(solution()(nums4), -1, "Test Case 4 Failed")

    nums5 = [1, -2, 3, -2, 1]
    assert_equal(solution()(nums5), 4, "Test Case 5 Failed")

    nums6 = [1,2,3,4,5]
    assert_equal(solution()([1, 2, 3, 4, 5]), 15, "Test Case 6 Failed")

    nums7 = [-1, -2, -3, -4, -5]
    assert_equal(solution()([-1, -2, -3, -4, -5]), -1, "Test Case 7 Failed")

    nums8 = [0, 0, 0, 0]
    assert_equal(solution()([0, 0, 0, 0]), 0, "Test Case 8 Failed")

    nums9 = [-5, 8, -8, 9, -9, 6, -6, 5]
    assert_equal(solution()([-5, 8, -8, 9, -9, 6, -6, 5]), 14, "Test Case 9 Failed")

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()