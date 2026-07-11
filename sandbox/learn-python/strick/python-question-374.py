# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5].  The length is 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. The length is 4.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest arithmetic subsequence with the given difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest arithmetic subsequence.
    """
    # dp[num] stores the length of the longest arithmetic subsequence ending with num
    dp = {}

    max_len = 0

    for num in nums:
        # If num - diff exists in dp, then we can extend the subsequence ending with num - diff
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, we start a new subsequence of length 1
        else:
            dp[num] = 1
        max_len = max(max_len, dp[num])

    return max_len


# Test cases
def test_solution():
    nums1 = [3, 0, 3, 2, 4, 5]
    diff1 = 1
    assert longest_arithmetic_subsequence(nums1, diff1) == 3

    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    assert longest_arithmetic_subsequence(nums2, diff2) == 4

    nums3 = [1, 2, 3, 4]
    diff3 = 1
    assert longest_arithmetic_subsequence(nums3, diff3) == 4

    nums4 = [1, 3, 5, 7]
    diff4 = 2
    assert longest_arithmetic_subsequence(nums4, diff4) == 4

    nums5 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff5 = 0
    assert longest_arithmetic_subsequence(nums5, diff5) == 2

    nums6 = [7,7,7,7,7,7]
    diff6 = 0
    assert longest_arithmetic_subsequence(nums6, diff6) == 6

    nums7 = [1,2,3,4,5]
    diff7 = 2
    assert longest_arithmetic_subsequence(nums7, diff7) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()