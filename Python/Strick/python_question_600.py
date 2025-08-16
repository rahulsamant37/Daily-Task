# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence in `nums` such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [3, 0, 3, 6].  The subsequence is [3, 6], so the length is 2. Another possible sequence is [0, 3, 6]. The longest sequence is [3, 0, 3, 6], but the subsequence must be increasing in indices. The correct longest sequence is [3, 6] or [0,3,6]. So the length is 3. The sequence must be [0,3,6].
Input: nums = [1, 2, 3, 4, 5], diff = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of 1 is [1, 2, 3, 4, 5].
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence in nums with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    # dp[num] stores the length of the longest increasing subsequence ending with num.
    dp = {}  # Use a dictionary to store the lengths efficiently

    max_len = 0  # Keep track of the maximum length found so far

    for num in nums:
        # If num - diff exists in dp, then we can extend the subsequence ending with num - diff.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, the longest increasing subsequence ending with num has length 1.
            dp[num] = 1

        # Update the maximum length found so far.
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 2
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], 2) == 1
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9, 2, 4, 6, 8], 2) == 5
    assert longest_increasing_subsequence_with_diff([4,12,10,0,-2,7,-8,9,-9,-12,-3,1,11,6,10,4,3,-6,12,-11,9,0,7,7,-2,-5,-12,10,10,-6,7,12,0,10,5,-10,4,1,1,4,-6,-12,-1,11,-3,-10,3,9], -2) == 3

if __name__ == "__main__":
    test_solution()