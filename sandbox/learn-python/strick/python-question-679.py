# Python Question: Maximum Subarray Sum Circular
'''
Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return the maximum possible sum of a non-empty subarray of `nums`.

A circular array means the end of the array connects to the beginning of the array.  Formally, the next element of `nums[i]` is `nums[(i + 1) % nums.length]` and the previous element of `nums[i]` is `nums[(i - 1 + nums.length) % nums.length]`.

A subarray may only include each element of the fixed buffer `nums` at most once.  Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1, k2 <= j` with `k1 % nums.length == k2 % nums.length`.

Example:
Input: nums = [1,-2,3,-2]
Output: 4
Explanation: The subarray [3] has the maximum possible sum of 3.

Input: nums = [5,-3,5]
Output: 10
Explanation: The subarray [5,5] has the maximum possible sum of 5 + 5 = 10.

Input: nums = [-3,-2,-3]
Output: -2
Explanation: The subarray [-2] has the maximum possible sum of -2.
'''

# Solution
def solution():
    def max_subarray(arr):
        """
        Finds the maximum subarray sum in a non-circular array.
        Uses Kadane's Algorithm.
        """
        max_so_far = -float('inf')
        current_max = 0
        for x in arr:
            current_max = max(x, current_max + x)
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    def min_subarray(arr):
        """
        Finds the minimum subarray sum in a non-circular array.
        Uses a modified Kadane's Algorithm.
        """
        min_so_far = float('inf')
        current_min = 0
        for x in arr:
            current_min = min(x, current_min + x)
            min_so_far = min(min_so_far, current_min)
        return min_so_far

    def maxSubarraySumCircular(nums):
        """
        Finds the maximum subarray sum in a circular array.
        """
        max_kadane = max_subarray(nums)  # Maximum subarray sum using Kadane's algorithm
        arr_sum = sum(nums)  # Total sum of the array
        min_kadane = min_subarray(nums)  # Minimum subarray sum using Kadane's algorithm

        # If all numbers are negative, the maximum subarray sum is the largest negative number.
        if arr_sum == min_kadane:
            return max_kadane

        # The maximum circular subarray sum is either the maximum subarray sum found by Kadane's algorithm,
        # or the total sum of the array minus the minimum subarray sum.  The idea is that removing the minimum subarray
        # leaves the maximum circular subarray.
        return max(max_kadane, arr_sum - min_kadane)

    return maxSubarraySumCircular
    # Test cases
def test_solution():
    maxSubarraySumCircular = solution()

    # Test case 1
    nums1 = [1,-2,3,-2]
    expected1 = 4
    assert maxSubarraySumCircular(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {maxSubarraySumCircular(nums1)}"

    # Test case 2
    nums2 = [5,-3,5]
    expected2 = 10
    assert maxSubarraySumCircular(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {maxSubarraySumCircular(nums2)}"

    # Test case 3
    nums3 = [-3,-2,-3]
    expected3 = -2
    assert maxSubarraySumCircular(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {maxSubarraySumCircular(nums3)}"

    # Test case 4
    nums4 = [3,-1,2,-1]
    expected4 = 4
    assert maxSubarraySumCircular(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {maxSubarraySumCircular(nums4)}"

    # Test case 5
    nums5 = [1, -2, 3, -2]
    expected5 = 4
    assert maxSubarraySumCircular(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {maxSubarraySumCircular(nums5)}"

    # Test case 6: All negative numbers
    nums6 = [-1, -2, -3]
    expected6 = -1
    assert maxSubarraySumCircular(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {maxSubarraySumCircular(nums6)}"

    # Test case 7: All positive numbers
    nums7 = [1, 2, 3]
    expected7 = 6
    assert maxSubarraySumCircular(nums7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {maxSubarraySumCircular(nums7)}"

    # Test case 8: Single element array
    nums8 = [5]
    expected8 = 5
    assert maxSubarraySumCircular(nums8) == expected8, f"Test Case 8 Failed: Expected {expected8}, Got {maxSubarraySumCircular(nums8)}"

    # Test case 9
    nums9 = [-2, 4, -5, 4, -5, 9, 4]
    expected9 = 15
    assert maxSubarraySumCircular(nums9) == 15, f"Test Case 9 Failed: Expected {15}, Got {maxSubarraySumCircular(nums9)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()