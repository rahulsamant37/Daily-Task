# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5].

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, diff):
        """
        Finds the length of the longest increasing subsequence (LIS) where the difference
        between consecutive elements in the subsequence is exactly `diff`.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements in the LIS.

        Returns:
            The length of the LIS with the specified difference.
        """
        # dp[num] stores the length of the longest increasing subsequence ending with num.
        dp = {}

        # Iterate through the nums array.
        for num in nums:
            # If num - diff exists in dp, it means we can extend an existing subsequence.
            if num - diff in dp:
                dp[num] = dp[num - diff] + 1
            # Otherwise, start a new subsequence of length 1.
            else:
                dp[num] = 1

        # Return the maximum length found in the dp dictionary.
        return max(dp.values()) if dp else 0

    return longest_increasing_subsequence_with_difference
    # Test cases
def test_solution():
    longest_increasing_subsequence_with_difference = solution()

    # Test case 1
    nums1 = [3, 0, 3, 2, 4, 5]
    diff1 = 1
    expected1 = 3
    assert longest_increasing_subsequence_with_difference(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_increasing_subsequence_with_difference(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    expected2 = 4
    assert longest_increasing_subsequence_with_difference(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_increasing_subsequence_with_difference(nums2, diff2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    diff3 = 1
    expected3 = 5
    assert longest_increasing_subsequence_with_difference(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_increasing_subsequence_with_difference(nums3, diff3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    diff4 = -1
    expected4 = 5
    assert longest_increasing_subsequence_with_difference(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_increasing_subsequence_with_difference(nums4, diff4)}"

    # Test case 5
    nums5 = [1, 1, 1, 1, 1]
    diff5 = 0
    expected5 = 5
    assert longest_increasing_subsequence_with_difference(nums5, diff5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_increasing_subsequence_with_difference(nums5, diff5)}"

    # Test case 6
    nums6 = []
    diff6 = 1
    expected6 = 0
    assert longest_increasing_subsequence_with_difference(nums6, diff6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_increasing_subsequence_with_difference(nums6, diff6)}"

    # Test case 7
    nums7 = [1]
    diff7 = 1
    expected7 = 1
    assert longest_increasing_subsequence_with_difference(nums7, diff7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {longest_increasing_subsequence_with_difference(nums7, diff7)}"

    # Test case 8: more complex case with positive and negative numbers
    nums8 = [-2, 0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
    diff8 = 2
    expected8 = 7
    assert longest_increasing_subsequence_with_difference(nums8, diff8) == expected8, f"Test Case 8 Failed: Expected {expected8}, got {longest_increasing_subsequence_with_difference(nums8, diff8)}"

    # Test case 9: diff = 0, multiple subsequences possible
    nums9 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    diff9 = 0
    expected9 = 4
    assert longest_increasing_subsequence_with_difference(nums9, diff9) == expected9, f"Test Case 9 Failed: Expected {expected9}, got {longest_increasing_subsequence_with_difference(nums9, diff9)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()