# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence in `nums` such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6]. Another one is [3, 6]. [3,3,6] is not increasing, so it's not a valid subsequence.  [3,4,5,6] is an increasing subsequence, but the difference between consecutive elements is not always 3. [3, 0] is not increasing. [0, 3, 4] is increasing but the difference between 0 and 3 is 3, and 3 and 4 is 1, which is not `diff`.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 3
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3]. Another one is [5,3,1] or [8, 6, 4, 2].

Input: nums = [1, 2, 3, 4, 5], diff = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of 1 is [1, 2, 3, 4, 5].

Input: nums = [1, 2, 3, 4, 5], diff = 0
Output: 1
Explanation: The longest increasing subsequence with a difference of 0 is [1], [2], [3], [4], or [5].
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
        The length of the longest increasing subsequence with the given difference.
    """

    # dp[x] stores the length of the longest increasing subsequence ending at x.
    dp = {}

    max_len = 0
    for num in nums:
        # If num - diff exists in the dp map, then we can extend the subsequence ending at num - diff
        # by adding num to it.  Otherwise, the longest increasing subsequence ending at num is just 1.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            dp[num] = 1

        # Update the maximum length found so far.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 3
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 4, 6, 8, 10], 2) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 4, 6, 8, 10], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 2, 4, 6, 8, 10], 1) == 2
    assert longest_increasing_subsequence_with_diff([1, 2, 4, 6, 8, 10], 3) == 1
    assert longest_increasing_subsequence_with_diff([1, 2, 4, 6, 8, 10], -1) == 1
    assert longest_increasing_subsequence_with_diff([], 2) == 0
    assert longest_increasing_subsequence_with_diff([5], 2) == 1

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()