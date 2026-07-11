# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6]. The length is 3. Another possible sequence is [3, 6]. The longest is [3, 4, 5, 6] with diff 1.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. The length is 4.

Input: nums = [4, 12, 10, 0, -2, 10, -7, 5, -1, 10, -4, 4, -6], diff = 3
Output: 2
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """
    n = len(nums)
    dp = {}  # Use a dictionary to store the length of the subsequence ending at each number.
    max_len = 0

    for i in range(n):
        # For each number in the array, check if the previous number (nums[i] - diff)
        # exists in the dp dictionary.

        if nums[i] - diff in dp:
            # If it exists, then we can extend the subsequence ending at nums[i] - diff
            # by adding nums[i]. The length of the new subsequence is the length of the
            # subsequence ending at nums[i] - diff plus 1.
            dp[nums[i]] = dp[nums[i] - diff] + 1
        else:
            # If it doesn't exist, then we start a new subsequence with nums[i].
            dp[nums[i]] = 1

        # Update the maximum length.
        max_len = max(max_len, dp[nums[i]])

    return max_len

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 4, 5, 6], 3) == 3
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([4, 12, 10, 0, -2, 10, -7, 5, -1, 10, -4, 4, -6], 3) == 2
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 5], 4) == 2
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 0) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([1], 0) == 1
    assert longest_arithmetic_subsequence([], 0) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()