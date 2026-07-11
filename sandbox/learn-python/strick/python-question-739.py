# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6].

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 3
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3] or [5, 3, 1].
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence is exactly `diff`.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the LIS.

    Returns:
        The length of the LIS.
    """
    # dp[num] stores the length of the LIS ending with the number 'num'.
    dp = {}
    max_len = 0

    for num in nums:
        # If num - diff exists in dp, it means we can extend an existing LIS.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, we start a new LIS with length 1.
            dp[num] = 1
        # Update the maximum length found so far.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 3
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 2) == 1
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1,4,7,10,13], 3) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()