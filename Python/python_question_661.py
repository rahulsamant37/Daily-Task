# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5], diff = 3
Output: 3
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], but 6 is not in the array. So, the longest subsequence is [0, 3, 6] -> [0, 3], [3, 0, 3, 4, 5] -> [0, 3], [3,4,5] -> [3,4]. The correct subsequence is [0, 3]. Another subsequence could be [3,4,5].
In our case, the longest is [0, 3, 6] is not applicable. The longest increasing subsequence with difference 3 is [0, 3]. Thus, the length is 2.
Example 2:
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1].
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence in nums with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """

    # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
    # The key is the number, and the value is the length of the longest increasing subsequence ending at that number.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the previous number (num - diff) is already in the dictionary,
        # it means we can extend the subsequence ending at (num - diff) by adding the current number (num).
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the longest increasing subsequence ending at the current number is just 1 (the number itself).
        else:
            dp[num] = 1

    # Find the maximum value in the dictionary, which represents the length of the longest increasing subsequence.
    if not dp:
        return 0
    return max(dp.values())

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 4, 5], 3) == 2
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], -1) == 1
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 1, 2, 1, 2], 1) == 2
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([5], 2) == 1
    assert longest_increasing_subsequence_with_difference([4, 12, 10, 0, -2, 10, 7, -8, 9, -9, -1, -3, 4, 14, -8, 13, 13, 1, 10, 11, 11, 12, 5, 10, 1, 14, 10, 4, 0, 12, 0, 13, 1, 6, 13, 0, 14, 7, 0, 10, 8, 7, 14, 1, 7, 10, 11, 0, 13, 14, 11, 10, 0, 2, 6, 7, 0, 13, 10, 7, 11, 0, 10, 10, 6, 0, 1, 7, 13, 11, 3, 14, 0, 3, 11, 9, 11, 11, 11, 11, 10, 13, 2, 9, 0, 10, 10, 6, 14, 12, 6, 1, 13, 0, 10, 13, 11, 10, 4, 12, 10, 10, 14], 2) == 2

if __name__ == "__main__":
    test_solution()