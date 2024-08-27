# Python Question: Find the Maximum Sum Subarray with at Most K Distinct Elements
'''
Given an array of integers `nums` and an integer `k`, find the contiguous subarray of `nums` that contains at most `k` distinct elements and has the maximum sum. Return the maximum sum.

Example:
Input: nums = [1, 2, 1, 3, 4, 2, 3], k = 2
Output: 9
Explanation: The subarray [3, 4, 2] has a sum of 9 and contains at most 2 distinct elements.  Other subarrays with at most 2 distinct elements are [1,2,1], [2,1], [1,3], [3,4], [4,2], [2,3], etc.
'''

# Solution
def solution():
    def max_sum_subarray_with_k_distinct(nums, k):
        """
        Finds the maximum sum of a contiguous subarray with at most k distinct elements.

        Args:
            nums: A list of integers.
            k: The maximum number of distinct elements allowed in the subarray.

        Returns:
            The maximum sum of a subarray with at most k distinct elements.
        """

        max_sum = 0
        window_start = 0
        window_sum = 0
        distinct_count = {}

        for window_end in range(len(nums)):
            right_num = nums[window_end]
            if right_num not in distinct_count:
                distinct_count[right_num] = 0
            distinct_count[right_num] += 1
            window_sum += right_num

            # Shrink the window until the number of distinct elements is at most k
            while len(distinct_count) > k:
                left_num = nums[window_start]
                distinct_count[left_num] -= 1
                if distinct_count[left_num] == 0:
                    del distinct_count[left_num]
                window_sum -= nums[window_start]
                window_start += 1

            # Update the maximum sum
            max_sum = max(max_sum, window_sum)

        return max_sum

    return max_sum_subarray_with_k_distinct


# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [1, 2, 1, 3, 4, 2, 3]
    k1 = 2
    expected1 = 9
    assert func(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(nums1, k1)}"

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 1
    expected2 = 5
    assert func(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(nums2, k2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 5
    expected3 = 15
    assert func(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(nums3, k3)}"

    # Test case 4
    nums4 = [1, 1, 1, 1, 1]
    k4 = 1
    expected4 = 5
    assert func(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {func(nums4, k4)}"

    # Test case 5
    nums5 = [1, 2, 1, 2, 1]
    k5 = 2
    expected5 = 7
    assert func(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {func(nums5, k5)}"

    # Test case 6 (empty array)
    nums6 = []
    k6 = 2
    expected6 = 0
    assert func(nums6, k6) == 0, f"Test Case 6 Failed: Expected {expected6}, Got {func(nums6, k6)}"

    # Test case 7 (k = 0, should return 0 for non-empty array)
    nums7 = [1, 2, 3]
    k7 = 0
    expected7 = 0
    assert func(nums7, k7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {func(nums7, k7)}"

    # Test case 8 (Negative numbers)
    nums8 = [-1, -2, -3, 4, 5]
    k8 = 2
    expected8 = 9
    assert func(nums8, k8) == expected8, f"Test Case 8 Failed: Expected {expected8}, Got {func(nums8, k8)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()