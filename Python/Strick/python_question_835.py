# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence in `nums` such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6]. The length is 3. Another possible subsequence is [3, 6].
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. The length is 4.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest arithmetic subsequence in `nums` with a difference of `diff`.

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
        # If the previous number in the sequence (num - diff) exists in dp,
        # then we can extend the subsequence by 1.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, the subsequence starting with num has length 1.
            dp[num] = 1
        # Update the maximum length found so far.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 4, 5, 6], 3) == 3
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 5, 9, 13, 17], 4) == 5
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([1, 2, 3, 1, 2, 3], 1) == 3
    assert longest_arithmetic_subsequence([], 1) == 0
    assert longest_arithmetic_subsequence([5], 2) == 1
    assert longest_arithmetic_subsequence([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99], 2) == 49
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()