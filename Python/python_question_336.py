# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with difference at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5].

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with difference at most 2 is [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [2, 4, 5], [3, 4, 5].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence with a maximum difference of k between consecutive elements.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence.
        """

        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # dp[i] stores the length of the LIS ending at index i

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    return longest_increasing_subsequence_with_k_difference


# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [1, 3, 2, 4, 5]
    k1 = 1
    expected1 = 4
    assert func(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {func(nums1, k1)}"

    # Test case 2
    nums2 = [1, 5, 2, 4, 3]
    k2 = 2
    expected2 = 3
    assert func(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {func(nums2, k2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    expected3 = 1
    assert func(nums3, k3) == 1, f"Test Case 3 Failed: Expected {expected3}, got {func(nums3, k3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    k4 = 1
    expected4 = 1
    assert func(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {func(nums4, k4)}"

    # Test case 5
    nums5 = [1, 3, 5, 2, 4, 6]
    k5 = 2
    expected5 = 4
    assert func(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {func(nums5, k5)}"

    # Test case 6
    nums6 = []
    k6 = 2
    expected6 = 0
    assert func(nums6,k6) == 0, f"Test Case 6 Failed: Expected {expected6}, got {func(nums6, k6)}"

    # Test case 7
    nums7 = [1]
    k7 = 5
    expected7 = 1
    assert func(nums7, k7) == 1, f"Test Case 7 Failed: Expected {expected7}, got {func(nums7, k7)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()