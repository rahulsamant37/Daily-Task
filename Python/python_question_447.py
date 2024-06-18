# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) with a twist:
For two numbers `nums[i]` and `nums[j]` where `i < j` to be considered a valid increasing sequence,
`nums[j]` must be greater than or equal to `2 * nums[i]`.

Example:
Input: nums = [1, 5, 2, 8, 4]
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [1, 2, 4] or [1, 2, 8].

Input: nums = [4, 6, 7, 7]
Output: 2
Explanation: The longest increasing subsequence satisfying the condition is [4, 7].

Input: nums = [1, 3, 2, 4, 6, 8]
Output: 4
Explanation: The longest increasing subsequence satisfying the condition is [1, 2, 4, 8].
'''

# Solution
def solution():
    def longest_increasing_subsequence_twisted(nums):
        """
        Finds the length of the longest increasing subsequence (LIS) with a twist.
        For two numbers nums[i] and nums[j] where i < j to be considered a valid increasing sequence,
        nums[j] must be greater than or equal to 2 * nums[i].

        Args:
            nums: A list of integers.

        Returns:
            The length of the LIS.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] can extend the increasing subsequence ending at nums[j]
                if nums[i] >= 2 * nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the LIS
        return max(dp)

    return longest_increasing_subsequence_twisted

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [1, 5, 2, 8, 4]
    expected1 = 3
    assert func(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(nums1)}"

    # Test case 2
    nums2 = [4, 6, 7, 7]
    expected2 = 2
    assert func(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(nums2)}"

    # Test case 3
    nums3 = [1, 3, 2, 4, 6, 8]
    expected3 = 4
    assert func(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(nums3)}"

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    expected4 = 1
    assert func(nums4) == 1, f"Test Case 4 Failed: Expected {1}, Got {func(nums4)}"

    # Test case 5
    nums5 = [2, 4, 8, 16]
    expected5 = 4
    assert func(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {func(nums5)}"

    # Test case 6
    nums6 = []
    expected6 = 0
    assert func(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {func(nums6)}"

    # Test case 7
    nums7 = [5]
    expected7 = 1
    assert func(nums7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {func(nums7)}"

    # Test case 8
    nums8 = [3, 1]
    expected8 = 1
    assert func(nums8) == 1, f"Test Case 8 Failed: Expected {1}, Got {func(nums8)}"

    # Test case 9
    nums9 = [1, 2, 1, 2]
    expected9 = 2
    assert func(nums9) == 2, f"Test Case 9 Failed: Expected {2}, Got {func(nums9)}"

    # Test case 10
    nums10 = [1, 2, 4, 3]
    expected10 = 3
    assert func(nums10) == 3, f"Test Case 10 Failed: Expected {3}, Got {func(nums10)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()