# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, -3, 4, -4, 7, 6], diff = 3
Output: 3
Explanation: The longest increasing subsequence with a difference of 3 is [-3, 0, 3] or [4, 7, 10], which has a length of 3. Because 10 is not in the original array, only [-3,0,3] or [4,7] are valid, resulting in the LIS being [-3,0,3] with length 3. Note that [0,3,6] is also valid, with length 3.

Input: nums = [1,5,7,8,5,3,4,2,1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.
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

    # dp[num] stores the length of the longest arithmetic subsequence ending with num
    dp = {}  # Use a dictionary for efficient lookup
    max_len = 0

    for num in nums:
        # If num - diff exists in dp, then we can extend the subsequence ending with num - diff
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, we start a new subsequence with length 1
            dp[num] = 1
        max_len = max(max_len, dp[num])  # Update the maximum length

    return max_len

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, -3, 4, -4, 7, 6], 3) == 3
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 5, 9, 13, 17], 4) == 5
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 0) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], -1) == 1
    assert longest_arithmetic_subsequence([5, 4, 3, 2, 1], -1) == 5
    assert longest_arithmetic_subsequence([5, 4, 3, 2, 1], 1) == 1
    assert longest_arithmetic_subsequence([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 10
    assert longest_arithmetic_subsequence([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1) == 1
    assert longest_arithmetic_subsequence([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], -1) == 10
    assert longest_arithmetic_subsequence([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 1) == 1
    assert longest_arithmetic_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()