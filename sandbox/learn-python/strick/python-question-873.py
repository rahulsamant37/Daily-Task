# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5]. The length is 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. The length is 4.

Input: nums = [4, 12, 10, 0, -2, 10, 7, 1, 14, 12], diff = -2
Output: 3
Explanation: One possible LIS is [12, 10, 8], where 8 would be inferred. However, the actual LIS in nums is [12, 10, 8] can't be directly constructed using indices in nums.  Another possible LIS is [10, 8, 6], same case.  The correct LIS to consider is [0, -2, -4]. The length is 3.
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # dp[num] stores the length of the longest increasing subsequence ending with num
    # using the given difference.
    dp = {}

    max_len = 0

    for num in nums:
        # If num - diff exists in the dp, it means we can extend a subsequence
        # ending with num - diff.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, we start a new subsequence of length 1.
            dp[num] = 1

        # Update the maximum length found so far.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 2, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_diff([4, 12, 10, 0, -2, 10, 7, 1, 14, 12], -2) == 3
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([9, 7, 5, 3, 1], -2) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()