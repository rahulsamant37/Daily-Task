# Python Question: Longest Increasing Subsequence with Gap
'''
Given an array of integers `nums` and an integer `gap`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `gap`.

Example:
Input: nums = [3, 10, 3, 6, 7, 8], gap = 1
Output: 4
Explanation: The longest increasing subsequence with a gap of 1 is [6, 7, 8]. Another valid sequence is [3,6,7,8]. Therefore, the length is 4.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], gap = 2
Output: 2
Explanation: The longest increasing subsequence with a gap of 2 is [1, 3]. Another valid sequence is [5,7]. Therefore, the length is 2.

Input: nums = [1, 2, 3, 4, 5], gap = 0
Output: 5
Explanation: The longest increasing subsequence with a gap of 0 is [1, 1, 1, 1, 1] or [2, 2, 2, 2, 2] or similar.  However, since we are looking for a subsequence, the longest length would be 1 if we consider only unique values. With gap = 0, we can take all same numbers as a subsequence.
'''

# Solution
def longest_increasing_subsequence_with_gap(nums, gap):
    """
    Finds the length of the longest increasing subsequence with a given gap.

    Args:
        nums: A list of integers.
        gap: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified gap.
    """

    # dp[x] stores the length of the longest increasing subsequence ending with x.
    dp = {}

    max_len = 0
    for num in nums:
        # If num - gap is in dp, then we can extend the subsequence ending with num - gap.
        if num - gap in dp:
            dp[num] = dp[num - gap] + 1
        else:
            # Otherwise, the longest increasing subsequence ending with num is just 1.
            dp[num] = 1

        # Update the maximum length.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_gap([3, 10, 3, 6, 7, 8], 1) == 4
    assert longest_increasing_subsequence_with_gap([1, 5, 7, 8, 5, 3, 4, 2, 1], 2) == 2
    assert longest_increasing_subsequence_with_gap([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_gap([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_gap([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_gap([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_gap([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_gap([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_gap([1, 1, 2, 2, 3, 3], 1) == 3
    assert longest_increasing_subsequence_with_gap([], 1) == 0
    assert longest_increasing_subsequence_with_gap([1], 1) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()