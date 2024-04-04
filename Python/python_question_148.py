# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6] with length 3.  However, the subsequence [3,6] also exists with difference 3. The optimal subsequence is [3, 3, 6] which doesn't meet the increasing criteria. The subsequence [3, 4, 5, 6] has length 4, but the difference is 1, not 3. The correct longest sequence with difference 3 is [3, 6], with length 2. Let's re-examine the optimal solution. The sequence [0,3,6] has length 3. The sequence [3,6] has length 2. The sequence [3] has length 1. The sequence [4] has length 1. The sequence [5] has length 1. The sequence [6] has length 1. Therefore, [0,3,6] is the longest increasing subsequence.

Input: nums = [1, 2, 3, 4, 5], diff = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of 1 is [1, 2, 3, 4, 5] with length 5.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with difference -2 is [7, 5, 3, 1] with length 4.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    dp = {}  # Use a dictionary to store the length of the longest subsequence ending at each number

    max_len = 0
    for num in nums:
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            dp[num] = 1
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 4, 5, 6], 3) == 2
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], 2) == 1
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 0) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([], 1) == 0
    assert longest_arithmetic_subsequence([5], 2) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()