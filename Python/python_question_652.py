# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6]. Another one is [3, 6]. The length is 3.
Another Example:
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. The length is 4.
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """
    # Use a dictionary to store the length of the longest subsequence ending at each number.
    # Key: number, Value: length of longest subsequence ending at that number
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number - diff exists in the dp dictionary, it means we can extend an existing subsequence.
        if num - diff in dp:
            # The length of the longest subsequence ending at the current number is 1 more than
            # the length of the longest subsequence ending at the previous number (num - diff).
            dp[num] = dp[num - diff] + 1
        else:
            # If the number - diff doesn't exist, it means we're starting a new subsequence of length 1.
            dp[num] = 1

    # The maximum value in the dp dictionary represents the length of the longest increasing subsequence.
    if not dp:
        return 0
    return max(dp.values())


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 3
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 2) == 1
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9, 11], 2) == 6
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9, 11], 0) == 1
    assert longest_increasing_subsequence_with_diff([10, 5, 0, -5, -10], -5) == 5
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()