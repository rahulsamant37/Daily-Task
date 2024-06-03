# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that the difference between consecutive elements is no more than 1.

For example:
Input: nums = [3, 10, 2, 1, 20]
Output: 2  (Longest increasing subsequence is [1, 2])

Input: nums = [1, 3, 2, 2, 5, 2, 3, 7]
Output: 4 (Longest increasing subsequence is [1, 2, 2, 3] or [2, 2, 3, 3])

Input: nums = [1, 2, 3, 4, 5]
Output: 5
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference_one(nums):
        """
        Finds the length of the longest increasing subsequence in `nums` such that the difference
        between consecutive elements is at most 1.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest increasing subsequence.
        """

        if not nums:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                # Check if nums[i] can extend the subsequence ending at nums[j].
                if nums[i] >= nums[j] and nums[i] - nums[j] <= 1:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the longest increasing subsequence.
        return max(dp)

    return longest_increasing_subsequence_with_difference_one

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    expected1 = 2
    assert func(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(nums1)}"

    # Test case 2
    nums2 = [1, 3, 2, 2, 5, 2, 3, 7]
    expected2 = 4
    assert func(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(nums2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    expected3 = 5
    assert func(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(nums3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    expected4 = 1
    assert func(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {func(nums4)}"

    # Test case 5
    nums5 = [1, 1, 1, 1, 1]
    expected5 = 5
    assert func(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {func(nums5)}"

    # Test case 6
    nums6 = []
    expected6 = 0
    assert func(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {func(nums6)}"

    # Test case 7
    nums7 = [2, 2, 3, 3, 4, 4]
    expected7 = 6
    assert func(nums7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {func(nums7)}"

    # Test case 8
    nums8 = [1, 2, 1, 2, 3, 2, 3, 4]
    expected8 = 4
    assert func(nums8) == expected8, f"Test Case 8 Failed: Expected {expected8}, Got {func(nums8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()