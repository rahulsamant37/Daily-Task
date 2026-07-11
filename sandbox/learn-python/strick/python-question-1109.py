# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], which has length 3. Another one is [3,6] which has length 2 and [3,4,5,6] which has difference 1, which is not allowed. Therefore the answer is [3,0,3,6] which has length 4.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has length 4.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence is exactly `diff`.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements.

    Returns:
        The length of the LIS with the specified difference.
    """

    # Use a dictionary to store the length of the LIS ending at each number.
    # The key is the number, and the value is the length of the LIS ending at that number.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number - diff is already in the dp dictionary, it means we can extend
        # an existing LIS ending at number - diff.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, this number starts a new LIS of length 1.
            dp[num] = 1

    # Return the maximum value in the dp dictionary, which represents the length
    # of the longest increasing subsequence with the specified difference.
    return max(dp.values()) if dp else 0

# Test cases
def test_longest_increasing_subsequence_with_difference():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([5], 2) == 1
    assert longest_increasing_subsequence_with_difference([5, 3, 1, 7, 9], 2) == 3

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_difference()