# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], with length 3. Another one is [3,6] which has length 2. [3, 4, 5, 6] is an increasing subsequence, but the difference between consecutive elements is not always 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 3
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1] or [5, 3, 1], with length 3.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence (LIS) with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the LIS.

    Returns:
        The length of the LIS.
    """

    # dp[x] stores the length of the longest increasing subsequence ending with x.
    dp = {}  # Use a dictionary for efficient lookup

    max_length = 0
    for num in nums:
        # If num - diff is already in the dictionary, it means we can extend an existing subsequence.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, this is the beginning of a new subsequence.
            dp[num] = 1

        max_length = max(max_length, dp[num])

    return max_length

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 2) == 1
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], -1) == 1
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([10, 15, 20, 25, 30], 5) == 5
    assert longest_increasing_subsequence_with_difference([10, 15, 20, 25, 30], -5) == 1
    assert longest_increasing_subsequence_with_difference([], 5) == 0
    assert longest_increasing_subsequence_with_difference([5], 5) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()