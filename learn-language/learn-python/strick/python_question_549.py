# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4, 5].
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence (LIS) in `nums`
    where the difference between consecutive elements in the subsequence is `diff`.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the LIS.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # Create a dictionary to store the length of the longest increasing subsequence
    # ending at each number in `nums`.  The key is the number, and the value is the length.
    dp = {}

    # Iterate through the numbers in `nums`.
    for num in nums:
        # If the number minus the difference is already in the `dp` dictionary,
        # it means we can extend an existing subsequence.
        if num - diff in dp:
            # The length of the LIS ending at `num` is one greater than the length
            # of the LIS ending at `num - diff`.
            dp[num] = dp[num - diff] + 1
        else:
            # If the number minus the difference is not in the `dp` dictionary,
            # it means we are starting a new subsequence.
            dp[num] = 1

    # The length of the longest increasing subsequence is the maximum value in the `dp` dictionary.
    if dp:
      return max(dp.values())
    else:
      return 0


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1], 0) == 4
    assert longest_increasing_subsequence_with_difference([7,5,10,6,9,4,11,1], 1) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()