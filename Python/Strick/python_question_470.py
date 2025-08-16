# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4], which has length 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has length 4.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest arithmetic subsequence with a given difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest arithmetic subsequence.
    """
    # Use a dictionary to store the length of the longest arithmetic subsequence ending at each number.
    # Key: number, Value: length of the longest arithmetic subsequence ending at that number.
    dp = {}

    max_length = 0
    for num in nums:
        # If num - diff exists in dp, it means we can extend the subsequence ending at num - diff by adding num.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, we start a new subsequence with length 1.
        else:
            dp[num] = 1

        # Update the maximum length found so far.
        max_length = max(max_length, dp[num])

    return max_length

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 2, 4], 1) == 3
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 0) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([1], 1) == 1
    assert longest_arithmetic_subsequence([], 1) == 0
    assert longest_arithmetic_subsequence([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15], 1) == 2
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()