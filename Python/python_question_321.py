# Python Question: Longest Increasing Subsequence with Limited Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) such that the difference between any two consecutive elements in the subsequence is at most `diff`.

Example:
Input: nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], diff = 2
Output: 4
Explanation: One possible LIS is [1, 1, 2, 3] or [3, 4, 5, 6], both with length 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_diff(nums, diff):
        """
        Finds the length of the longest increasing subsequence with a limited difference.

        Args:
          nums: A list of integers.
          diff: The maximum difference allowed between consecutive elements in the subsequence.

        Returns:
          The length of the longest increasing subsequence with the given difference constraint.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] can extend the subsequence ending at nums[j]
                if nums[i] > nums[j] and (nums[i] - nums[j]) <= diff:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the longest increasing subsequence
        return max(dp)

    return longest_increasing_subsequence_with_diff


# Test cases
def test_solution():
    nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    diff1 = 2
    expected1 = 4
    assert solution()(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {solution()(nums1, diff1)}"

    nums2 = [1, 2, 3, 4, 5]
    diff2 = 1
    expected2 = 5
    assert solution()(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {solution()(nums2, diff2)}"

    nums3 = [5, 4, 3, 2, 1]
    diff3 = 1
    expected3 = 1
    assert solution()(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {solution()(nums3, diff3)}"

    nums4 = [1, 5, 2, 6, 3, 7, 4, 8]
    diff4 = 3
    expected4 = 4
    assert solution()(nums4, diff4) == 4, f"Test Case 4 Failed: Expected {4}, Got {solution()(nums4, diff4)}"

    nums5 = []
    diff5 = 2
    expected5 = 0
    assert solution()(nums5, diff5) == 0, f"Test Case 5 Failed: Expected {expected5}, Got {solution()(nums5, diff5)}"

    nums6 = [7, 8, 9, 1, 2, 3]
    diff6 = 1
    expected6 = 3
    assert solution()(nums6, diff6) == 3, f"Test Case 6 Failed: Expected {expected6}, Got {solution()(nums6, diff6)}"

    nums7 = [1, 1, 1, 1, 1]
    diff7 = 0
    expected7 = 1
    assert solution()(nums7, diff7) == 1, f"Test Case 7 Failed: Expected {expected7}, Got {solution()(nums7, diff7)}"

    nums8 = [1, 3, 5, 2, 4, 6]
    diff8 = 1
    expected8 = 3
    assert solution()(nums8, diff8) == 3, f"Test Case 8 Failed: Expected {expected8}, Got {solution()(nums8, diff8)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()