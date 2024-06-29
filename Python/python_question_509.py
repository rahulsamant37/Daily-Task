# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, -3, 4, -4, 7, -7, 8], diff = 3
Output: 3
Explanation: The longest increasing subsequence with a difference of 3 is [-3, 0, 3] or [4, 7, 10] which has length 3. In this case, the subsequence [4, 7, 8] is not valid since the difference between 7 and 8 is 1, not 3. Note that the subsequence must be strictly increasing.

Input: nums = [1,5,7,8,5,3,4,2,1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1] which has length 4.
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

    # Use a dictionary to store the length of the longest increasing subsequence
    # ending at each number. The key is the number, and the value is the length
    # of the LIS ending at that number.
    dp = {}

    # Iterate through the numbers in the input array
    for num in nums:
        # If the number - diff is in the dp dictionary, it means there is a
        # subsequence that can be extended with the current number.
        if num - diff in dp:
            # The length of the LIS ending at the current number is one more
            # than the length of the LIS ending at num - diff.
            dp[num] = dp[num - diff] + 1
        else:
            # If num - diff is not in the dp dictionary, it means the current
            # number starts a new LIS with length 1.
            dp[num] = 1

    # The length of the longest increasing subsequence is the maximum value in the dp dictionary.
    if not dp:
        return 0
    return max(dp.values())

# Test cases
def test_longest_increasing_subsequence_with_diff():
    assert longest_increasing_subsequence_with_diff([3, 0, -3, 4, -4, 7, -7, 8], 3) == 3
    assert longest_increasing_subsequence_with_diff([1,5,7,8,5,3,4,2,1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1,4,5,7,2,3,6,8,9], 1) == 5
    assert longest_increasing_subsequence_with_diff([1,4,5,7,2,3,6,8,9], 2) == 3

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_diff()