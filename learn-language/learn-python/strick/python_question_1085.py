# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5], both of length 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: One possible longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], of length 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_diff(nums, diff):
        """
        Finds the length of the longest increasing subsequence with a specific difference.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence.
        """
        # dp[num] stores the length of the longest increasing subsequence ending with num.
        dp = {}

        # Iterate through the numbers in the input array.
        for num in nums:
            # If num - diff exists in dp, it means we can extend a previous subsequence.
            if num - diff in dp:
                dp[num] = dp[num - diff] + 1
            # Otherwise, this is the start of a new subsequence of length 1.
            else:
                dp[num] = 1

        # Return the maximum value in dp, which is the length of the longest subsequence.
        return max(dp.values()) if dp else 0

    return longest_increasing_subsequence_with_diff

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [3, 0, 3, 2, 4, 5]
    diff1 = 1
    expected1 = 3
    assert func(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    expected2 = 4
    assert func(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(nums2, diff2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    diff3 = 1
    expected3 = 5
    assert func(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(nums3, diff3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    diff4 = -1
    expected4 = 5
    assert func(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {func(nums4, diff4)}"

    # Test case 5
    nums5 = [1, 1, 1, 1, 1]
    diff5 = 0
    expected5 = 5
    assert func(nums5, diff5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {func(nums5, diff5)}"

    # Test case 6
    nums6 = []
    diff6 = 1
    expected6 = 0
    assert func(nums6, diff6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {func(nums6, diff6)}"

    # Test case 7
    nums7 = [1]
    diff7 = 1
    expected7 = 1
    assert func(nums7, diff7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {func(nums7, diff7)}"

    # Test case 8
    nums8 = [1, 2, 3, 1, 2, 3]
    diff8 = 1
    expected8 = 3
    assert func(nums8, diff8) == expected8, f"Test Case 8 Failed: Expected {expected8}, Got {func(nums8, diff8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()