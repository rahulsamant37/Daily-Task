# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4], or [3,4,5]. Its length is 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. Its length is 4.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest arithmetic subsequence with a given difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest arithmetic subsequence.
    """

    # dp[num] stores the length of the longest arithmetic subsequence ending with num
    dp = {}

    max_length = 0
    for num in nums:
        # If num - diff exists in dp, then we can extend the subsequence ending with num - diff
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the subsequence ending with num has length 1
        else:
            dp[num] = 1

        max_length = max(max_length, dp[num])

    return max_length

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 2, 4, 5], 1) == 3
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 1) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([], 1) == 0
    assert longest_arithmetic_subsequence([5], 1) == 1
    assert longest_arithmetic_subsequence([5, 4, 3, 2, 1], -1) == 5
    assert longest_arithmetic_subsequence([5, 4, 3, 2, 1], 1) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()