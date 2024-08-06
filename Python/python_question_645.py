# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5], which has length 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has length 4.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # Use a dictionary to store the length of the longest arithmetic subsequence
    # ending at each number in nums.
    dp = {}

    max_len = 0
    for num in nums:
        # If num - diff is in dp, then we can extend the subsequence ending at num - diff.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, start a new subsequence of length 1.
            dp[num] = 1
        
        # Update the maximum length.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 4, 5], 1) == 3
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 2, 3, 4], 1) == 4
    assert longest_arithmetic_subsequence([1, 3, 5, 7], 2) == 4
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], 0) == 1
    assert longest_arithmetic_subsequence([1], 1) == 1
    assert longest_arithmetic_subsequence([], 1) == 0
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], -1) == 1
    assert longest_arithmetic_subsequence([5, 4, 3, 2, 1], -1) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()