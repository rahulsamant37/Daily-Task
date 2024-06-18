# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5].
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
    # The key is the number, and the value is the length of the longest increasing subsequence ending at that number.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is in the dp dictionary, it means we can extend an existing subsequence.
        # Otherwise, the length of the subsequence ending at the current number is 1.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            dp[num] = 1

    # The length of the longest increasing subsequence is the maximum value in the dp dictionary.
    # If the dp dictionary is empty, it means there are no numbers in the input array, so the length is 0.
    if not dp:
        return 0

    return max(dp.values())

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 2, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 3
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([5], 2) == 1
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 2) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()