# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence in `nums` such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4, 5].
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence in `nums` such that the difference
    between consecutive elements in the subsequence is exactly `diff`.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """
    # dp[x] stores the length of the longest increasing subsequence ending with x.
    dp = {}

    max_len = 0
    for num in nums:
        # If num - diff exists in the dp table, it means we can extend an existing subsequence.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # If num - diff doesn't exist, it means we're starting a new subsequence.
            dp[num] = 1

        # Update the maximum length found so far.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 3
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([7, 5, 6, 4, 5, 3, 4, 2, 1], -1) == 7
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0

if __name__ == "__main__":
    test_solution()