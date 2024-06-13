# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5].

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1].
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """

    # Use a dictionary to store the length of the longest increasing subsequence
    # ending at each number.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is in the dictionary,
        # it means we can extend an existing subsequence.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, this number starts a new subsequence of length 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary, which represents the
    # length of the longest increasing subsequence.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 2, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], -1) == 1
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([7,7,7,7,7], 0) == 5
    assert longest_increasing_subsequence_with_difference([1,3,5,7,9],2) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()