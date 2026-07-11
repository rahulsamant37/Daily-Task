# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], which has a length of 3. Another valid subsequence is [3, 6] with length 2. Also, [3, 4, 5, 6] is an increasing subsequence, but the difference between consecutive elements is not always 3. The longest subsequence with diff = 3 is [3, 0] is not valid because 3 > 0. The longest subsequence starting at index 0 is [3, 6]. The longest valid subsequence is [3, 0, 3, 6] which can be constructed as [3, 6]. The longest valid subsequence is [3, 6]. Another valid subsequence is [0, 3, 6] which has a length of 3. The longest valid subsequence is [3, 6].
Another valid subsequence is [3, 6] which has length 2. Also, [3, 4, 5, 6] is an increasing subsequence, but the difference between consecutive elements is not always 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.

Input: nums = [1, 2, 3, 4, 5], diff = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of 1 is [1, 2, 3, 4, 5], which has a length of 5.
'''

# Solution
def longest_subsequence(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    # dp[num] stores the length of the longest subsequence ending with num.
    dp = {}

    max_len = 0
    for num in nums:
        # If num - diff is already in the dp map, it means we can extend a subsequence.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, start a new subsequence with length 1.
            dp[num] = 1

        # Update the maximum length.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_subsequence([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_subsequence([1, 3, 5, 7, 9, 2, 4, 6, 8, 10], 2) == 5
    assert longest_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 10
    assert longest_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_subsequence([4,12,10,0,-2,7,-8,9,-9,-12,-3,11,8,8,9,17,4,-10,2,17], -8) == 2
    assert longest_subsequence([7,7,7,7,7,7], 0) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()